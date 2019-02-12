import os
import shutil
import zipfile


class FileUtil:

    @staticmethod
    def validate_folder_exists(folder, is_create=False):
        """
        判断文件目录是否存在，如果不存在则创建
        :param folder: 待判断目录
        :param is_create: 是否创建
        :return:
        """
        if not os.path.exists(folder):
            if is_create:
                os.makedirs(folder)
            else:
                raise Exception("该目录不存在，请先创建该目录")
        return True

    @staticmethod
    def validate_file_exists(file):
        """
        判断文件是否存在
        :param file: 待判断文件
        :return:
        """
        if not os.path.isfile(file):
            raise Exception("该文件不存在，请先创建该目录")
        return True

    @staticmethod
    def validate_exists(path):
        """
        判断文件是否存在
        :param path: 待判断文件
        :return:
        """
        if not os.path.exists(path):
            raise Exception("该路径不存在，请先创建该目录")
        return True

    @staticmethod
    def copy_folder(source_path, target_path):
        """
        文件加复制到指定文件夹
        :param source_path: 待复制文件夹完整路径
        :param target_path: 存放目标文件夹路径
        :return:
        """
        try:
            # if os.path.exists(target_path):
            #     shutil.rmtree(target_path)
            shutil.copytree(source_path, target_path)
        except Exception as e:
            raise Exception("复制文件夹失败,%s" % e)

    @staticmethod
    def copy_file(src_file_path, dst_file_path):
        """
        文件复制到指定目录【任意文件】
        :param src_file_path: 待复制文件完整路径
        :param dst_file_path: 存放目标文件路径，带文件名的完整路径 如:c:/tmp/test.txt
        :return:
        """
        try:
            shutil.copyfile(src_file_path, dst_file_path)
        except Exception as e:
            raise Exception("复制文件失败,%s" % e)

    @staticmethod
    def remove_file(file_path):
        """
        移除文件/文件夹
        :param file_path: 目标文件路径
        :return:
        """
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            else:
                shutil.rmtree(file_path)
        except Exception as e:
            raise Exception("移除文件失败,%s" % e)

    @staticmethod
    def rename_file(origin_path, dest_path):
        """
        重命名文件/文件夹
        :param origin_path: 源文件路径
        :param dest_path: 目标文件路径
        :return:
        """
        try:
            shutil.move(origin_path, dest_path)
        except Exception as e:
            raise Exception("重命名文件失败,%s" % e)

    @staticmethod
    def zip_dir(tar_dir_name, zip_file_name):
        """
         函数目的: 压缩指定目录为zip文件
         使用DEMO: FileOperateUtil.zip_dir("C:/tmp/", "E:/test.zip")
        :param tar_dir_name: 待压缩的目录
        :param zip_file_name:  压缩后的zip文件路径 eg:C:/tmp/test.zip
        :return: boolean ,True-成功，False-失败
        """
        file_list = []
        ret = False
        try:
            # 判断是否为文件
            if os.path.isfile(tar_dir_name):
                file_list.append(tar_dir_name)
            else:
                # 循环目录，读取文件列表
                for root, dirs, files in os.walk(tar_dir_name):
                    for name in files:
                        file_list.append(os.path.join(root, name))
            # 创建ZIP文件操作对象
            zf = zipfile.ZipFile(zip_file_name, "w", zipfile.zlib.DEFLATED)
            try:
                for tar in file_list:
                    arc_name = tar[len(tar_dir_name):]
                    zf.write(tar, arc_name)
                ret = True
            except Exception as e:
                # log.debug("压缩文件发送异常，%s" % e)
                raise Exception("压缩文件发送异常")
            finally:
                zf.close()
        except Exception as e:
            # log.debug("---- 压缩文件发生异常，%s --" % e)
            ret = False
        return ret

    @staticmethod
    def unzip_file(zip_file_name, unzip_dir_path):
        """
        解压zip文件到指定目录
        使用DEMO：FileOperateUtil.unzip_file("C:/tmp/test.zip", "c:/tmp/zip/")
        :param zip_file_name: 为zip文件路径，
        :param unzip_dir_path:  为解压文件后的文件目录
        :return : boolean
        """
        # 判断目标文件目录是否存在，不存在就创建
        if not os.path.exists(unzip_dir_path):
            os.mkdir(unzip_dir_path)
        # 创建zip操作对象
        zf_obj = zipfile.ZipFile(zip_file_name)
        try:
            for name in zf_obj.namelist():
                name = name.replace('\\', '/')
                if name.endswith('/'):
                    p = os.path.join(unzip_dir_path, name[:-1])
                    if os.path.exists(p):
                        # 如果文件夹存在，就删除之：避免有新更新无法复制[递归删除]
                        shutil.rmtree(p)
                    os.mkdir(p)
                else:
                    ext_filename = os.path.join(unzip_dir_path, name)
                    ext_dir = os.path.dirname(ext_filename)
                    if not os.path.exists(ext_dir):
                        os.mkdir(ext_dir)
                    outfile = open(ext_filename, 'wb')
                    try:
                        outfile.write(zf_obj.read(name))
                    except Exception as e:
                        # log.debug("写文件发生异常 %s" % e)
                        raise Exception("解压文件发生异常")
                    finally:
                        outfile.close()
        except Exception as e:
            # log.debug("解压文件发生异常 %s" % e)
            raise Exception(e)
            shutil.rmtree(unzip_dir_path)
        return True