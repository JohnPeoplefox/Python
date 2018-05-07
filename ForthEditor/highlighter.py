
from PyQt5.QtGui import  (
    QSyntaxHighlighter, QFont,
    QTextCharFormat)
    
from PyQt5.QtCore import (
    Qt, QRegularExpression)


class Highlighter(QSyntaxHighlighter):

    def __init__(self, parent=None):
        
        super(Highlighter, self).__init__(parent)

        self.highlighting_rules = list()
        
        self.keywordFormat = QTextCharFormat()
        self.keywordFormat.setForeground(Qt.darkBlue)
        self.keywordFormat.setFontWeight(QFont.Bold)
        
        self.keyword_patterns = [
            '\\babort\\b', '\\bexit\\b',  '\\bdo\\b',
            '\\bloop\\b', '\\bunloop\\b', '\\bbegin\\b',
            '\\buntil\\b', '\\bwhile\\b', '\\brepeat\\b',
            '\\bexit\\b', '\\bif\\b', '\\belse\\b',
            '\\bthen\\b', '\\bcase\\b', '\\bendcase\\b',
            '\\bof\\b', '\\bendof\\b', '\\bagain\\b',
            '\\bleave\\b', '\\brequire\\b', '\\bincluded\\b',
            '\\bdecimal\\b', '\\bhex\\b', '\\balso\\b',
            '\\bonly\\b', '\\bprevious\\b', '\\bcreate\\b',
            '\\bdoes>\\b', '\\bvariable\\b', 'b\\value\\b',
            '\\b2variable\\b', '\\bconstant\\b', '\\babort"\\b',
            '\\bdup\\b', '\\bdrop\\b', '\\bswap\\b',
            '\\bover\\b', '\\bpick\\b', '\\broll\\b',
            '\\b2dup\\b', '\\b2drop\\b', '\\b2swas\\b',
            '\\b2over\\b', '\\b!\\b', '\\bc!\\b', '\\brot\\b',
            '\\b@\\b', '\\bc@\\b', '\\b2!\\b', '\\b2@\\b',
            '\\band\\b', '\\bor\\b', '\\bxor\\b', '\\binvert\\b',
            '\\bnegate\\b', '\\b/\\b', '\\b/mod\\b', '\\bbye\\b',
            '\\bmod\\b', '\\brshift\\b', '\\blshift\\b']

        for pattern in self.keyword_patterns:
            self.highlighting_rules.append(
                [QRegularExpression(pattern),
                 self.keywordFormat])


    def highlightBlock(self, text):

        for rule in self.highlighting_rules:

            match_iterator = rule[0].globalMatch(text)
            
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(),
                    match.capturedLength(), rule[1])

        self.setCurrentBlockState(0)
