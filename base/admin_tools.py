# -*- coding: utf-8 -*-
# pylint: disable=C0103

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def __init__(self):
        self.list_indent = 0
        self.is_in_reference = False
        self.reference_args = None
        self.first_already_set = False
        self.doc_cursor = None
        self.pptx_txBox = None
        HTMLParser.__init__(self, convert_charrefs=True)

    def set_pptx_txBox(self, val):
        self.pptx_txBox = val

    def handle_starttag(self, tag, attrs):
        # print("handle_starttag(%s, %s)", tag, attrs)
        if tag.strip() == 'ul':
            self.list_indent += 1
        elif tag.strip() == 'a':
            self.is_in_reference = True
            self.reference_args = attrs

    def handle_endtag(self, tag):
        # print("handle_endtag(%s)", tag)
        if tag.strip() == 'ul' and self.list_indent > 0:
            self.list_indent -= 1
        elif tag.strip() == 'a':
            self.is_in_reference = False
            self.reference_args = None

    def handle_data(self, data):
        # print("handle_data(%s)", data)
        if self.is_in_reference is True:
            for arg_key, arg_val in self.reference_args:
                if arg_key.strip() == 'href':
                    r = self.doc_cursor.add_run()
                    r.text = " " + data.strip()
                    hlink = r.hyperlink
                    hlink.address = arg_val
        elif len(data.strip()) > 0:
            if self.first_already_set is True:
                self.doc_cursor = self.pptx_txBox.add_paragraph()
            else:
                self.first_already_set = True
                self.doc_cursor = self.pptx_txBox
            self.doc_cursor.text = data.strip()
            self.doc_cursor.level = self.list_indent
