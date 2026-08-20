---
title: Using MovieExportSetSampleDescription to specify the format of exported data
apple_id: DTS10002029
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-12'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb59.html
archived_at: '2026-07-18T02:38:49.656937Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Import & Export](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxImportExport-date.html) >

|  |
| --- |
| Technical Q&A QTMTB59Using MovieExportSetSampleDescription to specify the format of exported data |

|  |
| --- |
| ---   Q: I'd like to use the `ConvertMovieToFile` function to export a WAV audio-only movie to an AIFF file using a specific compressor such as QUALCOMM PureVoice. How do I specify the movie export component use the designated compressor?  A: Use the `MovieExportSetSampleDescription` function to specify the format of the exported data. This function is supported by the Apple sound movie export component (though it is not necessarily implemented by all movie export components - if it's not, the component will return the `codecUnimpErr` error). Here's code showing how to use the `MovieExportSetSampleDescription` to specify the format of the exported data: |

|  |
| --- |
| __Listing 1__. Using the `MovieExportSetSampleDescription` function to specify the format of exported data. |

|  |
| --- |
| ``` OSErr ExportWAVEtoAIFF (Movie theMovie, FSSpec *theFile) {     ComponentInstance            myComponent = NULL;     SoundDescriptionHandle        myDesc = NULL;     ComponentResult                myErr = badComponentType;      // open a movie export component     myComponent = GetAIFFMovieExportComponent();     if (myComponent == NULL)         goto bail;      // create and fill in a sound description     myDesc = (SoundDescriptionHandle)NewHandleClear(sizeof(SoundDescription));     if (myDesc == NULL)     {         myErr = MemError();         goto bail;     }      // specify the export format     (**myDesc).descSize = sizeof(SoundDescription);     (**myDesc).sampleSize = 16;     (**myDesc).sampleRate = rate22050hz;     (**myDesc).dataFormat = kQUALCOMMCompression;     (**myDesc).dataRefIndex = 1;     (**myDesc).numChannels = 1;      // tell the export component to use the     // specified audio characteristics     myErr = MovieExportSetSampleDescription(myComponent,           (SampleDescriptionHandle)myDesc, SoundMediaType);     if (myErr != noErr)         goto bail;      // export the movie into a file     myErr = ConvertMovieToFile(                         theMovie,        // the movie to convert                         NULL,            // the first track                         theFile,         // the output file                         kQTFileTypeAIFF, // the output file type                         sigMoviePlayer,  // the output file creator                         smSystemScript,  // the script                         NULL,            // resource ID                         0L,              // no flags                         myComponent);    // the export component  bail:     // dispose of any storage we allocated     if (myComponent != NULL)         CloseComponent(myComponent);      if (myDesc != NULL)         DisposeHandle((Handle)myDesc);      return((OSErr)myErr); }  ComponentInstance GetAIFFMovieExportComponent() {     ComponentDescription cd;     Component c = 0;     ComponentInstance ci=0;       cd.componentType = MovieExportType;     cd.componentSubType = kQTFileTypeAIFF;     cd.componentManufacturer = SoundMediaType;     cd.componentFlags = 0;     cd.componentFlagsMask = 0;      c = FindNextComponent( c, &cd );      if (c != nil)     {         ci = OpenComponent(c);     }      return ci; } ```  [Sep 05 2000] |

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
