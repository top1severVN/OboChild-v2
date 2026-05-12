import sys
import re
import random as rnd 
import time as tm 
import math as mth 

green = "\033[32m"
red = "\033[31m"
blue = "\033[34m"
yellow = "\033[33m"
res = "\033[0m"

class function_math():
    """ đây là class function_math, nó sẽ thực thi các phép toán toán học như cộng, trừ, nhân, chia, sin, cos, tan, log, sqrt, pow, ptg, log10, log2, Psquare, Prect, Ptria3, Prhom, Pparam, Ptrape, Pcir1, Pcir2, Psemi và Pelip """
    def sin(a):
        """ đây là hàm sin, nó sẽ trả về sin của a """
        return mth.sin(mth.radians(a))
    def cos(a):
        """ đây là hàm cos, nó sẽ trả về cos của a """
        return mth.cos(mth.radians(a))
    def tan(a):
        """ đây là hàm tan, nó sẽ trả về tan của a """
        return mth.tan(mth.radians(a))
    def log(a):
        """ đây là hàm log, nó sẽ trả về log của a """
        return mth.log(mth.radians(a))
    def sqrt(a):
        """ đây là hàm sqrt, nó sẽ trả về căn bậc hai của a """
        return mth.sqrt(a)
    def pow(a, x):
        """ đây là hàm pow, nó sẽ trả về a mũ x """
        return mth.pow(a, x)
    def ptg(a, b):
        """ đây là hàm ptg, nó sẽ tính toán cạnh huyền của tam giác vuông có hai cạnh góc vuông là a và b """
        return mth.sqrt(pow(a, 2) + pow(b, 2))
    def log10(a):
        """ đây là hàm log10, nó sẽ trả về log cơ số 10 của a """
        return mth.log10(a)
    def log2(a):
        """ đây là hàm log2, nó sẽ trả về log cơ số 2 của a """
        return mth.log2(a)
    def Psquare(a):
        """ đây là hàm Psquare, nó sẽ trả về chu vi của hình vuông có cạnh a """
        return a * 4
    def Prect(a, b):
        """ đây là hàm Prect, nó sẽ trả về chu vi của hình chữ nhật có chiều dài a và chiều rộng b """
        return (a + b) * 2
    def Ptria3(a, b, c):
        """ đây là hàm Ptria3, nó sẽ trả về chu vi của tam giác có ba cạnh a, b và c """
        return a + b + c
    def Prhom(a):
        """ đây là hàm Prhom, nó sẽ trả về chu vi của hình thoi có cạnh a """
        return a * 4
    def Pparam(a, b):
        """ đây là hàm Pparam, nó sẽ trả về chu vi của hình bình hành có hai cạnh a và b """
        return (a + b) * 2
    def Ptrape(a, b, c, d):
        """ đây là hàm Ptrape, nó sẽ trả về chu vi của hình thang có bốn cạnh a, b, c và d """
        return a + b + c + d
    def Pcir1(d):
        """ đây là hàm Pcir1, nó sẽ trả về chu vi của hình tròn có đường kính d """
        return d * mth.pi
    def Pcir2(r):
        """ đây là hàm Pcir2, nó sẽ trả về chu vi của hình tròn có bán kính r """
        return r * 2 * mth.pi
    def Psemi(r):
        """ đây là hàm Psemi, nó sẽ trả về chu vi của hình bán nguyệt có bán kính r """
        return (r * mth.pi) + (2 * r)
    def Pelip(a, b):
        """ đây là hàm Pelip, nó sẽ trả về chu vi của hình elip có hai trục a và b """
        return mth.pi * (3 * (a + b) - mth.sqrt(3 * (a + b) * (a + (3 * b))))
    def Srect(a, b):
        """ đây là hàm Srect, nó sẽ trả về diện tích của hình chữ nhật có chiều dài a và chiều rộng b """
        return a * b
    def Ssquare(a):
        """ đây là hàm Ssquare, nó sẽ trả về diện tích của hình vuông có cạnh a """
        return a * a
    

class const():
    def pi():
        """ đây là hàm pi, nó sẽ trả về giá trị của số pi """
        return mth.pi
    def planck():
        """ đây là hàm planck, nó sẽ trả về giá trị của hằng số Planck """
        return 6,62607015e23
    def e():
        """ đây là hàm e, nó sẽ trả về giá trị của số e """
        return mth.e
    def c():
        """ đây là hàm c, nó sẽ trả về giá trị của tốc độ ánh sáng trong chân không """
        return 299792458
    def g():
        """ đây là hàm g, nó sẽ trả về giá trị của gia tốc trọng trường trên bề mặt Trái Đất """
        return 9,80665
    def avogadro():
        """ đây là hàm avogadro, nó sẽ trả về giá trị của hằng số Avogadro """
        return 6,02214076e23
    def boltzmann():
        """ đây là hàm boltzmann, nó sẽ trả về giá trị của hằng số Boltzmann """
        return 1,380649e-23
    def gas():
        """ đây là hàm gas, nó sẽ trả về giá trị của hằng số khí lý tưởng """
        return 8,314462618
    def electron():
        """ đây là hàm electron, nó sẽ trả về giá trị của điện tích của electron """
        return -1,602176634e-19
    def proton():
        """ đây là hàm proton, nó sẽ trả về giá trị của điện tích của proton """
        return 1,602176634e-19
    def neutron():
        """ đây là hàm neutron, nó sẽ trả về giá trị của khối lượng của neutron """
        return 1,67492749804e-27
    def electronmass():
        """ đây là hàm electronmass, nó sẽ trả về giá trị của khối lượng của electron """
        return 9,1093837015e-31
    def protonmass():
        """ đây là hàm protonmass, nó sẽ trả về giá trị của khối lượng của proton """
        return 1,007276466621e-27
    def neutronmass():
        """ đây là hàm neutronmass, nó sẽ trả về giá trị của khối lượng của neutron """  
        return 1,00866491588e-27
    def avogadromass():
        """ đây là hàm avogadromass, nó sẽ trả về giá trị của khối lượng mol của một chất """
        return 1 / 6,02214076e23 
    def G():
        """ đây là hàm G, nó sẽ trả về giá trị của hằng số hấp dẫn """
        return 6,67430e-11
    def E0():
        """ đây là hàm E0, nó sẽ trả về giá trị của hằng số điện môi trong chân không """
        return 8,854187817e-12
    def atm():
        """ đây là hàm atm, nó sẽ trả về giá trị của hằng số từ môi trường trong chân không """
        return 1,25663706212e-6
    def k():
        """ đây là hàm k, nó sẽ trả về giá trị của hằng số Coulomb """
        return 8,9875517923e9
    def gold():
        """ đây là hàm gold, nó sẽ trả về giá trị của tỷ lệ vàng """
        return 1,61803398875
    def silver():
        """ đây là hàm silver, nó sẽ trả về giá trị của tỷ lệ bạc """
        return 2,41421356237
    def bronze():
        """ đây là hàm bronze, nó sẽ trả về giá trị của tỷ lệ đồng """
        return 3,30277563773
    def atm():
        """ đây là hàm atm, nó sẽ trả về giá trị của áp suất khí quyển tiêu chuẩn """
        return 101325
    def calo():
        """ đây là hàm calo, nó sẽ trả về giá trị của calo """
        return 4,184
    def kcalo():
        """ đây là hàm kcalo, nó sẽ trả về giá trị của kilocalo """
        return 4184
    def lightyear():
        """ đây là hàm lightyear, nó sẽ trả về giá trị của năm ánh sáng """
        return 9,4607e15
    def parsec():
        """ đây là hàm parsec, nó sẽ trả về giá trị của parsec """
        return 3,0857e16
    def au():
        """ đây là hàm au, nó sẽ trả về giá trị của đơn vị thiên văn """
        return 149597870700
    def amu():
        """ đây là hàm amu, nó sẽ trả về giá trị của đơn vị khối lượng nguyên tử """
        return 1,66053906660e-27  
    def barn():
        """ đây là hàm barn, nó sẽ trả về giá trị của đơn vị diện tích hạt nhân """
        return 1e-28
    def ly():
        """ đây là hàm ly, nó sẽ trả về giá trị của đơn vị năm ánh sáng """
        return 9,4607e15
    def pc():
        """ đây là hàm pc, nó sẽ trả về giá trị của đơn vị parsec """
        return 3,0857e16
    def omega():
        """ đây là hàm omega, nó sẽ trả về giá trị của đơn vị góc radian """
        return 1
    def hbar():
        """ đây là hàm hbar, nó sẽ trả về giá trị của hằng số Planck rút gọn """
        return 1,054571817e-34
    def fine():
        """ đây là hàm fine, nó sẽ trả về giá trị của hằng số cấu trúc tinh tế """
        return 1/137.035999084
    def bohr():
        """ đây là hàm bohr, nó sẽ trả về giá trị của bán kính Bohr """
        return 5,29177210903e-11
    def rydberg():
        """ đây là hàm rydberg, nó sẽ trả về giá trị của hằng số Rydberg """
        return 10973731.568160
    def supergold():
        """ đây là hàm supergold, nó sẽ trả về giá trị của tỷ lệ vàng siêu phàm """
        return 1,902160583104
    def superbronze():
        """ đây là hàm superbronze, nó sẽ trả về giá trị của tỷ lệ đồng siêu phàm """
        return 3,73205080757
    def supersilver():
        """ đây là hàm supersilver, nó sẽ trả về giá trị của tỷ lệ bạc siêu phàm """
        return 2,41421356237
    def magicangle():
        """ đây là hàm magicangle, nó sẽ trả về giá trị của góc ma thuật """
        return 54.735610317245
    def goldenangle():
        """ đây là hàm goldenangle, nó sẽ trả về giá trị của góc vàng """
        return 137.507764050037
    def silverangle():
        """ đây là hàm silverangle, nó sẽ trả về giá trị của góc bạc """
        return 99.735610317245
    def bronzeangle():
        """ đây là hàm bronzeangle, nó sẽ trả về giá trị của góc đồng """
        return 120
    def somos():
        """ đây là hàm somos, nó sẽ trả về giá trị của dãy Somos """
        return [1, 1, 1, 1]
    def fibonacci(n):
        """ đây là hàm fibonacci, nó sẽ trả về giá trị của dãy Fibonacci tại vị trí n """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return function_math.fibonacci(n-1) + function_math.fibonacci(n-2)
    def lucas(n):
        """ đây là hàm lucas, nó sẽ trả về giá trị của dãy Lucas tại vị trí n """
        if n == 0:
            return 2
        elif n == 1:
            return 1
        else:
            return function_math.lucas(n-1) + function_math.lucas(n-2)
    def catalan(n):
        """ đây là hàm catalan, nó sẽ trả về giá trị của dãy Catalan tại vị trí n """
        if n == 0:
            return 1
        else:
            return function_math.catalan(n-1) * (2 * (2 * n - 1)) // (n + 1)
    def bell(n):
        """ đây là hàm bell, nó sẽ trả về giá trị của dãy Bell tại vị trí n """
        bell = [[0 for i in range(n+1)] for j in range(n+1)]
        bell[0][0] = 1
        for i in range(1, n+1):
            bell[i][0] = bell[i-1][i-1]
            for j in range(1, i+1):
                bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
        return bell[n][0]
    def tribonacci(n):
        """ đây là hàm tribonacci, nó sẽ trả về giá trị của dãy Tribonacci tại vị trí n """
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return function_math.tribonacci(n-1) + function_math.tribonacci(n-2) + function_math.tribonacci(n-3)
    def tetranacci(n):
        """ đây là hàm tetranacci, nó sẽ trả về giá trị của dãy Tetranacci tại vị trí n """
        if n == 0:
            return 0
        elif n == 1 or n == 2 or n == 3:
            return 1
        else:
            return function_math.tetranacci(n-1) + function_math.tetranacci(n-2) + function_math.tetranacci(n-3) + function_math.tetranacci(n-4)    
    def pentanacci(n):
        """ đây là hàm pentanacci, nó sẽ trả về giá trị của dãy Pentanacci tại vị trí n """
        if n == 0:
            return 0
        elif n == 1 or n == 2 or n == 3 or n == 4:
            return 1
        else:
            return function_math.pentanacci(n-1) + function_math.pentanacci(n-2) + function_math.pentanacci(n-3) + function_math.pentanacci(n-4) + function_math.pentanacci(n-5)        
    def hexagonal(n):
        """ đây là hàm hexagonal, nó sẽ trả về giá trị của dãy Hexagonal tại vị trí n """
        return n * (2 * n - 1)
    def heptagonal(n):
        """ đây là hàm heptagonal, nó sẽ trả về giá trị của dãy Heptagonal tại vị trí n """
        return n * (5 * n - 3) // 2
    def octagonal(n):
        """ đây là hàm octagonal, nó sẽ trả về giá trị của dãy Octagonal tại vị trí n """
        return n * (3 * n - 2)
    def centered_hexagonal(n):
        """ đây là hàm centered_hexagonal, nó sẽ trả về giá trị của dãy Centered Hexagonal tại vị trí n """
        return 3 * n * (n - 1) + 1
    def centered_heptagonal(n):
        """ đây là hàm centered_heptagonal, nó sẽ trả về giá trị của dãy Centered Heptagonal tại vị trí n """
        return (7 * n * n - 7 * n + 2) // 2
    def centered_octagonal(n):
        """ đây là hàm centered_octagonal, nó sẽ trả về giá trị của dãy Centered Octagonal tại vị trí n """
        return n * (2 * n - 1)
    def centered_square(n):
        """ đây là hàm centered_square, nó sẽ trả về giá trị của dãy Centered Square tại vị trí n """
        return n * n + (n - 1) * (n - 1)
    def centered_triangular(n):
        """ đây là hàm centered_triangular, nó sẽ trả về giá trị của dãy Centered Triangular tại vị trí n """
        return (3 * n * n - 3 * n + 2) // 2
    def centered_pentagonal(n):
        """ đây là hàm centered_pentagonal, nó sẽ trả về giá trị của dãy Centered Pentagonal tại vị trí n """
        return (5 * n * n - 5 * n + 2) // 2
    def centered_decagonal(n):
        """ đây là hàm centered_decagonal, nó sẽ trả về giá trị của dãy Centered Decagonal tại vị trí n """
        return n * (5 * n - 3) + 1
    def centered_dodecagonal(n):
        """ đây là hàm centered_dodecagonal, nó sẽ trả về giá trị của dãy Centered Dodecagonal tại vị trí n """
        return n * (6 * n - 5) + 1
    def centered_icosagonal(n):
        """ đây là hàm centered_icosagonal, nó sẽ trả về giá trị của dãy Centered Icosagonal tại vị trí n """
        return n * (10 * n - 9) + 1
    def centered_icositriagonal(n):
        """ đây là hàm centered_icositriagonal, nó sẽ trả về giá trị của dãy Centered Icositriagonal tại vị trí n """
        return n * (20 * n - 19) + 1
    def centered_icositetragonal(n):
        """ đây là hàm centered_icositetragonal, nó sẽ trả về giá trị của dãy Centered Icositetragonal tại vị trí n """
        return n * (40 * n - 39) + 1
    def centered_icosipentagonal(n):
        """ đây là hàm centered_icosipentagonal, nó sẽ trả về giá trị của dãy Centered Icosipentagonal tại vị trí n """
        return n * (80 * n - 79) + 1
    def centered_icosiheptagonal(n):
        """ đây là hàm centered_icosiheptagonal, nó sẽ trả về giá trị của dãy Centered Icosiheptagonal tại vị trí n """
        return n * (160 * n - 159) + 1
    def centered_icosioctagonal(n):
        """ đây là hàm centered_icosioctagonal, nó sẽ trả về giá trị của dãy Centered Icosioctagonal tại vị trí n """
        return n * (320 * n - 319) + 1
    def centered_icosisquare(n):
        """ đây là hàm centered_icosisquare, nó sẽ trả về giá trị của dãy Centered Icosisquare tại vị trí n """
        return n * (640 * n - 639) + 1
    def centered_icositriangular(n):
        """ đây là hàm centered_icositriangular, nó sẽ trả về giá trị của dãy Centered Icositriangular tại vị trí n """
        return n * (1280 * n - 1279) + 1
