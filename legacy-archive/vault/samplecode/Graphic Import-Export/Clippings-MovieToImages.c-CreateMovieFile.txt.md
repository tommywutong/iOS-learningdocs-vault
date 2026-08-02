---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_MovieToImages_c_CreateMovieFile_txt.html
archived_at: '2026-07-18T03:10:58.553149Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-MovieToImages.c-MovieExportDoUserDialog.txt.md)[Previous](Clippings-MovieToImages.c-ConvertMovieToFile.txt.md)

# Clippings/MovieToImages.c/CreateMovieFile.txt

```
    err = CreateMovieFile( &theFSSpec,                      // file specifier
                           FOUR_CHAR_CODE('TVOD'),          // creator ('TVOD')
                           smSystemScript,                  // script
                           createMovieFileDeleteCurFile     // flags
                         | createMovieFileDontOpenFile
                         | createMovieFileDontCreateResFile
                         | createMovieFileDontCreateMovie,
                           0,                               // resRefNum; 0 to not open file 
                           0 );                             // newMovie; 0 not to create movie
```

[Next](Clippings-MovieToImages.c-MovieExportDoUserDialog.txt.md)[Previous](Clippings-MovieToImages.c-ConvertMovieToFile.txt.md)

