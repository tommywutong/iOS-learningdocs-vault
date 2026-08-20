---
title: Image Decompressor Data-loading Procs
apple_id: DTS10001962
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-11'
source_url: https://developer.apple.com/library/archive/qa/qtmcc/qtmcc19.html
archived_at: '2026-07-18T02:38:47.444452Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [QuickTime Component Creation](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxQuickTimeComponentCreation-date.html) >

|  |
| --- |
| Technical Q&A QTMCC19Image Decompressor Data-loading Procs |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ---   Q: I'm writing a decompressor component to work with my graphics importer and I need to load all my image data into a single buffer before decompression. In implementing `ImageCodecPreflight` I've made sure to set `bandMin` to the full height of my image. However, I am finding the buffer size that I am passed in `ImageCodecBeginBand` is set to 32K, and not the size of the image on disk. Can you explain why that is and how I can call the data-loading proc correctly?  A: The caller of `FDecompressImage` (or one of the related functions in the Image Compression Manager) has a choice: they can provide all of the compressed data in a single buffer, or provide a smaller buffer and a data-loading proc.  A data-loading function's buffer will be at least 32K - `codecMinimumDataSize` is defined as 32K.  Image decompressor components should support both modes, since both modes are likely to occur. In current versions of QuickTime the video media handler will never use a data-loading proc, while the base graphics importer always does.  The data-loading proc interface is designed for ease of use by image decompressor components that only need to make a single pass through their input data. If a data-loading proc is supplied, you will need to call it regularly with the pointer you're reading data from and indicate the maximum read-ahead you might need. If necessary, the data-loading proc updates your pointer to make sure there's enough data ahead of you.  However, sometimes there are reasons why you can't integrate calls to the data-loading proc into your decompressor -- for example, if the actual decompression work is done by code or hardware you cannot modify. In these cases, you may need to copy the whole frame into a buffer by calling the data-loading proc multiple times, asking for `p->bufferSize` bytes each time.  The base graphics importer always ensures that the image description's `dataSize` contains the actual size of the entire compressed data.  Let's take a look at how this works:   |  | | --- | | ``` OSErr ICMDataProcPtr(Ptr *dataP, long bytesNeeded, long refcon); ``` |      1. When you call a data-loading proc, you pass it the address of your pointer into the data-loading proc's buffer. The data-loading proc may check that your pointer still points into its buffer, and it will use the pointer's current value to calculate how much data you have consumed.  |  | | --- | | ``` Ptr dataPtr = drp->codecData; Size bytesConsumed; Boolean done = false;  while(! done) {   if(dataProc) {     err = CallICMDataProc(dataProc, &dataPtr, 10000, dataRefCon);     if(err) goto bail;   }     err = consumeUpTo10000Bytes(..., dataPtr, &bytesConsumed, &done);     if(err) goto bail;     dataPtr += bytesConsumed; } ``` |      2. Passing NULL instead of the address of your pointer has a special meaning: if the `bytesNeeded` parameter is zero, it requests a reset to the start of the data-stream; if the `bytesNeeded` parameter is non-zero, it requests a relative seek by that many bytes. Before doing a relative seek, you should make sure the data-loading proc knows the location of your pointer in its buffer. You can do this by calling the data-proc to ask for zero bytes:   Reset to Start of Data-Stream:   |  | | --- | | ```   err = CallICMDataProc(dataProc, NULL, 0, dataRefCon); ``` |     Relative Seek:   |  | | --- | | ```   err = CallICMDataProc(dataProc, &dataPtr, 0, dataRefCon);   err = CallICMDataProc(dataProc, NULL, relativeSeekAmount, dataRefCon); ``` |     followed by read:   |  | | --- | | ```   err = CallICMDataProc(dataProc, &dataPtr, bytesNeeded, dataRefCon); ``` |      3. To load the data into a block of memory you've allocated, you could do this in your `BeginBand` routine:  |  | | --- | | ``` Ptr dataPtr = drp->codecData; Ptr bufferPtr = myBuffer; Size bytesRemaining = myBufferSize;  while(bytesRemaining > 0) {   Size bytesToRequest;   if(bytesRemaining < codecMinimumDataSize)     bytesToRequest = bytesRemaining;   else     bytesToRequest = codecMinimumDataSize;    err = CallICMDataProc(dataProc, &dataPtr, bytesToRequest, dataRefCon);   if(err) goto bail;   BlockMoveData(dataPtr, bufferPtr, bytesToRequest);   dataPtr += bytesToRequest;   bufferPtr += bytesToRequest;   bytesRemaining -= bytesToRequest; } ``` |     [Jul 10, 2003] |

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
