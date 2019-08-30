#!/usr/bin/python
# -*- coding: utf-8 -*
import hashlib,os,commands,sys

#存储大包（tar）模板，key为模板的分支名，value为模板的路径
def tamplate_tar(fenzhi):
    dictbig = {'development_ofs3.1.1': '/code/templates/ParaStor-3.0.0-centos7.5-development_ofs3.1.1_release_66b1291_66b1291_20190827_195832-2-1.tar.ib4.6.1',
               'development_ofs3.1.1_release': '/code/templates/ParaStor-3.0.0-centos7.5-development_ofs3.1.1_release_66b1291_66b1291_20190827_195832-2-1.tar.ib4.6.1',
               'feature_replication-rack-listen': '/code/templates/ParaStor-3.0.0-centos7.5-development_ofs3.1.1_release_66b1291_66b1291_20190827_195832-2-1.tar.ib4.6.1',
               'feature_ofs3.0_lastdebug': '/code/templates/ParaStor-3.0.0-centos7.5-feature_ofs3.0_lastdebug_720dbee_720dbee_20190822_150240-2-1.tar.ib4.6.1',
               'feature_ofs3.0_419_lastdebug': '/code/templates/ParaStor-3.0.0-centos7.5-feature_ofs3.0_419_lastdebug_2b2b4cc_2b2b4cc_20190806_141438-2-1.tar.ib4.6.1',
               'bugfix_ofs3.0_419_lastdebug_verify': '/code/templates/ParaStor-3.0.0-centos7.5-feature_ofs3.0_419_lastdebug_2b2b4cc_2b2b4cc_20190806_141438-2-1.tar.ib4.6.1',
               'feature_XSTOR1000-Epic-2018-04': '/code/templates/XStor-1.0.0-centos7.5-feature_XSTOR1000-Epic-2018-04_dc4a7b9_dc4a7b9_20190824_143910-2-1.tar.ib4.4.1',
               'feature_XSTOR1000-Epic-2018-04-lirj-fix4906': '/code/templates/XStor-1.0.0-centos7.5-feature_XSTOR1000-Epic-2018-04_dc4a7b9_dc4a7b9_20190824_143910-2-1.tar.ib4.4.1',
               'release_XSTOR1000-V1.0.0-POC-ELEC': '/code/templates/XStor-1.0.0-centos7.5-feature_XSTOR1000-Epic-2018-04_dc4a7b9_dc4a7b9_20190824_143910-2-1.tar.ib4.4.1'
               }
               #  'feature_ofs3.0_lastdebug': '/root/demo/list1tar.tar'}
    return dictbig[fenzhi]

#存储小包(tar.xz)模板，key为模板的分支名，value为模板的路径
def tamplate_xz(fenzhi):
    dictsmall = {
                'development_XSTOR1000-V1.1-Dev': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'development_XSTOR1000-V1.1-Dev_SSDC': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'XSTOR1000-ssdc-test': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'XSTOR1000-obs_Hotfix': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'XSTOR1000-V1.1-Dev_SSDC_development': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'feature_XSTOR1000-V1.1-demo-EBFS-cowork': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'feature_XSTOR1000-V1.1-Dev_SSDC-cowork': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'feature_XSTOR1000-V1.1-Dev_Jnl-MultiDevice_liull2': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'feature_XSTOR1000-V1.1-Dev_mgr': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'feature_XSTOR1000-V1.1-Dev_oSan_EBFS-cowork-snap-xiexd': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'feature_sysqos-cowork-regulator-caohb': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'feature_sysqos-cowork-khy': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz'
                }
    return dictsmall[fenzhi]

def compardirs(path1,path2):#对比文件夹内容
    file1m,file2m,diff,file_tp,file_cont,file_size = 0,0,[],0,0,0
    difftp = 1#此阈值表示文件类型差异数量差距
    diffcont = 1#此阈值表示文件内容差异数量差距（大小相同，类型不同的情况）
    diffsize = 1#此阈值表示文件大小差异数量差距
    diff_files = 1#此阈值表示文件缺少/增多数量差距
    finresult = False
    files1_list = os.listdir(path1)
    files2_list = os.listdir(path2)
    file1m = len(files1_list)
    file2m = len(files2_list)
    for name1 in files1_list:#files:
        file1 = os.path.join(path1, name1)
        file2 = os.path.join(path2, name1)
        if os.path.exists(file1) and os.path.exists(file2):
            result,filetp,filecont,filesize = comparfile(file1,file2)
            if result == True:#如果对比结果一致则返回True
                finresult = True
            else:
                diff.append(name1)
            if filetp == False:
                file_tp += 1
            if filecont == False:
                file_cont += 1
            if filesize == False:
                file_size += 1
        else:
            file2m += 1
    if abs(file1m-file2m) > diff_files:
        finresult = False
    if file_tp > difftp:
        finresult = False
    if file_cont > diffcont:
        finresult = False
    if file_size > diffsize:
        finresult = False
    return finresult,diff

def compardirs2(path1,path2,diff):
    if diff :
        for name in diff:
            file1 = os.path.join(path1,name)
            file2 = os.path.join(path2,name)
            file1path = un_compress(file1)  # filepath是解压后文件所在目录
            file2path = un_compress(file2)
            result,dif= compardirs(file1path, file2path)
    else:
        result = False
    return result

def Result(file1,file2):
    file1path = un_compress(file1)  # filepath是解压后文件所在目录
    file2path = un_compress(file2)
    result, diff = compardirs(file1path, file2path)
    if result == False:#如果一级文件夹有差异则继续对比
        result = compardirs2(file1path, file2path, diff)
    if os.path.isdir(file1path) and os.path.isdir(file2path):
        os.system('\\rm -r %s %s'%(file1path,file2path))
    return result

#获得分支名字
# def findfenzhi(filename):
#     fenzhi = filename[0:(len(filename)-40)]
#     b=0
#     for i in range(len(fenzhi)):
#         if fenzhi[i] == '-':
#             b=b+1
#         if b==3:
#             return fenzhi[(i+1):len(fenzhi)]
#             break

def un_compress(file):#识别压缩包类型并解压
    if os.path.isfile(file):
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
    if os.path.isfile(File):
        filttyp = commands.getstatusoutput('file %s -b' %File)
        fg = filttyp[1].split(',')[0]
        return fg
    else:
        fg = '/'
        return fg

def getMd5(file1):#获取MD5值
    if (os.path.isfile(file1)):
        m = hashlib.md5()
        f = open(file1,'rb')
        str = f.read()
        m.update(str)
        return m.hexdigest()

def comparfile(file1,file2):#对比文件
    filetp = False
    filecont = False
    filesize = False
    file1tp = fileguess(file1)
    file2tp = fileguess(file2)
    if file1tp == file2tp:        #先判断文件类型，若相同则继续对比，若不同则直接退出对比
        size1 = os.path.getsize(file1)#filesize(file1)
        size2 = os.path.getsize(file2)#filesize(file2)
        sizevalue = 1 #此处用来定义文件大小阈值，单位是字节（B），可设置
        if size1 == size2:#先判断文件尺寸，若相同则对比MD5值
            file1md5 = getMd5(file1)
            file2md5 = getMd5(file2)
            if file1md5 == file2md5:#两个文件大小、内容均无差异
                result = True
                return result,filetp,filecont,filesize
            else:#两个文件大小相同，内容不同
                result = False
                filecont = False
                return result,filetp,filecont,filesize

        elif abs(size1-size2)  > sizevalue:#允许文件大小有差异，但是若大于某一阈值，则输出错误
            result = False
            filesize = False
            return result,filetp,filecont,filesize
    else:#两个文件类型不同不进行对比
        filetp = False
        result = False
        return result,filetp,filecont,filesize
def result_main(file1,file2):
    if os.path.isfile(file1) and os.path.isfile(file2):
        size1 = os.path.getsize(file1)#文件1的大小
        size2 = os.path.getsize(file2)#文件2的大小
        if size1 == size2:     #首先对比文件大小，若文件大小一样，则继续对比MD5值
            m1 = getMd5(file1)
            m2 = getMd5(file2)
            if m1 == m2:
                return True
            else:
                return Result(file1, file2)
        else:
            return Result(file1, file2)
def Main():
    File = sys.argv[1] #运行python时传入参数
    filename = os.path.basename(File)
    class Networkerror(RuntimeError):
        def __init__(self, arg):
            self.args = arg
    try:
        if fileguess(File) == 'POSIX tar archive (GNU)':
            #判断文件类型是否为Tar包
            branch = commands.getstatusoutput(" echo %s | cut -d '-' -f 4- | sed 's/-2-1.*//' | rev | cut -d '_' -f 5- | rev" % filename)[1]
            tamplatefile = tamplate_tar(branch)
            #tamplatefile为对比模板文件
        elif fileguess(File) == 'XZ compressed data':
            branch = commands.getstatusoutput(" echo %s | cut -d '-' -f 4- | sed 's/-2-1.*//' | rev | cut -d '_' -f 4- | rev" % filename)[1]
            tamplatefile = tamplate_xz(branch)
        output = result_main(tamplatefile,File)
        print output
    except KeyError,e:
        print '输入文件不存在或模板不存在'
if __name__=='__main__':
    Main()