---
title: Decompressing MP3
apple_id: DTS10001958
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2000-09-22'
source_url: https://developer.apple.com/library/archive/qa/qtmcc/qtmcc15.html
archived_at: '2026-07-18T02:38:47.250565Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

|  |
| --- |
| Technical Q&A QTMCC15Decompressing MP3 |

|  |  |
| --- | --- |
|  Q: I am currently attempting to decompress an MP3 file into a buffer using the SoundConverter APIs and am having no luck. `SoundConverterConvertBuffer` seems to work fine when decoding certain files, but fails if the file is MP3 encoded. Does MP3 decompression require calling `SoundConverterSetInfo`? If so, what parameters do I pass in?  A: Yes, a call to `SoundConverterSetInfo` is required, but first you'll have to retrieve the decompression settings atom from the sound file. To do this, open the MP3 as a QuickTime movie using `NewMovieFromFile`. Use the `GetMediaSampleDescription` routine to retrieve a description of the sample data, then use `GetSoundDescriptionExtension` (passing in the sample description, and using the `siDecompressionParams` selector as parameters) to extract the decompression atom list from the sound track. Once you have the decompression atom list, call `SoundConverterSetInfo` using the `siDecompressionParams` selector as we did with the previous call. Without this setup, the decoder won't know how to interpret the sample data.  The sample routine below shows how to extract the decompression parameters.   |  | | --- | | ``` OSErr MyGetSoundDescriptionExtension(const FSSpec *inMP3file,     AudioFormatAtomPtr *outAudioAtom) {   Movie theMovie;   Track theTrack;   Media theMedia;   short theRefNum;   short theResID = 0;  // we want the first movie   Boolean wasChanged;    OSErr err = noErr;    // open the movie file   err = OpenMovieFile(inMP3file, &theRefNum, fsRdPerm);   if (err) goto bail;    // instantiate the movie   err = NewMovieFromFile(&theMovie, theRefNum, &theResID, NULL,       newMovieActive, &wasChanged);   if (err) goto bail;   CloseMovieFile(theRefNum);   theRefNum = 0;    // get the first sound track   theTrack = GetMovieIndTrackType(theMovie, 1, SoundMediaType,       movieTrackMediaType);   if (theTrack != NULL) {      // get the sound track media     theMedia = GetTrackMedia(theTrack);     if (theMedia != NULL) {       Size size;       Handle extension;       SoundDescriptionV1Handle sourceSoundDescription;        sourceSoundDescription = (SoundDescriptionV1Handle)NewHandle(0);        // get the description of the sample data       GetMediaSampleDescription(theMedia, 1,           (SampleDescriptionHandle)sourceSoundDescription);       err = GetMoviesError();        extension = NewHandle(0);        // get the "magic" decompression atom       // This extension to the SoundDescription information stores       // data specific to a given audio decompressor. Some audio       // decompression algorithms require a set of out-of-stream       // values to configure the decompressor.       err = GetSoundDescriptionExtension(           (SoundDescriptionHandle)sourceSoundDescription,           &extension, siDecompressionParams);        if (noErr == err) {         size = GetHandleSize(extension);         HLock(extension);         *outAudioAtom = (AudioFormatAtom*)NewPtr(size);         err = MemError();         // copy the atom data to our buffer...         BlockMoveData(*extension, *outAudioAtom, size);         HUnlock(extension);       } else {         // if it doesn't have an atom, that's ok         *outAudioAtom = NULL;         err = noErr;       }        DisposeHandle(extension);       DisposeHandle((Handle)sourceSoundDescription);     }   }  bail:   return err; } ``` |    A full sample application called MP3Player can be found on the [QuickTime Sample Code page](https://developer.apple.com/samplecode/Sample_Code/Sound/MP3Player.htm).   ---  [Sep 22 2000] |

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
