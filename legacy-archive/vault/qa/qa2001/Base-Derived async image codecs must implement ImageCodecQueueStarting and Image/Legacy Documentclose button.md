---
title: Base-Derived async image codecs must implement ImageCodecQueueStarting and
  ImageCodecQueueStopping
apple_id: DTS10001701
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2002-07-09'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1157.html
archived_at: '2026-07-18T02:38:16.845161Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > QuickTime Component Creation](https://developer.apple.com/referencelibrary/QuickTime/idxQuickTimeComponentCreation-date.html)

|  |
| --- |
| Technical Q&A QA1157Base-Derived async image codecs must implement ImageCodecQueueStarting and ImageCodecQueueStopping |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ---   Q: I've written a codec that uses the Base Image Decompressor. My Decompressor should be able to run asynchronously (the DrawBand function doesn't make any un-safe calls), and I've made sure to set the canAsync flag in the sub-codec capabilities record during ImageCodecInitialize. However, the codec doesn't seem to be running asynchronously. Am I missing something?  A: Asynchronous codecs derived from the Base Codec must make sure to implement the ImageCodecQueueStarting and ImageCodecQueueStopping routines in addition to setting the canAsync flag. Your codec must implement these calls or the Base Codec will fall back to synchronous playback.  If your codec doesn't need to do any work at these times, simply return noErr.  Listing 1 demonstrates setting up a dispatch file and implementing both selectors.  Listing 2 demonstrates how to let ComponentDispatchHelper do the work for you if your codec doesn't need to do any work in QueueStarting and QueueStopping.     |  | | --- | | ``` // MySubCodecDispatch.h  ...      ComponentRangeBegin (3)         ComponentCall     (Preflight)         ComponentCall     (Initialize)         ComponentCall     (BeginBand)         ComponentCall     (DrawBand)         ComponentCall     (EndBand)         ComponentCall     (QueueStarting)         ComponentCall     (QueueStopping)         ComponentDelegate (DroppingFrame)         ComponentDelegate (ScheduleFrame)         ComponentDelegate (CancelTrigger)     ComponentRangeEnd (3)  ...  // MySubCodec.c  ...  // ImageCodecQueueStarting //     The base image decompressor calls your image decompressor component's // ImageCodecQueueStarting function before decompressing the frames in the // queue. The base image decompressor never calls the ImageCodecQueueStarting // function at interrupt time. // If your codec supports asynchronous scheduled decompression you must // implement this selector. If your codec does not need to do anything at // this time simply return noErr. pascal ComponentResult EI_ImageCodecQueueStarting(EI_Globals glob) {  #pragma unused(glob)      return noErr; }  // ImageCodecQueueStopping //     The base image decompressor calls your ImageCodecQueueStopping // function to notify your codec that the frames in the queue have been // decompressed. After your image decompressor component handles an // ImageCodecQueueStopping call, it can perform any tasks that are required // when decompression of the frames is finished, such as disposing of data // structures that are no longer needed. // If your codec supports asynchronous scheduled decompression you must // implement this selector. If your codec does not need to do anything at // this time simply return noErr. // The base image decompressor never calls the ImageCodecQueueStopping // function at interrupt time. pascal ComponentResult EI_ImageCodecQueueStopping(EI_Globals glob) {  #pragma unused(glob)      return noErr; }  ... ``` | | __Listing 1__. Implementing QueueStarting & QueueStopping |      |  | | --- | | ``` // If your codec doesn't need to perform any work in QueueStarting // and QueueStopping, you can use ComponentNoError in your dispatcher // and let ComponentDispatchHelper do the work for you. // ComponentDispatchHelper will return noErr for these two selectors and not // badComponentSelector.  // MySubCodecDispatch.h  ...     ComponentRangeBegin (3)         ComponentCall     (Preflight)         ComponentCall     (Initialize)         ComponentCall     (BeginBand)         ComponentCall     (DrawBand)         ComponentCall     (EndBand)         ComponentNoError  (QueueStarting)         ComponentNoError  (QueueStopping)         ComponentDelegate (DroppingFrame)         ComponentDelegate (ScheduleFrame)         ComponentDelegate (CancelTrigger)     ComponentRangeEnd (3)  ... ``` | | __Listing 2__. Using ComponentNoError to implement QueueStarting & QueueStopping |    References: [QuickTime Codec Components](https://developer.apple.com/documentation/quicktime/qtdevdocs/RM/rmCodecComp.htm) [Base Image Decompressor Functions](https://developer.apple.com/documentation/quicktime/qtdevdocs/REF/refBaseImage.15.htm)     ---  [Jul 09 2002] |

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
