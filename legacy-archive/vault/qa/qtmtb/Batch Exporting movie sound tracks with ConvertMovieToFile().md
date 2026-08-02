---
title: Batch Exporting movie sound tracks with ConvertMovieToFile()
apple_id: DTS10002032
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-10'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb62.html
archived_at: '2026-07-18T02:38:49.876302Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Movie Basics](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxMovieBasics-date.html) >

|  |
| --- |
| Technical Q&A QTMTB62Batch Exporting movie sound tracks with ConvertMovieToFile() |

|  |
| --- |
| ---   Q: I'm trying to batch export Movie sound tracks as AIFF files encoded with QDesign. `ConvertMovieToFile()` does this nicely, but I would like to configure the encoder only once for multiple files and not every time my application is run.  A: `ConvertMovieToFile()` can take a `ComponentInstance` as its last parameter. If you want a particular movie export component to perform the conversion (such as the AIFF "spit" component) you may pass an instance of that component here. This allows you to communicate directly with the component beforehand establishing any conversion parameters the user might want.  Here's how:  Open an instance of the export component, then use `MovieExportDoUserDialog()` to request the component to display its user dialog box. This provides an opportunity for the user to configure the component and will get the component to fill out the parameters fully and correctly. Because some encoders have complicated combinations of sample rates and output bit rates, it is a lot of work to do this by hand.  Once configured, call `MovieExportGetSettingsAsAtomContainer()` and save the resulting `AtomContainer`, perhaps in a configuration or preference file. You now have configuration information which can be used over and over again. See Listing 1.  When performing a batch mode operation simply open an instance of the Exporter component, call `MovieExportSetSettingsFromAtomContainer()` with the AtomContainer previously saved. The Export component will be configured as it was before avoiding any user interaction. You can then call `ConvertMovieToFile()` using the fully configured Export component as the last parameter. See Listing 2.  Once you're finished with the component be sure to close it by calling `CloseComponent()`. |

|  |  |
| --- | --- |
| __Listing 1__.   |  | | --- | | ``` ComponentResult GetExportSettings(Movie inMovie, Track inTrack,      QTAtomContainer *outSettings) {     Component c = 0;     ComponentInstance theExporter = 0;     ComponentDescription cd = { MovieExportType,                                 kQTFileTypeAIFF,                                 StandardCompressionSubTypeSound,                                 hasMovieExportUserInterface,                                 hasMovieExportUserInterface };     ComponentResult err = invalidComponentID;     Boolean ignore;      c = FindNextComponent(0, &cd);     if (c == 0) goto bail;      err = OpenAComponent(c, &theExporter);     if (err || theExporter == 0) goto bail;      err = MovieExportDoUserDialog(theExporter, inMovie,          inTrack, 0,       GetTrackDuration(inTrack), &ignore);     if (err) goto bail;      err = MovieExportGetSettingsAsAtomContainer(theExporter,          outSettings);  bail:     if (theExporter)         CloseComponent(theExporter);      return err; } ``` | |

|  |  |
| --- | --- |
| __Listing 2__.   |  | | --- | | ``` OSErr DoExport(Movie inMovie, Track inTrack, FSSpec inFile[],      UInt16 inCount, QTAtomContainer *inSettings) {     Component c = 0;     ComponentInstance theExporter = 0;     ComponentDescription cd = { MovieExportType,                                 kQTFileTypeAIFF,                                 StandardCompressionSubTypeSound,                                 hasMovieExportUserInterface,                                 hasMovieExportUserInterface };     OSErr err = invalidComponentID;      c = FindNextComponent(0, &cd);     if (c == 0) goto bail;      err = OpenAComponent(c, &theExporter);     if (err || theExporter == 0) goto bail;      err = MovieExportSetSettingsFromAtomContainer(theExporter,          *inSettings);     if (err) goto bail;      while (inCount && !err) {         err = ConvertMovieToFile(inMovie,                                inTrack,                                &inFile[--inCount],                                kQTFileTypeAIFF,                                sigMoviePlayer,                                smSystemScript,                                NULL,                                0,                                theExporter);     }  bail:     if (theExporter)         CloseComponent(theExporter);      return err; } ``` |  [Sep 05 2000] |

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
