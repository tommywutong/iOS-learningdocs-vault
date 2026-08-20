---
title: QTExtractAndConvertToMovieFile
apple_id: DTS10004106
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2006-11-08'
source_url: https://developer.apple.com/library/archive/samplecode/QTExtractAndConvertToMovieFile/Introduction/Intro.html
archived_at: '2026-07-18T03:20:51.885126Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# QTExtractAndConvertToMovieFile

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2006-11-08 Demonstrates using MovieAudioExtraction and an AudioConverter to extract and convert audio to a QuickTime movie file. |
| __Build Requirements:__ | Xcode 2.3 or greater using the Mac OSX 10.4 Universal SDK |
| __Runtime Requirements:__ | Mac OS X 10.4.7, QuickTime 7.1.3 |

QTExtractAndConvertToMovie contains two Objective-C objects that are used together to implement audio extraction and audio conversion from a QuickTime Movie sound track to a movie file.
The first is a simple class called MovieWriter (this is a modified version of the AIFFWriter class that was included with the ExtractMovieAudioToAIFF and QTExtractAndConvertToAIFF samples). MovieWriter uses QuickTime's Movie Audio Extraction, Movie Storage and Media Creation APIs. The second is another simple class called AudioConverter which encapsulates Core Audio's Audio Converter API.
The sample uses an instance of the MovieWriter class to easily set up audio extraction from a QTKit QTMovie to a new destination Movie and its associated movie file (or movie storage as it's called in the API). MovieWriter uses an instance of the AudioConverter class to perform the conversion to a user selected destination format which is configured by the Standard Audio Dialog Component. The Audio Converter uses a Movie Audio Extraction Session in the Read Input Procedure to pull audio out of the source Movie. AddMediaSample2 is then used to add the converted audio to the movie storage.
This sample supports VBR as well as CBR audio encoding formats.
IMPORTANT NOTE FOR QUICKTIME DEVELOPERS:
While this example demonstrates using the Audio Converter APIs directly, QuickTime developers may want to consider using the crossplatform SCAudioFillBuffer API introduced in QuickTime 7.1. SCAudio is built on top of Core Audio and incorporates a mixer into its chain, so it can perform mix-downs in addition to encodes, decodes, and transcodes. It also maintains an interface identical to AudioConverter's AudioConverterFillComplexBuffer.
See the SCAudioCompress sample for more details.

[Next](main.m.md)

