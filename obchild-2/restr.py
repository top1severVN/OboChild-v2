import re


def _normalize_string(value):
    if isinstance(value, str):
        if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
            return value[1:-1]
        return value
    raise TypeError(f"Expected string, got {type(value).__name__}")


class stringlib:
    """Thư viện xử lý chuỗi cho Obo Child."""

    @staticmethod
    def length(value):
        """Trả về độ dài chuỗi."""
        text = _normalize_string(value)
        return len(text)

    @staticmethod
    def upper(value):
        """Chuyển chuỗi thành chữ in hoa."""
        text = _normalize_string(value)
        return text.upper()

    @staticmethod
    def lower(value):
        """Chuyển chuỗi thành chữ thường."""
        text = _normalize_string(value)
        return text.lower()

    @staticmethod
    def capitalize(value):
        """Viết hoa ký tự đầu tiên của chuỗi."""
        text = _normalize_string(value)
        return text.capitalize()

    @staticmethod
    def title(value):
        """Viết hoa mỗi từ trong chuỗi."""
        text = _normalize_string(value)
        return text.title()

    @staticmethod
    def strip(value, chars=None):
        """Loại bỏ khoảng trắng hoặc ký tự chỉ định ở đầu và cuối."""
        text = _normalize_string(value)
        return text.strip(chars) if chars is not None else text.strip()

    @staticmethod
    def split(value, separator=None):
        """Tách chuỗi thành danh sách theo dấu phân cách."""
        text = _normalize_string(value)
        return text.split(separator)

    @staticmethod
    def join(separator, items):
        """Nối danh sách chuỗi thành một chuỗi bằng dấu phân cách."""
        sep = _normalize_string(separator)
        if isinstance(items, (list, tuple)):
            normalized_items = [str(_normalize_string(item)) if isinstance(item, str) else str(item) for item in items]
            return sep.join(normalized_items)
        raise TypeError("items phải là list hoặc tuple")

    @staticmethod
    def replace(value, old, new, maxreplace=-1):
        """Thay thế old bằng new trong chuỗi."""
        text = _normalize_string(value)
        old_text = _normalize_string(old)
        new_text = _normalize_string(new)
        if maxreplace == -1:
            return text.replace(old_text, new_text)
        return text.replace(old_text, new_text, maxreplace)

    @staticmethod
    def substring(value, start, end=None):
        """Lấy phần con của chuỗi từ start đến end."""
        text = _normalize_string(value)
        if end is None:
            return text[start:]
        return text[start:end]

    @staticmethod
    def starts_with(value, prefix):
        """Kiểm tra chuỗi bắt đầu bằng prefix."""
        text = _normalize_string(value)
        return text.startswith(_normalize_string(prefix))

    @staticmethod
    def ends_with(value, suffix):
        """Kiểm tra chuỗi kết thúc bằng suffix."""
        text = _normalize_string(value)
        return text.endswith(_normalize_string(suffix))

    @staticmethod
    def contains(value, substring):
        """Kiểm tra chuỗi có chứa substring không."""
        text = _normalize_string(value)
        return _normalize_string(substring) in text

    @staticmethod
    def repeat(value, count):
        """Lặp chuỗi count lần."""
        text = _normalize_string(value)
        if not isinstance(count, int):
            raise TypeError("count phải là số nguyên")
        return text * count

    @staticmethod
    def find(value, substring, start=0):
        """Tìm vị trí substring trong chuỗi."""
        text = _normalize_string(value)
        return text.find(_normalize_string(substring), start)

    @staticmethod
    def regex_match(value, pattern):
        """Kiểm tra chuỗi khớp regex pattern."""
        text = _normalize_string(value)
        return bool(re.match(pattern, text))

