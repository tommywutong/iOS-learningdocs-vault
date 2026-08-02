---
title: What is SetMovieDefaultDataRef?
apple_id: DTS10002018
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1997-03-14'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb48.html
archived_at: '2026-07-18T02:38:49.191242Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMTB48What is SetMovieDefaultDataRef? |

|  |
| --- |
| Q I can't find documentation for the `SetMovieDefaultDataRef` function. What does it do, and how do I use it?  A `SetMovieDefaultDataRef` is defined in Movies.h as:  `pascal OSErr SetMovieDefaultDataRef(Movie theMovie, Handle dataRef, OSType dataRefType);` It allows you to control where data will be written to when added to a movie. For example, if a movie was loaded from a file, the default data reference is initialized to be the file from which the movie was loaded. This example will set the default data reference to be a handle in memory:   ```      OSErr ConvertGeneralMIDIToSoundTrack (void)      {           OSErr                              err = noErr;           StandardFileReply                  reply;           short                              refNum;           long                               logicalEOF;           Handle                             dataHandle = nil, tempHandle = nil;           Movie                              theMovie = nil, tempMovie = nil;            // Specify the General MIDI file to import           StandardGetFilePreview (nil, 0, nil, &reply);           if (reply.sfGood)           {                // Open the data fork and suck everything into a handle                err = FSpOpenDF (&reply.sfFile, fsRdPerm, &refNum);                err = GetEOF (refNum, &logicalEOF);                dataHandle = NewHandleClear (logicalEOF);                HLock (dataHandle);                err = FSRead (refNum, &logicalEOF, *dataHandle);                HUnlock (dataHandle);                FSClose (refNum);                 // Create a new movie in memory, set its default data reference                // to be a handle                tempMovie = NewMovie (newMovieActive);                tempHandle = NewHandleClear (4);                SetMovieDefaultDataRef (tempMovie, tempHandle,                     HandleDataHandlerSubType);                DisposeHandle (tempHandle);                 // Paste the handled data into our movie                err = PasteHandleIntoMovie (dataHandle, 'Midi', tempMovie, 0, nil);                 // Save the movie out to a flattened file                StandardPutFile ("\pSave MIDI to:", "\pMIDI movie", &reply);                if (reply.sfGood)                {                     theMovie = FlattenMovieData (tempMovie,                          flattenAddMovieToDataFork, &reply.sfFile, 'TVOD',                          smCurrentScript, createMovieFileDeleteCurFile);                }           }           return err;      } ```   This method works fine as long as you have enough memory, and don't want to save the movie to disk. To put data into a file, call this function in order to pass in an alias to the file as the data reference and `rAliasType` as the data reference type:  `SetMovieDefaultDataRef (tempMovie, fileAlias, rAliasType);` [Mar 14 1997] |

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
