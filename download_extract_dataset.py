import os
import requests
import cv2
from tqdm import tqdm

sourceDirectory = './VisiFireDataset'
targetDirectory = './FireSegmentationDataset'


# From
# A. E. Çetin. “Computer Vision Based Fire Detection Dataset.” 2014. http://signal.ee.bilkent.edu.tr/VisiFire/.
datasetLink = {
    'Video01':'http://signal.ee.bilkent.edu.tr/VisiFire/Demo/FireClips/controlled1.avi', 
    'Video02':'http://signal.ee.bilkent.edu.tr/VisiFire/Demo/FireClips/controlled2.avi',
    'Video03':'http://signal.ee.bilkent.edu.tr/VisiFire/Demo/FireClips/controlled3.avi',
    'Video04':'http://signal.ee.bilkent.edu.tr/VisiFire/Demo/FireClips/forest1.avi',
    'Video05':'http://signal.ee.bilkent.edu.tr/VisiFire/Demo/FireClips/forest2.avi',
    'Video06':'http://signal.ee.bilkent.edu.tr/VisiFire/Demo/FireClips/forest3.avi',
    'Video07':'http://signal.ee.bilkent.edu.tr/VisiFire/Demo/FireClips/forest4.avi',
    'Video08':'http://signal.ee.bilkent.edu.tr/VisiFire/Demo/FireClips/forest5.avi',
    'Video09':'http://signal.ee.bilkent.edu.tr/VisiFire/Demo/FireClips/fBackYardFire.avi',
    'Video10':'http://signal.ee.bilkent.edu.tr/VisiFire/Demo/FireClips/ForestFire1.avi',
    'Video11':'http://signal.ee.bilkent.edu.tr/VisiFire/Demo/FireClips/fire1.avi',
    'Video12':'http://signal.ee.bilkent.edu.tr/VisiFire/Demo/FireClips/40m_PanFire_20060824.avi'
}

datasetFile = {
    'Video01':'controlled1.avi', 
    'Video02':'controlled2.avi',
    'Video03':'controlled3.avi',
    'Video04':'forest1.avi',
    'Video05':'forest2.avi',
    'Video06':'forest3.avi',
    'Video07':'forest4.avi',
    'Video08':'forest5.avi',
    'Video09':'fBackYardFire.avi',
    'Video10':'ForestFire1.avi',
    'Video11':'fire1.avi',
    'Video12':'40m_PanFire_20060824.avi'
}

datasetFPS = {
    'Video01':15, 
    'Video02':15,
    'Video03':15,
    'Video04':15,
    'Video05':15,
    'Video06':15,
    'Video07':15,
    'Video08':15,
    'Video09':2,
    'Video10':15,
    'Video11':5,
    'Video12':30
}

def downloadFireData():
    print("Downloading Visi Fire Dataset.")

    directory = sourceDirectory+"/"
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    try:
        for video, url in tqdm(datasetLink.items(), position=0, leave=True):
            res = requests.get(url, stream=True)
            total_size_in_bytes= int(res.headers.get('content-length', 0))
            block_size = 1024
            progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True, position=1, leave=False)
            with open(directory + url.rsplit('/', 1)[-1], 'wb') as file:
                for data in res.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)
    except:
        print("Err: Connection problem")
        return -1

    print("Finish download")
    return 0

def checkDir():
    if(not os.path.exists(sourceDirectory)):
        print("ERR: VisiFire Dataset not found. Download and make sure it is in correct directory.")
        return -1
    return 0

def extractVideo(imgpersec, vidName, vidFile):
    vidObj = cv2.VideoCapture(sourceDirectory+"/"+vidFile)

    saveDir = targetDirectory+"/"+vidName+"/"+vidName+"_Frame"
    os.makedirs(saveDir, exist_ok=True)

    f_count = 0 
    success = 1 
    fps = round(float(vidObj.get(cv2.CAP_PROP_FPS)), 0)

    count = 0
    while success: 
        success, frame = vidObj.read()
        if(success!=1):
            break
        
        if (f_count%(int(fps/imgpersec)) == 0):
            count += 1
            if f_count < 100:
                nm = saveDir+"/"+vidName+"_Frame0"
            if f_count < 10:
                nm = saveDir+"/"+vidName+"_Frame00"
            cv2.imwrite(nm+"%d.jpg" % (f_count+1), frame) 
        f_count += 1


def extractData():
    for key in tqdm(datasetFile.keys()):
        extractVideo(datasetFPS[key], key, datasetFile[key])

if __name__ == '__main__':
    if(downloadFireData()==-1):
        exit()
    if(checkDir()==-1):
        exit()
    print("")
    print("Extracting Video Frames")
    extractData()