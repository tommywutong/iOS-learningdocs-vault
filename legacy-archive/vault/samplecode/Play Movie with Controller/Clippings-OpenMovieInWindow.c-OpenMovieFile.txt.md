---
title: Play Movie with Controller
apple_id: DTS10001041
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Play_Movie_with_Controller/Listings/Clippings_OpenMovieInWindow_c_OpenMovieFile_txt.html
archived_at: '2026-07-18T03:19:10.506856Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Play Movie with Controller](Play%20Movie%20with%20Controller.md)


[Next](Clippings-OpenMovieInWindow.c-SetMovieGWorld.txt.md)[Previous](Clippings-OpenMovieInWindow.c-NewMovieFromFile.txt.md)

Relevant replacement documents include:

- [http://developer.apple.com/mac/library/samplecode/QTKitPlayer/index.html](https://developer.apple.com/mac/library/samplecode/QTKitPlayer/index.html)

# Clippings/OpenMovieInWindow.c/OpenMovieFile.txt

```

        // ideally, we'd like read and write permission, but we'll settle for read-only permission
        myErr = OpenMovieFile(&myFSSpec, &myRefNum, fsRdWrPerm);
        if (myErr != noErr)
            myErr = OpenMovieFile(&myFSSpec, &myRefNum, fsRdPerm);
```

[Next](Clippings-OpenMovieInWindow.c-SetMovieGWorld.txt.md)[Previous](Clippings-OpenMovieInWindow.c-NewMovieFromFile.txt.md)

