#!/usr/bin/python
# -*- coding: utf-8 -*
import hashlib,os,commands,sys
#存储大包（tar）模板，key为模板的分支名，value为模板的路径
def template_tar(branch):
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
    return dictbig[branch]
#存储小包(tar.xz)模板，key为模板的分支名，value为模板的路径
def template_xz(branch):
    dictsmall = {
                'development_XSTOR1000-V1.1-Dev': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'development_XSTOR1000-V1.1-Dev_SSDC': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'XSTOR1000-ssdc-test': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'XSTOR1000-obs_Hotfix': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'XSTOR1000-V1.1-Dev_SSDC_development': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'feature_XSTOR1000-V1.1-demo-EBFS-cowork': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'feature_XSTOR1000-V1.1-demo-EBFS-cowork_goulinghan': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'feature_XSTOR1000-V1.1-Dev_SSDC-cowork': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'feature_XSTOR1000-V1.1-Dev_Jnl-MultiDevice_liull2': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'feature_XSTOR1000-V1.1-Dev_mgr': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'feature_XSTOR1000-V1.1-Dev_oSan_EBFS-cowork-snap-xiexd': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'feature_sysqos-cowork-regulator-caohb': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz',
                'feature_sysqos-cowork-khy': '/code/templates/xstor-1.0.0-centos7.5-feature_XSTOR1000-V1.1-PrepLpcEbfsLioc_cowork_0e1ae6f_20190826_141313-2-1.tar.xz'
                }
    return dictsmall[branch]
def compardirs(path1,path2,iteration=1):#对比文件夹内容
    # file1m,file2m,diff_temp,diff_tested,file_tp,file_cont,file_size = 0,0,[],[],0,0,0
    file1m, file2m,file_tp, file_cont, file_size = 0, 0, 0, 0, 0
    difftp = 1                                      #此阈值表示文件类型差异数量差距(本次测试无这种情况)
    diffcont = 1                                    #此阈值表示文件内容差异数量差距（大小相同，类型不同的情况，本次测试无这种情况）
    diffsize = 1                                    #此阈值表示文件大小差异数量差距(出现该情况)
    diff_files = 1                                  #此阈值表示文件缺少/增多数量差距（本次测试无该情况）
    finresult = True
    files1_list = os.listdir(path1)                 #列出文件夹path下的文件列表
    files2_list = os.listdir(path2)
    files1_list.sort()                              #将files_list列表进行排序
    files2_list.sort()
    file1m = len(files1_list)
    file2m = len(files2_list)
    for i in range(len(files1_list)):
        name_temp = files1_list[i]
        name_tested = files2_list[i]
        file_temp = os.path.join(path1, name_temp)
        file_tested = os.path.join(path2, name_tested)
        # if os.path.isfile(file_temp) and os.path.isfile(file_tested):
        result,filetp,filecont,filesize = comparelement(file_temp,file_tested)
        # if result == True:                      #如果对比结果一致则返回True
        #     finresult = True
        if result == False and iteration == 1:
            dir_temp = un_compress(file_temp)
            dir_tested = un_compress(file_tested)
            if os.path.exists(dir_temp) and os.path.exists(dir_tested):
                result2 = compardirs(dir_temp,dir_tested,2)
        if result2 == False:
            finresult = False
        if filetp == False:
            file_tp += 1
        if filecont == False:
            file_cont += 1
        if filesize == False:
            file_size += 1
    if abs(file1m-file2m) >= diff_files:
        print ('文件夹%s与模板文件个数差异%s个' %(os.path.basename(path2),abs(file1m-file2m)))
        finresult = False
    if file_tp >= difftp:
        print ('文件夹%s与模板件类型差异%s个' %(os.path.basename(path2),ile_tp))
        finresult = False
    if file_cont >= diffcont:
        print ('文件夹%s与模板文件内容差异%s个' %(os.path.basename(path2),file_cont))
        finresult = False
    if file_size >= diffsize:
        print ('文件夹%s与模板文件大小差异%s个' %(os.path.basename(path2),file_size))
        finresult = False
    return finresult     #,diff_temp,diff_tested
def find_template(file):
    filename = os.path.basename(file)
    if fileguess(file) == 'POSIX tar archive (GNU)':
        # 判断文件类型是否为Tar包
        branch = commands.getstatusoutput(
            " echo %s | cut -d '-' -f 4- | sed 's/-2-1.*//' | rev | cut -d '_' -f 5- | rev" % filename)[1]
        file_template = template_tar(branch)
        print ('模板%s内:' % os.path.basename(file_template))
        return file_template
        # file_template为对比模板文件
    elif fileguess(file) == 'XZ compressed data':
        branch = commands.getstatusoutput(
            " echo %s | cut -d '-' -f 4- | sed 's/-2-1.*//' | rev | cut -d '_' -f 4- | rev" % filename)[1]
        file_template = template_xz(branch)
        print ('模板%s内:' % os.path.basename(file_template))
        return file_template
def un_compress(file):#识别压缩包类型并解压
    dirnm=''
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
            dirnm = 'null'
        dirname = path + '/' + dirnm[1].split('/')[0]
            #print('未知文件类型')
    elif os.path.isdir(file):
        dirname = 'null'
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
def comparelement(file1,file2):#对比文件
    filetp = ''
    filecont = ''
    filesize = ''
    sizevalue = 1 #此处用来定义文件大小阈值，单位是字节（B），可设置
    result = True
    if os.path.isfile(file1) and os.path.isfile(file2):
        file_temp_typ = fileguess(file1)
        file_tested_typ = fileguess(file2)
        if file_temp_typ == file_tested_typ:                #先判断文件类型，若相同则继续对比，若不同则直接退出对比
            size_temp = os.path.getsize(file1)    #/ 1048576      #filesize(file1)
            size_tested = os.path.getsize(file2)  #/ 1048576    #filesize(file2)
            size_diff = abs(size_temp-size_tested)
            if size_temp == size_tested:                    #先判断文件尺寸，若相同则对比MD5值
                file1md5 = getMd5(file1)
                file2md5 = getMd5(file2)
                if file1md5 == file2md5:                    #两个文件大小、内容均无差异
                    result = True
                    # return result,filetp,filecont,filesize
                else:                                       #两个文件大小相同，内容不同
                    # print ('文件大小差异为 %s bit' %abs(file1md5-file2md5))
                    result = False
                    filecont = False
                    # return result,filetp,filecont,filesize

            elif size_diff >= sizevalue:   #允许文件大小有差异，但是若大于某一阈值，则输出错误
                # print ('%s与%s相差%sByte' %(os.path.basename(file1),os.path.basename(file2),abs(size_temp-size_tested)))
                print ('filesize-|temp-tested|:%s/byte' %size_diff)
                result = False
                filesize = False
                # return result,filetp,filecont,filesize
        else:                                               #两个文件类型不同不进行对比
            filetp = False
            result = False
    elif os.path.isdir(file1) and os.path.isdir(file2):
        size_temp = int(commands.getstatusoutput("du --max-depth=0 -b %s | awk '{print $1}'" %file1)[1])
        size_tested = int(commands.getstatusoutput("du --max-depth=0 -b %s | awk '{print $1}'" % file2)[1])
        size_diff = abs(size_temp - size_tested)
        if size_diff >= sizevalue:
            print ('dirsize-|temp-tested|:%s/byte' %size_diff)
            result = False
            filesize = False
    return result,filetp,filecont,filesize
def Main():
    # Result = ''
    file_tested = sys.argv[1]                           #运行python时传入参数
    # filename = os.path.basename(File)
    class Networkerror(RuntimeError):
        def __init__(self, arg):
            self.args = arg
    try:
        # if fileguess(File) == 'POSIX tar archive (GNU)':
        #     #判断文件类型是否为Tar包
        #     branch = commands.getstatusoutput(" echo %s | cut -d '-' -f 4- | sed 's/-2-1.*//' | rev | cut -d '_' -f 5- | rev" % filename)[1]
        #     file_template = template_tar(branch)
        #     print ('模板%s内:' % os.path.basename(file_template))
        #     #file_template为对比模板文件
        # elif fileguess(File) == 'XZ compressed data':
        #     branch = commands.getstatusoutput(" echo %s | cut -d '-' -f 4- | sed 's/-2-1.*//' | rev | cut -d '_' -f 4- | rev" % filename)[1]
        #     file_template = template_xz(branch)
        #     print ('模板%s内:' % os.path.basename(file_template))
        file_template = find_template(file_tested)
        if os.path.isfile(file_template) and os.path.isfile(file_tested):
            result, filetp, filecont, filesize = comparelement(file_template, file_tested)
            # print result
            if filetp == False:
                Result = False
            elif result == False:
                path_temp = un_compress(file_template)
                path_tested = un_compress(file_tested)
                Result = compardirs(path_temp, path_tested)
        # return Result
        # output = result_main(file_template,File)
        print Result
        if os.path.isdir(path_temp) and os.path.isdir(path_temp):
            os.system('\\rm -r %s %s'%(path_temp, path_tested))
    except KeyError,e:
        print '输入文件不存在或模板不存在'
if __name__=='__main__':
    Main()