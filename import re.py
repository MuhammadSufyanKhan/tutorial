import re

def remove_lowercase_words(input_string):
    words = input_string.split()
    uppercase_words = [word for word in words if not word[0].islower()]
    return ' '.join(uppercase_words)

if __name__ == "__main__":
    user_input = ("Anderson  fishers  Fishers  fortville  Fortville  frankfort  Frankfort  ingalls  Ingalls  kempton  Kempton  lapel  Lapel  lebanon  Lebanon  mc-cordsville  Mc Cordsville  markleville  Markleville  mulberry  Mulberry  noblesville  Noblesville  pendleton  Pendleton  rossville  Rossville  tipton  Tipton  advance  Advance  bargersville  Bargersville  boggstown  Boggstown  carthage  Carthage  charlottesville  Charlottesville  edinburgh  Edinburgh  franklin  Franklin  greenfield  Greenfield  greenwood  Greenwood  jamestown  Jamestown  knightstown  Knightstown  lizton  Lizton  martinsville  Martinsville  morgantown  Morgantown  needham  Needham  nineveh  Nineveh  north-salem  North Salem  shelbyville  Shelbyville  trafalgar  Trafalgar  whiteland  Whiteland  wilkinson  Wilkinson  la-crosse  La Crosse  la-porte  La Porte  mill-creek  Mill Creek  north-judson  North Judson  rolling-prairie  Rolling Prairie  san-pierre  San Pierre  wheatfield  Wheatfield  argos  Argos  bourbon  Bourbon  bremen  Bremen  culver  Culver  donaldson  Donaldson  goshen  Goshen  grovertown  Grovertown  hamlet  Hamlet  knox  Knox  lakeville  Lakeville  leesburg  Leesburg  middlebury  Middlebury  milford  Milford  millersburg  Millersburg  nappanee  Nappanee  new-carlisle  New Carlisle  new-paris  New Paris  north-liberty  North Liberty  north-webster  North Webster  pierceton  Pierceton  plymouth  Plymouth  shipshewana  Shipshewana  syracuse  Syracuse  topeka  Topeka  tyner  Tyner  walkerton  Walkerton  warsaw  Warsaw  winona-lake  Winona Lake  albion  Albion  arcola  Arcola  ashley  Ashley  auburn  Auburn  avilla  Avilla  berne  Berne  bluffton  Bluffton  churubusco  Churubusco  columbia-city  Columbia City  corunna  Corunna  craigville  Craigville  cromwell  Cromwell  decatur  Decatur  geneva  Geneva  hoagland  Hoagland  howe  Howe  hudson  Hudson  huntington  Huntington  kendallville  Kendallville  keystone  Keystone  kimmell  Kimmell  lagrange  Lagrange  laotto  Laotto  larwill  Larwill  ligonier  Ligonier  monroe  Monroe  orland  Orland  ossian  Ossian  petroleum  Petroleum  pleasant-lake  Pleasant Lake  poneto  Poneto  roanoke  Roanoke  rome-city  Rome City  south-whitley  South Whitley  waterloo  Waterloo  wolcottville  Wolcottville  fort-wayne  Fort Wayne  bringhurst  Bringhurst  camden  Camden  cutler  Cutler  delphi  Delphi  denver  Denver  flora  Flora  kewanna  Kewanna  la-fontaine  La Fontaine  lagro  Lagro  leiters-ford  Leiters Ford  logansport  Logansport  macy  Macy  marion  Marion  mexico  Mexico  monterey  Monterey  north-manchester  North Manchester  ora  Ora  peru  Peru  roann  Roann  rochester  Rochester  star-city  Star City  twelve-mile  Twelve Mile  urbana  Urbana  van-buren  Van Buren  wabash  Wabash  winamac  Winamac  aurora  Aurora  bennington  Bennington  dillsboro  Dillsboro  florence  Florence  guilford  Guilford  lawrenceburg  Lawrenceburg  milan  Milan  moores-hill  Moores Hill  patriot  Patriot  rising-sun  Rising Sun  sunman  Sunman  vevay  Vevay  columbus  Columbus  madison  Madison  bryant  Bryant  dunkirk  Dunkirk  kennard  Kennard  lewisville  Lewisville  liberty  Liberty  montpelier  Montpelier  new-castle  New Castle  pennville  Pennville  portland  Portland  salamonia  Salamonia  shirley  Shirley  spiceland  Spiceland  union-city  Union City  newberry  Newberry  elnora  Elnora  loogootee  Loogootee  montgomery  Montgomery  odon  Odon  haubstadt  Haubstadt  west-lafayette  West Lafayette  battle-ground  Battle Ground  brook  Brook  brookston  Brookston  burnettsville  Burnettsville  chalmers  Chalmers  crawfordsville  Crawfordsville  earl-park  Earl Park  fair-oaks  Fair Oaks  francesville  Francesville  goodland  Goodland  idaville  Idaville  kentland  Kentland  medaryville  Medaryville  monon  Monon  monticello  Monticello  new-ross  New Ross  remington  Remington  rensselaer  Rensselaer  reynolds  Reynolds  wolcott  Wolcott")
    
    # Remove words starting with lowercase letters
    processed_output = remove_lowercase_words(user_input)

    print("Result: ", processed_output)
