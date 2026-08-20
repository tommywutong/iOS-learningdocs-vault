---
title: Greenwich Mean Time offsets and the Map control panel
apple_id: DTS10001505
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-05-17'
source_url: https://developer.apple.com/library/archive/qa/ops/ops24.html
archived_at: '2026-07-18T02:29:50.172403Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A OPS24Greenwich Mean Time offsets and the Map control panel |

|  |  |  |  |
| --- | --- | --- | --- |
| ---   Q: Is there a way to read Greenwich Mean Time offsets from the Map control panel?  A: There's actually a system-level call to find out where you are. It's a Script Manager call named `ReadLocation` (used by the Map control panel), which returns a structure giving you all the information you need. Here's a description of the call, copied from MPW 411:   |  | | --- | | ``` pascal void ReadLocation(MachineLocation *loc)   = {0x205F,0x203C,0x000C,0x00E4,0xA051};  File {CIncludes}script.h ```   In C:   ``` pascal void ReadLocation(MachineLocation *loc); pascal void WriteLocation(const MachineLocation *loc);                    ``` |   These routines access the stored geographic location and time zone information for the Macintosh from parameter RAM. For example, the time zone information can be used to derive the absolute time (GMT) that a document or mail message was created. With this information, when the document is received across time zones, the creation date and time are correct. Otherwise, documents can appear to be created after they're read. (For example, someone could create a message in Tokyo on Tuesday and send it to Cupertino, where it's received and read on Monday.) Geographic information can also be used by applications that require it.  The `gmtDelta` field represents the current offset (in seconds) from Universal (Greenwich Mean) Time to the current time on the Macintosh. So, if the current Macintosh time is 1:00 AM and current GMT is 2:00 AM, then `gmtDelta` should be -3600, since the current time is one hour (3600 seconds) less than GMT. The `gmtDelta` field is a signed three-byte value.  The high bit (bit 7) of the `dlsDelta` field represents the current state of daylight savings time. If daylight savings time is in effect, then bit 7 of `dlsDelta` is set; if daylight savings time is not in effect, then bit 7 is clear. The other 7 bits (bits 0 through 6) of `dlsDelta` are reserved for future use by Apple. (This was defined for the release of AOCE; the daylight savings time checkbox in the System 7 Pro Date & Time control panel uses these semantics as do several other utilities.)  The value in `gmtDelta` always represents current offset from GMT, regardless of the setting in `dlsDelta`; GMT can always be calculated by subtracting `gmtDelta` from the current time. That means that during daylight savings time, the value in `gmtDelta` will be different from the value during standard time.  If the `MachineLocation` has never been set, it should be <0,0,0>. The top byte of the `gmtDelta` should be masked off and preserved when writing: it's reserved for future extension. The `gmtDelta` is in seconds east of GMT; for example, San Francisco is at minus 28,800 seconds (8 hours \* 3600 seconds per hour). The latitude and longitude are in fractions of a great circle, giving them accuracy to within less than a foot, which should be sufficient for most purposes. For example, `Fract` values of 1.0 = 90deg., -1.0 = -90deg., and -2.0 = -180deg.  In C:   |  | | --- | | ``` struct MachineLocation {   Fract latitude;   Fract longitude;   union {     char  dlsDelta;  /*signed byte; daylight savings delta*/     long  gmtDelta;  /*must mask - see documentation*/   }  gmtFlags; };                    ``` |   The `gmtDelta` is really a three-byte value, so you must take care to get and set it properly, as in the following C code examples:   |  | | --- | | ``` long GetGmtDelta(MachineLocation myLocation) {   long  internalGMTDelta;   internalGMTDelta = myLocation.gmtDelta & 0x00ffffff;     if ( (internalGMTDelta >> 23) & 1 )  // need to sign extend       internalGmtDelta = internalGmtDelta | 0xff000000;     return(internalGmtDelta); }  void SetGmtDelta(MachineLocation *myLocation, long myGmtDelta) {   char  tempSignedByte;   tempSignedByte = myLocation->dlsDelta;   myLocation->gmtDelta = myGmtDelta;   myLocation->dlsDelta = tempSignedByte; }                    ``` |  Updated: 17-May-1999 |

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
