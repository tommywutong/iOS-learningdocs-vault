---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Swift/XPC.html
archived_at: '2026-07-18T02:51:47.993654Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


# XPC Changes for Swift

### XPC

Modified [xpc_activity_register(_: UnsafePointer<Int8>, _: xpc_object_t, _: XPC.xpc_activity_handler_t)](https://developer.apple.com/documentation/xpc/1495824-xpc_activity_register)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_activity_register(_ identifier: UnsafePointer<Int8>, _ criteria: xpc_object_t, _ handler: XPC.xpc_activity_handler_t) ``` |
| To | ``` func xpc_activity_register(_ identifier: UnsafePointer<Int8>, _ criteria: xpc_object_t, _ handler: @escaping XPC.xpc_activity_handler_t) ``` |

Modified [xpc_array_apply(_: xpc_object_t, _: XPC.xpc_array_applier_t) -> Bool](https://developer.apple.com/documentation/xpc/1505727-xpc_array_apply)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_array_apply(_ xarray: xpc_object_t, _ applier: XPC.xpc_array_applier_t) -> Bool ``` |
| To | ``` func xpc_array_apply(_ xarray: xpc_object_t, _ applier: @escaping XPC.xpc_array_applier_t) -> Bool ``` |

Modified [xpc_connection_send_message_with_reply(_: xpc_connection_t, _: xpc_object_t, _: DispatchQueue?, _: XPC.xpc_handler_t)](https://developer.apple.com/documentation/xpc/1448795-xpc_connection_send_message_with)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_send_message_with_reply(_ connection: xpc_connection_t, _ message: xpc_object_t, _ replyq: DispatchQueue?, _ handler: XPC.xpc_handler_t) ``` |
| To | ``` func xpc_connection_send_message_with_reply(_ connection: xpc_connection_t, _ message: xpc_object_t, _ replyq: DispatchQueue?, _ handler: @escaping XPC.xpc_handler_t) ``` |

Modified [xpc_connection_set_event_handler(_: xpc_connection_t, _: XPC.xpc_handler_t)](https://developer.apple.com/documentation/xpc/1448805-xpc_connection_set_event_handler)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_set_event_handler(_ connection: xpc_connection_t, _ handler: XPC.xpc_handler_t) ``` |
| To | ``` func xpc_connection_set_event_handler(_ connection: xpc_connection_t, _ handler: @escaping XPC.xpc_handler_t) ``` |

Modified [xpc_dictionary_apply(_: xpc_object_t, _: XPC.xpc_dictionary_applier_t) -> Bool](https://developer.apple.com/documentation/xpc/1505404-xpc_dictionary_apply)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_apply(_ xdict: xpc_object_t, _ applier: XPC.xpc_dictionary_applier_t) -> Bool ``` |
| To | ``` func xpc_dictionary_apply(_ xdict: xpc_object_t, _ applier: @escaping XPC.xpc_dictionary_applier_t) -> Bool ``` |

Modified [xpc_main(_: XPC.xpc_connection_handler_t) -> Never](https://developer.apple.com/documentation/xpc/1505740-xpc_main)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_main(_ handler: XPC.xpc_connection_handler_t) -> Never ``` |
| To | ``` func xpc_main(_ handler: @escaping XPC.xpc_connection_handler_t) -> Never ``` |

Modified [xpc_set_event_stream_handler(_: UnsafePointer<Int8>, _: DispatchQueue?, _: XPC.xpc_handler_t)](https://developer.apple.com/documentation/xpc/1505578-xpc_set_event_stream_handler)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_set_event_stream_handler(_ stream: UnsafePointer<Int8>, _ targetq: DispatchQueue?, _ handler: XPC.xpc_handler_t) ``` |
| To | ``` func xpc_set_event_stream_handler(_ stream: UnsafePointer<Int8>, _ targetq: DispatchQueue?, _ handler: @escaping XPC.xpc_handler_t) ``` |

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
