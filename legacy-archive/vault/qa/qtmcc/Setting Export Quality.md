---
title: Setting Export Quality
apple_id: DTS10001956
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1999-12-06'
source_url: https://developer.apple.com/library/archive/qa/qtmcc/qtmcc13.html
archived_at: '2026-07-18T02:38:47.113930Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Import & Export](https://developer.apple.com/referencelibrary/QuickTime/idxImportExport-date.html)

|  |
| --- |
| Technical Q&A QTMCC13Setting Export Quality |

|  |  |
| --- | --- |
| ---   Q: We currently have a file which we would like to export in a different format. We're using `GetGraphicsImporterForFile()` and `GraphicsImportExportImageFile()` to do this. However, we didn't see how to change the compression factor if we're saving as a JPEG file. Is this possible?  A: This is possible with just a little more work than using `GraphicsImportExportImageFile()`. The idea is to use the Graphics Exporter Component APIs with a specific call to `GraphicsExportSetCompressionQuality()` or `GraphicsExportSetTargetDataSize()` to set the compression quality for the export.  Here's an overview of the steps to follow:   1. Select your Export Component. In the code below, we get the JPEG Export Component. 2. Specify the source for the export. This can be a Graphics Importer instance, a QuickDraw Picture, GWorld, PixMap, or a segment of compressed data described by an image description record. 3. Tell the Export Component where the input is coming from. The code below uses a Graphics Importer Instance. 4. Tell the Export Component the destination of the exported data. The code below uses a file. 5. Specify your settings. A variety of `Get` and `Set` functions are available to manipulate various graphics exporter settings. There are two examples in the code below. a. Explicitly tell the exporter we want low quality.     b. Ask the exporter to fit the file to a given size constraint and ramp the quality accordingly. 6. Do the export. The code below will write out the data and create a JPEG file.   Graphics Exporter Components Documentation can be found in the [QuickTime 4 API Documentation.](https://developer.apple.com/documentation/quicktime/qtdevdocs/RM/rmExporter.htm)   |  | | --- | | ``` Example:  OSErr DoEasyExportToJpeg() {     SFTypeList      myTypeList = {kQTFileTypeMovie, 0, 0, 0};     StandardFileReply     myReply;     GraphicsImportComponent theImportComponent = NULL;     GraphicsExportComponent theExportComponent = NULL;     OSErr       rc = noErr;      StandardGetFilePreview( NULL, 1, myTypeList, &myReply );     if (!myReply.sfGood) goto bail;      // 1. Open the JPEG Exporter Component.     // We'll connect an Import Component to this Export Component     // and very easily export a JPEG file.     rc = OpenADefaultComponent( GraphicsExporterComponentType, kQTFileTypeJPEG,           &theExportComponent );     if (rc) goto bail;      // 2. Find the Graphics Import Component for our file.     rc = GetGraphicsImporterForFile( &myReply.sfFile, &theImportComponent );     if (rc) goto bail;      // 3. Connect the Importer to the Exporter.     rc = GraphicsExportSetInputGraphicsImporter( theExportComponent,          theImportComponent );     if (rc) goto bail;      StandardPutFile( "\pExport File As...",          "\pMyJpeg.jpg", &myReply );     if (!myReply.sfGood) goto bail;      // 4. We're going to export this to a file.     rc = GraphicsExportSetOutputFile( theExportComponent,          &myReply.sfFile );     if (rc) goto bail;      // 5a. Set the image compression quality.     rc = GraphicsExportSetCompressionQuality( theExportComponent,          codecLowQuality );     if (rc) goto bail;      // 5b. Alternatively you could use GraphicsExportSetTargetDataSize().     // This API let's you specify the desired data size in bytes; the     // JPEG exporter will     // decrease the quality until it reaches the specified size or     // bottoms out on the     // quality setting.     //rc = GraphicsExportSetTargetDataSize( theExportComponent,          25000 ); // Max size 25k     //if (rc) goto bail;      // 6. Do the export, write the file.     rc = GraphicsExportDoExport( theExportComponent, NULL );  bail:  if ( theImportComponent != NULL )      CloseComponent( theImportComponent );  if ( theExportComponent != NULL )          CloseComponent( theExportComponent );      return rc; } ``` |  [Dec 06 1999] |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
