#------------------------import important packages-----------------------------#
from GetPaper import GET_PAPER
import pdfplumber
import os
import fitz
import json
#------------------------CLASS PDF PARSER-----------------------------#


paper = GET_PAPER("High-Performance Rotation Invariant Multiview Face Detection")


def GET_TEXT(path = paper): 
        # Read pdf into list of DataFrame
        results = [] # list of tuples that store the information as (text, font size, font name) 
        doc = fitz.open(path) # filePath is a string that contains the path to the pdf
        for page in doc:
            dict = doc[0].get_text("dict")
            blocks = dict["blocks"]
            print(blocks)
            for block in blocks:
                if "lines" in block.keys():
                    spans = block['lines']
                    for span in spans:
                        data = span['spans']
                        