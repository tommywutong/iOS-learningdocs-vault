---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/vmnet.html
archived_at: '2026-07-18T02:52:46.489710Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# vmnet Changes

## vmnet

Added vmpktdesc.init()Added vmpktdesc.init(vm_pkt_size: Int, vm_pkt_iov: UnsafeMutablePointer<iovec>, vm_pkt_iovcnt: UInt32, vm_flags: UInt32)Modified vmpktdesc [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vmpktdesc {     var vm_pkt_size: UInt     var vm_pkt_iov: UnsafePointer<iovec>     var vm_pkt_iovcnt: UInt32     var vm_flags: UInt32 } ``` |
| To | ``` struct vmpktdesc {     var vm_pkt_size: Int     var vm_pkt_iov: UnsafeMutablePointer<iovec>     var vm_pkt_iovcnt: UInt32     var vm_flags: UInt32     init()     init(vm_pkt_size vm_pkt_size: Int, vm_pkt_iov vm_pkt_iov: UnsafeMutablePointer<iovec>, vm_pkt_iovcnt vm_pkt_iovcnt: UInt32, vm_flags vm_flags: UInt32) } ``` |

Modified vmpktdesc.vm_pkt_iov

|  | Declaration |
| --- | --- |
| From | ``` var vm_pkt_iov: UnsafePointer<iovec> ``` |
| To | ``` var vm_pkt_iov: UnsafeMutablePointer<iovec> ``` |

Modified vmpktdesc.vm_pkt_size

|  | Declaration |
| --- | --- |
| From | ``` var vm_pkt_size: UInt ``` |
| To | ``` var vm_pkt_size: Int ``` |

Modified vmnet_estimated_packets_available_key

|  | Declaration |
| --- | --- |
| From | ``` var vmnet_estimated_packets_available_key: ConstUnsafePointer<Int8> ``` |
| To | ``` var vmnet_estimated_packets_available_key: UnsafePointer<Int8> ``` |

Modified vmnet_interface_id_key

|  | Declaration |
| --- | --- |
| From | ``` var vmnet_interface_id_key: ConstUnsafePointer<Int8> ``` |
| To | ``` var vmnet_interface_id_key: UnsafePointer<Int8> ``` |

Modified vmnet_mac_address_key

|  | Declaration |
| --- | --- |
| From | ``` var vmnet_mac_address_key: ConstUnsafePointer<Int8> ``` |
| To | ``` var vmnet_mac_address_key: UnsafePointer<Int8> ``` |

Modified vmnet_max_packet_size_key

|  | Declaration |
| --- | --- |
| From | ``` var vmnet_max_packet_size_key: ConstUnsafePointer<Int8> ``` |
| To | ``` var vmnet_max_packet_size_key: UnsafePointer<Int8> ``` |

Modified vmnet_mtu_key

|  | Declaration |
| --- | --- |
| From | ``` var vmnet_mtu_key: ConstUnsafePointer<Int8> ``` |
| To | ``` var vmnet_mtu_key: UnsafePointer<Int8> ``` |

Modified vmnet_operation_mode_key

|  | Declaration |
| --- | --- |
| From | ``` var vmnet_operation_mode_key: ConstUnsafePointer<Int8> ``` |
| To | ``` var vmnet_operation_mode_key: UnsafePointer<Int8> ``` |

Modified vmnet_read(interface_ref, UnsafeMutablePointer<vmpktdesc>, UnsafeMutablePointer<Int32>) -> vmnet_return_t

|  | Declaration |
| --- | --- |
| From | ``` func vmnet_read(_ interface: interface_ref, _ packets: UnsafePointer<vmpktdesc>, _ pktcnt: UnsafePointer<Int32>) -> vmnet_return_t ``` |
| To | ``` func vmnet_read(_ interface: interface_ref, _ packets: UnsafeMutablePointer<vmpktdesc>, _ pktcnt: UnsafeMutablePointer<Int32>) -> vmnet_return_t ``` |

Modified vmnet_write(interface_ref, UnsafeMutablePointer<vmpktdesc>, UnsafeMutablePointer<Int32>) -> vmnet_return_t

|  | Declaration |
| --- | --- |
| From | ``` func vmnet_write(_ interface: interface_ref, _ packets: UnsafePointer<vmpktdesc>, _ pktcnt: UnsafePointer<Int32>) -> vmnet_return_t ``` |
| To | ``` func vmnet_write(_ interface: interface_ref, _ packets: UnsafeMutablePointer<vmpktdesc>, _ pktcnt: UnsafeMutablePointer<Int32>) -> vmnet_return_t ``` |

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
