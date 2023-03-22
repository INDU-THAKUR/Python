#6. formatting a string

txt = "We have {:<8} chickens."  #-> Left aligns the result (within the available space)
print(txt.format(49))


txt = "We have {:>8} chickens."  #-> Right aligns the result (within the available space)
print(txt.format(49))


txt = "We have {:^8} chickens."  #->Center aligns the result (within the available space)
print(txt.format(49))


txt = "We have {:=8} chickens."  #->Places the sign to the left most position
print(txt.format(49))


txt = "We have {:+8} chickens."  #->Use a plus sign to indicate if the result is positive or negative
print(txt.format(49))

txt = "We have {:-8} chickens."  #->Use a minus sign for negative values only
print(txt.format(49))


txt = "We have {:} chickens."    #->Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
print(txt.format(49))


txt = "We have {:,} chickens."   #->Use a comma as a thousand separator
print(txt.format(49))


txt = "We have {:_} chickens."    #->Use a underscore as a thousand separator
print(txt.format(49))

 
txt = "We have {:b} chickens."    #->Binary format
print(txt.format(49))


txt = "We have {:c} chickens."    #->Converts the value into the corresponding unicode character
print(txt.format(49))


txt = "We have {:d} chickens."    #->Decimal format
print(txt.format(49))


txt = "We have {:e} chickens."   #->Scientific format, with a lower case e
print(txt.format(49))

 
txt = "We have {:E} chickens."   #->Scientific format, with an upper case E
print(txt.format(49))


txt = "We have {:f} chickens."   #->Fix point number format
print(txt.format(49))


txt = "We have {:F} chickens."   #->Fix point number format, in uppercase format (show inf and nan as INF and NAN)
print(txt.format(49))

txt = "We have {:g} chickens."   #->General format
print(txt.format(49))

txt = "We have {:G} chickens."   #->General format (using a upper case E for scientific notations)
print(txt.format(49))

txt = "We have {:o} chickens."   #->Octal format
print(txt.format(49))

txt = "We have {:x} chickens."   #->Hex format, lower case
print(txt.format(49))

txt = "We have {:X} chickens."   #->Hex format, upper case
print(txt.format(49))

txt = "We have {:n} chickens."   #=>Number format
print(txt.format(49))

txt = "We have {:%} chickens."   #->Percentage format
print(txt.format(49))
