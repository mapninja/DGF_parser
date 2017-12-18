# A Little Python Script to Process DigitalGlobe Foundation Grant Imagery

I wrote this little script to make processing DIgitalGlobe Foundation grant imagery folders into useable imagery for basic desktop analysis and mosaic all of the tiles into a VRTDataset. I'm going to add an export to MBTiles format, eventually.

## Usage:
Install GDAL

Put the DGF_Parser.py and gdal_pansharpen.py scripts in the top level of your unzipped DGF imagery grant download and run:

```$ python DGF_parser.py```

## Customization

I've got the script set to create JPG compressed (Quality=50%) VRT of TIFF files in the YCBCR color space, with internal tiling and overviews, per this blog post by Paul Ramsey: http://blog.cleverelephant.ca/2015/02/geotiff-compression-for-dummies.html

Feel free to tweak it however. Some things you can do are:
* Change the output bands from 7,5,3
* Change the JPEG_QUALITY
