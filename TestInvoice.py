import pytest
from Invoice import Invoice
@pytest.fixture()
def products():
    products = {'Pen' : {'qnt' : 10, 'unit_price' : 3.75, 'discount' : 5},
                'Notebook': {'qnt': 5,'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):

    invoice.totalImpurePrice(products)
    assert invoice.totalDiscount(products) == 5.62
#Test case for checking if no student discount works
def test_CanCalculateTotalPurePriceWithoutStudent(invoice, products):
    student = 'n'
    invoice.totalPurePrice(products,student)
    assert invoice.totalPurePrice(products,student) == 69.38

#Test case for checking if student discount works
def test_CanCalculateTotalPurePriceWithStudent(invoice, products):
    student='y'
    invoice.totalPurePrice(products,student)
    assert invoice.totalPurePrice(products,student) == 65.62



