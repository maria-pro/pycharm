# This is a sample Python script.
import pandas as pd
from transformers import pipeline
print(pipeline('sentiment-analysis')('I love you'))


