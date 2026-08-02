---
title: CreateMovie
apple_id: DTS10001035
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CreateMovie/Listings/Start_Code_QTFlatten_c.html
archived_at: '2026-07-18T03:05:13.104734Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CreateMovie](CreateMovie.md)


[Next](Start%20Code-QTSound.c.md)[Previous](Start%20Code-CreateMovie.c.md)

Relevant replacement documents include:

- [http://developer.apple.com/mac/library/samplecode/QTKitCreateMovie/index.html](https://developer.apple.com/mac/library/samplecode/QTKitCreateMovie/index.html)

# Start Code/QTFlatten.c

```c
#include <Movies.h>

#include "QTUtilities.h"
#include "QTFlatten.h"
#include "CreateMovie.h"
#include "ComFramework.h"

/************************************************************
*                                                           *
*                                                           *
*  QTSave_FlattenMovie                                      *                   
*  Save and flatten a movie resource into a file.           *
*                                                           *
*                                                           *
*************************************************************/

OSErr QTSave_FlattenMovie (Movie theMovie, FSSpec *myFile)
{
    Movie   aMovie = NULL;
    OSErr   myErr = noErr;

    // The FlattenMovieData function creates a new movie file and creates a new movie
    // that contains all of its movie data.
    // NOTE: Unlike the FlattenMovie, this function does not add the new movie resource
    // to the new movie file. Instead, the FlattenMovieData function returns the new
    // movie to your application. Your application must dispose of the returned movie.

// Step 1.
// Insert FlattenMovieData.clp here...

        myErr = GetMoviesError();
        CheckError( myErr, "FlattenMovie error" );

        // Dispose the returned movie because we don't need it. Our sample uses NewMovieFromFile
        // to open the newly flattened movie.
        if (aMovie == NULL)
            CheckError( invalidMovie, "FlattenMovie error" );
        else
            DisposeMovie(aMovie);

    return myErr;
}
```

[Next](Start%20Code-QTSound.c.md)[Previous](Start%20Code-CreateMovie.c.md)

