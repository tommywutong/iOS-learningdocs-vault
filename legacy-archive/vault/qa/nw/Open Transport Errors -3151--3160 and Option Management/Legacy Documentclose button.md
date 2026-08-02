---
title: Open Transport Errors -3151/-3160 and Option Management
apple_id: DTS10001466
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-04-12'
source_url: https://developer.apple.com/library/archive/qa/nw/nw54.html
archived_at: '2026-07-18T02:29:47.167250Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Networking > Carbon](https://developer.apple.com/referencelibrary/Networking/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A NW54Open Transport Errors -3151/-3160 and Option Management |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ---   Q: When I make an `OptionManagement` call to set an endpoint option, I receive one of two error messages, __Error -3155__ (bad option) or __Error -3160__ (buffer overflow). What should I be looking at to resolve these errors?  A: __Error -3151__ indicates that a bad option or option value was passed to an Open Transport endpoint. The following answers assume an understanding of making calls to `OTOptionManagement`. For more information on call to `OTOptionManagement`, please refer to ["Inside Macintosh: Networking With Open Transport"](https://developer.apple.com/documentation/mac/NetworkingOT/NetworkingWOT-37.html), chapter 7, Option Management. You can download an electronic copy of this documentation from the [Open Transport Web Page.](http://www.apple.com/macos/opentransport/)  The common reasons for __Error -3151__ are:   1. __The option length for the option is incorrect.__ Most Open Transport Option Management option values are 4 bytes long. Some options take string and structure values. You must set both the `TOptMgmt opt.len` field, and the `TOptionHeader len` field to the exact length of the option buffer request. You can also use the same buffer and `TOptMgmt` structure for the Option Management response, which is discussed in the next section regarding __Error -3160__.  __Error -3151__ occurs most often when the option value is 1 byte long, but a 4-byte length is specified. Again, there are two places where the length argument is set - in the `TOptMgmt` structure and in the `TOptionHeader` structure. 2. __A return `TOptMgmt` pointer was passed in the call to `OTOptionManagement`    and the `maxlen` field is not set correctly.__ Not setting this parameter    can also result in __Error -3160__, depending on its input value. The    `OTMultiCastPitch` code sample in the OpenTransport SDK demonstrates this    problem when trying to set the `IP_ADD_MEMBERSHIP` option. The corrected    call is shown as follows:      |  |    | --- |    | ```         optReq.flags = T_NEGOTIATE;         optReq.opt.len = sizeof(optBuffer);      // specify the size of the buffer         optReq.opt.maxlen = sizeof(optBuffer);   // <--- add this line of code          optReq.opt.buf = (UInt8*) optBuffer;         OTMemzero(optBuffer, sizeof(optBuffer));         opt->level = INET_IP;         opt->name = IP_ADD_MEMBERSHIP;         opt->len = sizeof(optBuffer);           // specify the size of the option ``` |      A similar correction is required in the same code sample when trying to    set the `IP_MULTICAST_TTL` option. The modified code sample is shown below.  The previous corrections applies to the Open Transport SDK v1.3 and    earlier. 3. __There is a known problem when using Open Transport v1.3 and earlier.__    You will encounter this error when using the `OTOptionManagement` T_ALLOPT    value to obtain all of the current IP option settings in one call. This    problem is demonstrated with the `OTMulticastPitchSample` code running    under Open Transport v 1.3 and earlier. The workaround is to ask    individually for the status of each option where the current setting is    desired.   The common reasons for __Error -3160__ are:   1. __The `TOptMgmt opt.maxlen` field was not initialized, or incorrectly set.__ This error can be returned even if the option was successfully negotiated. The solution is to set the `maxlen` field correctly. 2. __There is a known problem when using Open Transport v1.3 and earlier.__ If you try to negotiate a TCP/IP option whose length is 1 or 2 bytes, Open Transport will return this error if the return buffer is set for a buffer for less than a 4-byte response. Interestingly, the option may be successfully negotiated. The workaround for this problem is to define the size of the buffer as `kOTFourByteOptionSize` and to continue to set the two `len` fields as `kOTOneByteOptionSize` or `kOTTwoByteOptionSize` (as of this writing, there are no 2-byte option settings).   __Error -3160__ will not be returned if there is no return parameter specified. On the other hand, without checking the return value, you cannot know whether the return status of the option call was `T_SUCCESS` or not. This problem applies when trying to set the following options:   |  |  | | --- | --- | | __Option Level__ | __Option Name__ | | INET_UDP | UDP_RX_ICMP | | INET_IP | IP_RECVOPTS | | INET_IP | IP_TOS | | INET_IP | IP_TTL | | INET_IP | IP_MULTICAST_LOOP | | INET_IP | IP_MULTICAST_TTL | | INET_IP | IP_RECVDSTADDR | | INET_IP | IP_RECVIFADDR |   The following modifications and corrections apply to the `OTMultiCastPitchSample.cp` file.  __Correction 1:__  Change to the sample code for setting the `IP_MULTICAST_TTL` option.   |  | | --- | | ```         //         //  Setup time-to-live for multicast sends (defaults to 1)         //  Can reuse the TOptMgmt, but not Option itself is different.         //  While we could reuse the buffer above, I'll do it right to         //  demonstrate correctness.         //         UInt8 ttlOptBuffer[ kOTFourByteOptionSize ]; // <-- 4 byte option length buffer         TOption*         ttlOpt = (TOption*)ttlOptBuffer;          optReq.flags = T_NEGOTIATE;         optReq.opt.len = kOTOneByteOptionSize; // <-- leave as 1 byte option size         optReq.opt.maxlen = sizeof(ttlOptBuffer); // <-- set return buffer maxlen         optReq.opt.buf = (UInt8*) ttlOptBuffer;         OTMemzero(optBuffer, sizeof(ttlOptBuffer));         ttlOpt->level = INET_IP;         ttlOpt->name = IP_MULTICAST_TTL;         ttlOpt->len = kOTOneByteOptionSize; // <-- leave as 1 byte option size          *(char*)(ttlOpt->value) = kDefaultTTL;          err = gEndpt->OptionManagement(&optReq, &optReq); ``` |   __Correction 2:__ Change to the sample code for setting the `IP_MULTICAST_LOOP` option.   |  | | --- | | ```     //     //  Turn off loopback - unless you want to receive your own packets back.     //     TOptMgmt optReq;     UInt8 optBuffer[ kOTFourByteOptionSize ]; // <-- 4 byte option length buffer     TOption* opt = (TOption*)optBuffer;      OTMemzero(optBuffer, sizeof(optBuffer));     optReq.flags    = T_NEGOTIATE;     optReq.opt.len  = kOTOneByteOptionSize; // <-- leave as 1 byte option size     optReq.opt.maxlen   = sizeof(optBuffer); // <-- set return buffer maxlen     optReq.opt.buf  = (UInt8*) optBuffer;      opt->level = INET_IP;     opt->name = IP_MULTICAST_LOOP;     opt->len = kOTOneByteOptionSize; // <-- leave as 1 byte option size     *(char *)(opt->value) = gLoopbackState;      err = gEndpt->OptionManagement(&optReq, &optReq); ``` | |

#### [Apr 07 1997]

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

---
