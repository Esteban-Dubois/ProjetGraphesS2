import matplotlib.pyplot as plt





stations_yamanote = {
    "Tokyo": (139.7671, 35.6812), "Kanda": (139.7709, 35.6917),
    "Akihabara": (139.7731, 35.6983), "Okachimachi": (139.7747, 35.7074),
    "Ueno": (139.7770, 35.7137), "Uguisudani": (139.7780, 35.7204),
    "Nippori": (139.7712, 35.7277), "Nishi-Nippori": (139.7667, 35.7321),
    "Tabata": (139.7610, 35.7334), "Komagome": (139.7468, 35.7364),
    "Sugamo": (139.7397, 35.7334), "Otsuka": (139.7282, 35.7314),
    "Ikebukuro": (139.7109, 35.7289), "Mejiro": (139.7062, 35.7212),
    "Takadanobaba": (139.7037, 35.7122), "Shin-Okubo": (139.7002, 35.7013),
    "Shinjuku": (139.7003, 35.6894), "Yoyogi": (139.7022, 35.6830),
    "Harajuku": (139.7024, 35.6701), "Shibuya": (139.7016, 35.6585),
    "Ebisu": (139.7101, 35.6466), "Meguro": (139.7156, 35.6339),
    "Gotanda": (139.7234, 35.6264), "Osaki": (139.7286, 35.6197),
    "Shinagawa": (139.7387, 35.6284), "Takanawa Gateway": (139.7406, 35.6355),
    "Tamachi": (139.7476, 35.6457), "Hamamatsucho": (139.7571, 35.6556),
    "Shimbashi": (139.7583, 35.6664), "Yurakucho": (139.7607, 35.6750),
}

reseau_yamanote = {
    "Yamanote": {
        "color": "#9acd32",
        "path": ["Tokyo", "Kanda", "Akihabara", "Okachimachi", "Ueno", "Uguisudani", 
                 "Nippori", "Nishi-Nippori", "Tabata", "Komagome", "Sugamo", "Otsuka", 
                 "Ikebukuro", "Mejiro", "Takadanobaba", "Shin-Okubo", "Shinjuku", 
                 "Yoyogi", "Harajuku", "Shibuya", "Ebisu", "Meguro", "Gotanda", 
                 "Osaki", "Shinagawa", "Takanawa Gateway", "Tamachi", "Hamamatsucho", 
                 "Shimbashi", "Yurakucho", "Tokyo"]
    }
}





stations_asakusa = {
    "Nishi-magome": (139.7061, 35.5866),
    "Magome": (139.7118, 35.5962),
    "Nakanobu": (139.7145, 35.6046),
    "Togoshi": (139.7153, 35.6141),
    "Gotanda": (139.7234, 35.6264),
    "Takanawadai": (139.7317, 35.6329),
    "Sengakuji": (139.7363, 35.6384),
    "Mita": (139.7479, 35.6481),
    "Daimon": (139.7554, 35.6575),
    "Shimbashi": (139.7583, 35.6664),
    "Higashi-ginza": (139.7686, 35.6695),
    "Takaracho": (139.7744, 35.6757),
    "Nihombashi": (139.7744, 35.6822),
    "Ningyocho": (139.7825, 35.6861),
    "Higashi-nihombashi": (139.7845, 35.6922),
    "Asakusabashi": (139.7849, 35.6974),
    "Kuramae": (139.7915, 35.7032),
    "Asakusa": (139.7974, 35.7117),
    "Honjo-azumabashi": (139.8020, 35.7086),
    "Oshiage": (139.8131, 35.7115)
}

reseau_asakusa = {
    "Asakusa Line": {
        "color": "#E85298",
        "path": [
            "Nishi-magome", "Magome", "Nakanobu", "Togoshi", "Gotanda", 
            "Takanawadai", "Sengakuji", "Mita", "Daimon", "Shimbashi", 
            "Higashi-ginza", "Takaracho", "Nihombashi", "Ningyocho", 
            "Higashi-nihombashi", "Asakusabashi", "Kuramae", "Asakusa", 
            "Honjo-azumabashi", "Oshiage"
        ]
    }
}





stations_chuo = {
    "Nakano": (139.6657, 35.7058),
    "Shinjuku": (139.7003, 35.6894),
    "Yotsuya": (139.7302, 35.6860),
    "Ochanomizu": (139.7647, 35.7001),
    "Kanda": (139.7709, 35.6917),
    "Tokyo": (139.7671, 35.6812)
}

reseau_chuo = {
    "Chuo Line": {
        "color": "#ff4500",
        "path": ["Nakano", "Shinjuku", "Yotsuya", "Ochanomizu", "Kanda", "Tokyo"]
    }
}





stations_ginza = {
    "Shibuya": (139.7016, 35.6585),
    "Omote-sando": (139.7111, 35.6652),
    "Aoyama-itchome": (139.7240, 35.6728),
    "Akasaka-mitsuke": (139.7368, 35.6766),
    "Tameike-sanno": (139.7423, 35.6718),
    "Toranomon": (139.7499, 35.6701),
    "Shimbashi": (139.7583, 35.6664),
    "Ginza": (139.7651, 35.6719),
    "Kyobashi": (139.7711, 35.6762),
    "Nihombashi": (139.7744, 35.6822),
    "Mitsukoshimae": (139.7745, 35.6861),
    "Kanda-Gin": (139.7710, 35.6918), # Identifiée différemment pour éviter les conflits
    "Suehirocho": (139.7714, 35.7032),
    "Ueno-hirokoji": (139.7733, 35.7077),
    "Ueno": (139.7770, 35.7137),
    "Inaricho": (139.7828, 35.7126),
    "Tawaramachi": (139.7909, 35.7107),
    "Asakusa": (139.7974, 35.7117)
}

reseau_ginza = {
    "Ginza Line": {
        "color": "#ff9500",
        "path": [
            "Shibuya", "Omote-sando", "Aoyama-itchome", "Akasaka-mitsuke", 
            "Tameike-sanno", "Toranomon", "Shimbashi", "Ginza", "Kyobashi", 
            "Nihombashi", "Mitsukoshimae", "Kanda-Gin", "Suehirocho", 
            "Ueno-hirokoji", "Ueno", "Inaricho", "Tawaramachi", "Asakusa"
        ]
    }
}





stations_marunouchi = {
    "Ogikubo": (139.6244, 35.7045),
    "Minami-asagaya": (139.6358, 35.6997),
    "Shin-koenji": (139.6459, 35.6976),
    "Higashi-koenji": (139.6575, 35.6985),
    "Shin-nakano": (139.6685, 35.6978),
    "Nakano-sakaue": (139.6817, 35.6930),
    "Nishi-shinjuku": (139.6926, 35.6945),
    "Shinjuku": (139.7003, 35.6894),
    "Shinjuku-sanchome": (139.7046, 35.6911),
    "Shinjuku-gyoemmae": (139.7101, 35.6873),
    "Yotsuya-sanchome": (139.7208, 35.6878),
    "Yotsuya": (139.7302, 35.6860),
    "Akasaka-mitsuke": (139.7368, 35.6766),
    "Kokkai-gijidomae": (139.7451, 35.6734),
    "Kasumigaseki": (139.7516, 35.6740),
    "Ginza": (139.7651, 35.6719),
    "Tokyo": (139.7671, 35.6812),
    "Otemachi": (139.7646, 35.6848),
    "Awajicho": (139.7677, 35.6948),
    "Ochanomizu": (139.7647, 35.7001),
    "Hongo-sanchome": (139.7600, 35.7067),
    "Korakuen": (139.7516, 35.7075),
    "Myogadani": (139.7371, 35.7176),
    "Shin-otsuka": (139.7299, 35.7258),
    "Ikebukuro": (139.7109, 35.7289)
}

reseau_marunouchi = {
    "Marunouchi Line": {
        "color": "#f62e36",
        "path": [
            "Ogikubo", "Minami-asagaya", "Shin-koenji", "Higashi-koenji", 
            "Shin-nakano", "Nakano-sakaue", "Nishi-shinjuku", "Shinjuku", 
            "Shinjuku-sanchome", "Shinjuku-gyoemmae", "Yotsuya-sanchome", 
            "Yotsuya", "Akasaka-mitsuke", "Kokkai-gijidomae", "Kasumigaseki", 
            "Ginza", "Tokyo", "Otemachi", "Awajicho", "Ochanomizu", 
            "Hongo-sanchome", "Korakuen", "Myogadani", "Shin-otsuka", "Ikebukuro"
        ]
    }
}





stations_hibiya = {
    "Naka-meguro": (139.7003, 35.6443),
    "Ebisu": (139.7101, 35.6466),
    "Hiroo": (139.7222, 35.6522),
    "Roppongi": (139.7314, 35.6628),
    "Kamiyacho": (139.7451, 35.6629),
    "Toranomon Hills": (139.7495, 35.6672),
    "Kasumigaseki": (139.7516, 35.6740),
    "Hibiya": (139.7597, 35.6733),
    "Ginza": (139.7651, 35.6719),
    "Higashi-ginza": (139.7686, 35.6695),
    "Tsukiji": (139.7719, 35.6685),
    "Hatchobori": (139.7774, 35.6746),
    "Kayabacho": (139.7770, 35.6800),
    "Nihombashi": (139.7744, 35.6822),
    "Ningyocho": (139.7825, 35.6861),
    "Kodenmacho": (139.7788, 35.6922),
    "Akihabara": (139.7731, 35.6983),
    "Naka-okachimachi": (139.7753, 35.7063),
    "Ueno": (139.7770, 35.7137),
    "Iriya": (139.7841, 35.7208),
    "Minowa": (139.7915, 35.7297),
    "Minami-senju": (139.7991, 35.7336),
    "Kita-senju": (139.8044, 35.7485)
}

reseau_hibiya = {
    "Hibiya Line": {
        "color": "#b5b5b6",
        "path": [
            "Naka-meguro", "Ebisu", "Hiroo", "Roppongi", "Kamiyacho", 
            "Toranomon Hills", "Kasumigaseki", "Hibiya", "Ginza", "Higashi-ginza", 
            "Tsukiji", "Hatchobori", "Kayabacho", "Nihombashi", "Ningyocho", 
            "Kodenmacho", "Akihabara", "Naka-okachimachi", "Ueno", "Iriya", 
            "Minowa", "Minami-senju", "Kita-senju"
        ]
    }
}





stations_hanzomon = {
    "Shibuya": (139.7016, 35.6585),
    "Omote-sando": (139.7111, 35.6652),
    "Aoyama-itchome": (139.7240, 35.6728),
    "Nagatacho": (139.7405, 35.6793),
    "Hanzomon": (139.7417, 35.6857),
    "Kudanshita": (139.7516, 35.6953),
    "Jimbocho": (139.7570, 35.6955),
    "Otemachi": (139.7646, 35.6848),
    "Mitsukoshimae": (139.7745, 35.6861),
    "Suitengumae": (139.7847, 35.6830),
    "Kiyosumi-shirakawa": (139.8003, 35.6821),
    "Sumiyoshi": (139.8152, 35.6890),
    "Kinshicho": (139.8143, 35.6968),
    "Oshiage": (139.8131, 35.7115)
}

reseau_hanzomon = {
    "Hanzomon Line": {
        "color": "#8c77b8",
        "path": [
            "Shibuya", "Omote-sando", "Aoyama-itchome", "Nagatacho", "Hanzomon", 
            "Kudanshita", "Jimbocho", "Otemachi", "Mitsukoshimae", "Suitengumae", 
            "Kiyosumi-shirakawa", "Sumiyoshi", "Kinshicho", "Oshiage"
        ]
    }
}





stations_tozai = {
    "Nakano": (139.6657, 35.7058),
    "Ochiai": (139.6865, 35.7107),
    "Takadanobaba": (139.7037, 35.7122),
    "Waseda": (139.7212, 35.7055),
    "Kagurazaka": (139.7347, 35.7037),
    "Iidabashi": (139.7448, 35.7019),
    "Kudanshita": (139.7516, 35.6953),
    "Takebashi": (139.7562, 35.6912),
    "Otemachi": (139.7646, 35.6848),
    "Nihombashi": (139.7744, 35.6822),
    "Kayabacho": (139.7770, 35.6800),
    "Monzen-nakacho": (139.7954, 35.6720),
    "Kiba": (139.8066, 35.6692),
    "Toyocho": (139.8172, 35.6693),
    "Minami-sunamachi": (139.8315, 35.6677),
    "Nishi-kasai": (139.8594, 35.6657),
    "Kasai": (139.8732, 35.6635),
    "Urayasu": (139.8931, 35.6653)
}

reseau_tozai = {
    "Tozai Line": {
        "color": "#009bbd",
        "path": [
            "Nakano", "Ochiai", "Takadanobaba", "Waseda", "Kagurazaka", 
            "Iidabashi", "Kudanshita", "Takebashi", "Otemachi", "Nihombashi", 
            "Kayabacho", "Monzen-nakacho", "Kiba", "Toyocho", "Minami-sunamachi", 
            "Nishi-kasai", "Kasai", "Urayasu"
        ]
    }
}





stations_mita = {
    "Meguro": (139.7156, 35.6339),
    "Shirokanedai": (139.7262, 35.6382),
    "Shirokane-takanawa": (139.7342, 35.6429),
    "Mita": (139.7479, 35.6481),
    "Shibakoen": (139.7521, 35.6541),
    "Onarimon": (139.7533, 35.6616),
    "Uchisaiwaicho": (139.7563, 35.6692),
    "Hibiya": (139.7597, 35.6733),
    "Otemachi": (139.7646, 35.6848),
    "Jimbocho": (139.7570, 35.6955),
    "Suidobashi": (139.7540, 35.7058),
    "Kasuga": (139.7523, 35.7078),
    "Hakusan": (139.7508, 35.7220),
    "Sengoku": (139.7437, 35.7282),
    "Sugamo": (139.7397, 35.7334),
    "Nishi-sugamo": (139.7303, 35.7438),
    "Itabashi-kuyakushomae": (139.7099, 35.7512)
}

reseau_mita = {
    "Mita Line": {
        "color": "#0067b0",
        "path": [
            "Meguro", "Shirokanedai", "Shirokane-takanawa", "Mita", "Shibakoen", 
            "Onarimon", "Uchisaiwaicho", "Hibiya", "Otemachi", "Jimbocho", 
            "Suidobashi", "Kasuga", "Hakusan", "Sengoku", "Sugamo", 
            "Nishi-sugamo", "Itabashi-kuyakushomae"
        ]
    }
}





stations_shinjuku_line = {
    "Shinjuku": (139.7003, 35.6894),
    "Shinjuku-sanchome": (139.7046, 35.6911),
    "Akebonobashi": (139.7225, 35.6924),
    "Ichigaya": (139.7348, 35.6912),
    "Kudanshita": (139.7516, 35.6953),
    "Jimbocho": (139.7570, 35.6955),
    "Ogawamachi": (139.7667, 35.6948),
    "Iwamotocho": (139.7758, 35.6970),
    "Bakuro-yokoyama": (139.7821, 35.6927),
    "Hamacho": (139.7876, 35.6888),
    "Morishita": (139.7972, 35.6887),
    "Kikukawa": (139.8062, 35.6885),
    "Sumiyoshi": (139.8152, 35.6890),
    "Nishi-ojima": (139.8258, 35.6894),
    "Ojima": (139.8351, 35.6910),
    "Higashi-ojima": (139.8465, 35.6915),
    "Funabori": (139.8643, 35.6841)
}

reseau_shinjuku_line = {
    "Shinjuku Line": {
        "color": "#b0ca71",
        "path": [
            "Shinjuku", "Shinjuku-sanchome", "Akebonobashi", "Ichigaya", 
            "Kudanshita", "Jimbocho", "Ogawamachi", "Iwamotocho", 
            "Bakuro-yokoyama", "Hamacho", "Morishita", "Kikukawa", 
            "Sumiyoshi", "Nishi-ojima", "Ojima", "Higashi-ojima", "Funabori"
        ]
    }
}





stations_yurakucho = {
    "Ikebukuro": (139.7109, 35.7289),
    "Higashi-ikebukuro": (139.7202, 35.7252),
    "Gokokuji": (139.7265, 35.7197),
    "Edogawabashi": (139.7327, 35.7088),
    "Iidabashi": (139.7448, 35.7019),
    "Ichigaya": (139.7348, 35.6912),
    "Kojimachi": (139.7369, 35.6836),
    "Nagatacho": (139.7405, 35.6793),
    "Sakuradamon": (139.7513, 35.6775),
    "Yurakucho": (139.7607, 35.6750),
    "Ginza-itchome": (139.7674, 35.6743),
    "Shintomicho": (139.7745, 35.6711),
    "Tsukishima": (139.7844, 35.6644),
    "Toyosu": (139.7963, 35.6548),
    "Tatsumi": (139.8105, 35.6455),
    "Shin-kiba": (139.8271, 35.6458)
}

reseau_yurakucho = {
    "Yurakucho Line": {
        "color": "#c1a470",
        "path": [
            "Ikebukuro", "Higashi-ikebukuro", "Gokokuji", "Edogawabashi", 
            "Iidabashi", "Ichigaya", "Kojimachi", "Nagatacho", "Sakuradamon", 
            "Yurakucho", "Ginza-itchome", "Shintomicho", "Tsukishima", 
            "Toyosu", "Tatsumi", "Shin-kiba"
        ]
    }
}





stations_namboku = {
    "Meguro": (139.7156, 35.6339),
    "Shirokane-takanawa": (139.7342, 35.6429),
    "Azabu-juban": (139.7354, 35.6547),
    "Roppongi-itchome": (139.7390, 35.6657),
    "Tameike-sanno": (139.7423, 35.6718),
    "Nagatacho": (139.7405, 35.6793),
    "Yotsuya": (139.7302, 35.6860),
    "Ichigaya": (139.7348, 35.6912),
    "Iidabashi": (139.7448, 35.7019),
    "Korakuen": (139.7516, 35.7075),
    "Todaimae": (139.7582, 35.7206),
    "Hon-komagome": (139.7538, 35.7250),
    "Komagome": (139.7468, 35.7364),
    "Nishigahara": (139.7422, 35.7460),
    "Oji": (139.7378, 35.7517)
}

reseau_namboku = {
    "Namboku Line": {
        "color": "#00ac9b",
        "path": [
            "Meguro", "Shirokane-takanawa", "Azabu-juban", "Roppongi-itchome", 
            "Tameike-sanno", "Nagatacho", "Yotsuya", "Ichigaya", "Iidabashi", 
            "Korakuen", "Todaimae", "Hon-komagome", "Komagome", "Nishigahara", "Oji"
        ]
    }
}





stations_fukutoshin = {
    "Ikebukuro": (139.7109, 35.7289),
    "Zoshigaya": (139.7145, 35.7203),
    "Nishi-waseda": (139.7075, 35.7073),
    "Higashi-shinjuku": (139.7075, 35.6983),
    "Shinjuku-sanchome": (139.7046, 35.6911),
    "Kita-sando": (139.7058, 35.6791),
    "Meiji-jingumae": (139.7052, 35.6687),
    "Shibuya": (139.7016, 35.6585)
}

reseau_fukutoshin = {
    "Fukutoshin Line": {
        "color": "#9c5e31",
        "path": [
            "Ikebukuro", "Zoshigaya", "Nishi-waseda", "Higashi-shinjuku", 
            "Shinjuku-sanchome", "Kita-sando", "Meiji-jingumae", "Shibuya"
        ]
    }
}





stations_sobu = {
    "Mitaka": (139.5603, 35.7027),
    "Kichijoji": (139.5804, 35.7031),
    "Asagaya": (139.6358, 35.7048),
    "Koenji": (139.6496, 35.7053),
    "Nakano": (139.6657, 35.7058),
    "Higashi-Nakano": (139.6838, 35.7061),
    "Okubo": (139.6974, 35.7008),
    "Shinjuku": (139.7003, 35.6894),
    "Yoyogi": (139.7022, 35.6830),
    "Sendagaya": (139.7111, 35.6812),
    "Shinanomachi": (139.7203, 35.6801),
    "Yotsuya": (139.7302, 35.6860),
    "Ichigaya": (139.7348, 35.6912),
    "Iidabashi": (139.7448, 35.7019),
    "Suidobashi": (139.7540, 35.7058),
    "Ochanomizu": (139.7647, 35.7001),
    "Akihabara": (139.7731, 35.6983),
    "Asakusabashi": (139.7849, 35.6974),
    "Ryogoku": (139.7929, 35.6961),
    "Kinshicho": (139.8143, 35.6968)
}

reseau_sobu = {
    "Sobu Line": {
        "color": "#ffd700",
        "path": ["Mitaka", "Kichijoji", "Asagaya", "Koenji", "Nakano", "Higashi-Nakano", "Okubo", "Shinjuku", "Yoyogi", "Sendagaya", "Shinanomachi", "Yotsuya", "Ichigaya", "Iidabashi", "Suidobashi", "Ochanomizu", "Akihabara", "Asakusabashi", "Ryogoku", "Kinshicho"]
    }
}





stations_keiyo = {
    "Tokyo": (139.7671, 35.6812),
    "Hatchobori": (139.7774, 35.6746),
    "Etchujima": (139.7925, 35.6675),
    "Shiomi": (139.8172, 35.6586),
    "Shin-Kiba": (139.8271, 35.6458),
    "Kasai-Rinkai-Koen": (139.8631, 35.6444),
    "Maihama": (139.8845, 35.6364)
}

reseau_keiyo = {
    "Keiyo Line": {
        "color": "#c9242f",
        "path": ["Tokyo", "Hatchobori", "Etchujima", "Shiomi", "Shin-Kiba", "Kasai-Rinkai-Koen", "Maihama"]
    }
}





stations_toyoko = {
    "Shibuya": (139.7016, 35.6585),
    "Daikan-yama": (139.7064, 35.6482),
    "Naka-meguro": (139.7003, 35.6443),
    "Yutenji": (139.6912, 35.6375),
    "Gakugei-daigaku": (139.6852, 35.6297),
    "Toritsu-daigaku": (139.6761, 35.6174),
    "Jiyugaoka": (139.6685, 35.6074)
}

reseau_toyoko = {
    "Toyoko Line": {
        "color": "#da0442",
        "path": ["Shibuya", "Daikan-yama", "Naka-meguro", "Yutenji", "Gakugei-daigaku", "Toritsu-daigaku", "Jiyugaoka"]
    }
}





stations_odakyu = {
    "Shinjuku": (139.7003, 35.6894),
    "Yoyogi-Uehara": (139.6848, 35.6691),
    "Shimokitazawa": (139.6673, 35.6616),
    "Meidaimae": (139.6504, 35.6684),
    "Gotokuji": (139.6447, 35.6491),
    "Seijo-Gakuenmae": (139.5986, 35.6406)
}

reseau_odakyu = {
    "Odakyu Line": {
        "color": "#223a70",
        "path": ["Shinjuku", "Yoyogi-Uehara", "Shimokitazawa", "Meidaimae", "Gotokuji", "Seijo-Gakuenmae"]
    }
}





stations_keio = {
    "Shinjuku": (139.7003, 35.6894),
    "Sasazuka": (139.6672, 35.6736),
    "Meidaimae": (139.6504, 35.6684),
    "Chitose-Karasuyama": (139.6006, 35.6573),
    "Chofu": (139.5445, 35.6521)
}

reseau_keio = {
    "Keio Line": {
        "color": "#dd0077",
        "path": ["Shinjuku", "Sasazuka", "Meidaimae", "Chitose-Karasuyama", "Chofu"]
    }
}



tous_les_dicos = [
    stations_yamanote, stations_asakusa, stations_chuo, stations_ginza, 
    stations_marunouchi, stations_hibiya, stations_hanzomon, stations_tozai,
    stations_mita, stations_shinjuku_line, stations_yurakucho, stations_namboku,
    stations_fukutoshin, stations_sobu, stations_keiyo, stations_toyoko,
    stations_odakyu, stations_keio
]
stations_globales = {}
for d in tous_les_dicos: stations_globales.update(d)

reseau_global = {
    "Yamanote": reseau_yamanote["Yamanote"], "Asakusa": reseau_asakusa["Asakusa Line"],
    "Chuo": reseau_chuo["Chuo Line"], "Ginza": reseau_ginza["Ginza Line"],
    "Marunouchi": reseau_marunouchi["Marunouchi Line"], "Hibiya": reseau_hibiya["Hibiya Line"],
    "Hanzomon": reseau_hanzomon["Hanzomon Line"], "Tozai": reseau_tozai["Tozai Line"],
    "Mita": reseau_mita["Mita Line"], "Shinjuku_L": reseau_shinjuku_line["Shinjuku Line"],
    "Yurakucho": reseau_yurakucho["Yurakucho Line"], "Namboku": reseau_namboku["Namboku Line"],
    "Fukutoshin": reseau_fukutoshin["Fukutoshin Line"], "Sobu": reseau_sobu["Sobu Line"],
    "Keiyo": reseau_keiyo["Keiyo Line"], "Toyoko": reseau_toyoko["Toyoko Line"],
    "Odakyu": reseau_odakyu["Odakyu Line"], "Keio": reseau_keio["Keio Line"]
}

adjacence = {}
for ligne in reseau_global.values():
    path = ligne["path"]
    for i in range(len(path) - 1):
        u, v = path[i], path[i+1]
        if u not in adjacence: adjacence[u] = set()
        if v not in adjacence: adjacence[v] = set()
        adjacence[u].add(v); adjacence[v].add(u)

def bfs_chemin(start, end, graph):
    if start not in graph or end not in graph: return None
    queue = [[start]]
    visited = {start}
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end: return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(list(path) + [neighbor])
    return None

def obtenir_infos_segment(s1, s2, reseau):
    for nom, info in reseau.items():
        p = info["path"]
        for i in range(len(p)-1):
            if (p[i] == s1 and p[i+1] == s2) or (p[i] == s2 and p[i+1] == s1):
                return nom, info["color"]
    return "Inconnue", "gray"

def dessiner_mon_graphe(ax):
    for info in reseau_global.values():
        c, p = info["color"], info["path"]
        for i in range(len(p)-1):
            if p[i] in stations_globales and p[i+1] in stations_globales:
                ax.plot([stations_globales[p[i]][0], stations_globales[p[i+1]][0]], 
                        [stations_globales[p[i]][1], stations_globales[p[i+1]][1]], 
                        color=c, linewidth=1, alpha=0.4)
    for nom, (x, y) in stations_globales.items():
        ax.scatter(x, y, s=10, color='gray', alpha=0.5, zorder=2)
        ax.text(x, y, nom, fontsize=5, alpha=0.7)

plt.ion()
fig, ax = plt.subplots(figsize=(15, 12))
dessiner_mon_graphe(ax)
ax.set_aspect('equal')
ax.axis('off')
plt.title("Référentiel Métro Tokyo - Entrez les noms exacts (ex: Shinjuku)")
plt.draw()

stations_normalisees = {s.lower(): s for s in stations_globales.keys()}

while True:
    print("\n" + "="*30)
    dep_raw = input("Station de départ : ").strip().lower()
    if dep_raw == 'exit': break
    arr_raw = input("Station d'arrivée : ").strip().lower()
    
    dep = stations_normalisees.get(dep_raw)
    arr = stations_normalisees.get(arr_raw)
    
    if not dep or not arr:
        print(f"Erreur : Station(s) introuvable(s).")
        continue

    chemin = bfs_chemin(dep, arr, adjacence)
    
    if chemin:
        ligne_actuelle = None
        changements = 0
        print(f"\nTrajet trouvé ({len(chemin)} stations) :")
        for i in range(len(chemin)-1):
            nom_l, coul_l = obtenir_infos_segment(chemin[i], chemin[i+1], reseau_global)
            if nom_l != ligne_actuelle:
                if ligne_actuelle is not None: changements += 1
                print(f" -> À {chemin[i]}, prendre la ligne {nom_l} ({coul_l})")
                ligne_actuelle = nom_l
        print(f" -> Arrivée à {chemin[-1]}\nTotal de changements : {changements}")

        x_p = [stations_globales[s][0] for s in chemin]
        y_p = [stations_globales[s][1] for s in chemin]
        trace = ax.plot(x_p, y_p, color='black', linewidth=3, zorder=3)
        points = ax.scatter(x_p, y_p, color='black', s=30, zorder=4)
        plt.draw()
        
        input("\nAppuyez sur Entrée pour effacer le tracé et recommencer...")
        trace[0].remove()
        points.remove()
        plt.draw()
