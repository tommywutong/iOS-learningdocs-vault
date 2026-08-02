---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/CoreFoundation.html
archived_at: '2026-07-18T02:54:11.225280Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# CoreFoundation Changes

## CoreFoundation

CFAvailability.hModified #def CF_AVAILABLE_IOS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_DEPRECATED_IOS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_AVAILABLE

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_AVAILABLE_IOS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_AVAILABLE_MAC

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_DEPRECATED

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_DEPRECATED_IOS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_DEPRECATED_MAC

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_OPTIONS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

CFBase.hAdded [CFAutorelease()](https://developer.apple.com/documentation/corefoundation/1521271-cfautorelease)Added [#def kCFCoreFoundationVersionNumber10_7_5](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_7_5)Added [#def kCFCoreFoundationVersionNumber10_8](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_8)Added [#def kCFCoreFoundationVersionNumber10_8_1](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_8_1)Added [#def kCFCoreFoundationVersionNumber10_8_2](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_8_2)Added [#def kCFCoreFoundationVersionNumber10_8_3](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_8_3)Added [#def kCFCoreFoundationVersionNumber10_8_4](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_8_4)Modified #def CF_AVAILABLE_IOS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_DEPRECATED_IOS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_AVAILABLE

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_AVAILABLE_IOS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_AVAILABLE_MAC

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_DEPRECATED

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_DEPRECATED_IOS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_ENUM_DEPRECATED_MAC

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

Modified #def CF_OPTIONS

|  | Header |
| --- | --- |
| From | CoreFoundation/CFBase.h |
| To | CoreFoundation/CFAvailability.h |

CFDate.hAdded #def CF_CALENDAR_DEPRECATEDAdded #def CF_CALENDAR_ENUM_DEPRECATEDCFFileSecurity.hAdded [CFFileSecurityClearOptions](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions)Modified [CFFileSecurityClearProperties()](https://developer.apple.com/documentation/corefoundation/1426500-cffilesecurityclearproperties)

|  | Declaration |
| --- | --- |
| From | Boolean CFFileSecurityClearProperties ( CFFileSecurityRef fileSec, CFOptionFlags clearPropertyMask); |
| To | Boolean CFFileSecurityClearProperties ( CFFileSecurityRef fileSec, CFFileSecurityClearOptions clearPropertyMask); |

CFPreferences.hModified [CFPreferencesCopyApplicationList()](https://developer.apple.com/documentation/corefoundation/1515523-cfpreferencescopyapplicationlist)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

CFRunLoop.hAdded [CFRunLoopTimerGetTolerance()](https://developer.apple.com/documentation/corefoundation/1543275-cfrunlooptimergettolerance)Added [CFRunLoopTimerSetTolerance()](https://developer.apple.com/documentation/corefoundation/1542980-cfrunlooptimersettolerance)CFStream.hAdded [CFReadStreamCopyDispatchQueue()](https://developer.apple.com/documentation/corefoundation/1539632-cfreadstreamcopydispatchqueue)Added [CFReadStreamSetDispatchQueue()](https://developer.apple.com/documentation/corefoundation/1539688-cfreadstreamsetdispatchqueue)Added [CFWriteStreamCopyDispatchQueue()](https://developer.apple.com/documentation/corefoundation/1539741-cfwritestreamcopydispatchqueue)Added [CFWriteStreamSetDispatchQueue()](https://developer.apple.com/documentation/corefoundation/1539656-cfwritestreamsetdispatchqueue)CFString.hModified [CFStringFold()](https://developer.apple.com/documentation/corefoundation/1542031-cfstringfold)

|  | Declaration |
| --- | --- |
| From | void CFStringFold ( CFMutableStringRef theString, CFOptionFlags theFlags, CFLocaleRef theLocale); |
| To | void CFStringFold ( CFMutableStringRef theString, CFStringCompareFlags theFlags, CFLocaleRef theLocale); |

CFURL.hAdded [CFURLIsFileReferenceURL()](https://developer.apple.com/documentation/corefoundation/1543161-cfurlisfilereferenceurl)Added [kCFURLTagNamesKey](https://developer.apple.com/documentation/corefoundation/kcfurltagnameskey)Added [kCFURLUbiquitousItemDownloadingErrorKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemdownloadingerrorkey)Added [kCFURLUbiquitousItemDownloadingStatusCurrent](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemdownloadingstatuscurrent)Added [kCFURLUbiquitousItemDownloadingStatusDownloaded](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemdownloadingstatusdownloaded)Added [kCFURLUbiquitousItemDownloadingStatusKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemdownloadingstatuskey)Added [kCFURLUbiquitousItemDownloadingStatusNotDownloaded](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemdownloadingstatusnotdownloaded)Added [kCFURLUbiquitousItemUploadingErrorKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemuploadingerrorkey)Modified [CFURLCreateFromFSRef()](https://developer.apple.com/documentation/corefoundation/1584385-cfurlcreatefromfsref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CFURLGetFSRef()](https://developer.apple.com/documentation/corefoundation/1584387-cfurlgetfsref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [kCFURLBookmarkCreationPreferFileIDResolutionMask](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions/kcfurlbookmarkcreationpreferfileidresolutionmask)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [kCFURLHFSPathStyle](https://developer.apple.com/documentation/corefoundation/cfurlpathstyle/kcfurlhfspathstyle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [kCFURLUbiquitousItemIsDownloadedKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemisdownloadedkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

CFURLAccess.hModified [CFURLCreateDataAndPropertiesFromResource()](https://developer.apple.com/documentation/corefoundation/1420742-cfurlcreatedataandpropertiesfrom)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CFURLCreatePropertyFromResource()](https://developer.apple.com/documentation/corefoundation/1420715-cfurlcreatepropertyfromresource)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CFURLDestroyResource()](https://developer.apple.com/documentation/corefoundation/1420709-cfurldestroyresource)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CFURLWriteDataAndPropertiesToResource()](https://developer.apple.com/documentation/corefoundation/1420723-cfurlwritedataandpropertiestores)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [kCFURLFileDirectoryContents](https://developer.apple.com/documentation/corefoundation/kcfurlfiledirectorycontents)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [kCFURLFileExists](https://developer.apple.com/documentation/corefoundation/kcfurlfileexists)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [kCFURLFileLastModificationTime](https://developer.apple.com/documentation/corefoundation/kcfurlfilelastmodificationtime)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [kCFURLFileLength](https://developer.apple.com/documentation/corefoundation/kcfurlfilelength)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [kCFURLFileOwnerID](https://developer.apple.com/documentation/corefoundation/kcfurlfileownerid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [kCFURLFilePOSIXMode](https://developer.apple.com/documentation/corefoundation/kcfurlfileposixmode)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [kCFURLHTTPStatusCode](https://developer.apple.com/documentation/corefoundation/kcfurlhttpstatuscode)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [kCFURLHTTPStatusLine](https://developer.apple.com/documentation/corefoundation/kcfurlhttpstatusline)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

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
