---
title: Keyframes and AddMediaSample
apple_id: DTS10001963
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-11'
source_url: https://developer.apple.com/library/archive/qa/qtmcc/qtmcc20.html
archived_at: '2026-07-18T02:38:47.482915Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Movie Creation](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxMovieCreation-date.html) >

|  |
| --- |
| Technical Q&A QTMCC20Keyframes and AddMediaSample |

|  |  |
| --- | --- |
| ---   Q: I'm generating QuickTime movie files from my own data and encountering problems when the movie controller is used to scrub my movie files. These movies seem to play fine unless they are started in the middle or if the movie controller is being moved back and forth. In this case, the picture falls apart until a key frame is processed. Is there a movie option I need to set when creating the movie or something that needs to be done when adding frames?  A: You need to set the flags correctly when adding media samples and be make sure to mark keyframes and difference frames.  With `SCCompressSequenceFrame`, you get a value called `notSyncFlag` back to tell you this information. This flag will be set to the `mediaSampleNotSync` constant for a difference frame, so you can pass it in the flags parameter to `AddMediaSample`.  When you compress video with `CompressSequenceFrame` you get a similarity parameter back. If this is non-zero, pass `mediaSampleNotSync` in the flags to `AddMediaSample`.  If you don't do this, all frames will be marked as keyframes, and QuickTime doesn't do the extra work to decompress preceding frames when your users scrub back and forth.   |  | | --- | | ``` // Frame compress loop for (frameNum = 0; frameNum < frameCount; frameNum++) {    short notSyncFlag;    .   .   .    // Compress the frame   SCCompressSequenceFrame(ci,              // compression seq ID                           GetGWorldPixMap(srcGWorld),                           &srcRect,                           &compressedData, // handle to newly compressed data                           &dataSize,       // size of compressed data                           &notSyncFlag);   // key frame flag    // Append the compressed image data to the media   AddMediaSample(dstMedia,      // media specifier        compressedData,          // sample data        0,        dataSize,                // size of sample data        duration,      (SampleDescriptionHandle)idh,      1,                         // number of samples      notSyncFlag,               // sync sample flags 1 = mediaSampleNotSync      NULL);   .   .   . } ``` |   The above snippet from ConvertToMovie Jr. shows how this flag is returned and how it's passed to `AddMediaSample`; the full sample can be found at the following URL: [http://developer.apple.com/samplecode/Sample_Code/QuickTime/Importers_and_Exporters/ConvertToMovieJr.htm](https://developer.apple.com/samplecode/Sample_Code/QuickTime/Importers_and_Exporters/ConvertToMovieJr.htm)   [Dec 01 2000] |

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
