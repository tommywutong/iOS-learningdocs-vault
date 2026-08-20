---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_MovieToImages_c_MovieImportFile_txt.html
archived_at: '2026-07-18T03:10:58.684455Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-MovieToImages.c-OpenADefaultComponent1.txt.md)[Previous](Clippings-MovieToImages.c-MovieImportDoUserDialog.txt.md)

# Clippings/MovieToImages.c/MovieImportFile.txt

```
    err = MovieImportFile( movieImporter,   // movie importer component instance
                           &theFSSpec,      // data file
                           movie,           // the movie to recieve the data
                           NULL,            // specific target track
                           &usedTrack,      // pointer to track that received the imported data
                           0,               // time to place imported data 
                           &addedDuration,  // the duration of the data added to the movie
                           0,               // in flags
                           &outFlags );     // out flags
```

[Next](Clippings-MovieToImages.c-OpenADefaultComponent1.txt.md)[Previous](Clippings-MovieToImages.c-MovieImportDoUserDialog.txt.md)

