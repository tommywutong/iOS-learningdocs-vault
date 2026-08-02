---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/ICADevices.html
archived_at: '2026-07-18T02:54:28.417352Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# ICADevices Changes

## ICADevices

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

ICADevices.hAdded ICARawFileHeaderAdded ICDAddBandInfoToNotificationDictionary()Added ICDCreateColorSpace()Added ICLoggingEnabledAdded ICLoggingLevelBasicInfoAdded ICLoggingLevelErrorAdded ICLoggingLevelMaskAdded ICLoggingLevelTimingInfoAdded ICLoggingLevelVerboseInfoAdded ICLoggingLevelWarningICD_CameraCalls.hAdded addedAfterCCCMaskAdded fileInTempCacheMaskAdded largeFileSizeMaskModified ICDInitiateNotificationCallback()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified ICDCreateICAThumbnailFromICNS()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICDStatusChanged()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.3 |

Modified ICDCreateICAThumbnailFromIconRef()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

ICD_ScannerCalls.hModified ICDScannerCreateICAThumbnailFromICNS()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICDScannerInitiateNotificationCallback()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

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
