from PIL import Image #使用这个库可以对图片进行基本的处理，
import os


#本文件将对一些常见操作进行基本封装





#裁剪成正方形, flag为true则表示填充， 为false则表示不填充的最大化裁剪
def cutPic(img4, flag=True):
    if flag:
        longer_side = max(img4.size)
        horizontal_padding = (longer_side - img4.size[0]) / 2
        horizontal_padding = (int)(horizontal_padding)
        vertical_padding = (longer_side - img4.size[1]) / 2
        vertical_padding = (int)(vertical_padding)
        img5 = img4.crop(
            (
                -horizontal_padding,
                -vertical_padding,
                img4.size[0] + horizontal_padding,
                img4.size[0] + horizontal_padding *2 -vertical_padding  
            )
        )
        return img5
    else:
        longer_side = min(img4.size)
        horizontal_padding = (longer_side - img4.size[0]) / 2
        horizontal_padding = (int)(horizontal_padding)
        vertical_padding = (longer_side - img4.size[1]) / 2
        vertical_padding = (int)(vertical_padding)
        img5 = img4.crop(
            (
                -horizontal_padding,
                -vertical_padding,
                img4.size[0] + horizontal_padding,
                img4.size[0] + horizontal_padding *2 -vertical_padding  
            )
        )
        return img5



#读取某个目录中的所有文件名称
def getPathFile(path):
    ans = []
    for i,j,k in os.walk(path): #三个数据分别是当前路径，文件夹名称数组， 文件数组
        ans.append([i, k])
        #print(i,j,k) 
    return ans


#用来对某个文件夹内的所有图片进行裁剪处理以及放缩，如果内涵文件夹将进行递归处理
def filePicCut(path, width=562, height=562):
    file =  getPathFile(path)
    for i in file:
        dirName , fileName = i
        for j in fileName:
            try: 
                filePath = dirName +"/" + j
                print(filePath)
                img  = Image.open(filePath)
                img = cutPic(img)
                img = img.resize((width, height))
                img.save(filePath)
            except:
                print(filePath + "文件修改失败")
            




#对图片进行所略处理
# img = img.resize(width, height)



if __name__ == "__main__":
    filePicCut("/home/lwl/Study/code/Python/selenium/BaiduPic")
    img  = Image.open('/home/lwl/Study/code/Python/selenium/BaiduPic/images/0.jpg')
    img.show()

    