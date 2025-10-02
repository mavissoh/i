from flask_login import login_required, current_user
from flask import request, Blueprint, render_template, flash, redirect

from models.loan import Loan

loansBlueprint = Blueprint("loans", __name__)

def goBack():
    # go back to the page that posted the form
    return redirect(request.referrer)

@loansBlueprint.post('/loans/add/<title>')
@login_required
def addLoan(title):
    book = Loan.findBook(title)
    flash(Loan.createLoan(book=book, member=current_user))
    return goBack()

@loansBlueprint.post('/loans/return/<title>')
@login_required
def returnLoan(title):
    book = Loan.findBook(title)
    flash(Loan.updateLoan(book=book, member=current_user, renew=False))
    return goBack()

@loansBlueprint.post('/loans/renew/<title>')
@login_required
def renewLoan(title):
    book = Loan.findBook(title)
    flash(Loan.updateLoan(book=book, member=current_user, renew=True))
    return goBack()

@loansBlueprint.post('/loans/delete/<title>')
@login_required
def deleteLoan(title):
    book = Loan.findBook(title)
    flash(Loan.deleteLoan(book=book, member=current_user))
    return goBack()

@loansBlueprint.route('/loans')
@login_required
def showLoans():
    loans = Loan.retrieveLoans(member=current_user)
    return render_template("loans.html", loans=loans, panel="Current Loans")