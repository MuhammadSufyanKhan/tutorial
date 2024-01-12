def print_words_until_next_capital(sentence):
    words = sentence.split()
    current_word = ""

    for word in words:
        if word[0].isupper():
            if current_word:
                print(current_word)
            current_word = word
        else:
            current_word += word

    if current_word:
        print(current_word)

if __name__ == "__main__":
    input_sentence = "AberdeenAdaAdamsAdamsvilleAddystonAdelphiAkronAlbanyAlexandriaAlgerAllenAllianceAmandaAmberleyAmboyAmeliaAmherstAndersonAnnaAnsoniaAquillaArcadiaArcanumArchboldArlingtonArlington HeightsAshleyAshtabulaAshvilleAthensAtticaAtwaterAtwood LakeAuburnAuglaizeAugstinburgAuroraAvonAvon CityAvon LakeBailey LakesBainbridgeBairdsBallvilleBalticBaltimoreBarbertonBarnhillBartlowBataviaBathBayBazettaBeach CityBeachwoodBeaverBeavercreekBedfordBedford HeightsBellbrookBelle CenterBelle ValleyBellefontaineBellevueBellvilleBeloitBenningtonBentleyvilleBentonBentonvilleBereaBerkshireBerlinBerneBethelBethlehemBettsvilleBeverlyBexleyBig PrarieBig SpringBiglickBirchwood ManorBlakesleeBlanchesterBlanchsterBlendonBloomBloomdaleBloomingburgBloomvilleBlue AshBlue CreekBlufftonBolivarBostonBoston HeightsBotkinsBournevilleBowerstonBowling GreenBracevilleBradfordBradnerBradyBrady LakeBratenahlBrecksvilleBremenBriarwood BeachBriceBrimfieldBristolvilleBronsonBrook ParkBrookfieldBrooklynBrownBrown -St ParisBrownhelmBrunswickBrunswick HillsBrushcreekBryanBuckeye LakeBucklandBucyrus CityBuildingBulterBurbankBurgoonBurlingtonBurtonButlerCaananCadiz NonupgCaldwellCaledoniaCambridgeCamdenCanaanCanal WinchesterCantonCardingtonCareyCarlisleCarrollCarroltonCassCastineCatawbaCatawba IslandCecilCedarvilleCelinaCenterCenterburgCentervilleChagrin FallsChampionChardonCharlesChatfieldChathamChesterChestervilleChickasawChillicotheChippewaChippewa LakeCincinnatiCinnamon LakeCirclevilleClaibourneClaridonClarksburgClarksfieldClayClaytonClear CreekClearcreekClerkClevelandCleveland EastCleveland HeightsClevesCliftonClintonClydeCoaltonCoitsvilleColdwaterColerainCollegeCollege CornerCollinsColumbiaColumbia StationColumbusCommercial PointConcordConesvilleCongressConneautCoolvilleCopleyCortlandCorwinCoshoctonCountrysideCoventryCovingtonCraig BeachCranberryCraneCrawfordCrawford CountyCreeksideCrestlineCrestline CityCrestonCrooksvilleCrosbyCrotonCumberlandCuyahoga FallsCuyahoga HeightsCygnetCynthianDanburyDanvilleDarbyDarbyvilleDaytonDeer CreekDeer ParkDeerfieldDefianceDegraffDelawareDelhiDellroyDelphosDeltaDenisonDenison UniversityDeshlerDonnelsvilleDonnesvilleDoverDoylesDresdenDublinDuchouquetDunbridgeDuncan FallsDundasDunkirkEagleEagleportEast CantonEast LibertyEast PointEast SpartaEatonEdenEdgertonEdinburgEdisonEldoradoElizabethElmoreElmwood PlaceElyriaEmeraldEnglewoodEnonEnterpriseErieEtnaEuclidEvendaleFairbornFairfaxFairfieldFairlawnFairport HarborFallsFarmingtonFayetteFayettevilleFelicityFiceFindlayFitchvilleFlatrockFlorenceFloridaFohlForestFort LoramieFostoriaFountain PlaceFowlerFrankfortFranklinFrazeysburgFrederickFredericksburgFreedomFremontFriendlyFultonFultonhamGahannaGalenaGalionGalion CityGambierGarfield HeightsGarrettsvilleGates MillsGenevaGeneva CityGeneva On The LakeGenoaGeorgeGermanGettysbergGibsonburgGirardGlendaleGlenmontGlenwillowGloria GlensGnadenhuttenGolf ManorGordonGoshenGrand PrarieGrand RapidsGrandview HeightsGrangerGranvilleGratiotGratisGreenGreen AcresGreen CampGreen SpringsGreencreekGreenfieldGreenvilleGreenwichGrotonGroveGrove CityGroveportGuilfordGuysvilleHaleHallHallsvilleHambdenHamdenHamlerHanoverHanovertonHarbor HillsHardingHarlemHarmonyHarpersfieldHarpsterHarrisHarrisburgHarrisonHartfordHartlandHartvilleHaskinsHavilandHeathHeath OhHebronHenryHide A Way HillsHigginsportHighlandHighland HeightsHighland HillsHilliarHilliardHillsboroHinkleyHiramHoaglinHockingHolgateHoliday CityHolmesvilleHomerHopedaleHopewellHowardHowlandHubbardHuber HeightsHudsonHunting ValleyHuntingtonHuntsvilleIndependenceIndian HillIndian TrailsIrontonIsraelIthacaJacksonJackson CenterJamesJasperJeffersonJeffersonvilleJeneraJeromeJeromesvilleJerryJerseyJerusalemJewettJohnsJohnsonJohnstonJunctionJunction CityKentKent State UniversityKenton CityKettlersvilleKilbuckKillbuckKimboltonKingstonKingsvilleKirkersvilleKirtlandKirtland HillsKnoxLa RueLafayetteLakeLake BuckhornLake ChoctawLake MohawkLake SnowdenLake SouthLakemoreLakengrenLakesideLakeviewLakevilleLakewoodLancasterLanierLattyLaurelvilleLeavittsburgLebanonLeesburgLeesvilleLehmkuhls LandingLemonLennoxLeroyLewisburgLexingtonLibertyLiberty CenterLickLickingLimaLimavilleLincoln HeightsLinndaleLisbonLithopolisLockbourneLockingtonLocklandLodiLogan CityLondon CityLorainLoramieLordsLost CreekLoudonLoudonvilleLouisvilleLovelandLowellvilleLucasLuckeyLymeLyndhurstLyonsMacedoniaMad RiverMadeiraMadisonMae CliffMaeheadMagnetic SpringsMagnoliaMalintaMaltaMalvernManchesterMansfieldMantuaMaple HeightsMarengoMargarettaMariemontMarionMarlboroMarseillesMartinsburgMary AnnMarysvilleMasonMayfieldMayfield HeightsMcarthurMccombMcconnelsvilleMcguffeyMcleanMeccaMechanicsburgMeigsMendonMetamoraMeyers LakeMiamiMiddleMiddleburgMiddlefieldMiddletonMidvaleMidwayMifflinMilanMilfordMill CreekMillburyMillersburgMillersportMillvilleMiltonMineral CityMinervaMinerva ParkMinfordMinsterMogadoreMonclovaMonroeMontezumaMontgomeryMontpelierMontvilleMoorefieldMoreland HillsMorganMorralMount GileadMount VernonMt BlanchardMt HealthyMt SterlingMt VernonMt VictoryMt. CoryMt. OrabMuhlenburgMunroe FallsMunsonMurrayMuskingham CollegeMuskinghumMutualNapoleonNashvilleNeapolisNeaveNelsonNelson LedgesNevadaNew AlbanyNew BloomingtonNew BostonNew BremenNew CalisleNew CarlisleNew ConcordNew CumberlandNew FranklinNew HampshireNew HavenNew HollandNew JasperNew KnoxvilleNew LebanonNew LexingtonNew LondonNew MadisonNew MarketNew MarshfiedNew ParisNew PhiladelphiaNew ReigelNew RussiaNew ViennaNew WashingtonNewarkNewberryNewburgh HeightsNewburyNewcomersNewmarshfieldNewtonNewton FallsNeyNileNilesNimishillenNobleNorth BaltimoreNorth BendNorth BloomfieldNorth CantonNorth College HillNorth HamptonNorth JacksonNorth KingsvilleNorth LewisburgNorth OlmstedNorth PerryNorth RandallNorth RidgevilleNorth RobinsonNorth RoyaltonNorth StarNorthfieldNorthwoodNortonNorwalkNorwichNorwoodOak HarborOak HillOaklandOakrunOakwoodObertzObetzOhio CityOhio State UniversityOliveOntarioOrangeOrange ValleyOrangevilleOregonOrientOsgoodOsnaburgOstranderOttawaOxfordPainesvillePaintPalmyraParisPark LayneParrallPataskalaPattersonPauldingPee PeePeeblesPembervillePennisulaPepper PikePerryPerry CountyPerrysburgPerrysvillePeruPettisvilePhillipsburgPhiloPickawayPickeringtonPiercePikePiketonPiquaPitsburgPittPlainPlain CityPlainfieldPleasantPleasant HillPleasant PlainPleasantvillePlumwoodPlymouthPolandPolkPoplar GrovePort ClintonPort WashingtonPortagePorterPorterfieldPotsdamPowellPrairiePrarieProspectProvidencePulaskiQuincyRadnorRainsboroRandolphRangeRavennaRawsonReadingReedRemindersvilleRepublicReynoldsburgRiceRichfieldRichlandRichmondRichmond DaleRichmond HeightsRichwoodRidgeRidgefieldRidgewayRileyRio GrandeRipleyRittmanRiverleaRiversideRobertsvilleRobinsRockbridgeRockfordRocky RidgeRootsRosevilleRosewoodRossRossburgRoswellRoundheadRowsburgRoyaltonRushRushcreekRushvilleRushylvaniaRussellRussells PointRussellvilleRusselvilleRussiaRutlandSabinaSagamore HillsSaint MartinSalemSalisburySalt CreekSaltcreekSanduskySandySandy ValleySarniniaSavannahSaybrookScioSciotoScipioScottSealSeamanSebringSendSenecaSevilleShaker HeightsShalersvilleSharonSharonvilleShawneeShawnee HillsSheffieldSheffield LakeShelbySherrodsvilleShilohShreveSidneySilver CreekSilver LakeSilvertonSmithSolonSomerfordSomersSomersetSonoraSouth AmherstSouth BloomfieldSouth CharlestonSouth EuclidSouth LebanonSouth RussellSouth SalemSouth SolonSouth ViennaSouth ZanesvilleSouthingtonSpartaSpencerSpring CreekSpring LakeSpring ValleySpringdaleSpringfieldSt AlbansSt BernardSt JohnsSt. HenrySt. JosephSt. LouisvilleSt. ParisStautonSterlingStewartStokesStonelickStoutsvilleStowStrasburgStreetsboroStrongsvilleStrykerSuffieldSugar Bush KnollsSugar GroveSugarcreekSunburySunfishSuperiorSwan CreekSwantonSycamoreSymmesTallmadgeTaylorTerrace ParkThe PlainsThe StruthersThompsonThornThornvilleThurstonTiffinTipp CityTiroToledoTontoganyTrentonTrinwayTrotwoodTroyTruroTurtle CreekTuscarawasTwinTwin PinesTwinsburgTymochteeUhrichsvilleUnionUnionville CenterUniopolisUpper ArlingtonUpper SanduskyUrbana CityUrbana CountyUrbancrestUticaValleyValley HiVan BurenVan WertVanlueVaughnsvilleVenedociaVeniceVermilionVernonVersaillesViennaVioletWabashWadsworthWaite HillWakemanWalbridgeWaldoWalnutWalton HillsWarrenWarrensville HeightsWarsawWarwickWashingtnWaterWatervilleWauseonWaverly CityWayneWayne LakesWaynesburgWaynesfieldWaynesvilleWeathersfieldWebsterWellstonWest AlexandriaWest ChesterWest ElktonWest JeffersonWest LafayetteWest ManchesterWest MansfieldWest RushvilleWest SalemWest UnionWest UnityWestervilleWestfieldWestlakeWestlandWestonWestviewWestville-GrahmWhartonWheelingWhetstoneWhitehallWhitehouseWhitewaterWilliamsburgWilliamsportWillowickWillshireWilmingtonWilmotWilshire HillsWinchesterWindhamWoodingtonWoodlawnWoodmere ValleyWoodvilleWorthingtonWrenWright Patterson Airforce BaseWyomingXeniaYankee LakeYellow SpringsYorkYorkshireYoungsZaleskiZaneZanesfieldZanesvilleZoar")
    print("Words from capital letter to small letter until new capital letter:")
    print_words_until_next_capital(input_sentence)
