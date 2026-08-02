---
title: Adding dependencies with kmodload
apple_id: DTS10001646
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-12-05'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1097.html
archived_at: '2026-07-18T02:38:13.645665Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Darwin](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxDarwin-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Darwin > Hardware & Drivers](https://developer.apple.com/referencelibrary/Darwin/idxHardwareDrivers-date.html)

|  |
| --- |
| Technical Q&A QA1097Adding dependencies with kmodload |

|  |  |  |  |
| --- | --- | --- | --- |
| ---   Q: When using `kmodload`, why do I get a "Can't find superclass" error?  A: You may see an error similar to Listing 1 if your KEXT uses classes from other I/O Kit families.   |  | | --- | | ``` kmodload: Can't find superclass for _13AppleUSBMouse : _12IOHIPointing ``` | | __Listing 1__. kmodload error |     This error can be eliminated by specifying your dependencies using the `-d` option. For example...     |  | | --- | | ``` kmodload -o AppleUSBMouse.sym -d IOHIDSystem.kext/Contents/MacOS/IOHIDSystem ``` |   If you depend on more than one I/O Kit family, use multiple `-d` arguments, one for each family. Remember, you should only use `kmodload` when creating symbol files for use with 2-machine debugging. Otherwise, use `kextload`.   ---  [Dec 05 2001] |

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
