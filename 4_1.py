# coding=utf-8

import numpy as np


numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
numeric_strings.astype(float)
print(numeric_strings.dtype)