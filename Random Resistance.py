from math import pi, sin, sqrt, fabs
import random
import time

def GenerateRandomResistanceLine(sigma1, sigma2, sigma3, accuracy):
    Resistanceline = []
    i = 0
    while i <= 1:
        tetta = 2 * pi * i
        i += accuracy
        g = 0
        while g <= 1:
            sinphi = (2 * g) - 1
            cosphi = sqrt(1 - (sinphi * sinphi))
            sintetta = sin(tetta)
            costetta = sqrt(1 - (sintetta * sintetta))
            g += accuracy
            x = fabs(sintetta * cosphi)
            y = fabs(sintetta * sinphi)
            z = fabs(costetta)
            Resistance = (sigma1 * x) + (sigma2 * y) + (sigma3 * z)
            Resistanceline.append(Resistance)
    return Resistanceline

# не рекомендуется выставлять значение accuracy ниже 0.003
# при accuracy = 0.005 время генерации списка около 5 секунд
# среднее время выбора случайного элемента 1.5*E(-6) секунд
# пример выбора случайного числа из построенного списка ниже
# a = GenerateRandomResistanceLine(100 , 90, 7, 0.0005)
# b = random.choice(a)

def NormalizedVectorProduct(a:list, b:list):
    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]
    z1 = a[2]
    z2 = b[2]
    x = y1 * z2 - y2 * z1
    y = x2 * z1 - x1 * z2
    z = x1 * y2 - x2 * y1
    k = 1/(sqrt((x * x) + (y * y) + (z * z)))
    NormalizedVector = []
    NormalizedVector.append(x*k)
    NormalizedVector.append(y*k)
    NormalizedVector.append(z*k)
    return NormalizedVector

def RandomVectorLine(accuracy):
    RandomVectorLine = []
    i = 0
    while i <= 1:
        tetta = 2 * pi * i
        i += accuracy
        g = 0
        while g <= 1:
            sinphi = (2 * g) - 1
            cosphi = sqrt(1 - (sinphi * sinphi))
            sintetta = sin(tetta)
            costetta = sqrt(1 - (sintetta * sintetta))
            g += accuracy
            x = sintetta * cosphi
            y = sintetta * sinphi
            z = costetta
            RVector = []
            RVector.append(x)
            RVector.append(y)
            RVector.append(z)
            RandomVectorLine.append(RVector)
    return RandomVectorLine

def Random6ResistanceLine(sigma1, sigma2, sigma3, accuracy, RandomResistance6LineLength):
    RVLine = RandomVectorLine(accuracy)
    i = 0
    Random6ResistanceLine = []
    d1 = 1 / (2 * sqrt(3))
    d2 = 0.5
    d3 = sqrt((2 / 3))
    lc = 1
    lv = 1
    ls = 1
    for i in range(RandomResistance6LineLength):
        xx = random.choice(RVLine)
        g = random.choice(RVLine)
        Random6ResistanceLine = []
        if xx == g:
            while not g == xx:
                g = random.choice(RVLine)
        zz = NormalizedVectorProduct(a, g)
        yy = NormalizedVectorProduct(a, c)
        c = []
        fyy0 = fabs(yy[0])
        fyy1 = fabs(yy[1])
        fyy2 = fabs(yy[2])
        fzz0 = fabs(zz[0])
        fzz1 = fabs(zz[1])
        fzz2 = fabs(zz[2])
        c.append(yy[0])
        c.append(yy[1])
        c.append(yy[2])
        v = []
        v.append(zz[0])
        v.append(zz[1])
        v.append(zz[2])
        s1 = []
        s2 = []
        s3 = []
        s4 = []
        d1xx0 = d1 * xx[0]
        d2yy0 = d2 * yy[0]
        d3zz0 = d3 * zz[0]
        d1xx1 = d1 * xx[1]
        d2yy1 = d2 * yy[1]
        d3zz1 = d3 * zz[1]
        d1xx2 = d1 * xx[2]
        d2yy2 = d2 * yy[2]
        d3zz2 = d3 * zz[2]
        s1.append(d1xx0 + d2yy0 + d3zz0)
        s1.append(d1xx1 + d2yy1 + d3zz1)
        s1.append(d1xx2 + d2yy2 + d3zz2)
        s2.append(d1xx0 + d2yy0 - d3zz0)
        s2.append(d1xx1 + d2yy1 - d3zz1)
        s2.append(d1xx2 + d2yy2 - d3zz2)
        s3.append(d1xx0 - d2yy0 + d3zz0)
        s3.append(d1xx1 - d2yy1 + d3zz1)
        s3.append(d1xx2 - d2yy2 + d3zz2)
        s4.append(d1xx0 - d2yy0 - d3zz0)
        s4.append(d1xx1 - d2yy1 - d3zz1)
        s4.append(d1xx2 - d2yy2 - d3zz2)
        Rc = (sigma1 * fyy0 + sigma2 * fyy1 + sigma3 * fyy2) * lc
        Rv = (sigma1 * fzz0 + sigma2 * fzz1 + sigma3 * fzz2) * lv
        Rs1 = ls * ((sigma1 * fabs(d1xx0 + d2yy0 + d3zz0)) + (sigma2 * fabs(d1xx1 + d2yy1 + d3zz1)) + (sigma3 * fabs(d1xx2 + d2yy2 + d3zz2)))
        Rs2 = ls * ((sigma1 * fabs(d1xx0 + d2yy0 - d3zz0)) + (sigma2 * fabs(d1xx1 + d2yy1 - d3zz1)) + (sigma3 * fabs(d1xx2 + d2yy2 - d3zz2)))
        Rs3 = ls * ((sigma1 * fabs(d1xx0 - d2yy0 + d3zz0)) + (sigma2 * fabs(d1xx1 - d2yy1 + d3zz1)) + (sigma3 * fabs(d1xx2 - d2yy2 + d3zz2)))
        Rs4 = ls * ((sigma1 * fabs(d1xx0 - d2yy0 - d3zz0)) + (sigma2 * fabs(d1xx1 - d2yy1 - d3zz1)) + (sigma3 * fabs(d1xx2 - d2yy2 - d3zz2)))
        R6 = []
        R6.append(Rc)
        R6.append(Rv)
        R6.append(Rs1)
        R6.append(Rs2)
        R6.append(Rs3)
        R6.append(Rs4)
        Random6ResistanceLine.append(R6)
    return Random6ResistanceLine

# строки с append на с v и si можно удалить