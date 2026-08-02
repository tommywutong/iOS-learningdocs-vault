---
title: Endian Concerns When Playing 'snd ' Resources
apple_id: DTS10002165
resource_type: QA
platform: macOS
topic: Cross Platform
technology: null
published: '1999-11-08'
source_url: https://developer.apple.com/library/archive/qa/qtw/qtw97.html
archived_at: '2026-07-18T02:38:53.343818Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > QuickTime for Windows](https://developer.apple.com/referencelibrary/QuickTime/idxQuickTimeforWindows-date.html)

|  |
| --- |
| Technical Q&A QTW97Endian Concerns When Playing 'snd ' Resources |

|  |
| --- |
| ---   Q: Do I need to byte-swap a `'snd '` resource before passing it to the Sound Manager `SndPlay` function on Windows in order for it to play correctly? Currently I'm reading the resource into memory myself.  A: No, you don't, providing you use the Resource Manager functions to read in the resource.  Standard Macintosh `'snd '` resources are big-endian on disk, and native-endian in RAM (like virtually all other resources). It is the responsibility of the Resource Manager to do the necessary flipping. The Sound Manager assumes all `'snd '` resources come into RAM via calls to Resource Manager functions like `GetResource`. If you read the resource into memory yourself, you have bypassed this mechanism, and you will end up with a non native-endian `'snd '` resource. Since the QuickTime & Sound Manager API's assume the `'snd '` resource is native-endian (little-endian in this case), they are getting very confused.  The easy way to solve this is to use the Resource Manager functions to read in the resource. The hard way is to parse through the resource (make sure you know about all the possible variants!) and flip the bytes yourself. [Nov 08 1999] |

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
