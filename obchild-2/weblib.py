import json
import urllib.request
import urllib.error
import urllib.parse


def stringnor(value):
    """Chuẩn hóa chuỗi, loại bỏ dấu nháy đơn hoặc kép nếu có."""
    if isinstance(value, str):
        if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
            return value[1:-1]
        return value
    raise TypeError(f"Expected string, got {type(value).__name__}")


def headernor(headers):
    """Chuẩn hóa headers thành dict string cho urllib."""
    if headers is None:
        return {}
    if isinstance(headers, dict):
        return {str(k): str(v) for k, v in headers.items()}
    raise TypeError("headers phải là dict")


class web:
    """Thư viện web"""

    @staticmethod
    def fetch(url, timeout=10, headers=None):
        """Lấy nội dung văn bản từ một URL."""
        target = stringnor(url)
        hdrs = headernor(headers)
        request = urllib.request.Request(target, headers=hdrs)
        with urllib.request.urlopen(request, timeout=timeout) as response:
            charset = response.headers.get_content_charset() or 'utf-8'
            return response.read().decode(charset, errors='replace')

    @staticmethod
    def getjson(url, timeout=10, headers=None):
        """Lấy và giải mã JSON từ một URL."""
        data = web.fetch(url, timeout=timeout, headers=headers)
        return json.loads(data)

    @staticmethod
    def status_code(url, timeout=10, headers=None):
        """Lấy mã trạng thái HTTP của một URL."""
        target = stringnor(url)
        hdrs = headernor(headers)
        request = urllib.request.Request(target, headers=hdrs)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.status
        except urllib.error.HTTPError as err:
            return err.code

    @staticmethod
    def headering(url, timeout=10, headers=None):
        """Lấy header HTTP từ một URL."""
        target = stringnor(url)
        hdrs = headernor(headers)
        request = urllib.request.Request(target, headers=hdrs)
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return dict(response.headers)

    @staticmethod
    def download(url, destination, timeout=10, headers=None):
        """Tải file từ URL và lưu vào đường dẫn destination."""
        target = stringnor(url)
        dest = stringnor(destination)
        hdrs = stringnor(headers)
        request = urllib.request.Request(target, headers=hdrs)
        with urllib.request.urlopen(request, timeout=timeout) as response:
            content = response.read()
        with open(dest, 'wb') as file:
            file.write(content)
        return dest

    @staticmethod
    def jsonpost(url, data, timeout=10, headers=None):
        """Gửi JSON bằng POST và trả về nội dung phản hồi."""
        target = stringnor(url)
        hdrs = headernor(headers)
        body = json.dumps(data).encode('utf-8')
        hdrs.setdefault('Content-Type', 'application/json')
        request = urllib.request.Request(target, data=body, headers=hdrs, method='POST')
        with urllib.request.urlopen(request, timeout=timeout) as response:
            charset = response.headers.get_content_charset() or 'utf-8'
            return response.read().decode(charset, errors='replace')

    @staticmethod
    def formpost(url, fields, timeout=10, headers=None):
        """Gửi form bằng POST (application/x-www-form-urlencoded)."""
        target = stringnor(url)
        hdrs = headernor(headers)
        if not isinstance(fields, dict):
            raise TypeError('fields phải là dict')
        body = urllib.parse.urlencode(fields).encode('utf-8')
        hdrs.setdefault('Content-Type', 'application/x-www-form-urlencoded')
        request = urllib.request.Request(target, data=body, headers=hdrs, method='POST')
        with urllib.request.urlopen(request, timeout=timeout) as response:
            charset = response.headers.get_content_charset() or 'utf-8'
            return response.read().decode(charset, errors='replace')
