---
title: watchOS 2.1 API Diffs
apple_id: TP40016636
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS21APIDiffs/Swift/Dispatch.html
archived_at: '2026-07-18T02:58:08.356191Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 2.1 API Diffs](watchOS%202.0%20to%20watchOS%202.1%20API%20Differences.md)


# Dispatch Changes for Swift

### Dispatch

Modified [dispatch_block_flags_t [struct]](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct dispatch_block_flags_t : RawRepresentable {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     var rawValue: UInt } ``` | RawRepresentable |
| To | ``` struct dispatch_block_flags_t : RawRepresentable, Equatable {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     var rawValue: UInt } ``` | Equatable, RawRepresentable |

Modified [OS_dispatch_data](https://developer.apple.com/documentation/dispatch/os_dispatch_data)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol OS_dispatch_data : OS_dispatch_object, NSObjectProtocol { } ``` | NSObjectProtocol, OS_dispatch_object |
| To | ``` protocol OS_dispatch_data : OS_dispatch_object { } ``` | OS_dispatch_object |

Modified [OS_dispatch_group](https://developer.apple.com/documentation/dispatch/os_dispatch_group)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol OS_dispatch_group : OS_dispatch_object, NSObjectProtocol { } ``` | NSObjectProtocol, OS_dispatch_object |
| To | ``` protocol OS_dispatch_group : OS_dispatch_object { } ``` | OS_dispatch_object |

Modified [OS_dispatch_io](https://developer.apple.com/documentation/dispatch/os_dispatch_io)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol OS_dispatch_io : OS_dispatch_object, NSObjectProtocol { } ``` | NSObjectProtocol, OS_dispatch_object |
| To | ``` protocol OS_dispatch_io : OS_dispatch_object { } ``` | OS_dispatch_object |

Modified [OS_dispatch_queue](https://developer.apple.com/documentation/dispatch/os_dispatch_queue)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol OS_dispatch_queue : OS_dispatch_object, NSObjectProtocol { } ``` | NSObjectProtocol, OS_dispatch_object |
| To | ``` protocol OS_dispatch_queue : OS_dispatch_object { } ``` | OS_dispatch_object |

Modified [OS_dispatch_queue_attr](https://developer.apple.com/documentation/dispatch/os_dispatch_queue_attr)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol OS_dispatch_queue_attr : OS_dispatch_object, NSObjectProtocol { } ``` | NSObjectProtocol, OS_dispatch_object |
| To | ``` protocol OS_dispatch_queue_attr : OS_dispatch_object { } ``` | OS_dispatch_object |

Modified [OS_dispatch_semaphore](https://developer.apple.com/documentation/dispatch/os_dispatch_semaphore)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol OS_dispatch_semaphore : OS_dispatch_object, NSObjectProtocol { } ``` | NSObjectProtocol, OS_dispatch_object |
| To | ``` protocol OS_dispatch_semaphore : OS_dispatch_object { } ``` | OS_dispatch_object |

Modified [OS_dispatch_source](https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol OS_dispatch_source : OS_dispatch_object, NSObjectProtocol { } ``` | NSObjectProtocol, OS_dispatch_object |
| To | ``` protocol OS_dispatch_source : OS_dispatch_object { } ``` | OS_dispatch_object |

Modified DISPATCH_CURRENT_QUEUE_LABEL

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_CURRENT_QUEUE_LABEL: dispatch_queue_t! ``` |
| To | ``` var DISPATCH_CURRENT_QUEUE_LABEL: dispatch_queue_t! { get } ``` |

Modified DISPATCH_IO_RANDOM

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_IO_RANDOM: dispatch_io_type_t ``` |
| To | ``` var DISPATCH_IO_RANDOM: dispatch_io_type_t { get } ``` |

Modified DISPATCH_IO_STOP

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_IO_STOP: dispatch_io_close_flags_t ``` |
| To | ``` var DISPATCH_IO_STOP: dispatch_io_close_flags_t { get } ``` |

Modified DISPATCH_IO_STREAM

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_IO_STREAM: dispatch_io_type_t ``` |
| To | ``` var DISPATCH_IO_STREAM: dispatch_io_type_t { get } ``` |

Modified DISPATCH_IO_STRICT_INTERVAL

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_IO_STRICT_INTERVAL: dispatch_io_interval_flags_t ``` |
| To | ``` var DISPATCH_IO_STRICT_INTERVAL: dispatch_io_interval_flags_t { get } ``` |

Modified DISPATCH_MACH_SEND_DEAD

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_MACH_SEND_DEAD: dispatch_source_mach_send_flags_t ``` |
| To | ``` var DISPATCH_MACH_SEND_DEAD: dispatch_source_mach_send_flags_t { get } ``` |

Modified DISPATCH_MEMORYPRESSURE_CRITICAL

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_MEMORYPRESSURE_CRITICAL: dispatch_source_memorypressure_flags_t ``` |
| To | ``` var DISPATCH_MEMORYPRESSURE_CRITICAL: dispatch_source_memorypressure_flags_t { get } ``` |

Modified DISPATCH_MEMORYPRESSURE_NORMAL

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_MEMORYPRESSURE_NORMAL: dispatch_source_memorypressure_flags_t ``` |
| To | ``` var DISPATCH_MEMORYPRESSURE_NORMAL: dispatch_source_memorypressure_flags_t { get } ``` |

Modified DISPATCH_MEMORYPRESSURE_WARN

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_MEMORYPRESSURE_WARN: dispatch_source_memorypressure_flags_t ``` |
| To | ``` var DISPATCH_MEMORYPRESSURE_WARN: dispatch_source_memorypressure_flags_t { get } ``` |

Modified DISPATCH_PROC_EXEC

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_PROC_EXEC: dispatch_source_proc_flags_t ``` |
| To | ``` var DISPATCH_PROC_EXEC: dispatch_source_proc_flags_t { get } ``` |

Modified DISPATCH_PROC_EXIT

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_PROC_EXIT: dispatch_source_proc_flags_t ``` |
| To | ``` var DISPATCH_PROC_EXIT: dispatch_source_proc_flags_t { get } ``` |

Modified DISPATCH_PROC_FORK

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_PROC_FORK: dispatch_source_proc_flags_t ``` |
| To | ``` var DISPATCH_PROC_FORK: dispatch_source_proc_flags_t { get } ``` |

Modified DISPATCH_PROC_SIGNAL

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_PROC_SIGNAL: dispatch_source_proc_flags_t ``` |
| To | ``` var DISPATCH_PROC_SIGNAL: dispatch_source_proc_flags_t { get } ``` |

Modified DISPATCH_QUEUE_PRIORITY_BACKGROUND

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_QUEUE_PRIORITY_BACKGROUND: dispatch_queue_priority_t ``` |
| To | ``` var DISPATCH_QUEUE_PRIORITY_BACKGROUND: dispatch_queue_priority_t { get } ``` |

Modified DISPATCH_QUEUE_PRIORITY_DEFAULT

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_QUEUE_PRIORITY_DEFAULT: dispatch_queue_priority_t ``` |
| To | ``` var DISPATCH_QUEUE_PRIORITY_DEFAULT: dispatch_queue_priority_t { get } ``` |

Modified DISPATCH_QUEUE_PRIORITY_HIGH

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_QUEUE_PRIORITY_HIGH: dispatch_queue_priority_t ``` |
| To | ``` var DISPATCH_QUEUE_PRIORITY_HIGH: dispatch_queue_priority_t { get } ``` |

Modified DISPATCH_QUEUE_PRIORITY_LOW

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_QUEUE_PRIORITY_LOW: dispatch_queue_priority_t ``` |
| To | ``` var DISPATCH_QUEUE_PRIORITY_LOW: dispatch_queue_priority_t { get } ``` |

Modified DISPATCH_QUEUE_SERIAL

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_QUEUE_SERIAL: dispatch_queue_attr_t! ``` |
| To | ``` var DISPATCH_QUEUE_SERIAL: dispatch_queue_attr_t! { get } ``` |

Modified DISPATCH_TARGET_QUEUE_DEFAULT

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_TARGET_QUEUE_DEFAULT: dispatch_queue_t! ``` |
| To | ``` var DISPATCH_TARGET_QUEUE_DEFAULT: dispatch_queue_t! { get } ``` |

Modified DISPATCH_TIMER_STRICT

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_TIMER_STRICT: dispatch_source_timer_flags_t ``` |
| To | ``` var DISPATCH_TIMER_STRICT: dispatch_source_timer_flags_t { get } ``` |

Modified DISPATCH_VNODE_ATTRIB

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_VNODE_ATTRIB: dispatch_source_vnode_flags_t ``` |
| To | ``` var DISPATCH_VNODE_ATTRIB: dispatch_source_vnode_flags_t { get } ``` |

Modified DISPATCH_VNODE_DELETE

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_VNODE_DELETE: dispatch_source_vnode_flags_t ``` |
| To | ``` var DISPATCH_VNODE_DELETE: dispatch_source_vnode_flags_t { get } ``` |

Modified DISPATCH_VNODE_EXTEND

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_VNODE_EXTEND: dispatch_source_vnode_flags_t ``` |
| To | ``` var DISPATCH_VNODE_EXTEND: dispatch_source_vnode_flags_t { get } ``` |

Modified DISPATCH_VNODE_LINK

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_VNODE_LINK: dispatch_source_vnode_flags_t ``` |
| To | ``` var DISPATCH_VNODE_LINK: dispatch_source_vnode_flags_t { get } ``` |

Modified DISPATCH_VNODE_RENAME

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_VNODE_RENAME: dispatch_source_vnode_flags_t ``` |
| To | ``` var DISPATCH_VNODE_RENAME: dispatch_source_vnode_flags_t { get } ``` |

Modified DISPATCH_VNODE_REVOKE

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_VNODE_REVOKE: dispatch_source_vnode_flags_t ``` |
| To | ``` var DISPATCH_VNODE_REVOKE: dispatch_source_vnode_flags_t { get } ``` |

Modified DISPATCH_VNODE_WRITE

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_VNODE_WRITE: dispatch_source_vnode_flags_t ``` |
| To | ``` var DISPATCH_VNODE_WRITE: dispatch_source_vnode_flags_t { get } ``` |

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
