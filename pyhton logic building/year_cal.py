def century(year):
     if year <= 0:
        return "0"
     elif year <= 100:
        return "1"
     elif year % 100 == 0:
        return f"{year // 100}"
     else:
        return f"{year // 100 + 1}"

def century(year):
    return (year - 1) // 100 + 1

# Example usage:
year = 1970
print(century(year)) 
year = 1705
print(century(year))