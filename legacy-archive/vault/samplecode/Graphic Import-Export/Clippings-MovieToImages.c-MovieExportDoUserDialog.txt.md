---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_MovieToImages_c_MovieExportDoUserDialog_txt.html
archived_at: '2026-07-18T03:10:58.603545Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-MovieToImages.c-MovieImportDoUserDialog.txt.md)[Previous](Clippings-MovieToImages.c-CreateMovieFile.txt.md)

# Clippings/MovieToImages.c/MovieExportDoUserDialog.txt

```
    err = MovieExportDoUserDialog( movieExporter,               // component instance
                                   movie,                       // movie to be exported                 
                                   NULL,                        // specific track to export
                                   0,                           // start time
                                   GetMovieDuration( movie ),   // duration to be exported
                                   &canceled );                 // boolean set to true if user canceled
```

[Next](Clippings-MovieToImages.c-MovieImportDoUserDialog.txt.md)[Previous](Clippings-MovieToImages.c-CreateMovieFile.txt.md)

