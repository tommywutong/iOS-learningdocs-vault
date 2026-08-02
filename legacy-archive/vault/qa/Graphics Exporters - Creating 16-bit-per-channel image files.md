---
title: Graphics Exporters - Creating 16-bit-per-channel image files
apple_id: DTS10003332
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2004-06-03'
source_url: https://developer.apple.com/library/archive/qa/qa1354/_index.html
archived_at: '2026-07-18T02:30:25.919634Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1354

# Graphics Exporters - Creating 16-bit-per-channel image files

## Q:  Can QuickTime Graphics Exporters create 16-bit-per-channel images?

A: Yes, the PNG and TIFF Graphics Exporters can create 16-bit-per-channel image files given a 16-bit-per-channel pixmap. Refer to [Technical Q&A QA1114, '48 bit & 64 bit Pixel Format support in QuickTime'](https://developer.apple.com/qa/qa2001/qa1114.html) for a discussion of 16-bit-per-channel pixel format support.

In order to make this work however, the depth value you should set when calling `GraphicsExportSetDepth` looks as though you are asking for an 8-bit-per-channel image file. See Table 1.

While it seems like the obvious values for `GraphicsExportSetDepth` would be `k16GrayCodecType`, `k32AlphaGrayCodecType`, `k48RGBCodecType` and `k64ARGBCodecType` respectively, these choices do not currently (QuickTime 6.5.1) produce the desired output.

__Table 1__

| PixMap and image file depth | PixelFormat for GraphicsExportSetDepth |
| 16-bit greyscale | k8IndexedGrayPixelFormat |
| 32-bit alpha+greyscale | k32ARGBPixelFormat |
| 48-bit rgb | k24RGBPixelFormat |
| 64-bit alpha+rgb | k32ARGBPixelFormat |

__Listing 1__  Exporting 48-bit RGB source.

```c
// Use with the ImproveYourImage sample, see references below.

#include "MacShell.h"

void ExportDeepImageAsTIFF(void)
{
    Handle hOpenTypeList = NewHandle(0);
    long   numTypes = 0;
    FSSpec theFSSpec;
    Boolean isSelected, isReplacing;
    GraphicsImportComponent importer = 0;
    GraphicsExportComponent exporter = 0;
    Rect naturalBounds;
    unsigned long actualSizeWritten;
    ImageDescriptionHandle desc = NULL;
    Handle h = NULL;
    OSType pixelFormat;
    GWorldPtr gworld = NULL;
    OSErr err = noErr;

    BuildGraphicsImporterValidFileTypes(hOpenTypeList, &numTypes);
    HLock( hOpenTypeList );

    err = GetOneFileWithPreview(numTypes, (OSTypePtr)*hOpenTypeList, &theFSSpec, NULL);
    DisposeHandle(hOpenTypeList);
    if (err) return;

    // locate and open a graphics importer component
    err = GetGraphicsImporterForFile(&theFSSpec, &importer);
    if (err) return;

    // find out the real colorspace
    err = GraphicsImportGetImageDescription(importer, &desc);
    if (err) goto bail;

    err = GetImageDescriptionExtension(desc, &h, kImageDescriptionColorSpace, 1);
    DisposeHandle((Handle)desc);
    if (err) goto bail;
    if( !h || !*h ) goto bail;

    pixelFormat = *(OSType*)*h;
    pixelFormat = EndianU32_BtoN(pixelFormat);
    DisposeHandle(h);

    // if the imported image is 48-bit RGB,
    // export it as a 16-bit-per-channel TIFF file
    if (k48RGBCodecType == pixelFormat) {

        // draw the image into an offscreen gworld of that colorspace
        err = GraphicsImportGetNaturalBounds(importer, &naturalBounds);
        if (err) goto bail;

        err = QTNewGWorld(&gworld, pixelFormat, &naturalBounds,
                           NULL, NULL, kICMTempThenAppMemory);
        if (err) goto bail;

        err = GraphicsImportSetGWorld(importer, gworld, NULL);
        if (err) goto bail;

        err = GraphicsImportDraw(importer);
        if (err) goto bail;

        // write the image out as a tiff file
        err = PutFile("\pSave the image as:", "\pTest.tiff", &theFSSpec,
                       &isSelected, &isReplacing);
        if (err) goto bail;

        // find and open the TIFF Graphics Exporter component
        err = OpenADefaultComponent(GraphicsExporterComponentType, kQTFileTypeTIFF,
                                     &exporter);
        if (err) goto bail;

        // set the input source
        err = GraphicsExportSetInputGWorld(exporter, gworld);
        if (err) goto bail;

        // set the export destination
        err = GraphicsExportSetOutputFile(exporter, &theFSSpec);
        if (err) goto bail;

        // set the export depth, see table 1 in QA1345
        err = GraphicsExportSetDepth(exporter, k24RGBPixelFormat);
        if (err) goto bail;

        // export the file
        GraphicsExportDoExport(exporter, &actualSizeWritten);
    }

bail:

    if (importer) CloseComponent(importer);
    if (exporter) CloseComponent(exporter);
    if (gworld) DisposeGWorld(gworld);
}
```


- [Sample Code 'ImproveYourImage'](https://developer.apple.com/samplecode/ImproveYourImage/index.html)
- [QuickTime Import & Export Documentation.](https://developer.apple.com/documentation/QuickTime/ImportExport-date.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-06-03 | New document that discusses how to use QuickTime Graphics Exporters to create 16-bit-per-channel image files. |

