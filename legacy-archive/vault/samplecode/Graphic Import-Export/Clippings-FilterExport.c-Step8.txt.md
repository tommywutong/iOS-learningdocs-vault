---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_FilterExport_c_Step8_txt.html
archived_at: '2026-07-18T03:10:58.086722Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-GettingMoreInfo.c-DoesDrawAllPixels.txt.md)[Previous](Clippings-FilterExport.c-Step1.txt.md)

# Clippings/FilterExport.c/Step8.txt

```swift
    // make an image description for the effect sample and set its size
    err = MakeImageDescriptionForEffect( effectType,        // four-character code identifying the type of effect to make an image description for
                                         &effectDesc );     // returned handle of correctly filled-out image description for the selected effect type
    (*effectDesc)->width = naturalBounds.right;
    (*effectDesc)->height = naturalBounds.bottom;

    // build a decompression sequence for the effect
    SetIdentityMatrix( &matrix );
    err = DecompressSequenceBeginS( &imageSequence,             // sequence id
                                    effectDesc,                 // description
                                    *videoFilter,               // data
                                    GetHandleSize(videoFilter), // size of the data buffer
                                    destGWorld,                 // graphics port for the destination image
                                    NULL,                       // graphics device handle
                                    NULL,                       // rect 
                                    &matrix,                    // matrix to use                    
                                    ditherCopy,                 // graphics mode
                                    NULL,                       // mask
                                    0,                          // flags
                                    codecNormalQuality,         // accuracy setting
                                    NULL );                     // codec

    // the offscreen gworld is a data source for the video effect
    err = MakeImageDescriptionForPixMap( GetGWorldPixMap(sourceGWorld), &offscreenDesc );

    // create a new data source for the sequence
    err = CDSequenceNewDataSource( imageSequence,           // sequence identifier returned by the DecompressSequenceBeginS()
                                   &effectDataSource,       // returned data source identifier
                                   'srca',                  // four-character code describing how the input will be used
                                   1,                       // source input number
                                   (Handle)offscreenDesc,   // input data description (ImageDescriptionHandle)
                                   NULL,                    // transfer procedure
                                   0 );                     // refCon

    // sets data in a new frame to a specific data source
    err = CDSequenceSetSourceData( effectDataSource,        // data source identifier 
                                   GetPixBaseAddr(GetGWorldPixMap(sourceGWorld)),   // pointer to data
                                   (**offscreenDesc).dataSize );                    // data size

    // render the effect to the second offscreen
    err = DecompressSequenceFrameS( imageSequence,              // sequence identifier
                                    *videoFilter,               // source data  
                                    GetHandleSize(videoFilter), // data size
                                    0,                          // in flags
                                    NULL,                       // out flags
                                    NULL );                     // async completion function; NULL for synchronous
```

[Next](Clippings-GettingMoreInfo.c-DoesDrawAllPixels.txt.md)[Previous](Clippings-FilterExport.c-Step1.txt.md)

