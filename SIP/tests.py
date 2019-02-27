import pytest
import pistusPayment.py
import brouillons.py

def test_read_float() :
    assert(pistusPayment.read_float("1 234,56€") == 1234.56)
    assert(pistusPayment.read_float("100.20") == 100.20)
    assert(pistusPayment.read_float("£200.65") == 200.65)

def test_check_word() :
    assert brouillons.print_check('python', 'yponth')
    assert brouillons.print_check('', '')
    assert brouillons.print_check('', 'c')
    assert not brouillons.print_check('c', '')
    assert brouillons.print_check('python', 'yponths')
    assert not brouillons.print_check('pythons', 'yponth')

def test_update_turns():
    assert brouillons.check_guess('p', 'python', 9) == (True, 9)
    assert brouillons.check_guess('a', 'python', 9) == (False, 8)
    assert brouillons.check_guess('', '', 9) == (True, 9)
    assert brouillons.check_guess('', 'c', 9) == (True, 9)
    assert brouillons.check_guess('a', '', 9) == (False, 8)

def test_get_guessed_word():
    assert brouillons.get_guessed_word('', '') == ''
    assert brouillons.get_guessed_word('', 'c') == ''
    assert brouillons.get_guessed_word('centralesupelec', '') == '***************'
    assert brouillons.get_guessed_word('centralesupelec', 'c') == 'c*************c'
    assert brouillons.get_guessed_word('centralesupelec', 'cs') == 'c*******s*****c'
    assert brouillons.get_guessed_word('centralesupelec', 'centralsup') == 'centralesupelec'
    assert brouillons.get_guessed_word('centralesupelec', 'supcentral') == 'centralesupelec'

def test_check_guessed_word():
    assert brouillons.check_guessed_word('', '')
    assert brouillons.check_guessed_word('', 'c')
    assert not brouillons.check_guessed_word('centralesupelec', '')
    assert not brouillons.check_guessed_word('centralesupelec', 'cs')
    assert brouillons.check_guessed_word('centralesupelec', 'centralsup')
    assert brouillons.check_guessed_word('centralesupelec', 'supcentral')

def test_calc_score():
    assert brouillons.calc_score('', 0) == 0
    assert brouillons.calc_score('guess', 4) == 9
    assert brouillons.calc_score('guess', 8) == 5
