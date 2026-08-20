---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/Hypervisor.html
archived_at: '2026-07-18T02:51:25.537341Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# Hypervisor Changes for Swift

### Hypervisor

Modified [hv_uvaddr_t](https://developer.apple.com/documentation/hypervisor/hv_uvaddr_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias hv_uvaddr_t = UnsafePointer<Void> ``` |
| To | ``` typealias hv_uvaddr_t = UnsafeRawPointer ``` |

Modified [hv_vcpu_create(_: UnsafeMutablePointer<hv_vcpuid_t>!, _: hv_vcpu_options_t) -> hv_return_t](https://developer.apple.com/documentation/hypervisor/1441691-hv_vcpu_create)

|  | Declaration |
| --- | --- |
| From | ``` func hv_vcpu_create(_ vcpu: UnsafeMutablePointer<hv_vcpuid_t>, _ flags: hv_vcpu_options_t) -> hv_return_t ``` |
| To | ``` func hv_vcpu_create(_ vcpu: UnsafeMutablePointer<hv_vcpuid_t>!, _ flags: hv_vcpu_options_t) -> hv_return_t ``` |

Modified [hv_vcpu_get_exec_time(_: hv_vcpuid_t, _: UnsafeMutablePointer<UInt64>!) -> hv_return_t](https://developer.apple.com/documentation/hypervisor/1441687-hv_vcpu_get_exec_time)

|  | Declaration |
| --- | --- |
| From | ``` func hv_vcpu_get_exec_time(_ vcpu: hv_vcpuid_t, _ time: UnsafeMutablePointer<UInt64>) -> hv_return_t ``` |
| To | ``` func hv_vcpu_get_exec_time(_ vcpu: hv_vcpuid_t, _ time: UnsafeMutablePointer<UInt64>!) -> hv_return_t ``` |

Modified [hv_vcpu_interrupt(_: UnsafeMutablePointer<hv_vcpuid_t>!, _: UInt32) -> hv_return_t](https://developer.apple.com/documentation/hypervisor/1441468-hv_vcpu_interrupt)

|  | Declaration |
| --- | --- |
| From | ``` func hv_vcpu_interrupt(_ vcpus: UnsafeMutablePointer<hv_vcpuid_t>, _ vcpu_count: UInt32) -> hv_return_t ``` |
| To | ``` func hv_vcpu_interrupt(_ vcpus: UnsafeMutablePointer<hv_vcpuid_t>!, _ vcpu_count: UInt32) -> hv_return_t ``` |

Modified [hv_vcpu_read_fpstate(_: hv_vcpuid_t, _: UnsafeMutableRawPointer!, _: Int) -> hv_return_t](https://developer.apple.com/documentation/hypervisor/1441058-hv_vcpu_read_fpstate)

|  | Declaration |
| --- | --- |
| From | ``` func hv_vcpu_read_fpstate(_ vcpu: hv_vcpuid_t, _ buffer: UnsafeMutablePointer<Void>, _ size: Int) -> hv_return_t ``` |
| To | ``` func hv_vcpu_read_fpstate(_ vcpu: hv_vcpuid_t, _ buffer: UnsafeMutableRawPointer!, _ size: Int) -> hv_return_t ``` |

Modified [hv_vcpu_read_msr(_: hv_vcpuid_t, _: UInt32, _: UnsafeMutablePointer<UInt64>!) -> hv_return_t](https://developer.apple.com/documentation/hypervisor/1441346-hv_vcpu_read_msr)

|  | Declaration |
| --- | --- |
| From | ``` func hv_vcpu_read_msr(_ vcpu: hv_vcpuid_t, _ msr: UInt32, _ value: UnsafeMutablePointer<UInt64>) -> hv_return_t ``` |
| To | ``` func hv_vcpu_read_msr(_ vcpu: hv_vcpuid_t, _ msr: UInt32, _ value: UnsafeMutablePointer<UInt64>!) -> hv_return_t ``` |

Modified [hv_vcpu_read_register(_: hv_vcpuid_t, _: hv_x86_reg_t, _: UnsafeMutablePointer<UInt64>!) -> hv_return_t](https://developer.apple.com/documentation/hypervisor/1441678-hv_vcpu_read_register)

|  | Declaration |
| --- | --- |
| From | ``` func hv_vcpu_read_register(_ vcpu: hv_vcpuid_t, _ reg: hv_x86_reg_t, _ value: UnsafeMutablePointer<UInt64>) -> hv_return_t ``` |
| To | ``` func hv_vcpu_read_register(_ vcpu: hv_vcpuid_t, _ reg: hv_x86_reg_t, _ value: UnsafeMutablePointer<UInt64>!) -> hv_return_t ``` |

Modified [hv_vcpu_write_fpstate(_: hv_vcpuid_t, _: UnsafeMutableRawPointer!, _: Int) -> hv_return_t](https://developer.apple.com/documentation/hypervisor/1441657-hv_vcpu_write_fpstate)

|  | Declaration |
| --- | --- |
| From | ``` func hv_vcpu_write_fpstate(_ vcpu: hv_vcpuid_t, _ buffer: UnsafeMutablePointer<Void>, _ size: Int) -> hv_return_t ``` |
| To | ``` func hv_vcpu_write_fpstate(_ vcpu: hv_vcpuid_t, _ buffer: UnsafeMutableRawPointer!, _ size: Int) -> hv_return_t ``` |

Modified [hv_vm_map(_: hv_uvaddr_t!, _: hv_gpaddr_t, _: Int, _: hv_memory_flags_t) -> hv_return_t](https://developer.apple.com/documentation/hypervisor/1441187-hv_vm_map)

|  | Declaration |
| --- | --- |
| From | ``` func hv_vm_map(_ uva: hv_uvaddr_t, _ gpa: hv_gpaddr_t, _ size: Int, _ flags: hv_memory_flags_t) -> hv_return_t ``` |
| To | ``` func hv_vm_map(_ uva: hv_uvaddr_t!, _ gpa: hv_gpaddr_t, _ size: Int, _ flags: hv_memory_flags_t) -> hv_return_t ``` |

Modified [hv_vmx_read_capability(_: hv_vmx_capability_t, _: UnsafeMutablePointer<UInt64>!) -> hv_return_t](https://developer.apple.com/documentation/hypervisor/1441276-hv_vmx_read_capability)

|  | Declaration |
| --- | --- |
| From | ``` func hv_vmx_read_capability(_ field: hv_vmx_capability_t, _ value: UnsafeMutablePointer<UInt64>) -> hv_return_t ``` |
| To | ``` func hv_vmx_read_capability(_ field: hv_vmx_capability_t, _ value: UnsafeMutablePointer<UInt64>!) -> hv_return_t ``` |

Modified [hv_vmx_vcpu_read_vmcs(_: hv_vcpuid_t, _: UInt32, _: UnsafeMutablePointer<UInt64>!) -> hv_return_t](https://developer.apple.com/documentation/hypervisor/1441636-hv_vmx_vcpu_read_vmcs)

|  | Declaration |
| --- | --- |
| From | ``` func hv_vmx_vcpu_read_vmcs(_ vcpu: hv_vcpuid_t, _ field: UInt32, _ value: UnsafeMutablePointer<UInt64>) -> hv_return_t ``` |
| To | ``` func hv_vmx_vcpu_read_vmcs(_ vcpu: hv_vcpuid_t, _ field: UInt32, _ value: UnsafeMutablePointer<UInt64>!) -> hv_return_t ``` |

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
