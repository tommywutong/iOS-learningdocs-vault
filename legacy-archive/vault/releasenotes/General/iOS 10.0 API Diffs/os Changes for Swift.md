---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/os.html
archived_at: '2026-07-18T02:55:46.878430Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# os Changes for Swift

### os

Removed OS_OBJECT_HAVE_OBJC_SUPPORTRemoved OS_OBJECT_USE_OBJCRemoved OS_OBJECT_USE_OBJC_RETAIN_RELEASERemoved [os_release(_: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/os/1524245-os_release)Removed [os_retain(_: UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>](https://developer.apple.com/documentation/os/1524246-os_retain)Added [OSLog](https://developer.apple.com/documentation/os/oslog)Added [OSLog.default](https://developer.apple.com/documentation/os/oslog/2320724-default)Added [OSLog.init(__subsystem: UnsafePointer<Int8>, category: UnsafePointer<Int8>)](https://developer.apple.com/documentation/os/oslog/1643744-init)Added [OSLog.init(subsystem: String, category: String)](https://developer.apple.com/documentation/os/oslog/2320726-init)Added [OSLog.isEnabled(type: OSLogType) -> Bool](https://developer.apple.com/documentation/os/1643749-os_log_type_enabled)Added [OSLogType [struct]](https://developer.apple.com/documentation/os/oslogtype)Added [OSLogType.debug](https://developer.apple.com/documentation/os/oslogtype/2320717-debug)Added [OSLogType.default](https://developer.apple.com/documentation/os/oslogtype/2320721-default)Added [OSLogType.error](https://developer.apple.com/documentation/os/oslogtype/2320727-error)Added [OSLogType.fault](https://developer.apple.com/documentation/os/oslogtype/2320725-fault)Added [OSLogType.info](https://developer.apple.com/documentation/os/oslogtype/2320719-info)Added [OSLogType.init(_: UInt8)](https://developer.apple.com/documentation/os/oslogtype/2320716-init)Added [OSLogType.init(rawValue: UInt8)](https://developer.apple.com/documentation/os/oslogtype/2320722-init)Added [OSLogType.rawValue](https://developer.apple.com/documentation/os/oslogtype/2320723-rawvalue)Added [os_log(_: StaticString, dso: UnsafeRawPointer?, log: OSLog, type: OSLogType, _: CVarArg)](https://developer.apple.com/documentation/os/2320718-os_log)Added [os_trace_debug_enabled() -> Bool](https://developer.apple.com/documentation/os/1588724-os_trace_debug_enabled)Added [os_trace_info_enabled() -> Bool](https://developer.apple.com/documentation/os/1645631-os_trace_info_enabled)Added [OS_TRACE_TYPE_DEBUG](https://developer.apple.com/documentation/os/os_trace_type_debug)Added [os_trace_type_enabled(_: UInt8) -> Bool](https://developer.apple.com/documentation/os/1645627-os_trace_type_enabled)Added [OS_TRACE_TYPE_INFO](https://developer.apple.com/documentation/os/os_trace_type_info)Added [OS_TRACE_TYPE_RELEASE](https://developer.apple.com/documentation/os/os_trace_type_release)Added [xpc_object_t](https://developer.apple.com/documentation/xpc/xpc_object_t)

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
