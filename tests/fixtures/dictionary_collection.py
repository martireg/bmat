from copy import deepcopy

test_work = {
    "title": "Bmat Remix ft. gravity",
    "contributors": ["Martí Regola", "Isaac Newton"],
    "iswc": "T9214745718",
    "source": "mozilla",
    "id": 1,
}

expected_work = deepcopy(test_work)


test_work_csv = """title,contributors,iswc,source,id
Shape of You,Edward Sheeran,T9204649558,warner,1
Shape of You,Edward Christopher Sheeran,T9204649558,sony,1
Adventure of a Lifetime,O Brien Edward John|Yorke Thomas Edward|Greenwood Colin Charles,T0101974597,warner,2
Adventure of a Lifetime,O Brien Edward John|Selway Philip James|Marti Regola,T0101974597,warner,3
Adventure of a Lifetime,O Brien Edward John|Yorke Thomas Edward|Greenwood Colin Charles,T0101974597,warner,
Me Enamoré,Rayo Gibo Antonio|Ripoll Shakira Isabel Mebarak,T9214745718,universal,1
Me Enamore,Rayo Gibo Antonio|Ripoll Shakira Isabel Mebarak,T9214745718,warner,4
Je ne sais pas,Obispo Pascal Michel|Florence Lionel Jacques,,sony,2
Je ne sais pas,Obispo Pascal Michel|Florence Lionel Jacques,T0046951705,sony,3"""
