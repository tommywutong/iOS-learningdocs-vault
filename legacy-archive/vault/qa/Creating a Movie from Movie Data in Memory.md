---
title: Creating a Movie from Movie Data in Memory
apple_id: DTS10003293
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2006-03-21'
source_url: https://developer.apple.com/library/archive/qa/qa1341/_index.html
archived_at: '2026-07-18T02:30:25.405863Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1341

# Creating a Movie from Movie Data in Memory

## Q:  I can create a movie from a movie file using the `NewMovieFromFile` API, but how do I create a movie from movie data which resides in memory?

A: You can use QuickTime data references to accomplish this.

Simply wrap a handle data reference or pointer data reference around the data, then use the `NewMovieFromDataRef` API to create the movie. Play or otherwise use the movie normally, then dispose of the movie, data reference and data when done.

Calling `NewMovieFromDataRef` for any non-QuickTime movie data in a handle or pointer data reference  __without__  specifying any of the data reference extensions (filename, file type, MIME type, and so on) will fail with the -2048 `noMovieFound` error. You must set at least one of the data reference extensions.

Alternately, you can use the [MovieImportDataRef](https://developer.apple.com/documentation/QuickTime/APIREF/movieimportdataref.htm) function and directly specify the movie importer component you would like to use to perform the import (rather than let QuickTime decide based on the data reference extensions). See [Q&A QTMTB52 - Playing memory resident WAVE data using QuickTime](https://developer.apple.com/qa/qtmtb/qtmtb52.html) for an example code listing.

The code snippet in Listing 1 shows how to create a pointer data reference for data (MP3 data in this case) contained in a `NSData` data buffer. A data reference extension for file name is also added to the data reference to enable QuickTime to more easily determine which movie importer component to use. The `createPointerDataRefWithExtensions` routine is taken from [Technical Note TN1195, 'Tagging Handle and Pointer Data References in QuickTime'](https://developer.apple.com/technotes/tn/tn1195.html).

This pointer data reference is then passed to `NewMovieFromDataRef` to create the movie:

__Listing 1__  Creating a movie from an NSData data buffer using a pointer data reference.

```
//
// LoadAndPlayMovieFromNSData
//
// Given an NSData data buffer, make a pointer data
// reference then create a movie for the data.
// Optionally add a file name data reference
// extension to the data reference before creating
// the movie.
//
// Parameters
//
//   data             A data buffer containing the
//                    data you wish to import
//   fileName         If you know the original file name
//                    you should pass it here to help
//                    QuickTime locate a movie importer
//                    for the data.

void LoadAndPlayMovieFromNSData(NSData *data, NSString *fileName)
{
    Str255 fileName255;
    Handle ptrDataRef = NULL;
    Movie newMovie = NULL;

    c2pstrcpy(fileName255, [fileName UTF8String]);
    ptrDataRef = createPointerDataRefWithExtensions(
                         [data bytes],          /* pointer to data */
                         (Size)[data length],   /* data size */
                         fileName255,           /* file name */
                         0,                     /* file type */
                         nil                    /* mime type string */
                         );
    if (ptrDataRef)
    {
        short id = 0;
        OSErr err = noErr;

           /* now create a movie from the data reference */
        err = NewMovieFromDataRef(&newMovie,
                                  newMovieActive,
                                  &id,
                                  ptrDataRef,
                                  PointerDataHandlerSubType);
        if (err == noErr)
        {
            // ...play/manipulate your movie here

            // when finished, clean up
            DisposeMovie(newMovie);
        }

        DisposeHandle(ptrDataRef);

    }
}
```

Similarly, the code snippet in Listing 2 shows how to create a pointer data reference from a pointer to a block of MP3 data along with data reference extensions for file name. Once again, the pointer data reference is passed to `NewMovieFromDataRef` to create the movie:

__Listing 2__  Creating a movie using a pointer data reference.

```
//
// createMovieFromMemory
//
// Given a pointer to some movie data, it creates a
// pointer data reference and then calls NewMovieFromDataRef
// with this data reference to create a movie.
//
// Parameters
//
//   data             A Pointer to your movie data
//   dataSize         The actual size of the movie data
//                    specified by the data pointer
//   fileName         If you know the original file name
//                    you should pass it here to help
//                    QuickTime determine which importer
//                    to use. Pass nil if you do not wish
//                    to specify the fileName


void createMovieFromMemory(void     *data,
                            Size    dataSize,
                            Str255  fileName)
{
    Handle myDataRef = NULL;

    myDataRef = createPointerDataRefWithExtensions(
                    data,       /* pointer to data */
                    dataSize,   /* size of data */
                    fileName,   /* file name */
                    0,          /* file type */
                    nil); /* mime type */

    if (myDataRef)
    {
        OSErr err       = noErr;
        short id        = 0;
        Movie newMovie  = NULL;

        err = NewMovieFromDataRef(
                              &newMovie,
                              newMovieActive,
                              &id,
                              myDataRef,
                              PointerDataHandlerSubType);
        if (err == noErr)
        {
            // ... play/manipulate your movie here

            // clean up when finished using movie

            DisposeMovie(newMovie);
        }

        // more clean up
        DisposeHandle(myDataRef);
    }
}
```

Lastly, the code snippet in Listing 3 shows how to create a handle data reference for MP3 data in a handle along with the same data reference extensions as shown in Listing 2. Again, the `createHandleDataRefWithExtensions` routine is taken from [Technical Note TN1195, 'Tagging Handle and Pointer Data References in QuickTime'](https://developer.apple.com/technotes/tn/tn1195.html).

__Listing 3__  Creating a movie using a handle data reference.

```
//
// createMovieFromHandleMemory
//
// Given a pointer to some movie data, it creates a
// pointer data reference and then calls NewMovieFromDataRef
// with this data reference to create a movie.
//
// Parameters
//
//   data             A Pointer to your movie data
//   dataSize         The actual size of the movie data
//                    specified by the data pointer
//   fileName         If you know the original file name
//                    you should pass it here to help
//                    QuickTime determine which importer
//                    to use. Pass nil if you do not wish
//                    to specify the fileName


void createMovieFromHandleMemory(Handle     dataHandle,
                                 Str255     fileName)
{
    Handle myDataRef = NULL;

    myDataRef = createHandleDataRefWithExtensions(
                        dataHandle,     /* data handle */
                        fileName,       /* file name */
                        0,              /* file type */
                        nil,            /* mime type */
                        nil,            /* initialization data */
                        0); /* init data byte count */

    if (myDataRef)
    {
        OSErr err       = noErr;
        short id        = 0;
        Movie newMovie  = NULL;

        err = NewMovieFromDataRef(
                              &newMovie,
                              newMovieActive,
                              &id,
                              myDataRef,
                              HandleDataHandlerSubType);
        if (err == noErr)
        {
            // ... play/manipulate your movie here

            // clean up when finished using movie

            DisposeMovie(newMovie);
        }

        // more clean up
        DisposeHandle(myDataRef);
    }
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-03-21 | Explain why movie import might fail with the -2048 noMovieFound error. |
| 2004-05-20 | New document that describes how to create a movie from movie data in memory. |

