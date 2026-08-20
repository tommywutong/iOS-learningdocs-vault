---
title: High-Efficiency Advanced Audio Coding (HE-AAC)
apple_id: DTS40008748
resource_type: Technical Note
platform: iOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2009-04-21'
source_url: https://developer.apple.com/library/archive/technotes/tn2236/_index.html
archived_at: '2026-07-26T19:54:09.598633Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2236

# High-Efficiency Advanced Audio Coding (HE-AAC)

This Technical Note discusses the High-Efficiency Advanced Audio Coding compression scheme for digital audio.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzuhawugsbrfvjukq2ujfhu4mi)[What is MPEG AAC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzuhawugsbrfvjvkqstivbviskpjyyq)[What is HE-AAC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzuhawugsbrfvjvkqstivbviskpjyza)[Recommended Bit Rate Range](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzuhawugsbrfvjukq2ujfhu4na)[Difference between ADTS and MPEG Based Files](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzuhawugsbrfvjukq2ujfhu4ni)[Signalling the Presence of SBR Data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzuhawugsbrfvjukq2ujfhu4nq)[What is Signalling?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzuhawugsbrfvjvkqstivbviskpjy3a)[Signalling modes supported by Apple for HE-AAC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzuhawugsbrfvjvkqstivbviskpjy3q)[AAC Codec Format IDs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzuhawugsbrfvjukq2ujfhu4oi)[References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzuhawugsbrfvjukq2ujfhu4mjq)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzuhawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

### What is MPEG AAC

MPEG AAC is a perceptual audio compression scheme developed by the MPEG group and designed to be the successor to the MP3 format.

MPEG formal listening tests have demonstrated that for a 2-channel audio track, Low Complexity AAC (a.k.a AAC-LC or generally referred as AAC) is able to provide slightly better audio quality at 96 kbs than MP3 at 128 kbs.

### What is HE-AAC

High Efficiency AAC (HE-AAC) is an extension of AAC-LC optimized for low-bitrate applications such as streaming audio and podcasts.

HE-AAC uses spectral band replication (SBR) to enhance the compression efficiency of the upper half of the frequency band. HE-AAC version 2 (HE-AAC v2) adds Parametric Stereo (PS) to further enhance the compression efficiency of stereo signals at very low bit rates only.

The sound quality for HE-AAC v1 at 64 kb/s is comparable to AAC-LC at 96 kb/s.

[Back to Top](#)

## Recommended Bit Rate Range

Based on the unique characteristics of each AAC codec, for stereo audio sampled at 44.1 kHz the recommended operational bitrate ranges are:

- HE-AAC v2 for lower bitrates between 16 - 40 kb/s.
- HE-AAC v1 for bitrates between 32 - 80 kb/s.
- AAC-LC for bitrates higher than 80 kb/s.

[Back to Top](#)

## Difference between ADTS and MPEG Based Files

AAC compressed audio data may be stored in either an MPEG-4 container file format (.mp4, .m4a) or more basic MPEG-2 based file formats such as a ADTS (.aac, .adts) Audio Data Transport Stream file.

An MPEG-4 file contains a header that includes meta-data followed by "tracks" which can include video as well as audio data, for example, H.264 encoded Video and AAC encoded Audio.

ADTS in contrast is a streaming format consisting of a series of frames, each frame having a header followed by the AAC data.

Therefore, a decoder can start playing a ADTS stream at any point within that stream making it ideal for "radio" like applications. To decode an MPEG-4 file however, the file header must first be read in order to properly playback the file.

[Back to Top](#)

## Signalling the Presence of SBR Data

### What is Signalling?

The HE-AAC bitstream is a combination of AAC-LC data and SBR data and is backward compatible with existing AAC-LC decoders. A decoder only capable of decoding AAC-LC audio data will only play the AAC-LC part of an HE-AAC encoded bitstream resulting in lower audio quality.

There are two ways to signal the presence of SBR data:

- Explicit signaling: the presence of SBR data is signaled explicitly by means of the SBR AOT in the `AudioSpecificConfig()` contained within an MPEG-4 file. This allows retrieval of configuration specific data from the file header, which includes separate specifications of the sampling rates for the HE-AAC and AAC-LC decoders.
- Implicit signaling: if SBR extension elements (`EXT SBR DATA` or `EXT SBR DATA CRC`) are detected in the bitstream, this implicitly means that SBR data is present.

### Signalling modes supported by Apple for HE-AAC

- In the MPEG-4 file format, explicit signalling only. This includes the backwards compatibility mode which is the recommended signalling mode for maximum compatibility.
- In the ADTS format implicit signalling is supported as ADTS files only contain the actual audio payload and no meta-data fields.
[Back to Top](#)

## AAC Codec Format IDs

Starting with iPhone OS 2.2, support has been added for HE-AAC v1 audio coding. The following four character code IDs are used to identify AAC audio data formats on the platform and are declared in `<CoreAudio/CoreAudioTypes.h>`.

__Table 1__

| Declaration | Four Character Code | Description |
| kAudioFormatMPEG4AAC | 'aac ' | MPEG-4 Low Complexity AAC |
| kAudioFormatMPEG4AAC_HE | 'aach' | MPEG-4 High Efficiency AAC |

[Back to Top](#)

## References

- [Advanced Audio Coding](http://en.wikipedia.org/wiki/Advanced_Audio_Coding)
- [High-Efficiency Advanced Audio Coding](https://developer.apple.com/library/archive/technotes/tn2236/High-Efficiency Advanced Audio Coding)
- [Spectral band replication](http://en.wikipedia.org/wiki/Spectral_band_replication)
- [Parametric Stereo](http://en.wikipedia.org/wiki/Parametric_Stereo)
- [MPEG-4](http://en.wikipedia.org/wiki/MPEG-4)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-04-21 | New document that discusses HE-AAC audio. |

