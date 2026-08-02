---
title: ExtractMovieAudioToAIFF
apple_id: DTS10003824
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2006-03-31'
source_url: https://developer.apple.com/library/archive/samplecode/ExtractMovieAudioToAIFF/Introduction/Intro.html
archived_at: '2026-07-18T03:08:02.420334Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# ExtractMovieAudioToAIFF

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0.1, 2006-03-31 Now ensures a Movie is fully loaded before extraction can begin. See Q&A1469. |
| __Build Requirements:__ | Xcode 2.2 or greater using the Mac OSX 10.4 Universal SDK |
| __Runtime Requirements:__ | Mac OS X 10.4.x w/QuickTime 7 |

ExtractMovieAudioToAIFF contains simple class called AIFFWriter that encapsulates the functionality of two sets of APIs; QuickTime's Audio Extraction API's and Core Audio's Audio File APIs.
This class will either perform the extraction and file writing on a separate thread if it can, or do so on the main thread in slices thereby not blocking the UI. It also implements a progress callback similar to a movie export progress proc. so clients of the class can drive some UI element like a progress bar.
The sample application uses an instance of the AIFFWriter class to easily perform audio extraction from a QTKit QTMovie to an AIFF file.
The AIFFWriter class uses the default extraction channel layout which is the aggregate channel layout of the movie (for example, all Rights mixed together, all Left Surrounds mixed together, etc).
The output stream description for the file is 16-bit, interleaved big endian with the sample rate set to the highest sample rate found in the movie.
This project builds a Universal Binary target.

[Next](main.m.md)

