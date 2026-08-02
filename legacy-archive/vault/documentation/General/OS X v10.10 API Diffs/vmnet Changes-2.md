---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/vmnet.html
archived_at: '2026-07-15T07:34:58.323390Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# vmnet Changes

## vmnet (Added)

Added interface_event_t [struct]Added interface_event_t.init(_: UInt32)Added interface_event_t.valueAdded operating_modes_t [struct]Added operating_modes_t.init(_: UInt32)Added operating_modes_t.valueAdded vmnet_return_t [struct]Added vmnet_return_t.init(_: UInt32)Added vmnet_return_t.valueAdded vmpktdesc [struct]Added vmpktdesc.vm_flagsAdded vmpktdesc.vm_pkt_iovAdded vmpktdesc.vm_pkt_iovcntAdded vmpktdesc.vm_pkt_sizeAdded VMNET_BUFFER_EXHAUSTEDAdded VMNET_FAILUREAdded VMNET_HOST_MODEAdded VMNET_INTERFACE_PACKETS_AVAILABLEAdded VMNET_INVALID_ACCESSAdded VMNET_INVALID_ARGUMENTAdded VMNET_MEM_FAILUREAdded VMNET_PACKET_TOO_BIGAdded VMNET_SETUP_INCOMPLETEAdded VMNET_SHARED_MODEAdded VMNET_SUCCESSAdded VMNET_TOO_MANY_PACKETSAdded interface_refAdded vmnet_estimated_packets_available_keyAdded vmnet_interface_id_keyAdded vmnet_interface_set_event_callback(interface_ref, interface_event_t, dispatch_queue_t!,((interface_event_t, xpc_object_t!) -> Void)!) -> vmnet_return_tAdded vmnet_mac_address_keyAdded vmnet_max_packet_size_keyAdded vmnet_mtu_keyAdded vmnet_operation_mode_keyAdded vmnet_read(interface_ref, UnsafeMutablePointer<vmpktdesc>, UnsafeMutablePointer<Int32>) -> vmnet_return_tAdded vmnet_start_interface(xpc_object_t!, dispatch_queue_t!,((vmnet_return_t, xpc_object_t!) -> Void)!) -> interface_refAdded vmnet_stop_interface(interface_ref, dispatch_queue_t!,((vmnet_return_t) -> Void)!) -> vmnet_return_tAdded vmnet_write(interface_ref, UnsafeMutablePointer<vmpktdesc>, UnsafeMutablePointer<Int32>) -> vmnet_return_t

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
