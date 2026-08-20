---
title: Multi-Buffer Aware Image Decompressors
apple_id: DTS10003757
resource_type: Technical Note
platform: macOS
topic: null
technology: QuickTime
published: '2005-07-12'
source_url: https://developer.apple.com/library/archive/technotes/tn2148/_index.html
archived_at: '2026-07-26T19:54:08.539779Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2148

# Multi-Buffer Aware Image Decompressors

__Important:__ This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

This technical note discusses how Image Decompressors can maximize performance by supporting multi-buffer decompression and turning on the `subCodecIsMultiBufferAware` flag added in QuickTime 7.

[Overview](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvg4wugsbrfvke4vcbi4yq)[What You Need To Do](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvg4wugsbrfvke4vcbi42q)[Compatibility Notes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvg4wugsbrfvke4vcbi4za)[Sample Code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvg4wugsbrfvke4vcbi4zq)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvg4wvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Overview

For maximum performance, video decompressor components should be marked as multi-buffer aware by setting the `subCodecIsMultiBufferAware` flag to `true`.

By setting this flag, the decompressor informs the Image Compression Manager that it is able to draw each frame to a new pixel buffer. This contract with the Image Compression Manager reduces the amount of buffer copies necessary to play through Core Video.

[Back to Top](#)

## What You Need To Do

In your image decompressor's `ImageCodecInitialize` function, make sure to set the `subCodecIsMultiBufferAware` flag to `true`. This flag is part of the `ImageSubCodecDecompressCapabilities` structure passed to the `Initialize` function. See Listing 1.

__Listing 1__  `ImageCodecInitialize` function.

```
ComponentResult MyDecompressor_Initialize(MyDecompressorGlobals *storage,
                                          ImageSubCodecDecompressCapabilities *cap)
{
    // Specify the size of the ImageSubCodecDecompressRecord structure
    cap->decompressRecordSize = sizeof(MyDecompressRecord);

    // Say we can support asynchronous decompression - With the help of the base
    // image decompressor, any image decompressor that uses only interrupt-safe
    // calls for decompression operations can support asynchronous decompression
    cap->canAsync = true;

    // set other capabilities as appropriate

    .
    .
    .

    // subCodecIsMultiBufferAware added in QuickTime 7
    // tell the base codec that we are "multi-buffer aware" - This promises that we
    // always draw using ImageSubCodecDecompressRecord.baseAddr/rowBytes
    // passed to our ImageCodecDrawBand function, and that we always overwrite every
    // pixel in the buffer - it is important to set this in order to get optimal
    // performance when playing through Core Video
    //
    // add this line of code
    cap->subCodecIsMultiBufferAware = true;

    .
    .
    .
}
```

__By setting this flag, a decompressor MUST honor a contract with the Image Compression Manager and be able to do the following__:

- Always draw using the `ImageSubCodecDecompressRecord.baseAddr/rowBytes` passed to `ImageCodecDrawBand`. Do not save the values of these fields in `ImageCodecBeginBand`, because that function may be called before the actual destination buffer is known.
- Ignore the base address and row bytes in the `port` and `dstPixMap` passed to `ImageCodecBeginBand` as part of the `CodecDecompressParams` struct. During multi-buffer playback, these will not point to the correct buffer. In particular, the decompressor must not call QuickDraw to draw to the `port`.

  NOTE: It's OK to use the `dstPixMap` to find the pixel format of the output buffers during the `ImageCodecPreflight` function.
- Always write every pixel in the buffer.

Decompressors that do not set this flag will use a compatibility mode which involves an extra buffer copy per frame when playing to a multi-buffer destination through Core Video.

Some old decompressors (particularly those that do not perform motion compensation), do not write every pixel of difference frames, relying on the old pixels staying present. These decompressors should __NOT__ set the `subCodecIsMultiBufferAware` flag.

[Back to Top](#)

## Compatibility Notes

While `subCodecIsMultiBufferAware` is new field added to the `ImageSubCodecDecompressCapabilities` structure for QuickTime 7 and Mac OS 10.4, it is completely safe to set this field all the way back to QuickTime 5.0.1. This is because this byte reuses a former padding field. On releases before QuickTime 7 this field is simply ignored.

[Back to Top](#)

## Sample Code

The [ExampleIPBCodec](https://developer.apple.com/samplecode/ExampleIPBCodec/ExampleIPBCodec.html) sample demonstrates modern (QuickTime 7 and greater) techniques for writing both Image Compressors and Decompressors.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-07-12 | New document that describes how to mark a video decompressor component as multi-buffer aware for maximum performance with CoreVideo. |

