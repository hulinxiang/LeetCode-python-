def my_func(astring):
    l = []
    s = ""
    for i in range(len(astring)):
        if "a" <= astring[i] <= "z":  # lower-case letter
            astring.isalpha()
            # do special thing with first element
            if i == len(astring) - 1:
                l = l + [s]
        elif "A" <= astring[i] <= "Z":  # character is a number
            s = s + astring[i]
            # do special thing with first element
            if i == len(astring) - 1:
                l = l + [s]
        else:
            # upper-case letter
            if len(s) == 0:
                i = i - 1 + 1
            else:
                l = l + [s]

            s = ""  # set s to empty string
    return l
