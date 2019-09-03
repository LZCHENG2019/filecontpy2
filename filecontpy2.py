#!/usr/bin/python
# -*- coding: utf-8 -*
#20190902存
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
    result = True

    path_num_value = 1                  #文件数量差异阈值
    path_size_value = 1                 #文件大小差异阈值
    path_diff_value = 1                 #文件内容差异阈值

    path1_num = 0
    path2_num = 0
    path1_size = 0
    path2_size = 0

    files1_list = os.listdir(path1)                 #列出文件夹path下的文件列表
    files2_list = os.listdir(path2)

    for i in range(len(files1_list)):               #解压path1内的全部压缩文件
        file = path1+'/'+files1_list[i]
        if os.path.isfile(file):
            file_path = un_compress(file)
    for i in range(len(files2_list)):
        file =path2+'/'+files2_list[i]
        if os.path.isfile(file):
            file_path = un_compress(file)
    try:
        commands("\\rm %s/*.tar*" % path1)
        commands("\\rm %s/*.tar*" % path2)
    except:
        pass

    path1_num = int(commands.getstatusoutput("ls %s -lR | grep '^-' | wc -l" % path1)[1])       #计算path1文件夹内所有文件数（包含子文件）
    path2_num = int(commands.getstatusoutput("ls %s -lR | grep '^-' | wc -l" % path2)[1])
    path1_size = int(commands.getstatusoutput("du %s -s -k| awk '{print $1}'" % path1)[1])        #计算path1文件夹所占大小
    path2_size = int(commands.getstatusoutput("du %s -s -k| awk '{print $1}'" % path2)[1])

    a = commands.getstatusoutput("diff -rqH %s %s 2>/dev/null | wc -l" %(path1,path2))[1]
    path_diff = int(a)         #计算path1与path2里面各级文件差异的数量
    if abs(path1_size-path2_size) >= path_size_value:
        result =  False
        print ('文件大小差异%skb' %abs(path1_size-path2_size))
    if abs(path1_num-path2_num) >= path_num_value:
        result = False
        print ('文件数量差异%s个' % abs(path1_num - path2_num))
    if path_diff >= path_diff_value:
        result = False
        print ('文件内容差异%s个' % path_diff)
    return result
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
    result = False
    if os.path.isfile(file1) and os.path.isfile(file2):
        file_temp_typ = fileguess(file1)
        file_tested_typ = fileguess(file2)
        if file_temp_typ == file_tested_typ:                #先判断文件类型，若相同则继续对比，若不同则直接退出对比
            size_temp = os.path.getsize(file1)    #/ 1048576      #filesize(file1)
            size_tested = os.path.getsize(file2)  #/ 1048576    #filesize(file2)
            # size_diff = abs(size_temp-size_tested)
            if size_temp == size_tested:                    #先判断文件尺寸，若相同则对比MD5值
                file1md5 = getMd5(file1)
                file2md5 = getMd5(file2)
                if file1md5 == file2md5:                    #两个文件大小、内容均无差异
                    result = True
                    return result
                    # return result,filetp,filecont,filesize
                else:                                       #两个文件大小相同，内容不同
                    # print ('文件大小差异为 %s bit' %abs(file1md5-file2md5))
                    file_temp_path = un_compress(file1)
                    file_tested_path = un_compress(file2)
                    # os.system("\\rm *.tar*")
                    result = compardirs(file_temp_path,file_tested_path)

            else:   #允许文件大小有差异，但是若大于某一阈值，则输出错误
                file_temp_path = un_compress(file1)
                file_tested_path = un_compress(file2)
                # os.system("\\rm *.tar*")
                result = compardirs(file_temp_path, file_tested_path)

        else:                                               #两个文件类型不同不进行对比
            # filetp = False
            result = False
    # if os.path.isdir(file_temp_path) and os.path.isdir(file_tested_path):
    #     os.system('\\rm -r %s %s' % (file_temp_path, file_tested_path))
    return result
def Main():
    file_tested = sys.argv[1]                           #运行python时传入参数
    # filename = os.path.basename(File)
    class Networkerror(RuntimeError):
        def __init__(self, arg):
            self.args = arg
    try:
        file_template = find_template(file_tested)
        if os.path.isfile(file_template) and os.path.isfile(file_tested):
            result = comparelement(file_template, file_tested)
        print result
    except KeyError,e:
        print '输入文件不存在或模板不存在'
if __name__=='__main__':
    Main()