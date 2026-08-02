---
title: How to get the Monitor ID as displayed in the Monitors & Sound Control Panel
apple_id: DTS10001908
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-01-16'
source_url: https://developer.apple.com/library/archive/qa/qd/qd55.html
archived_at: '2026-07-18T02:38:38.413200Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A QD55How to get the Monitor ID as displayed in the Monitors & Sound Control Panel |

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ---   Q: I am trying to use the Display Manager call `DMGetDisplayIDByGDevice()` to get the monitor ID as displayed in the Monitors & Sound Control Panel when a user presses the "Identify Monitors" button. Unfortunately, `DMGetDisplayIDByGDevice()` does not seem to return this value. How do I get the actual monitor ID number?  A: There is a call defined in `Displays.h` that is not described in the Display Manager documentation that you should use. Essentially, what you want to do is use `DMGetDisplayIDByGDevice` to get the `displayID`, and then use the `DMGetNameByAVID` with that `displayID` to get the "name" of the device. The "name" is a string containing the device name (e.g., Multiple Scan Display) and the device number (e.g., 1). The device number is the number that appears in the Monitors & Sound Control Panel. To obtain just the device number, or monitor ID, use masks to retrieve just that section of the name. For example:   |  | | --- | | ``` err = DMGetDisplayIDByGDevice(gd, &displayID, false); err = DMGetNameByAVID(displayID, kSuppressNameMask + kForceNumberMask, &theStr); ``` |   Keep in mind, these calls work with Display Manager 2.0. To use these calls on systems with Display Manager 1.0, you need to ensure that you user has the Display Enabler installed. The Display Enabler is included with the Display Manager SDK. You will find the Display Manager SDK [here](https://developer.apple.com/sdk/index.html) or on the MacOS SDK CD.  More specifics on the call `DMGetNameByAVID` To determine the "name" and/or device number of the requested device, use the `DMGetNameByAVID` function.   |  | | --- | | ``` extern pascal OSErr DMGetNameByAVID             (AVIDType theID, unsigned long nameFlags, Str255 *name) ``` |  |  |  | | --- | --- | | `theID` | AVIDType is an ID for ports and devices. The old Display ID type is carried on for compatibility . Basically, theID is the displayID for the video device whose GDevice record you wish to obtain. |     |  |  |  | | --- | --- | --- | | `nameFlags` | |  | | --- | | ``` enum {         /* bits for nameFlags */         kSuppressNumberBit      = 0,         kSuppressNumberMask     = 1,         kForceNumberBit         = 1,         kForceNumberMask        = 2,         kSuppressNameBit        = 2,         kSuppressNameMask       = 4     }; ``` | |     |  |  | | --- | --- | | __\*name__ | \*name is a string containing the device name, i.e.,, Multiple Scan Display and device number, the order for which the device appears in the device tree. |    To obtain a section of the "name," use the `nameFlags` parameter.  To obtain just the name, i.e., Multiple Scan Display, use the flag `kSuppressNumberMask` in the `nameFlags` parameter.   |  | | --- | | ```      err = DMGetNameByAVID(displayID, kSuppressNumberMask, &nameStr); ``` |   To obtain just the number, use the `kSuppressNameMask` + `kForceNumberMask` masks.   |  | | --- | | ```      err = DMGetNameByAVID(displayID, kSuppressNameMask + kForceNumberMask,         &numberStr); ``` |   To obtain both in the same string, use the `kForceNumberMask` flag.   |  | | --- | | ```      err = DMGetNameByAVID(displayID, kForceNumberMask, &nameStr);     ``` | |

#### [Jan 16 2003]

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
