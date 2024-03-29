import re

def print_capital_words(sentence):
    words_with_space = re.findall(r'\b[A-Z][a-z]*\b', sentence)
    words_without_space = re.findall(r'[A-Z][a-z]*', sentence)

    print("Capital words with spaces:")
    for i, word in enumerate(words_with_space, start=1):
        print(f"{i}. {word}")

    print("\nCapital words without spaces:")
    for i, word in enumerate(words_without_space, start=1):
        print(f"{i}. {word}")

if __name__ == "__main__":
    input_paragraph = ("AdamsvilleAddisonAlabaster CityAlbertvilleArabArgoAritonAshlandAshvilleAthensAuburnAutaugaBarbour CountyBeauregardBeavertonBessemerBeulahBirminghamBlount CountyBlountsvilleBoazBon AirBridgeportBrightonBrooksideBrookwoodButler CountyCalera CityCamp HillCarbon HillCardiffCenter PointCentreChambers CountyChelseaCherokee CountyChildersburgChilton CountyClayClay CountyClayhatcheeClioCoalingCoffee CountyCokerCoosa CountyCoosadaCordova CityCrossvilleCullmanDadevilleDale CountyDalevilleDallasDeatsvilleDecaturDekalbDekalb CountyDodge CityDoraDothanDouglasEast Lawrence CountyEclecticEldridgeElkmontElmoreElmore CountyEnterpriseEtowahFairfieldFairviewFalkvilleFloralaFort DepositFort PayneFranklin CountyFt RuckerFultondaleGarden CityGardendaleGenevaGeneva CountyGeorgianaGeraldineGood HopeGoodwaterGraysvilleGreenvilleGrimesGuinGuntersvilleHale CountyHammondvilleHancevilleHarpersvilleHartfordHartselleHaydenHelenaHelena CityHokes BluffHolly PondHollywoodHomewoodHooverHoover CityHouston CountyHueyIndian SpringsIrondaleJacksonJackson CountyJackson GapJasper CityJefferson CountyKansas CityKellytonKimberlyLafayetteLakeviewLamar CountyLanettLauderdaleLawrence CountyLee CountyLeedsLevel PlainsLimestone CountyLinevilleLipscombLittlevilleLlbrookLockhartLouisvilleMaconMalvernMargaretMarion CountyMarshall CountyMaxwell-Gunter Air ForceMay CityMentoneMidfieldMidland CityMontevallo CityMontgomeryMontgomery CountyMoody CityMorganMorgan CountyMorrisMoultonMoundvilleMountain BrookMountainboroMulga CityNapier FieldNew BrocktonNew SiteNewtonNorthportOak GroveOpelikaParrishPaxtonPelhamPhil CampbellPiedmontPike RoadPinckardPinsonPleasant GrovePrattvillePricevilleRandolph CountyRehobethRoanokeRockfordRussellvilleSamsonSardisScottsboroSelmaShelby CountySipseySlocombSomervilleSouth VinemontSouthsideSpringvilleSt Clair CountySteeleStevensonSulligentSumitonSylacaugaSylvan SpringsTalladegaTalladega CountyTallapoosa CountyTallasseeTarrantTaylorTrinityTrussvilleTuscaloosa CountyTuskegeeUnion GroveValleyValley GrandeValley HeadVanceVernonVestavia HillsVincentWadleyWalker CountyWarriorWest JeffersonWest PointWestoverWetumpkaWiltonWinstonWoodville")
    print_capital_words(input_paragraph)
