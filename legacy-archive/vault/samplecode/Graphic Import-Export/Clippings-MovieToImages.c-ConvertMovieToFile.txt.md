---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_MovieToImages_c_ConvertMovieToFile_txt.html
archived_at: '2026-07-18T03:10:58.479839Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-MovieToImages.c-CreateMovieFile.txt.md)[Previous](Clippings-ImagesFromURL.c-ImporterForDataRef.txt.md)

# Clippings/MovieToImages.c/ConvertMovieToFile.txt

```
    err = ConvertMovieToFile( movie,            // movie specifier
                              NULL,             // specific track for export; NULL for all tracks
                              &theFSSpec,       // output file
                              0,                // file type                
                              0,                // file creator
                              smSystemScript,   // script 
                              NULL,             // resource id
                              0,                // flags
                              movieExporter );  // movie export component to use for the operation -- pass in a component instance
                                                // this allows setting any conversion parameters with the export component directly
```

[Next](Clippings-MovieToImages.c-CreateMovieFile.txt.md)[Previous](Clippings-ImagesFromURL.c-ImporterForDataRef.txt.md)

