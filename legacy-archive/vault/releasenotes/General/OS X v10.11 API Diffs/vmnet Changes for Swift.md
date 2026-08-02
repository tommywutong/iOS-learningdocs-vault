---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/vmnet.html
archived_at: '2026-07-18T02:53:48.378795Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# vmnet Changes for Swift

### vmnet

Removed interface_event_t.init(_: UInt32)Removed interface_event_t.valueRemoved operating_modes_t [struct]Removed operating_modes_t.init(_: UInt32)Removed operating_modes_t.valueRemoved vmnet_return_t [struct]Removed vmnet_return_t.init(_: UInt32)Removed vmnet_return_t.valueRemoved vmpktdesc.init()Removed vmpktdesc.init(vm_pkt_size: Int, vm_pkt_iov: UnsafeMutablePointer<iovec>, vm_pkt_iovcnt: UInt32, vm_flags: UInt32)Removed VMNET_BUFFER_EXHAUSTEDRemoved VMNET_FAILURERemoved VMNET_HOST_MODERemoved VMNET_INTERFACE_PACKETS_AVAILABLERemoved VMNET_INVALID_ACCESSRemoved VMNET_INVALID_ARGUMENTRemoved VMNET_MEM_FAILURERemoved VMNET_PACKET_TOO_BIGRemoved VMNET_SETUP_INCOMPLETERemoved VMNET_SHARED_MODERemoved VMNET_SUCCESSRemoved VMNET_TOO_MANY_PACKETSAdded interface_event_t.init(rawValue: UInt32)Added [interface_event_t.VMNET_INTERFACE_PACKETS_AVAILABLE](https://developer.apple.com/documentation/vmnet/interface_event_t/1419506-vmnet_interface_packets_availabl)Added [operating_modes_t [enum]](https://developer.apple.com/documentation/vmnet/operating_modes_t)Added [operating_modes_t.VMNET_HOST_MODE](https://developer.apple.com/documentation/vmnet/operating_modes_t/vmnet_host_mode)Added [operating_modes_t.VMNET_SHARED_MODE](https://developer.apple.com/documentation/vmnet/operating_modes_t/vmnet_shared_mode)Added [vmnet_return_t [enum]](https://developer.apple.com/documentation/vmnet/vmnet_return_t)Added [vmnet_return_t.VMNET_BUFFER_EXHAUSTED](https://developer.apple.com/documentation/vmnet/vmnet_return_t/vmnet_buffer_exhausted)Added [vmnet_return_t.VMNET_FAILURE](https://developer.apple.com/documentation/vmnet/vmnet_return_t/vmnet_failure)Added [vmnet_return_t.VMNET_INVALID_ACCESS](https://developer.apple.com/documentation/vmnet/vmnet_return_t/vmnet_invalid_access)Added [vmnet_return_t.VMNET_INVALID_ARGUMENT](https://developer.apple.com/documentation/vmnet/vmnet_return_t/vmnet_invalid_argument)Added [vmnet_return_t.VMNET_MEM_FAILURE](https://developer.apple.com/documentation/vmnet/vmnet_return_t/vmnet_mem_failure)Added [vmnet_return_t.VMNET_PACKET_TOO_BIG](https://developer.apple.com/documentation/vmnet/vmnet_return_t/vmnet_packet_too_big)Added [vmnet_return_t.VMNET_SETUP_INCOMPLETE](https://developer.apple.com/documentation/vmnet/vmnet_return_t/vmnet_setup_incomplete)Added [vmnet_return_t.VMNET_SUCCESS](https://developer.apple.com/documentation/vmnet/vmnet_return_t/vmnet_success)Added [vmnet_return_t.VMNET_TOO_MANY_PACKETS](https://developer.apple.com/documentation/vmnet/vmnet_return_t/vmnet_too_many_packets)Modified [interface_event_t [struct]](https://developer.apple.com/documentation/vmnet/interface_event_t)

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct interface_event_t {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | OS X 10.10 |
| To | ``` struct interface_event_t : OptionSetType {     init(rawValue rawValue: UInt32)     static var VMNET_INTERFACE_PACKETS_AVAILABLE: interface_event_t { get } } ``` | OptionSetType | OS X 10.11 |

Modified [vmpktdesc [struct]](https://developer.apple.com/documentation/vmnet/vmpktdesc)

|  | Declaration |
| --- | --- |
| From | ``` struct vmpktdesc {     var vm_pkt_size: Int     var vm_pkt_iov: UnsafeMutablePointer<iovec>     var vm_pkt_iovcnt: UInt32     var vm_flags: UInt32     init()     init(vm_pkt_size vm_pkt_size: Int, vm_pkt_iov vm_pkt_iov: UnsafeMutablePointer<iovec>, vm_pkt_iovcnt vm_pkt_iovcnt: UInt32, vm_flags vm_flags: UInt32) } ``` |
| To | ``` struct vmpktdesc {     var vm_pkt_size: Int     var vm_pkt_iov: UnsafeMutablePointer<iovec>     var vm_pkt_iovcnt: UInt32     var vm_flags: UInt32 } ``` |

Modified [vmnet_interface_set_event_callback(_: interface_ref, _: interface_event_t, _: dispatch_queue_t?, _: ((interface_event_t, xpc_object_t) -> Void)?) -> vmnet_return_t](https://developer.apple.com/documentation/vmnet/1419568-vmnet_interface_set_event_callba)

|  | Declaration |
| --- | --- |
| From | ``` func vmnet_interface_set_event_callback(_ interface: interface_ref, _ flags: interface_event_t, _ queue: dispatch_queue_t!, _ handler: ((interface_event_t, xpc_object_t!) -> Void)!) -> vmnet_return_t ``` |
| To | ``` func vmnet_interface_set_event_callback(_ interface: interface_ref, _ flags: interface_event_t, _ queue: dispatch_queue_t?, _ handler: ((interface_event_t, xpc_object_t) -> Void)?) -> vmnet_return_t ``` |

Modified [vmnet_start_interface(_: xpc_object_t, _: dispatch_queue_t, _: (vmnet_return_t, xpc_object_t?) -> Void) -> interface_ref](https://developer.apple.com/documentation/vmnet/1419500-vmnet_start_interface)

|  | Declaration |
| --- | --- |
| From | ``` func vmnet_start_interface(_ interface_desc: xpc_object_t!, _ queue: dispatch_queue_t!, _ handler: ((vmnet_return_t, xpc_object_t!) -> Void)!) -> interface_ref ``` |
| To | ``` func vmnet_start_interface(_ interface_desc: xpc_object_t, _ queue: dispatch_queue_t, _ handler: (vmnet_return_t, xpc_object_t?) -> Void) -> interface_ref ``` |

Modified [vmnet_stop_interface(_: interface_ref, _: dispatch_queue_t, _: (vmnet_return_t) -> Void) -> vmnet_return_t](https://developer.apple.com/documentation/vmnet/1419526-vmnet_stop_interface)

|  | Declaration |
| --- | --- |
| From | ``` func vmnet_stop_interface(_ interface: interface_ref, _ queue: dispatch_queue_t!, _ handler: ((vmnet_return_t) -> Void)!) -> vmnet_return_t ``` |
| To | ``` func vmnet_stop_interface(_ interface: interface_ref, _ queue: dispatch_queue_t, _ handler: (vmnet_return_t) -> Void) -> vmnet_return_t ``` |

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
