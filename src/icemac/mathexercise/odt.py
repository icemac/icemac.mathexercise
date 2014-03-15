# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .main import get_parser
from .model import generate_problems
from odf.opendocument import OpenDocumentText
from odf.style import Style, TextProperties, PageLayout, PageLayoutProperties
from odf.style import MasterPage
from odf.text import H, P


class ExcercisesDoc:

    def __init__(self, count, min, max, filename):
        self.count = count
        self.min = min
        self.max = max
        self.filename = filename

    def create_doc(self):
        doc = OpenDocumentText()

        # Page layout: A4
        pagelayout = PageLayout(name="A4")
        doc.automaticstyles.addElement(pagelayout)
        pagelayout.addElement(PageLayoutProperties(
            margin="2cm", pageheight="297mm", pagewidth="210mm",
            printorientation="portrait"))
        # Use page layout on master page, to set it:
        masterpage = MasterPage(name="Standard", pagelayoutname="A4")
        doc.masterstyles.addElement(masterpage)

        # Styles
        s = doc.styles
        self.h1style = Style(name="Heading 1", family="paragraph")
        self.h1style.addElement(TextProperties(
            attributes={'fontsize': "24pt", 'fontweight': "bold"}))
        s.addElement(self.h1style)
        return doc

    def render(self):
        doc = self.create_doc()
        for block_id in range(0, self.count, 10):
            block_num = block_id / 10 + 1
            self.render_block(doc, block_num)
        doc.save(self.filename)

    def render_block(self, doc, num):
        problems = generate_problems(10, self.min, self.max)
        self.render_subblock(doc, num, problems, 'Aufgaben', False)
        self.render_subblock(doc, num, problems, 'Lösungen', True)

    def render_subblock(self, doc, num, problems, text, show_solution):
        base = (num - 1) * 10 + 1
        doc.text.addElement(
            H(outlinelevel=1, stylename=self.h1style,
              text="{} Teil {}".format(text, num)))
        for i, p in enumerate(problems):
            p = P(text="{}) {}".format(base + i, p.render(show_solution)))
            doc.text.addElement(p)
        doc.text.addElement(P())


def main():
    parser = get_parser()
    parser.add_argument('outputfile', help='Name des Ausgabedokuments')
    args = parser.parse_args()
    doc = ExcercisesDoc(args.count, args.min, args.max, args.outputfile)
    doc.render()
