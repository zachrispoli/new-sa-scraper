import os
import time
import requests

pagesDir = 'pages/'
saRootPath = 'http://skillattack.com/sa4/'
masterMusicFilename = 'master_music.txt'

# download master_music.txt (songlist)
if not os.path.isfile(masterMusicFilename):
    print("downloading " + masterMusicFilename)
    response = requests.get(saRootPath + '/data/' + masterMusicFilename)
    masterMusicFile = open(masterMusicFilename, 'w')
    masterMusicFile.write(response.text)
    masterMusicFile.close()

# create pages directory
if not os.path.isdir(pagesDir):
    print("creating pages directory")
    os.makedirs(pagesDir)

# get total song count
masterMusicFile = open(masterMusicFilename, 'r').read()
totalSongCount = len(masterMusicFile.split('\n')) - 2
print(str(totalSongCount) + ' total songs')

index = 0
while index <= totalSongCount:
    # download song at index (if it doesn't already exist in pages dir)
    newPagePath = pagesDir + str(index) + '.html'
    if not os.path.isfile(newPagePath):
        print('downloading song at index ' + str(index))
        response = requests.get(saRootPath + 'music.php?index=' + str(index))
        webContent = response.text

        pageFile = open(newPagePath, 'w')
        pageFile.write(webContent)
        pageFile.close()

        # polite scrapers wait ten seconds between requests. (･ω･)
        print('throttling for 10 seconds', end = '', flush=True)
        for second in range(0,9):
            print ('.', end = '', flush=True)
            time.sleep(1)
    else:
        print('page for song at index ' + str(index) + ' already exists. skipping.')

    index += 1
