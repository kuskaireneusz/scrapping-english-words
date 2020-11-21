from Scrapping.GetDataFromSite import FetchSite

siteNameA1 = FetchSite('https://www.ang.pl/slownictwo/slownictwo-angielskie-poziom-a1')
siteNameA1.saveMultipleListTofile(True, 13, 'a1-words')

siteNameA2 = FetchSite('https://www.ang.pl/slownictwo/slownictwo-angielskie-poziom-a2')
siteNameA2.saveMultipleListTofile(True, 13, 'a2-words')

siteNameB1 = FetchSite('https://www.ang.pl/slownictwo/slownictwo-angielskie-poziom-b1')
siteNameB1.saveMultipleListTofile(True, 13, 'b1-words')

siteNameB2 = FetchSite('https://www.ang.pl/slownictwo/slownictwo-angielskie-poziom-b2')
siteNameB2.saveMultipleListTofile(True, 13, 'b2-words')

