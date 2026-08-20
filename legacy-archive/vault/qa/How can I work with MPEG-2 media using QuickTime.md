---
title: How can I work with MPEG-2 media using QuickTime?
apple_id: DTS10004422
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-10-19'
source_url: https://developer.apple.com/library/archive/qa/qa1540/_index.html
archived_at: '2026-07-18T02:32:15.604685Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1540

# How can I work with MPEG-2 media using QuickTime?

## Q:  When I try and open MPEG-2 media with QuickTime using the `NewMovieFromDataRef` function I get the -2048 (`noMovieFound`) error.  How can I work with MPEG-2 media using QuickTime?

A: Important

The Core Media Framework in OS X Lion has built-in support for MPEG-2 media. The AV Foundation Framework is built on top of the Core Media Framework, and can be used to play time-based audiovisual media. See the [AV Foundation Programming Guide](https://developer.apple.com/library/mac/documentation/AudioVideo/Conceptual/AVFoundationPG/AVFoundationPG.pdf) for more information.

If your application needs to play MPEG-2 media on Mac OS X 10.6 Snow Leopard or earlier versions of Mac OS X, please read the rest of this technote.

You can purchase and install the [QuickTime MPEG-2 Playback Component](http://www.apple.com/quicktime/mpeg2/).

This component gives users the ability to import and play back MPEG-2 content, including both multiplexed (or "muxed", where the audio and video tracks are interleaved together into one track) and non-multiplexed (elementary) streams. However, while multiplexed streams can be played back, de-multiplexing of these streams is not supported, and neither is editing (copy/paste, and so on).

The MPEG-2 Playback Component is composed of a media handler that understands the MPEG-2 media type and actually plays back the media, and a movie import component that allows QuickTime to create a movie with MPEG-2 media in a single MPEG-2 track (muxed media is not presented as separate video and audio tracks). There is no MPEG-2 decoder component. All the necessary functionality is implemented via the media handler and the importer.

The MPEG-2 Playback Component will allow the transcode of MPEG-2 video to other formats, whether that video originates in an elementary video stream or in a multiplexed stream. However, the ability to transcode MPEG-2 audio is not supported. Transcoding is supported for video only. As an alternative, you could first export your media to an intermediate QuickTime movie, and then export the audio track from this intermediate movie.

You can programatically open MPEG-2 media files using the MPEG-2 Playback Component as you would normally for any of the other QuickTime supported media types. Simply use any of the QTKit methods for creating a QTMovie such as the `-movieWithFile` method. Here's a short code snippet:

__Listing 1__  Opening MPEG-2 media using QTKit.

```
QTMovie *movie = [QTMovie movieWithFile:@"/Volumes/MacintoshHD/MyFile.m2v" error:nil];
if (movie)
{
    /* do stuff with movie here... */
}
```

Similarly, you can use any of the QuickTime Movie Toolbox APIs for opening QuickTime supported media such as `NewMovieFromDataRef` and others (`NewMovieFromProperties`, and so on).

Here's a code snippet:

__Listing 2__  Opening MPEG-2 media using the `NewMovieFromDataRef` Movie Toolbox API.

```
Movie    myMovie = NULL;
OSType   myDataRefType;
Handle   myDataRef = NULL;
short    myResID = 0;
OSErr    myErr = noErr;

// create the data reference
myErr = QTNewDataReferenceFromFullPathCFString(CFSTR("/Volumes/MacintoshHD/MyFile.mpg"),
                        kQTNativeDefaultPathStyle,0, &myDataRef, &myDataRefType);
if (myErr != noErr) goto bail;

// get the Movie
myErr = NewMovieFromDataRef(&myMovie, newMovieActive,
                            &myResID, myDataRef, myDataRefType);
if (myErr != noErr) goto bail;

/*
    do stuff with movie here...
*/

bail:

// dispose the data reference handle - we no longer need it
if (myDataRef)
{
    DisposeHandle(myDataRef);
}

// remember to call DisposeMovie when done with the returned Movie
if (myMovie)
{
    DisposeMovie(myMovie);
}
```

You can also use the MPEG-2 import component directly to open MPEG-2 media using those APIs that allow you to pass an importer component as a parameter, such as the `MovieImportDataRef` API. The MPEG-2 import component is registered for the file type .mpg (you can see this using the [Sample Code 'Fiendishthngs'](https://developer.apple.com/samplecode/Fiendishthngs/index.html) which iterates over all the components installed on the system).

When the MPEG-2 playback media handler is installed, a number of other importer components are registered as aliases, and they all call through to the designated MPEG-2 importer (.mpg) already on the system. These other component aliases are for files with extensions .m2s, .vob and so on. Therefore, you should always use the above mentioned MPEG-2 importer even if your MPEG-2 media does not contain the .mpg extension.

You can use the `FindNextComponent` function to locate the MPEG-2 importer. Once you've located the importer, you can then use APIs that accept an importer component as a parameter, such as `MovieImportDataRef`, to open your MPEG media. Here's a code snippet:

__Listing 3__  Calling the MPEG-2 importer component directly to open MPEG-2 media files.

```
void doMovieImport(CFStringRef inPathToMPEG2file)
{
    Handle outDataRef;
    OSType outDataRefType;
    // create a data reference for our media file
    OSErr err = QTNewDataReferenceFromFullPathCFString(inPathToMPEG2file,
                                                 kQTNativeDefaultPathStyle,
                                                 0,
                                                 &outDataRef,
                                                 &outDataRefType);
    if (err == noErr)
    {
        ComponentDescription cd;
        Component miComponent = 0;

        cd.componentType = MovieImportType;
        cd.componentSubType = 'MPG ';
        cd.componentManufacturer = 0; // Any manufacturer is OK
        cd.componentFlags = canMovieImportFiles | movieImportSubTypeIsFileExtension;
        cd.componentFlagsMask = canMovieImportFiles | movieImportSubTypeIsFileExtension;

        // locate the MPEG-2 importer component
        miComponent = FindNextComponent( miComponent, &cd );

        if (miComponent)
        {
            ComponentInstance miComponentInstance = OpenComponent (miComponent);
            if (miComponentInstance)
            {
                // create a new movie
                Movie movie = NewMovie(0);
                assert(movie != NULL);

                Track        targetTrack = nil;
                TimeValue    addedDuration = 0;
                long         outFlags = 0;

                // perform the import of the media
                ComponentResult result = MovieImportDataRef(miComponentInstance,
                                                            outDataRef,
                                                            outDataRefType,
                                                            movie,
                                                            nil,
                                                            &targetTrack,
                                                            0,
                                                            &addedDuration,
                                                            movieImportCreateTrack,
                                                            &outFlags);
                if (result == noErr)
                {
                    /* ... do stuff with movie here.... */

                }

                // cleanup when done
                DisposeMovie(movie);
            }
        }
    }
}
```

Lastly, if you would like to get the static frame rate of your MPEG media, see [Technical Q&A QA1262, 'Calculating the static video frame rate of a QuickTime movie.'](https://developer.apple.com/qa/qa2001/qa1262.html)

- [Apple MPEG-2 Playback Component](http://www.apple.com/quicktime/mpeg2/)
- [Apple MPEG-2 Playback Component FAQ](http://www.apple.com/quicktime/mpeg2/faq.html)
- [Technical Q&A QA1262, 'Calculating the static video frame rate of a QuickTime movie.'](https://developer.apple.com/qa/qa2001/qa1262.html)
- [Sample Code 'Fiendishthngs'](https://developer.apple.com/samplecode/Fiendishthngs/index.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-10-19 | Added information about Core Media support for MPEG-2 media on OS X Lion. |
| 2009-08-27 | Bug fix in code (Listing 3) to correctly open the MPEG-2 importer component. |
| 2007-08-29 | New document that how to work with MPEG-2 media using QuickTime. |

