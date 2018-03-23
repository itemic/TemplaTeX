import os
import sys
import math

# Globals
DOC_START = "\\begin{document}"
DOC_END = "\\end{document}"

class TeXFile:
	def __init__(self, name="default", font_size=None):
		self.name = f"{name}.tex"
		if font_size is None:
			self.font_size = 11
		else:
			self.font_size = font_size
		self.documentclass = f"\\documentclass[{self.font_size}pt,a4paper]"

	def generate(self):
		f = open(self.name, "w+")
		f.write(self.documentclass + "\n")
		f.write(DOC_START + "\n")
		f.write(DOC_END)
		f.close()

t = TeXFile()
t.generate()