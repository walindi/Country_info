from countryinfo import CountryInfo

count = input ("Enter country name: ")
country = CountryInfo(count)

print("Capital is: ",country.capital())
print("Currency is: ",country.currencies())
print("Language is: ",country.languages())
print("Borders are: ",country.borders())
print("Other names are: ",country.alt_spellings())
