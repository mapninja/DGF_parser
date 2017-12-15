#Import modules
import glob, os, gdal, fnmatch

#Set base directory to location of script
base_directory = os.path.abspath('')

#Make a list of Multispectral directories with 'MUL' in the path
multi_directory_list = glob.glob(os.path.join(base_directory, '*MUL'))

#Make Panchromatic directory [pan_directory] path by replacing 'MUL' with 'PAN'
for multi_directory in multi_directory_list:
    pan_directory = multi_directory.replace('MUL','PAN')
    print(multi_directory)
    print(pan_directory)
    #Make a list of TIF files in the multi_directory
    multi_tiffs_list = fnmatch.filter((os.listdir(multi_directory)), '*.TIF')
    for multi_tiff_name in multi_tiffs_list:
        print(multi_tiff_name)
        multi_rowcol_wildcard = '*'+multi_tiff_name[19:24]+'*'
        #print(multi_rowcol)
        pan_tiffs_list = fnmatch.filter((os.listdir(pan_directory)), '*.TIF')
        pan_tiff_name = fnmatch.filter(pan_tiffs_list, multi_rowcol_wildcard)
        #print(pan_tiff_name[0])
        print('pansharpen')
        os.system('python gdal_pansharpen.py -co NBITS=12 -co COMPRESS=JPEG -co JPEG_QUALITY=50 -co PHOTOMETRIC=YCBCR -co TILED=YES ' + os.path.join(pan_directory,pan_tiff_name[0]) + ' ' + os.path.join(multi_directory,multi_tiff_name) + ',band=7 ' + os.path.join(multi_directory,multi_tiff_name) + ',band=5 ' + os.path.join(multi_directory,multi_tiff_name) + ',band=3 ' + base_directory + '/sharp_' + multi_tiff_name)
        os.system('gdaladdo --config COMPRESS_OVERVIEW JPEG --config PHOTOMETRIC_OVERVIEW YCBCR --config INTERLEAVE_OVERVIEW PIXEL -r average ' + base_directory + '/sharp_' + multi_tiff_name + ' 2 4 8 16')
print('create VRT mosaic from SHARP images')
os.system('gdalbuildvrt sharpmosaic.vrt *.TIF')
print('MBtiles out')
print('gdal_translate sharpmosaic.vrt sharpmosaic.mbtiles -of MBTILES')
print('gdaladdo -r average sharpmosaic.mbtiles 2 4 8 16')
