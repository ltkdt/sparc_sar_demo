import asf_search as asf

aoi = "POLYGON((105.7962 9.8697,106.2458 9.8697,106.2458 10.0234,105.7962 10.0234,105.7962 9.8697))"


opts = {
    'platform': asf.PLATFORM.SENTINEL1,
    'start': '2022-01-01T00:00:00Z',
    'end': '2022-02-01T23:59:59Z'
}

results = asf.geo_search(intersectsWith=aoi, **opts)

print(f'{len(results)} results found')

print(results)

'''
Results: ASF products object

ASFProduct provides a number of metadata fields, such as:

    Geographic coordinates
        Latitude/Longitude
        Shape type
    Scene and product metadata
        Path, frame
        Platform, beam, polarization
        File name, size, URL
        and many others

Geographic coordinates are stored in the geometry attribute:
'''

# Preview csv file before writing
# print(*results.csv(), sep='')

# Store results in a CSV

with open("search_results.csv", "w") as f:
   f.writelines(results.csv())

# Downloading

session = asf.ASFSession().auth_with_creds(username="username", password="password")

# processes: maximum number downloads to run in parallel
results.download(path='./download_data', session=session, processes=5) # 1 process tai 5 anh