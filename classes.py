def class_init(p):
    m_class = ["Warrior", "Mage", "Warpriest", "Trickster", "Engineer", "Brawler", "Necromancer", "Arachnomancer","Businessman","Bard"]
    m_str_mod = [
    2, #Warrior
    -1, #Mage
    1, #Warpriest
    1, #Trickster
    -3, #Engineer
    4, #Brawler
    0, #Necromancer
    -1, #Arachnomancer
    -2, #Businessman
    -3] #Bard
    
    m_spd_mod = [
    0, #Warrior
    1, #Mage
    2, #Warpriest
    5, #Trickster
    0, #Engineer
    0, #Brawler
    1, #Necromancer
    0, #Arachnomancer
    0, #Businessman
    8] #Bard
    
    m_def_mod = [
    2, #Warrior
    -2, #Mage
    -3, #Warpriest
    -3, #Trickster
    1, #Engineer
    0, #Brawler
    -1, #Necromancer
    0, #Arachnomancer
    0, #Businessman
    -1] #Bard
    
    m_mhp_mod = [
    4, #Warrior
    -1, #Mage
    -1, #Warpriest
    0, #Trickster
    2, #Engineer
    0, #Brawler
    -5, #Necromancer
    0, #Arachnomancer
    -4, #Businessman
    -2] #Bard
    
    m_classid = [
    0, #Warrior
    1, #Mage
    2, #Warpriest
    3, #Trickster
    4, #Engineer
    5, #Brawler
    6, #Necromancer
    7, #Arachnomancer
    8, #Businessman
    9] #Bard
    
    
    p_class_p = [m_class[p], m_str_mod[p], m_spd_mod[p], m_def_mod[p], m_mhp_mod[p], m_classid[p]]
    return p_class_p
    