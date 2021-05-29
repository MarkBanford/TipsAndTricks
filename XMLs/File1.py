import pandas as pd
import pandas_read_xml as pdx

data = pdx.read_xml('https://www.sec.gov/Archives/edgar/data/1000351/000114554921012283/primary_doc.xml', ['edgarSubmission'])