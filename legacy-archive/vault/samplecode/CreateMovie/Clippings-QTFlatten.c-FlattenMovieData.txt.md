---
title: CreateMovie
apple_id: DTS10001035
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CreateMovie/Listings/Clippings_QTFlatten_c_FlattenMovieData_txt.html
archived_at: '2026-07-18T03:05:08.000066Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CreateMovie](CreateMovie.md)


[Next](Clippings-QTSound.c-AddMediaSample.txt.md)[Previous](Clippings-CreateMovie.c-CreateMovieFile.txt.md)

Relevant replacement documents include:

- [http://developer.apple.com/mac/library/samplecode/QTKitCreateMovie/index.html](https://developer.apple.com/mac/library/samplecode/QTKitCreateMovie/index.html)

# Clippings/QTFlatten.c/FlattenMovieData.txt

```
        aMovie = FlattenMovieData(theMovie,                         /* movie specifier */
                                  flattenAddMovieToDataFork |       /* moive flatten flags */   
                                  flattenForceMovieResourceBeforeMovieData,
                                  myFile,                           /* FSSpec for creted movie */
                                  FOUR_CHAR_CODE('TVOD'),           /* creator */
                                  smSystemScript,                   /* script tag */
                                  createMovieFileDeleteCurFile |    /* creation flags */
                                  createMovieFileDontCreateResFile);
```

[Next](Clippings-QTSound.c-AddMediaSample.txt.md)[Previous](Clippings-CreateMovie.c-CreateMovieFile.txt.md)

