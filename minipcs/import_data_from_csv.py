# open file & create csvreader
import csv
import pandas

# import the relevant model
from app.models import CPU, MiniPC, BRAND

df = pandas.read_excel(
    "/home/david/Nextcloud/1. Suivi/Informatique/MiniPC.ods"
)
print(df)
# for line in csv:
#     line = parse line to a list
#     # add some custom validation\parsing for some of the fields
#
#     foo = MiniPC(brand=jkl, model=jkl)
#     try:
#         foo.save()
#     except Exception as e:
#         # if the're a problem anywhere, you wanna know about it
#         print(f"there was a problem with line {i} : {e}")
