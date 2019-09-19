monthCoversions = {
   "jan": "January",
   "Mar": "March",#
}

print (monthCoversions["Mar"])
print (monthCoversions.get("jan"))
print (monthCoversions.get("love", "Not a valid word"))

a={"one":1}

b={"two":2}
b=a
print (a)
print (b)


