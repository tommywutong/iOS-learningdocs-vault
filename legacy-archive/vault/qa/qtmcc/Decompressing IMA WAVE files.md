---
title: Decompressing IMA WAVE files
apple_id: DTS10001954
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1998-10-19'
source_url: https://developer.apple.com/library/archive/qa/qtmcc/qtmcc11.html
archived_at: '2026-07-18T02:38:46.982645Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Import & Export](https://developer.apple.com/referencelibrary/QuickTime/idxImportExport-date.html)

|  |
| --- |
| Technical Q&A QTMCC11Decompressing IMA WAVE files |

|  |  |  |  |
| --- | --- | --- | --- |
| ---   Q: I want to decompress and play Window's Microsoft ADPCM-compressed WAVE files on the Mac, but I want to use the Sound Manager, not QuickTime. Is this possible?  A: Yes, this is possible, for the most part. However, you must still use QuickTime, at least partially, unless you want to write your own sound decompressor component to handle the ADPCM sounds. You won't need to use the QuickTime API to play the sound: you will use the Sound Manager's API, but you will still need to ensure that QuickTime 3.0 or later is installed.  This Q&A details how you would use the QuickTime IMA sound decompressor components that come with QuickTime 3.0 (along with the Sound Manager's APIs) so that you can decompress and play the sound yourself.  QuickTime supplies two sound decompressor components: one for Microsoft ADPCM compressed WAVE files, and one for Intel IMA-DVI compressed WAVE files, whose signatures are `kMicrosoftADPCMFormat` and `kDVIIntelIMAFormat`, respectively.  However, playing a IMA-compressed WAVE file via the Sound Manager is not as simple as merely specifying one of these sound decompressors. Due to the file format variances allowed in IMA-compressed WAVE files, the decompressor component has to be configured so that it can correctly decompress the sound.  You configure the decompressor component by reading the `'fmt '` chunk out of the WAVE file and passing it, as a QuickTime atom, to the appropriate decompressor component. You do not need to do any endian conversion on the `'fmt '` chunk before you place it in the atom, because the IMA decompressor components expect the data to be in little endian format, exactly as it comes out of the WAVE file.  Once the atom has been constructed, send it to the decompressor component via `SoundConverterSetInfo` with the `siDecompressionParams` selector.  Once this has been done, you can use the Sound Manager's `SoundConvert` routines to decompress the sound into a buffer so that you can play the uncompressed sound (because you cannot directly play the compressed sound), or do anything else to the uncompressed sound that you want to.   |  | | --- | | Note: Make sure that you make your buffers of compressed data large enough; 8K is a good starting point, but you may need to make it larger to handle every possible WAVE. If the buffer is not large enough, the call to `SoundConverterGetBufferSizes` will fail with an the error code `notEnoughBufferSpace` (-207). If you get this error you should increase the size of the buffer and call `SoundConverterGetBufferSizes` again, repeating the process until it does not return an error (or returns an error other than `notEnoughBufferSpace`). |     |  | | --- | | Here is sample code showing how to create the atom and pass it to the decompressor component. You will need to supply your own code to parse the WAVE file's header and extract the `'fmt '` chunk. |     |  | | --- | | ``` typedef struct adpcmcoef_tag {     short   iCoef1;     short   iCoef2; } ADPCMCOEFSET;  typedef struct waveformat_extended_tag {     short       wFormatTag;         /* format type */     short       nChannels;          /* number of channels (i.e. mono, stereo...) */     long        nSamplesPerSec;     /* sample rate */     long        nAvgBytesPerSec;    /* for buffer estimation */     short       nBlockAlign;        /* block size of data */     short       wBitsPerSample;     /* Number of bits per sample of mono data */     short       cbSize;             /* The count in bytes of the extra size */ } WAVEFORMATEX;  typedef struct adpcmwaveformat_tag {     WAVEFORMATEX    wfx;     short           wSamplesPerBlock;     short           wNumCoef;     ADPCMCOEFSET    aCoef[32]; } ADPCMWAVEFORMAT;  typedef struct {     long            atomSize;           // how big this structure is (big endian)     long            atomType;           // atom type - always kMicrosoftADPCMFormat                                         // (big endian)                                         // everything below here is little endian -                                         // right out of the wave header     ADPCMWAVEFORMAT adpcm; } AtomMSADPCMWaveFormatEx;  typedef struct {     AudioFormatAtom             formatData;     AtomMSADPCMWaveFormatEx     endianData;     AudioTerminatorAtom         terminatorData; } AudioCompressionAtom, *AudioCompressionAtomPtr, **AudioCompressionAtomHandle;  OSErr ASoundGetWAVEHeader (...) {     ...     case FormatID:         format = EndianU16_LtoN (WAVETemplate->fmt.wFormatTag);         switch (format) {             case 2:     // MS ADPCM             case 17:    // IMA ADPCM                 BlockMoveData (&(WAVETemplate->fmt.wFormatTag), formatChunk,                 EndianU32_LtoN (WAVETemplate->fmt.ckSize));         ...         }     ... }  OSErr DecompressWave (...) {     AudioCompressionAtom    decomAtom;      if (err == noErr) {         // Parse the WAVE file and get the 'fmt ' atom.         err = ASoundGetWAVEHeader (&theSoundInfo, &length,         (fmtChunk*)&(decomAtom.endianData.adpcm));     }      if (err == noErr) {         // Figure out which type of ADPCM file we have.         switch (EndianU16_LtoN (decomAtom.endianData.adpcm.wfx.wFormatTag)) {             case 0x0002:                 waveFormat = kMicrosoftADPCMFormat;                 break;             case 0x0011:                 waveFormat = kDVIIntelIMAFormat;                 break;             default:                 err = badFormat;         }     }      if (err == noErr) {         inputFormat.flags = 0;         inputFormat.format = waveFormat;         inputFormat.numChannels = EndianU16_LtoN           (decomAtom.endianData.adpcm.wfx.nChannels);         inputFormat.sampleSize = EndianU16_LtoN           (decomAtom.endianData.adpcm.wfx.wBitsPerSample);         inputFormat.sampleRate = (EndianU32_LtoN           (decomAtom.endianData.adpcm.wfx.nSamplesPerSec)) << 16;         inputFormat.sampleCount = 0;         inputFormat.buffer = nil;         inputFormat.reserved = 0;          outputFormat.flags = 0;         outputFormat.format = kSoundNotCompressed;         outputFormat.numChannels = EndianU16_LtoN           (decomAtom.endianData.adpcm.wfx.nChannels);         outputFormat.sampleSize = 16;         outputFormat.sampleRate = (EndianU32_LtoN           (decomAtom.endianData.adpcm.wfx.nSamplesPerSec)) << 16;         outputFormat.sampleCount = 0;         outputFormat.buffer = nil;         outputFormat.reserved = 0;          err = SoundConverterOpen (&inputFormat, &outputFormat, &sc);     }      if (err == noErr) {         // Make atom to send to ADPCM decompressor so it knows how to         // decompress the data.         decomAtom.formatData.size = sizeof (AudioFormatAtom);         decomAtom.formatData.atomType = kAudioFormatAtomType;         decomAtom.formatData.format = waveFormat;          decomAtom.endianData.atomSize = sizeof (AtomMSADPCMWaveFormatEx);         decomAtom.endianData.atomType = waveFormat;          decomAtom.terminatorData.size = sizeof (AudioTerminatorAtom);         decomAtom.terminatorData.atomType = kAudioTerminatorAtomType;          err = SoundConverterSetInfo (sc, siDecompressionParams, &decomAtom);     }      if (err == noErr) {         targetBytes = 4096;         do {             targetBytes *= 2;             err = SoundConverterGetBufferSizes               (sc, targetBytes, &inputFrames, &inputBytes, &outputBytes);         } while (err == notEnoughBufferSpace && targetBytes < (MaxBlock () / 4));     } } ``` |    From this point on, use standard sound conversion code to uncompress the sound. [Oct 19 1998] |

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
