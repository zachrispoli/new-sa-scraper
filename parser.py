import os

pagesDir = 'pages/'
dataDir = 'data/'

# create pages directory
if not os.path.isdir(dataDir):
    print("creating data directory")
    os.makedirs(dataDir)

# parse all pages in pages directory
for pagePath in os.listdir(pagesDir):
    index = pagePath.split('.html')[0]
    dataPath = dataDir + index + '.csv'
    if(('.html' in pagePath) and (not os.path.isfile(dataPath))):
        print("parsing " + pagesDir + pagePath)
        file = open(pagesDir + pagePath, "r")
        html_doc = file.read()

        # TODO parse scores and stuff
        
        dataFile = open(dataPath, 'w')
        dataFile.write('dummy,dummy,dummy')
        dataFile.close()
