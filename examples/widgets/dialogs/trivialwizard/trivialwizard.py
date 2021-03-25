
#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2016 The Qt Company Ltd.
## Contact: http://www.qt.io/licensing/
##
## This file is part of the Qt for Python examples of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
## $QT_END_LICENSE$
##
#############################################################################

"""PySide6 port of the widgets/dialogs/trivialwizard example from Qt v5.x"""

from PySide6 import QtWidgets


def create_intro_page():
    page = QtWidgets.QWizardPage()
    page.setTitle("Introduction")

    label = QtWidgets.QLabel("This wizard will help you register your copy of "
            "Super Product Two.")
    label.setWordWrap(True)

    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(label)
    page.setLayout(layout)

    return page


def create_registration_page():
    page = QtWidgets.QWizardPage()
    page.setTitle("Registration")
    page.setSubTitle("Please fill both fields.")

    name_label = QtWidgets.QLabel("Name:")
    name_line_edit = QtWidgets.QLineEdit()

    email_label = QtWidgets.QLabel("Email address:")
    email_line_edit = QtWidgets.QLineEdit()

    layout = QtWidgets.QGridLayout()
    layout.addWidget(name_label, 0, 0)
    layout.addWidget(name_line_edit, 0, 1)
    layout.addWidget(email_label, 1, 0)
    layout.addWidget(email_line_edit, 1, 1)
    page.setLayout(layout)

    return page


def create_conclusion_page():
    page = QtWidgets.QWizardPage()
    page.setTitle("Conclusion")

    label = QtWidgets.QLabel("You are now successfully registered. Have a nice day!")
    label.setWordWrap(True)

    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(label)
    page.setLayout(layout)

    return page


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)

    wizard = QtWidgets.QWizard()
    wizard.addPage(create_intro_page())
    wizard.addPage(create_registration_page())
    wizard.addPage(create_conclusion_page())

    wizard.setWindowTitle("Trivial Wizard")
    wizard.show()

    sys.exit(wizard.exec_())
