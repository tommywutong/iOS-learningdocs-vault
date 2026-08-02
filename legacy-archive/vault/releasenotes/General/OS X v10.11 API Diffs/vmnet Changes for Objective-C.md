---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/vmnet.html
archived_at: '2026-07-18T02:53:15.051773Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# vmnet Changes for Objective-C

### vmnet

#### vmnet.h

Modified [vmnet_interface_set_event_callback()](https://developer.apple.com/documentation/vmnet/1419568-vmnet_interface_set_event_callba)

|  | Declaration |
| --- | --- |
| From | ``` vmnet_return_t vmnet_interface_set_event_callback (     interface_ref interface,     interface_event_t flags,     dispatch_queue_t queue,     void (^handler)(interface_event_t event_id, xpc_object_t event) ); ``` |
| To | ``` vmnet_return_t vmnet_interface_set_event_callback (     interface_ref _Nonnull interface,     interface_event_t flags,     dispatch_queue_t _Nullable queue,     void (^ _Nullablehandler)(interface_event_t event_id, xpc_object_t _Nonnull event) ); ``` |

Modified [vmnet_read()](https://developer.apple.com/documentation/vmnet/1419528-vmnet_read)

|  | Declaration |
| --- | --- |
| From | ``` vmnet_return_t vmnet_read (     interface_ref interface,     struct vmpktdesc *packets,     int *pktcnt ); ``` |
| To | ``` vmnet_return_t vmnet_read (     interface_ref _Nonnull interface,     struct vmpktdesc * _Nonnull packets,     int * _Nonnull pktcnt ); ``` |

Modified [vmnet_start_interface()](https://developer.apple.com/documentation/vmnet/1419500-vmnet_start_interface)

|  | Declaration |
| --- | --- |
| From | ``` interface_ref vmnet_start_interface (     xpc_object_t interface_desc,     dispatch_queue_t queue,     void (^handler)(vmnet_return_t status, xpc_object_t interface_param) ); ``` |
| To | ``` interface_ref _Nullable vmnet_start_interface (     xpc_object_t _Nonnull interface_desc,     dispatch_queue_t _Nonnull queue,     void (^ _Nonnullhandler)(vmnet_return_t status, xpc_object_t _Nullable interface_param) ); ``` |

Modified [vmnet_stop_interface()](https://developer.apple.com/documentation/vmnet/1419526-vmnet_stop_interface)

|  | Declaration |
| --- | --- |
| From | ``` vmnet_return_t vmnet_stop_interface (     interface_ref interface,     dispatch_queue_t queue,     void (^handler)(vmnet_return_t status) ); ``` |
| To | ``` vmnet_return_t vmnet_stop_interface (     interface_ref _Nonnull interface,     dispatch_queue_t _Nonnull queue,     void (^ _Nonnullhandler)(vmnet_return_t status) ); ``` |

Modified [vmnet_write()](https://developer.apple.com/documentation/vmnet/1419532-vmnet_write)

|  | Declaration |
| --- | --- |
| From | ``` vmnet_return_t vmnet_write (     interface_ref interface,     struct vmpktdesc *packets,     int *pktcnt ); ``` |
| To | ``` vmnet_return_t vmnet_write (     interface_ref _Nonnull interface,     struct vmpktdesc * _Nonnull packets,     int * _Nonnull pktcnt ); ``` |

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
