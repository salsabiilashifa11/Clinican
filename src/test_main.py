#import pytest
import hashlib
from shifa.signin.signin import SigninWindow
from aisha.pembelianapoteker.pembelianapoteker import toString
from detha.pembelian.pembelian import getIdTransaksi, getTotalQuantity
from adila.payment import PaymentWindow

def test_passverification():
    assert(SigninWindow.verify("shifashifa") == '5db4fc92c667e6a472482ba71cf1c4d6bbafdd3e052a09ddf186426b01aa6eac')
    assert(SigninWindow.verify("adila") == '96b9a12c78b4a7c128e0d3c0b17718d361904ed77c8b787363e34a1b2013341f')
    assert(SigninWindow.verify("kucing") != '6d4e9a15dc535e36f7f4d1a907ec86b3c66d7a704828aa97c701fcc16c4782fc')

def test_ArraytoString():
    assert(toString([100,56,85,2711,9]) == ['100','56','85','2711','9'])

def test_getIdTransaksi():
    assert(getIdTransaksi(1) == 2)
    assert(getIdTransaksi(5) == 6)
    assert(getIdTransaksi(4) != 2)

def test_getTotalQuantity():
    assert(getTotalQuantity([1,3,5]) == 9)
    assert(getTotalQuantity([2,3,1,5,6]) == 17)
    assert(getTotalQuantity([2,6,8,3,6,7,8]) != 10)

def test_paymentVerivication():
    transaksi = [(2, 5, 1, 'PROMAG 12 TABLET', 1, 20, 15600, 15600),
                 (2, 5, 2, 'BYE BYE FEVER ANAK', 2, 20, 25200, 50400)]
    assert (PaymentWindow.totalHarga(transaksi)) == 66000
