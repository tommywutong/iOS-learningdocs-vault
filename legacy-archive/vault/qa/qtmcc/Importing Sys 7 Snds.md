---
title: Importing Sys 7 Snds
apple_id: DTS10001959
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-11'
source_url: https://developer.apple.com/library/archive/qa/qtmcc/qtmcc16.html
archived_at: '2026-07-18T02:38:47.299281Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Import & Export](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxImportExport-date.html) >

|  |
| --- |
| Technical Q&A QTMCC16Importing Sys 7 Snds |

|  |  |
| --- | --- |
| ---   Q: I'm using standard Movie Toolbox APIs such as `OpenMovieFile`, `NewMovieFromFile`, and `StartMovie` to support simple media playback within my application. Although this is very easy and versatile, I can't get Macintosh standard system sound files to work. Can I make QuickTime play these sound files for me or do I have to use the Sound Manager directly?  A: "System 7 sound files" are files with the file type `'sfil'` and contain a `'snd '` sound resource. QuickTime can import these files, but it can't import them in-place. You need a new place to put the extracted sound samples.  One way to accomplish this task is to create a handle data reference and import the samples into that handle. Here's an example showing how you might do it:   |  | | --- | | ``` // This routine will return an imported 'snd ' as a QuickTime Movie // Error checking has been removed for the sake of convenience // Parameters: inFile - file to import //             inSoundDataH - an already allocated zero sized handle // Returns:    New Imported Sound Movie or 0 Movie System7SoundToMovie(const FSSpec *inFile, Handle inSoundDataH) {   Movie theMovie = 0;   FInfo fndrInfo;    OSErr err = noErr;    FSpGetFInfo(inFile, &fndrInfo);   if (kQTFileTypeSystemSevenSound == fndrInfo.fdType) {      // QuickTime can't import these files in place, but that's ok,     // we just need a new place to put this stuff      Handle hDataRef = NULL;     MovieImportComponent theImporter = 0;     long ignore;      // Create a movie.     theMovie = NewMovie(newMovieActive);      // Build the data ref. -- create a Handle-sized Handle to hold the real Handle.     PtrToHand(&inSoundDataH, &hDataRef, sizeof(Handle));      // Set where the data will be written when added to a movie     // This reference points to the passed in handle which will be resized     // appropriately by the call to MovieImportFile     SetMovieDefaultDataRef(theMovie, hDataRef, HandleDataHandlerSubType);      // Do the import     OpenADefaultComponent(MovieImportType,           kQTFileTypeSystemSevenSound, &theImporter);     MovieImportFile(theImporter, inFile, theMovie,           NULL, NULL, 0, NULL, 0, &ignore);     CloseComponent(theImporter);      // Don't need the dataRef anymore but don't dispose     // of the sound data handle until     // after the the movie has been disposed or very bad     // things will happen!     DisposeHandle(hDataRef);   }    return theMovie; } ``` |    You can still play these files by calling `GetResource` and `PlaySnd` if you wish.   ---  [Sep 22 2000] |

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
