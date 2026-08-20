---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/XPC.html
archived_at: '2026-07-18T02:53:55.290037Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# XPC Changes for Swift

### XPC

Modified [xpc_array_get_array(_: xpc_object_t, _: Int) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505537-xpc_array_get_array)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_array_get_array(_ `self`: xpc_object_t, _ index: Int) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_array_get_array(_ self: xpc_object_t, _ index: Int) -> xpc_object_t! ``` |

Modified [xpc_array_get_dictionary(_: xpc_object_t, _: Int) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505954-xpc_array_get_dictionary)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_array_get_dictionary(_ `self`: xpc_object_t, _ index: Int) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_array_get_dictionary(_ self: xpc_object_t, _ index: Int) -> xpc_object_t! ``` |

Modified [xpc_dictionary_get_array(_: xpc_object_t, _: UnsafePointer<Int8>) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505498-xpc_dictionary_get_array)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_get_array(_ `self`: xpc_object_t, _ key: UnsafePointer<Int8>) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_dictionary_get_array(_ self: xpc_object_t, _ key: UnsafePointer<Int8>) -> xpc_object_t! ``` |

Modified [xpc_dictionary_get_dictionary(_: xpc_object_t, _: UnsafePointer<Int8>) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505379-xpc_dictionary_get_dictionary)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_get_dictionary(_ `self`: xpc_object_t, _ key: UnsafePointer<Int8>) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_dictionary_get_dictionary(_ self: xpc_object_t, _ key: UnsafePointer<Int8>) -> xpc_object_t! ``` |

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
