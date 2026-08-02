---
title: The package does not contain an Info.plist
apple_id: DTS40016315
resource_type: QA
platform: iOS|Xcode Developer Tools|macOS
topic: General
technology: null
published: '2015-07-14'
source_url: https://developer.apple.com/library/archive/qa/qa1273/_index.html
archived_at: '2026-07-18T02:30:19.338739Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1273

# The package does not contain an Info.plist

## Q:  Xcode displays an "The package does not contain an Info.plist" message when validating or submitting my app. How do I fix it?

A: Note

If you are getting this message while submitting a hosted In-App Purchase product, see [I am unable to upload my hosted content to iTunes Connect with Xcode 6](https://developer.apple.com/library/ios/technotes/tn2413/_index.html#//apple_ref/doc/uid/DTS40016228-CH1-SUBSCRIPTIONS-I_AM_UNABLE_TO_UPLOAD_MY_HOSTED_CONTENT_TO_ITUNES_CONNECT_WITH_XCODE_6) for details on how to resolve it.

You may be getting this message for one or more of the following reasons:

- Your app's Info.plist file does not contain a CFBundlePackageType (Bundle OS Type code) key, which specifies the type of bundle being created. Add this key to your Info.plist, then set it to `APPL` to resolve your issue as shown in Figure 1. See [CFBundlePackageType](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/TP40009249-111321-TPXREF112) for more information.

__Figure 1__  Setting CFBundlePackageType to APPL

!!

- Your app's Info.plist does not contain a [CFBundleVersion](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/TP40009249-102364-TPXREF106) (Bundle version) key or a [CFBundleShortVersionString](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/TP40009249-111349-TPXREF113) (Bundle versions string, short) key. Your app must provide and set both of these keys. See [Setting the Version Number and Build String](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/ConfiguringYourApp/ConfiguringYourApp.html#//apple_ref/doc/uid/TP40012582-CH28-SW18) for more information.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-07-14 | New document that describes how to resolve the "The package does not contain an Info.plist" error message. |

