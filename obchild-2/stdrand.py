import sys
import random as rnd

class random():
    """ đây là class random, nó sẽ trả về một giá trị ngẫu nhiên trong một khoảng cho trước """
    def rand(a, b):
        """ a: giá trị nhỏ nhất của khoảng, b: giá trị lớn nhất của khoảng """
        return rnd.uniform(a, b)
    def intt(a, b):
        """ a: giá trị nhỏ nhất của khoảng, b: giá trị lớn nhất của khoảng """
        return rnd.randint(a, b)
    def play(a, b):
        """ a: giá trị nhỏ nhất của khoảng, b: giá trị lớn nhất của khoảng """
        return rnd.choice(range(a, b+1))
    def flat(a, b):
        """ a: giá trị nhỏ nhất của khoảng, b: giá trị lớn nhất của khoảng """
        return rnd.random() * (b - a) + a
    def bool():
        """ đây là hàm rndbool, nó sẽ trả về một giá trị ngẫu nhiên là True hoặc False """
        return rnd.choice([True, False])
    def string(length):
        """ length: độ dài của chuỗi ngẫu nhiên sẽ được trả về """
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        return ''.join(rnd.choice(letters) for i in range(length))
    def lister(length, a, b):
        """ length: độ dài của danh sách ngẫu nhiên sẽ được trả về, a: giá trị nhỏ nhất của khoảng, b: giá trị lớn nhất của khoảng """
        return [rnd.uniform(a, b) for i in range(length)]
    def intlist(length, a, b):
        """ length: độ dài của danh sách ngẫu nhiên sẽ được trả về, a: giá trị nhỏ nhất của khoảng, b: giá trị lớn nhất của khoảng """
        return [rnd.randint(a, b) for i in range(length)]
    def boollist(length):
        """ length: độ dài của danh sách ngẫu nhiên sẽ được trả về """
        return [rnd.choice([True, False]) for i in range(length)]
    def strlist(length, str_length):
        """ length: độ dài của danh sách ngẫu nhiên sẽ được trả về, str_length: độ dài của chuỗi ngẫu nhiên sẽ được trả về """
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        return [''.join(rnd.choice(letters) for i in range(str_length)) for j in range(length)]
    def matrixx(rows, cols, a, b):
        """ rows: số hàng của ma trận ngẫu nhiên sẽ được trả về, cols: số cột của ma trận ngẫu nhiên sẽ được trả về, a: giá trị nhỏ nhất của khoảng, b: giá trị lớn nhất của khoảng """
        return [[rnd.uniform(a, b) for j in range(cols)] for i in range(rows)]
    def intmatrix(rows, cols, a, b):
        """ rows: số hàng của ma trận ngẫu nhiên sẽ được trả về, cols: số cột của ma trận ngẫu nhiên sẽ được trả về, a: giá trị nhỏ nhất của khoảng, b: giá trị lớn nhất của khoảng """
        return [[rnd.randint(a, b) for j in range(cols)] for i in range(rows)]
    def boolmatrix(rows, cols):
        """ rows: số hàng của ma trận ngẫu nhiên sẽ được trả về, cols: số cột của ma trận ngẫu nhiên sẽ được trả về """
        return [[rnd.choice([True, False]) for j in range(cols)] for i in range(rows)]
    def strmatrix(rows, cols, str_length):
        """ rows: số hàng của ma trận ngẫu nhiên sẽ được trả về, cols: số cột của ma trận ngẫu nhiên sẽ được trả về, str_length: độ dài của chuỗi ngẫu nhiên sẽ được trả về """
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        return [[''.join(rnd.choice(letters) for i in range(str_length)) for j in range(cols)] for k in range(rows)]
    def shuffler(lst):
        """ lst: danh sách sẽ được xáo trộn ngẫu nhiên """
        return rnd.shuffle(lst)
    def sampler(lst, k):
        """ lst: danh sách sẽ được lấy mẫu ngẫu nhiên, k: số lượng phần tử sẽ được lấy mẫu """
        return rnd.sample(lst, k)
    def boir(lst, k):
        """ lst: danh sách sẽ được lấy mẫu ngẫu nhiên có thể lặp lại, k: số lượng phần tử sẽ được lấy mẫu """
        return rnd.choices(lst, k=k)
    def ghost(lst):       
        """ lst: danh sách sẽ được chọn ngẫu nhiên một phần tử """
        return rnd.choice(lst)
    def bytes(n):
        """ n: số lượng byte ngẫu nhiên sẽ được trả về """
        return rnd.randbytes(n)
    def stock(a):
        """ a: giá trị sẽ được sử dụng làm hạt giống cho bộ sinh số ngẫu nhiên """
        return rnd.seed(a)
    def status():
        """ đây là hàm getstate, nó sẽ trả về trạng thái hiện tại của bộ sinh số ngẫu nhiên """
        return rnd.getstate()
    def setus(state):
        """ state: trạng thái sẽ được thiết lập cho bộ sinh số ngẫu nhiên """
        return rnd.setstate(state)
    def permut(lst):
        """ lst: danh sách sẽ được hoán vị ngẫu nhiên """
        return rnd.permutation(lst)