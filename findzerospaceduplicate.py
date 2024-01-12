def replace_zeros_with_double_spaces(input_string):
    return input_string.replace('0', '##').replace('##', '  ')

def eliminate_duplicates(input_string):
    words = input_string.split()
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return ' '.join(unique_words)

if __name__ == "__main__":
    user_input = ("0000aliceville00Aliceville 0000carrollton00Carrollton 0000emelle00Emelle 0000ethelsville00Ethelsville 0000gordo00Gordo 0000reform00Reform 0000addison00Addison 0000bankston00Bankston 0000bear-creek00Bear Creek 0000beaverton00Beaverton 0000berry00Berry 0000brilliant00Brilliant 0000carbon-hill00Carbon Hill 0000detroit00Detroit 0000double-springs00Double Springs 0000eldridge00Eldridge 0000fayette00Fayette 0000guin00Guin 0000hackleburg00Hackleburg 0000haleyville00Haleyville 0000hamilton00Hamilton 0000hodges00Hodges 0000houston00Houston 0000kennedy00Kennedy 0000lynn00Lynn 0000millport00Millport 0000phil-campbell00Phil Campbell 0000sulligent00Sulligent 0000vernon00Vernon 0000vina00Vina 0000winfield00Winfield 0000danville00Danville 0000eva00Eva 0000falkville00Falkville 0000hartselle00Hartselle 0000russellville00Russellville 0000dutton00Dutton 0000fackler00Fackler 0000hollywood00Hollywood 0000langston00Langston 0000scottsboro00Scottsboro 0000section00Section 0000woodville00Woodville 0000fort-payne00Fort Payne 0000fyffe00Fyffe 0000mentone00Mentone 0000rainsville00Rainsville 0000valley-head00Valley Head 0000banks00Banks 0000brantley00Brantley 0000brundidge00Brundidge 0000clayton00Clayton 0000clio00Clio 0000equality00Equality 0000eufaula00Eufaula 0000dozier00Dozier 0000forest-home00Forest Home 0000fort-deposit00Fort Deposit 0000georgiana00Georgiana 0000glenwood00Glenwood 0000goshen00Goshen 0000grady00Grady 0000greenville00Greenville 0000highland-home00Highland Home 0000honoraville00Honoraville 0000louisville00Louisville 0000luverne00Luverne 0000rutledge00Rutledge 0000tallassee00Tallassee 0000troy00Troy 0000titus00Titus 0000verbena00Verbena 0000ashland00Ashland 0000cragford00Cragford 0000daviston00Daviston 0000delta00Delta 0000fruithurst00Fruithurst 0000graham00Graham 0000heflin00Heflin 0000lineville00Lineville 0000muscadine00Muscadine 0000piedmont00Piedmont 0000ranburne00Ranburne 0000roanoke00Roanoke 0000wadley00Wadley 0000wedowee00Wedowee 0000woodland00Woodland 0000dothan00Dothan 0000abbeville00Abbeville 0000ariton00Ariton 0000ashford00Ashford 0000black00Black 0000chancellor00Chancellor 0000clopton00Clopton 0000coffee-springs00Coffee Springs 0000columbia00Columbia 0000cottonwood00Cottonwood 0000cowarts00Cowarts 0000daleville00Daleville 0000elba00Elba 0000enterprise00Enterprise 0000geneva00Geneva 0000hartford00Hartford 0000headland00Headland 0000jack00Jack 0000midland-city00Midland City 0000new-brockton00New Brockton 0000newton00Newton 0000newville00Newville 0000ozark00Ozark 0000fort-rucker00Fort Rucker 0000shorterville00Shorterville 0000skipperville00Skipperville 0000slocomb00Slocomb 0000webb00Webb 0000andalusia00Andalusia 0000florala00Florala 0000kinston00Kinston 0000mc-kenzie00Mc Kenzie 0000opp00Opp 0000red-level00Red Level 0000samson00Samson 0000bayou-la-batre00Bayou La Batre 0000bon-secour00Bon Secour 0000coden00Coden 0000dauphin-island00Dauphin Island 0000elberta00Elberta 0000foley00Foley 0000grand-bay00Grand Bay 0000gulf-shores00Gulf Shores 0000irvington00Irvington 0000lillian00Lillian 0000loxley00Loxley 0000magnolia-springs00Magnolia Springs 0000orange-beach00Orange Beach 0000robertsdale00Robertsdale 0000seminole00Seminole 0000silverhill00Silverhill 0000summerdale00Summerdale 0000theodore00Theodore 0000mobile00Mobile 0000alberta00Alberta 0000catherine00Catherine 0000maplesville00Maplesville 0000marion-junction00Marion Junction 0000orrville00Orrville 0000pine-hill00Pine Hill 0000safford00Safford 0000thomasville00Thomasville 0000randolph00Randolph 0000auburn00Auburn 0000camp-hill00Camp Hill 0000notasulga00Notasulga")
    
    # Replace zeros with double spaces
    processed_output = replace_zeros_with_double_spaces(user_input)
    
    # Eliminate duplicate words
    processed_output = eliminate_duplicates(processed_output)

    print("Result: ", processed_output)