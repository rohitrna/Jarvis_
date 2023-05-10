import webbrowser
#import Speach_to_txt as st
def SatImagery():
    new = 2
    term = input("Enter Region:")
    if (term == "US Pacific Coast"):
        tabUrl = "https://www.star.nesdis.noaa.gov/GOES/sector_band.php?sat=G17&sector=wus&band=GEOCOLOR&length=12"
    if (term == "region list"):
        print("US Pacific Coast, PACUS, North Pacific, Canada, US Atlantic Coast, Tropical Pacific, East Pacific, Central America, East Full Disk, West Full Disk")
        SatImagery()
    if (term == "PACUS"):
        tabUrl = "https://www.star.nesdis.noaa.gov/GOES/conus_band.php?sat=G17&band=GEOCOLOR&length=24"
    if (term == "North Pacific"):
        tabUrl = "https://www.star.nesdis.noaa.gov/GOES/sector_band.php?sat=G17&sector=np&band=GEOCOLOR&length=12"
    if (term == "Canada"):
        tabUrl = "https://www.star.nesdis.noaa.gov/GOES/sector_band.php?sat=G16&sector=can&band=GEOCOLOR&length=12"
    if (term == "Alaska"):
        tabUrl = "https://www.star.nesdis.noaa.gov/GOES/sector_band.php?sat=G17&sector=ak&band=GEOCOLOR&length=12"
    if (term == "US Atlantic Coast"):
        tabUrl = "https://www.star.nesdis.noaa.gov/GOES/sector_band.php?sat=G16&sector=eus&band=GEOCOLOR&length=12"
    if (term == "Tropical Pacific"):
        tabUrl = "https://www.star.nesdis.noaa.gov/GOES/sector_band.php?sat=G17&sector=tpw&band=GEOCOLOR&length=12"
    if (term == "East Pacific"):
        tabUrl = "https://www.star.nesdis.noaa.gov/GOES/sector_band.php?sat=G16&sector=eep&band=GEOCOLOR&length=12"
    if (term == "Central America"):
        tabUrl = "https://www.star.nesdis.noaa.gov/GOES/sector_band.php?sat=G16&sector=cam&band=GEOCOLOR&length=12"
    if (term == "East Full Disk"):
        tabUrl = "https://www.star.nesdis.noaa.gov/GOES/fulldisk_band.php?sat=G16&band=GEOCOLOR&length=12"
    if (term == "West Full Disk"):
        tabUrl = "https://www.star.nesdis.noaa.gov/GOES/fulldisk_band.php?sat=G17&band=GEOCOLOR&length=12"

    #term = st.listen()
    
    webbrowser.open(tabUrl)
    return()

