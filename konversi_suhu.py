print("Program Konversi Suhu dari Celcius")
print("===================================")
print()

celcius = float(input("Masukkan suhu dalam derajat Celcius: "))

def fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def reamur(celcius):
    reamur = celcius * 4/5
    return reamur

def kelvin(celcius):
    kelvin = celcius + 273 
    return kelvin

print(f"\nHasil Konversi:")
print(f"{celcius}°C = {fahrenheit(celcius)}°F")
print(f"{celcius}°C = {reamur(celcius)}°R")
print(f"{celcius}°C = {kelvin(celcius)}K")

#pseudocode
"""
BEGIN
    PRINT "Program Konversi Suhu dari Celcius"
    PRINT "==================================="
    PRINT newline
    
    INPUT celcius WITH PROMPT "Masukkan suhu dalam derajat Celcius: "
    
    // Conversion functions
    FUNCTION fahrenheit(celcius)
        RETURN (celcius × 9/5) + 32
    END FUNCTION
    
    FUNCTION reamur(celcius)
        RETURN celcius × 4/5
    END FUNCTION
    
    FUNCTION kelvin(celcius)
        RETURN celcius + 273
    END FUNCTION
    
    // Display results
    PRINT newline
    PRINT "Hasil Konversi:"
    PRINT celcius + "°C = " + fahrenheit(celcius) + "°F"
    PRINT celcius + "°C = " + reamur(celcius) + "°R"
    PRINT celcius + "°C = " + kelvin(celcius) + "K"
END
"""
