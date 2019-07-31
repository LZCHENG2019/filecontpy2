#!/usr/bin/python
# -*- coding: utf-8 -*
import hashlib,os,commands,sys#difflib,argparse,
#获得分支名字
def findfenzhi(filename):
    fenzhi = filename[0:(len(filename)-40)]
    b=0
    for i in range(len(fenzhi)):
        if fenzhi[i] == '-':
            b=b+1
        if b==3:
            return fenzhi[(i+1):len(fenzhi)]
            break
#判断后缀名是大包小包
# def model(file):
#     return os.path.splitext(file)[1]
#存储大包模板，key为模板的分支名，value为模板的路径
def bighashmap(fenzhi):
    dictbig = {'feature_XSTOR1000-Epic-2018-04': '/root/demo/demo/demo/list1tar.tar',
               'feature_ofs3.0_lastdebug': '/root/demo/list1tar.tar'}
    return dictbig[fenzhi]
#存储小包模板，key为模板的分支名，value为模板的路径
def smallhashmap(fenzhi):
    dictsmall = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    return dictsmall[fenzhi]

def un_compress(file):#识别压缩包类型并解压
    if os.path.exists(file):
        kind = fileguess(file)#filetype.guess(file)
        path = os.path.split(file)[0]#获取文件路径，例：/root/demo
        if kind == 'XZ compressed data':#.xz文件解压
            dirnm = commands.getstatusoutput("tar Jxvf %s -C %s | xargs awk 'BEGIN{print ARGV[1]}'" % (file, path))
        elif kind == 'POSIX tar archive (GNU)':#tar包解压
            dirnm = commands.getstatusoutput("tar xvf %s -C %s | xargs awk 'BEGIN{print ARGV[1]}'" %(file,path))
        elif kind == 'gzip compressed data':#.gz文件解压
            dirnm = commands.getstatusoutput("tar zxvf %s -C %s | xargs awk 'BEGIN{print ARGV[1]}'" % (file, path))
        else:
            print('未知文件类型')
        dirname = path + '/' + dirnm[1].split('/')[0]
        return dirname
def fileguess(File):#获取文件类型
    if os.path.exists(File):
        filttyp = commands.getstatusoutput('file %s -b' %File)
        fg = filttyp[1].split(',')[0]
        return fg
    else:
        fg = '/'
        return fg
def getMd5(file1):#获取MD5值
    if (os.path.exists(file1)):
        m = hashlib.md5()
        f = open(file1,'rb')
        str = f.read()
        m.update(str)
        return m.hexdigest()
    # else:
    #     m = file1
    #     print(file1 + '文件错误或不存在')
    #     return m
def comparfile(file1,file2):#对比文件
    filetp = 'true'
    filecont = 'true'
    filesize = 'true'
    file1tp = fileguess(file1)
    file2tp = fileguess(file2)
    if file1tp == file2tp:        #先判断文件类型，若相同则继续对比，若不同则直接退出对比
        size1 = os.path.getsize(file1)#filesize(file1)
        size2 = os.path.getsize(file2)#filesize(file2)
        sizevalue = 1 #此处用来定义文件大小阈值，单位是字节（B），可设置
        if size1 == size2:#先判断文件尺寸，若相同则对比MD5值
            file1md5 = getMd5(file1)
            file2md5 = getMd5(file2)
            if file1md5 == file2md5:
                # print('%s 和%s 大小、内容均无差异' %(file1,file2),)#'\n','文件类型为 %s' % file1tp,'\n',
                  #'基准文件大小：%s' % size1,'\n','待测文件大小：%s' % size2)#大小内容均相同
                result = 'true'
                return result,filetp,filecont,filesize
            else:
                result = 'false'
                filecont = 'false'
                # print('%s 和%s 大小相同，内容不同' % (file1, file2),'\n','文件类型为 %s' % file1tp,'\n',
                #   '基准文件大小：%s' % size1,'\n','待测文件大小：%s' % size2)#大小一样，内容不一样
                return result,filetp,filecont,filesize

        elif abs(size1-size2)  > sizevalue:#允许文件大小有差异，但是若大于某一阈值，则输出错误
            result = 'false'
            filesize = 'false'
            # print('%s 和 %s 文件大小差距过大' % (file1, file2),'\n','文件类型为 %s' % file1tp,'\n',
            #       '基准文件大小：%s' % size1,'\n','待测文件大小：%s' % size2)
            return result,filetp,filecont,filesize
    else:
        # print(' %s 和 %s 类型不同，不进行对比' %(file1,file2))
        filetp = 'false'
        result = 'false'
        return result,filetp,filecont,filesize
def compardirs(path1,path2):#对比文件夹内容
    file1m,file2m,diff,file_tp,file_cont,file_size = 0,0,[],0,0,0
    difftp = 1#此阈值用来调节文件夹内文件类型差异数量差距过大时报警
    diffcont = 1#此阈值用来调节文件夹内文件内容差异数量差距过大时报警（大小相同，类型不同的情况）
    diffsize = 1#此阈值用来调节文件夹内文件大小差异数量差距过大时报警
    diffdirs = 1#此阈值用来调节文件夹内文件缺少/增多数量差距过大时报警
    finresult = 'true'
    files1_list = os.listdir(path1)
    files2_list = os.listdir(path2)
    file1m = len(files1_list)
    file2m = len(files2_list)
    for name1 in files1_list:#files:
        file1 = os.path.join(path1, name1)
        file2 = os.path.join(path2, name1)
        if os.path.exists(file1) and os.path.exists(file2):
            result,filetp,filecont,filesize = comparfile(file1,file2)
            if result == 'true':#如果对比结果一致则返回'true'
                finresult = 'true'
            else:
                diff.append(name1)
            if filetp == 'false':
                file_tp += 1
            if filecont == 'false':
                file_cont += 1
            if filesize == 'false':
                file_size += 1

    if abs(file1m-file2m) > diffdirs:
        finresult = 'false'
        return finresult,diff
    if file_tp > difftp:
        finresult = 'false'
        return finresult,diff
    if file_cont > diffcont:
        finresult = 'false'
        return finresult,diff
    if file_size > diffsize:

        finresult = 'false'
        return finresult,diff
    return finresult,diff
def compardirs2(path1,path2,diff):
    for name in diff:
        file1 = os.path.join(path1,name)
        file2 = os.path.join(path2,name)
        file1path = un_compress(file1)  # filepath是解压后文件所在目录
        file2path = un_compress(file2)
        result,dif= compardirs(file1path, file2path)
        return result
def final_result(file1,file2):
    file1path = un_compress(file1)  # filepath是解压后文件所在目录
    file2path = un_compress(file2)
    result, diff = compardirs(file1path, file2path)
    if result == 'true':
        Result = True
        # os.system('\\rm -r %s %s' % (file1path, file2path))
        # return True
        # print True
    else:
        result2 = compardirs2(file1path, file2path, diff)
        if result2 =='true':
            Result = True
            # os.system('\\rm -r %s %s' % (file1path, file2path))
            # return True
            # print True
        else:
            Result = False
            # os.system('\\rm -r %s %s' % (file1path, file2path))
            # return False
            # print False
    os.system('\\rm -r %s %s'%(file1path,file2path))
    return Result
def main1(file1,file2):
    if os.path.exists(file1) and os.path.exists(file2):
        size1 = os.path.getsize(file1)#filesize(file1)#文件1的大小
        size2 = os.path.getsize(file2)#filesize(file2)#文件2的大小
        if size1 == size2:     #首先对比文件大小，若文件大小一样，则继续对比MD5值
            m1 = getMd5(file1)
            m2 = getMd5(file2)
            if m1 == m2:
                return True
                # print True
            else:
                return final_result(file1, file2)
        else:
            return final_result(file1, file2)
            # print 'exist'
    # else:
    #     a='文件不存在，请重新输入'
    #     return a
def Main():
    File = sys.argv[1] #运行python时传入参数
    filename = os.path.basename(File)
    class Networkerror(RuntimeError):
        def __init__(self, arg):
            self.args = arg
    try:
        if fileguess(File) == 'POSIX tar archive (GNU)':
            #判断文件类型是否为Tar包
            modelfile = bighashmap(findfenzhi(filename))
        else:
            modelfile = smallhashmap(findfenzhi(filename))
        # if model(File) == '.tar':
        #     modelpath = bighashmap(findfenzhi(filename))
        # else:
        #     modelpath = smallhashmap(findfenzhi(filename))

        # process = os.popen('python /root/test/filecontpy2.py %s %s' % (modelpath, path))
        # output = process.read().rstrip()
        # process.close
        output = main1(modelfile,File)
        print output
        if (output == True):

            print '允许拷贝！'
        if (output == False):
            print '差别过大，不可拷贝！'
    except KeyError,e:
        print '输入模板不存在或模板不存在'
    # parser = argparse.ArgumentParser()
    # parser.add_argument("file1")
    # parser.add_argument("file2")
    # args = parser.parse_args()
    # file1 = args.file1
    # file2 = args.file2
if __name__=='__main__':
    Main()