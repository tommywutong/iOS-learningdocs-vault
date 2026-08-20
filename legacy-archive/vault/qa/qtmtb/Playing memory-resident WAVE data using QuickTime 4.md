---
title: Playing memory-resident WAVE data using QuickTime 4
apple_id: DTS10002022
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1999-07-21'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb52.html
archived_at: '2026-07-18T02:38:49.346979Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Audio](https://developer.apple.com/referencelibrary/QuickTime/idxMusicAudio-date.html)

|  |
| --- |
| Technical Q&A QTMTB52Playing memory-resident WAVE data using QuickTime 4 |

|  |  |  |
| --- | --- | --- |
| ---   Q: How do I play memory-resident WAVE data using QuickTime 4?  A: QuickTime 4 has a built-in WAV file importer. You can open and play a WAV file quite easily by opening the file as if it were a QuickTime movie file and playing the "movie" (WAV file). For example, here's some QuickTime code which you can use to play any WAV file (simply select your WAV file at the file prompt and QuickTime will play it as a sound-only movie):   |  | | --- | | ``` OSErr PlayWAVfile () {     SFTypeList        myTypeList;     StandardFileReply myReply;     OSErr             err = noErr;     short             movieRefNum, resID = 0;     Movie             movie;          StandardGetFilePreview(NULL, -1, myTypeList, &myReply);         if (!myReply.sfGood)         {             err = userCanceledErr;             return err;         }         else         {             err = OpenMovieFile(&myReply.sfFile, &movieRefNum, fsRdPerm);             if (!err)             {                 err = NewMovieFromFile(&movie,                                        movieRefNum,                                        &resID,                                        NULL,                                        newMovieActive,                                        NULL);             }              if (err)             {                 if (movie)                 {                     DisposeMovie(movie);                 }             }             else             {                 SetMovieVolume(movie, kFullVolume);                 GoToBeginningOfMovie(movie);                 StartMovie(movie);                 while (!IsMovieDone(movie))                 {                     MoviesTask(movie, 0);                     err = GetMoviesError();                 }             }         }          return err; } ``` |    It's a bit more work to play a WAV sound using QuickTime if your WAV data is in memory instead of in a file. In this case, one option is to create a new movie and add the WAV data as a separate sound track (since the QuickTime WAV importer only works with files). [Inside Macintosh: QuickTime chapter 2](https://developer.apple.com/documentation/quicktime/qtdevdocs/RM/frameset.htm) contains sample code which shows how to create a movie from scratch and add a sound track to the movie. Simply add the WAV data to the sound track of your movie as you would normally then play the movie.  You can also use the QuickTime WAV movie import component along with the `MovieImportDataRef` function to add memory-resident WAV file data to a movie. The `MovieImportDataRef` function lets you specify the data reference to use for the import operation (in this case, a handle data reference for the WAV file data). Note that this does not mean you actually pass the handle to your data in the `dataRef` parameter; instead, the `dataRef` is a handle that starts with the handle to your data (see code below):   |  | | --- | | ``` void ImportWAVDataFromMemory(Ptr waveDataPtr, long waveDataSize) {     Handle                  myHandle, dataRef = nil;     Movie                   movie;     MovieImportComponent    miComponent;     Track                   targetTrack = nil;     TimeValue               addedDuration = 0;     long                    outFlags = 0;     OSErr                   err;     ComponentResult         result;          myHandle = NewHandleClear((Size)waveDataSize);         BlockMove(waveDataPtr,                     *myHandle,                     waveDataSize);          err = PtrToHand(&myHandle,                         &dataRef,                         sizeof(Handle));          miComponent = OpenDefaultComponent(MovieImportType,                                             kQTFileTypeWave);         movie = NewMovie(0);          result = MovieImportDataRef(miComponent,                                     dataRef,                                     HandleDataHandlerSubType,                                     movie,                                     nil,                                     &targetTrack,                                     nil,                                     &addedDuration,                                     movieImportCreateTrack,                                     &outFlags);          SetMovieVolume(movie, kFullVolume);         GoToBeginningOfMovie(movie);         StartMovie(movie);         while (!IsMovieDone(movie))         {             MoviesTask(movie, 0);             err = GetMoviesError();         } } ``` |    [Jul 21 1999] |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
