---
title: SCAudioCompress
apple_id: DTS10003962
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2006-08-22'
source_url: https://developer.apple.com/library/archive/samplecode/scaudiocompress/Introduction/Intro.html
archived_at: '2026-07-26T19:54:08.853914Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# SCAudioCompress

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2006-08-22 Xcode 2.4 |
| __Build Requirements:__ | Macintosh: Xcode 2.4 or greater with QuickTime 7.1.x SDK Windows: Visual Studio Dot Net (Visual C++ Dot Net edition) with QuickTime 7.1.x SDK. |
| __Runtime Requirements:__ | Mac OS X 10.4.6 w/QuickTime 7.1.1 or greater or a version of Windows capable of running QuickTime 7.1 or greater. |

__Important__ This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

scaudiocompress is a command line utility that illustrates usage of the SCAudio component SCAudioFillBuffer API's.
Since QuickTime 7, SCAudio (also known as Standard Audio Compression component, StdAudio, StdAudio Dialog and even 'scdi'/'audi') has allowed clients to configure an audio export operation, given an input format, (optionally) a starting output format, and (optionally) some rules about the kinds of output allowed.
StdAudio exposes all of its functionality via properties and the QTSet/GetComponentProperty{Info} API's. In addition, it allows a client to display the standard QuickTime audio compression dialog using SCRequestImageSettings().
New in QuickTime 7.1, the StdAudio component not only allows one to configure an export, it can actually perform the export using an interface identical to AudioConverter's AudioConverterFillComplexBuffer API.
The value added is that:
(1) the StdAudio path incorporates a mixer into its chain, so it can perform mix-downs in addition to encodes, decodes, and transcodes.
(2) It is available on MacOSX/Windows as part of the QuickTime 7.1 SDK. SCAudioFillBuffer's processing chain uses:
(1) an AudioConverter for decode (if necessary)
(2) a MatrixMixer for mixing (if necessary)
(3) another AudioConverter for encode (if necessary)
The scaudiocompress tool demonstrates how to read source packets of audio using AudioFile API (when reading from audio files) or MovieAudioExtraction (when sourcing from a QuickTime movie). The source data is pulled through the StdAudio compression chain, then written to an output file using AddMediaSample2 (if writing to a QuickTime movie), AudioFileWritePackets (if writing a .caf file), or fwrite (if writing a raw interleaved headerless pcm file). scaudiocompress can be run headlessly, or in "interactive" mode, popping up the StdAudio dialog to allow a user to select an output format, if desired.
The code runs on Mac OS X or Windows (NOTE: on Windows, reading/writing is limited to QuickTime movies, as the AudioFile API is not available in the Windows environment).

[Next](ReadMe.txt.md)

