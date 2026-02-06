dict_= {'mercury':0.2408467,'venus':0.61519726,'earth':1.0,'mars':1.8808158,'jupiter':11.862615,'saturn':29.447498,'uranus':84.016846,'neptune':164.79132}
class SpaceAge:
    def __init__(self,seconds):
        self.seconds = seconds
    def on_mercury(self):
        years = dict_['mercury'] * 365.25
        age_years = self.seconds/(60*60*24*years)
        return round(age_years,2)
    def on_venus(self):
        years = dict_['venus'] * 365.25
        age_years = self.seconds/(60*60*24*years)
        return round(age_years,2)
    def on_earth(self):
        age_years = self.seconds/(60*60*24*365.25)
        return round(age_years,2)
    def on_mars(self):
        years = dict_['mars'] * 365.25
        age_years = self.seconds/(60*60*24*years)
        return round(age_years,2)
    def on_jupiter(self):
        years = dict_['jupiter'] * 365.25
        age_years = self.seconds/(60*60*24*years)
        return round(age_years,2)
    def on_saturn(self):
        years = dict_['saturn'] * 365.25
        age_years = self.seconds/(60*60*24*years)
        return round(age_years,2)
    def on_uranus(self):
        years = dict_['uranus'] * 365.25
        age_years = self.seconds/(60*60*24*years)
        return round(age_years,2)
    def on_neptune(self):
        years = dict_['neptune'] * 365.25
        age_years = self.seconds/(60*60*24*years)
        return round(age_years,2)
