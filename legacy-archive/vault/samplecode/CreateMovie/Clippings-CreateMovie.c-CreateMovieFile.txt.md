---
title: CreateMovie
apple_id: DTS10001035
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CreateMovie/Listings/Clippings_CreateMovie_c_CreateMovieFile_txt.html
archived_at: '2026-07-18T03:05:07.920570Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CreateMovie](CreateMovie.md)


[Next](Clippings-QTFlatten.c-FlattenMovieData.txt.md)[Previous](Clippings-CreateMovie.c-AddMovieResource.txt.md)

Relevant replacement documents include:

- [http://developer.apple.com/mac/library/samplecode/QTKitCreateMovie/index.html](https://developer.apple.com/mac/library/samplecode/QTKitCreateMovie/index.html)

# Clippings/CreateMovie.c/CreateMovieFile.txt

```
        err = CreateMovieFile(&mySpec,                          /* FSSpec specifier */
                              kMyCreatorType,                   /* file creator type */
                              smCurrentScript,                  /* movie file creation flags */ 
                              createMovieFileDeleteCurFile |
                              createMovieFileDontCreateResFile |
                              newMovieActive,
                              &resRefNum,                       /* file ref num */
                              &theMovie );                      /* field to recieve movie specification */
```

[Next](Clippings-QTFlatten.c-FlattenMovieData.txt.md)[Previous](Clippings-CreateMovie.c-AddMovieResource.txt.md)

