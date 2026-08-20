---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/Hypervisor.html
archived_at: '2026-07-18T02:53:35.666790Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# Hypervisor Changes for Swift

### Hypervisor

Removed hv_vmx_capability_t.valueRemoved hv_x86_reg_t.valueAdded hv_vmx_capability_t.init(rawValue: UInt32)Added hv_vmx_capability_t.rawValueAdded hv_x86_reg_t.init(rawValue: UInt32)Added hv_x86_reg_t.rawValueAdded [VMX_EPT_VPID_SUPPORT_AD](https://developer.apple.com/documentation/hypervisor/vmx_ept_vpid_support_ad)Added [VMX_EPT_VPID_SUPPORT_EXONLY](https://developer.apple.com/documentation/hypervisor/1469645-anonymous_constants/vmx_ept_vpid_support_exonly)Modified [hv_vmx_capability_t [struct]](https://developer.apple.com/documentation/hypervisor/hv_vmx_capability_t)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct hv_vmx_capability_t {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct hv_vmx_capability_t : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [hv_x86_reg_t [struct]](https://developer.apple.com/documentation/hypervisor/hv_x86_reg_t)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct hv_x86_reg_t {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct hv_x86_reg_t : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

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
