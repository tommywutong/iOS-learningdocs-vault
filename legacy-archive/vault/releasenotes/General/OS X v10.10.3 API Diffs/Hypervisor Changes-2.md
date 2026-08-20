---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/Hypervisor.html
archived_at: '2026-07-18T02:52:30.650052Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# Hypervisor Changes

## Hypervisor

Removed CPU_BASED2_DESCR_TABLE_EXITAdded CPU_BASED2_APIC_REG_VIRTAdded CPU_BASED2_DESC_TABLEAdded CPU_BASED2_EPT_VEAdded CPU_BASED2_INVPCIDAdded CPU_BASED2_RDRANDAdded CPU_BASED2_RDSEEDAdded CPU_BASED2_VIRT_INTR_DELIVERYAdded CPU_BASED2_VMCS_SHADOWAdded CPU_BASED2_VMFUNCAdded CPU_BASED2_XSAVES_XRSTORSAdded HV_VMX_CAP_EXITAdded HV_VMX_CAP_PREEMPTION_TIMERAdded PIN_BASED_POSTED_INTRAdded VMCS_CTRL_EOI_EXIT_BITMAP_0Added VMCS_CTRL_EOI_EXIT_BITMAP_1Added VMCS_CTRL_EOI_EXIT_BITMAP_2Added VMCS_CTRL_EOI_EXIT_BITMAP_3Added VMCS_CTRL_EPTP_INDEXAdded VMCS_CTRL_EPTP_LIST_ADDRAdded VMCS_CTRL_EXECUTIVE_VMCS_PTRAdded VMCS_CTRL_POSTED_INT_DESC_ADDRAdded VMCS_CTRL_POSTED_INT_N_VECTORAdded VMCS_CTRL_VIRT_EXC_INFO_ADDRAdded VMCS_CTRL_VMFUNC_CTRLAdded VMCS_CTRL_VMREAD_BITMAP_ADDRAdded VMCS_CTRL_VMWRITE_BITMAP_ADDRAdded VMCS_CTRL_XSS_EXITING_BITMAPAdded VMCS_GUEST_INT_STATUSAdded VMCS_GUEST_SMBASEAdded VMCS_GUEST_VMX_TIMER_VALUEAdded VMCS_RO_IO_RCXAdded VMCS_RO_IO_RDIAdded VMCS_RO_IO_RIPAdded VMCS_RO_IO_RSIAdded VMENTRY_DEACTIVATE_DUAL_MONITORAdded VMENTRY_LOAD_IA32_PATAdded VMENTRY_LOAD_IA32_PERF_GLOBAL_CTRLAdded VMENTRY_SMMAdded VMEXIT_LOAD_IA32_PATAdded VMEXIT_LOAD_IA32_PERF_GLOBAL_CTRLAdded VMEXIT_SAVE_IA32_PATAdded VMX_REASON_APIC_WRITEAdded VMX_REASON_EPT_INVEPTAdded VMX_REASON_GDTR_IDTRAdded VMX_REASON_GETSECAdded VMX_REASON_INVPCIDAdded VMX_REASON_INVVPIDAdded VMX_REASON_IO_SMIAdded VMX_REASON_LDTR_TRAdded VMX_REASON_MTFAdded VMX_REASON_OTHER_SMIAdded VMX_REASON_RDRANDAdded VMX_REASON_RDSEEDAdded VMX_REASON_RDTSCPAdded VMX_REASON_RSMAdded VMX_REASON_VIRTUALIZED_EOIAdded VMX_REASON_VMFUNCAdded VMX_REASON_WBINVDAdded VMX_REASON_XRSTORSAdded VMX_REASON_XSAVESAdded hv_vm_sync_tsc(UInt64) -> hv_return_tModified hv_uvaddr_t

|  | Declaration |
| --- | --- |
| From | ``` typealias hv_uvaddr_t = ConstUnsafePointer<()> ``` |
| To | ``` typealias hv_uvaddr_t = UnsafePointer<Void> ``` |

Modified hv_vcpu_create(UnsafeMutablePointer<hv_vcpuid_t>, hv_vcpu_options_t) -> hv_return_t

|  | Declaration |
| --- | --- |
| From | ``` func hv_vcpu_create(_ vcpu: UnsafePointer<hv_vcpuid_t>, _ flags: hv_vcpu_options_t) -> hv_return_t ``` |
| To | ``` func hv_vcpu_create(_ vcpu: UnsafeMutablePointer<hv_vcpuid_t>, _ flags: hv_vcpu_options_t) -> hv_return_t ``` |

Modified hv_vcpu_get_exec_time(hv_vcpuid_t, UnsafeMutablePointer<UInt64>) -> hv_return_t

|  | Declaration |
| --- | --- |
| From | ``` func hv_vcpu_get_exec_time(_ vcpu: hv_vcpuid_t, _ time: UnsafePointer<UInt64>) -> hv_return_t ``` |
| To | ``` func hv_vcpu_get_exec_time(_ vcpu: hv_vcpuid_t, _ time: UnsafeMutablePointer<UInt64>) -> hv_return_t ``` |

Modified hv_vcpu_interrupt(UnsafeMutablePointer<hv_vcpuid_t>, UInt32) -> hv_return_t

|  | Declaration |
| --- | --- |
| From | ``` func hv_vcpu_interrupt(_ vcpus: UnsafePointer<hv_vcpuid_t>, _ vcpu_count: UInt32) -> hv_return_t ``` |
| To | ``` func hv_vcpu_interrupt(_ vcpus: UnsafeMutablePointer<hv_vcpuid_t>, _ vcpu_count: UInt32) -> hv_return_t ``` |

Modified hv_vcpu_read_fpstate(hv_vcpuid_t, UnsafeMutablePointer<Void>, Int) -> hv_return_t

|  | Declaration |
| --- | --- |
| From | ``` func hv_vcpu_read_fpstate(_ vcpu: hv_vcpuid_t, _ buffer: UnsafePointer<()>, _ size: UInt) -> hv_return_t ``` |
| To | ``` func hv_vcpu_read_fpstate(_ vcpu: hv_vcpuid_t, _ buffer: UnsafeMutablePointer<Void>, _ size: Int) -> hv_return_t ``` |

Modified hv_vcpu_read_msr(hv_vcpuid_t, UInt32, UnsafeMutablePointer<UInt64>) -> hv_return_t

|  | Declaration |
| --- | --- |
| From | ``` func hv_vcpu_read_msr(_ vcpu: hv_vcpuid_t, _ msr: UInt32, _ value: UnsafePointer<UInt64>) -> hv_return_t ``` |
| To | ``` func hv_vcpu_read_msr(_ vcpu: hv_vcpuid_t, _ msr: UInt32, _ value: UnsafeMutablePointer<UInt64>) -> hv_return_t ``` |

Modified hv_vcpu_read_register(hv_vcpuid_t, hv_x86_reg_t, UnsafeMutablePointer<UInt64>) -> hv_return_t

|  | Declaration |
| --- | --- |
| From | ``` func hv_vcpu_read_register(_ vcpu: hv_vcpuid_t, _ reg: hv_x86_reg_t, _ value: UnsafePointer<UInt64>) -> hv_return_t ``` |
| To | ``` func hv_vcpu_read_register(_ vcpu: hv_vcpuid_t, _ reg: hv_x86_reg_t, _ value: UnsafeMutablePointer<UInt64>) -> hv_return_t ``` |

Modified hv_vcpu_write_fpstate(hv_vcpuid_t, UnsafeMutablePointer<Void>, Int) -> hv_return_t

|  | Declaration |
| --- | --- |
| From | ``` func hv_vcpu_write_fpstate(_ vcpu: hv_vcpuid_t, _ buffer: UnsafePointer<()>, _ size: UInt) -> hv_return_t ``` |
| To | ``` func hv_vcpu_write_fpstate(_ vcpu: hv_vcpuid_t, _ buffer: UnsafeMutablePointer<Void>, _ size: Int) -> hv_return_t ``` |

Modified hv_vm_map(hv_uvaddr_t, hv_gpaddr_t, Int, hv_memory_flags_t) -> hv_return_t

|  | Declaration |
| --- | --- |
| From | ``` func hv_vm_map(_ uva: hv_uvaddr_t, _ gpa: hv_gpaddr_t, _ size: UInt, _ flags: hv_memory_flags_t) -> hv_return_t ``` |
| To | ``` func hv_vm_map(_ uva: hv_uvaddr_t, _ gpa: hv_gpaddr_t, _ size: Int, _ flags: hv_memory_flags_t) -> hv_return_t ``` |

Modified hv_vm_protect(hv_gpaddr_t, Int, hv_memory_flags_t) -> hv_return_t

|  | Declaration |
| --- | --- |
| From | ``` func hv_vm_protect(_ gpa: hv_gpaddr_t, _ size: UInt, _ flags: hv_memory_flags_t) -> hv_return_t ``` |
| To | ``` func hv_vm_protect(_ gpa: hv_gpaddr_t, _ size: Int, _ flags: hv_memory_flags_t) -> hv_return_t ``` |

Modified hv_vm_unmap(hv_gpaddr_t, Int) -> hv_return_t

|  | Declaration |
| --- | --- |
| From | ``` func hv_vm_unmap(_ gpa: hv_gpaddr_t, _ size: UInt) -> hv_return_t ``` |
| To | ``` func hv_vm_unmap(_ gpa: hv_gpaddr_t, _ size: Int) -> hv_return_t ``` |

Modified hv_vmx_read_capability(hv_vmx_capability_t, UnsafeMutablePointer<UInt64>) -> hv_return_t

|  | Declaration |
| --- | --- |
| From | ``` func hv_vmx_read_capability(_ field: hv_vmx_capability_t, _ value: UnsafePointer<UInt64>) -> hv_return_t ``` |
| To | ``` func hv_vmx_read_capability(_ field: hv_vmx_capability_t, _ value: UnsafeMutablePointer<UInt64>) -> hv_return_t ``` |

Modified hv_vmx_vcpu_read_vmcs(hv_vcpuid_t, UInt32, UnsafeMutablePointer<UInt64>) -> hv_return_t

|  | Declaration |
| --- | --- |
| From | ``` func hv_vmx_vcpu_read_vmcs(_ vcpu: hv_vcpuid_t, _ field: UInt32, _ value: UnsafePointer<UInt64>) -> hv_return_t ``` |
| To | ``` func hv_vmx_vcpu_read_vmcs(_ vcpu: hv_vcpuid_t, _ field: UInt32, _ value: UnsafeMutablePointer<UInt64>) -> hv_return_t ``` |

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
