---
title: SampleRaster
apple_id: DTS40009295
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: null
published: '2011-09-06'
source_url: https://developer.apple.com/library/archive/samplecode/SampleRaster/Listings/README_txt.html
archived_at: '2026-07-18T03:23:03.255484Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleRaster](SampleRaster.md)


[Next](commandtosample.c.md)[Previous](SampleRaster.md)

# README.txt

```
The SampleRaster project implements a CUPS printer driver that simulates a
typical CMYK inkjet raster printer.  The driver provides the following
components:

    - CUPS raster filter (rastertosample)
    - CUPS command filter (commandtosample)
    - CUPS backend (sampletopdf)
    - Cocoa-based printer utility application (SampleUtility.app)
    - Cocoa-based print dialog plugin (SampleRasterPDE.bundle)
    - Printer icon
    - ICC color profiles
    - iPhoto/Preview printer presets
    - Custom printer-state-reason keywords
    - On-line help
    - Driver information file (sample.drv) which is compiled into a PPD file
      (sample.ppd).

The CUPS backend is provided for testing purposes only.  Most printer drivers
do not require their own backend - the system-supplied backends handle all
standard interfaces and network protocols for printing - and very few backends
are as complicated as the sampletopdf backend.


INSTALLATION

You must be running Mac OS X 10.6 or higher to compile or install from
source.

The "makepackage.sh" script can be used to create an installable driver
package, or you can just install from source directly with the following
command:

    sudo xcodebuild -target SampleRaster -configuration Debug_10.6 install DSTROOT=/

Once you have installed the software, open the Print & Scan preference pane
and click on the "+" button to add a printer.  Choose the "Sample Raster Driver"
listing from the list and click "Add".


NOTES

Products requiring PPC support must be built on 10.6.x or 10.5.x using XCode 3.
Products with only Intel support can be build with 10.6.6 or later using
Xcode 4.

The ink level monitoring supported by the printer utility and help will only
work with Mac OS X 10.5.3 and higher.  The driver as a whole works with Mac
OS X 10.6 and higher. Builds targeting Mac OS X 10.6 and higher use the Grand
Central Dispatch version of the ink level monitoring code.

The backend writes the virtual printed pages to PDF files in a per-queue
directory in /Library/Caches, typically /Library/Caches/Sample_Raster_Driver
if the default printer name is used when you add the printer.

If you use this sample project as the start point for your product,
before releasing your product, make sure you adjust the VALID_ARCHS value
of each target in the project file and the RC_ARCHS value to be passed to
'xcodebuild' in your build script, based on the versions of OS you support.
```

[Next](commandtosample.c.md)[Previous](SampleRaster.md)

