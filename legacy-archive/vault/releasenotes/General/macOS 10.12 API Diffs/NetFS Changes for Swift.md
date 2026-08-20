---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/NetFS.html
archived_at: '2026-07-18T02:51:30.501360Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# NetFS Changes for Swift

### NetFS

Added kNetFSOpenURLMountKeyModified AsyncRequestID

|  | Declaration |
| --- | --- |
| From | ``` typealias AsyncRequestID = UnsafeMutablePointer<Void> ``` |
| To | ``` typealias AsyncRequestID = UnsafeMutableRawPointer ``` |

Modified NetFSMountURLAsync(_: CFURL!, _: CFURL!, _: CFString!, _: CFString!, _: CFMutableDictionary!, _: CFMutableDictionary!, _: UnsafeMutablePointer<AsyncRequestID?>!, _: DispatchQueue!, _: NetFS.NetFSMountURLBlock!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func NetFSMountURLAsync(_ url: CFURL!, _ mountpath: CFURL!, _ user: CFString!, _ passwd: CFString!, _ open_options: CFMutableDictionary!, _ mount_options: CFMutableDictionary!, _ requestID: UnsafeMutablePointer<AsyncRequestID>, _ dispatchq: dispatch_queue_t!, _ mount_report: NetFSMountURLBlock!) -> Int32 ``` |
| To | ``` func NetFSMountURLAsync(_ url: CFURL!, _ mountpath: CFURL!, _ user: CFString!, _ passwd: CFString!, _ open_options: CFMutableDictionary!, _ mount_options: CFMutableDictionary!, _ requestID: UnsafeMutablePointer<AsyncRequestID?>!, _ dispatchq: DispatchQueue!, _ mount_report: NetFS.NetFSMountURLBlock!) -> Int32 ``` |

Modified NetFSMountURLBlock

|  | Declaration |
| --- | --- |
| From | ``` typealias NetFSMountURLBlock = (Int32, AsyncRequestID, CFArray!) -> Void ``` |
| To | ``` typealias NetFSMountURLBlock = (Int32, AsyncRequestID?, CFArray?) -> Swift.Void ``` |

Modified NetFSMountURLCancel(_: AsyncRequestID!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func NetFSMountURLCancel(_ requestID: AsyncRequestID) -> Int32 ``` |
| To | ``` func NetFSMountURLCancel(_ requestID: AsyncRequestID!) -> Int32 ``` |

Modified NetFSMountURLSync(_: CFURL!, _: CFURL!, _: CFString!, _: CFString!, _: CFMutableDictionary!, _: CFMutableDictionary!, _: UnsafeMutablePointer<Unmanaged<CFArray>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func NetFSMountURLSync(_ url: CFURL!, _ mountpath: CFURL!, _ user: CFString!, _ passwd: CFString!, _ open_options: CFMutableDictionary!, _ mount_options: CFMutableDictionary!, _ mountpoints: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> Int32 ``` |
| To | ``` func NetFSMountURLSync(_ url: CFURL!, _ mountpath: CFURL!, _ user: CFString!, _ passwd: CFString!, _ open_options: CFMutableDictionary!, _ mount_options: CFMutableDictionary!, _ mountpoints: UnsafeMutablePointer<Unmanaged<CFArray>?>!) -> Int32 ``` |

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
