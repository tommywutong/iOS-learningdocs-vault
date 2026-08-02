---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/frameworks/Hypervisor.html
archived_at: '2026-07-18T02:51:49.461092Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# Hypervisor Changes

## Hypervisor

hv.hAdded [hv_vcpu_create()](https://developer.apple.com/documentation/hypervisor/1441691-hv_vcpu_create)Added [hv_vcpu_destroy()](https://developer.apple.com/documentation/hypervisor/1441507-hv_vcpu_destroy)Added [hv_vcpu_enable_native_msr()](https://developer.apple.com/documentation/hypervisor/1441240-hv_vcpu_enable_native_msr)Added [hv_vcpu_flush()](https://developer.apple.com/documentation/hypervisor/1441386-hv_vcpu_flush)Added [hv_vcpu_get_exec_time()](https://developer.apple.com/documentation/hypervisor/1441687-hv_vcpu_get_exec_time)Added [hv_vcpu_interrupt()](https://developer.apple.com/documentation/hypervisor/1441468-hv_vcpu_interrupt)Added [hv_vcpu_invalidate_tlb()](https://developer.apple.com/documentation/hypervisor/1441588-hv_vcpu_invalidate_tlb)Added [hv_vcpu_read_fpstate()](https://developer.apple.com/documentation/hypervisor/1441058-hv_vcpu_read_fpstate)Added [hv_vcpu_read_msr()](https://developer.apple.com/documentation/hypervisor/1441346-hv_vcpu_read_msr)Added [hv_vcpu_read_register()](https://developer.apple.com/documentation/hypervisor/1441678-hv_vcpu_read_register)Added [hv_vcpu_run()](https://developer.apple.com/documentation/hypervisor/1441231-hv_vcpu_run)Added [hv_vcpu_write_fpstate()](https://developer.apple.com/documentation/hypervisor/1441657-hv_vcpu_write_fpstate)Added [hv_vcpu_write_msr()](https://developer.apple.com/documentation/hypervisor/1441434-hv_vcpu_write_msr)Added [hv_vcpu_write_register()](https://developer.apple.com/documentation/hypervisor/1441540-hv_vcpu_write_register)Added [hv_vm_create()](https://developer.apple.com/documentation/hypervisor/1441424-hv_vm_create)Added [hv_vm_destroy()](https://developer.apple.com/documentation/hypervisor/1441356-hv_vm_destroy)Added [hv_vm_map()](https://developer.apple.com/documentation/hypervisor/1441187-hv_vm_map)Added [hv_vm_protect()](https://developer.apple.com/documentation/hypervisor/1441400-hv_vm_protect)Added [hv_vm_sync_tsc()](https://developer.apple.com/documentation/hypervisor/1441102-hv_vm_sync_tsc)Added [hv_vm_unmap()](https://developer.apple.com/documentation/hypervisor/1441378-hv_vm_unmap)hv_arch_vmx.hRemoved CPU_BASED2_DESCR_TABLE_EXITAdded [CPU_BASED2_APIC_REG_VIRT](https://developer.apple.com/documentation/hypervisor/1469645-anonymous_constants/cpu_based2_apic_reg_virt)Added [CPU_BASED2_DESC_TABLE](https://developer.apple.com/documentation/hypervisor/cpu_based2_desc_table)Added [CPU_BASED2_EPT_VE](https://developer.apple.com/documentation/hypervisor/cpu_based2_ept_ve)Added [CPU_BASED2_INVPCID](https://developer.apple.com/documentation/hypervisor/1469645-anonymous_constants/cpu_based2_invpcid)Added [CPU_BASED2_RDRAND](https://developer.apple.com/documentation/hypervisor/cpu_based2_rdrand)Added [CPU_BASED2_RDSEED](https://developer.apple.com/documentation/hypervisor/cpu_based2_rdseed)Added [CPU_BASED2_VIRT_INTR_DELIVERY](https://developer.apple.com/documentation/hypervisor/cpu_based2_virt_intr_delivery)Added [CPU_BASED2_VMCS_SHADOW](https://developer.apple.com/documentation/hypervisor/1469645-anonymous_constants/cpu_based2_vmcs_shadow)Added [CPU_BASED2_VMFUNC](https://developer.apple.com/documentation/hypervisor/cpu_based2_vmfunc)Added [CPU_BASED2_XSAVES_XRSTORS](https://developer.apple.com/documentation/hypervisor/cpu_based2_xsaves_xrstors)Added [PIN_BASED_POSTED_INTR](https://developer.apple.com/documentation/hypervisor/pin_based_posted_intr)Added [VMCS_CTRL_EOI_EXIT_BITMAP_0](https://developer.apple.com/documentation/hypervisor/vmcs_ctrl_eoi_exit_bitmap_0)Added [VMCS_CTRL_EOI_EXIT_BITMAP_1](https://developer.apple.com/documentation/hypervisor/vmcs_ctrl_eoi_exit_bitmap_1)Added [VMCS_CTRL_EOI_EXIT_BITMAP_2](https://developer.apple.com/documentation/hypervisor/vmcs_ctrl_eoi_exit_bitmap_2)Added [VMCS_CTRL_EOI_EXIT_BITMAP_3](https://developer.apple.com/documentation/hypervisor/1469436-virtual_machine_control_structur/vmcs_ctrl_eoi_exit_bitmap_3)Added [VMCS_CTRL_EPTP_INDEX](https://developer.apple.com/documentation/hypervisor/1469436-virtual_machine_control_structur/vmcs_ctrl_eptp_index)Added [VMCS_CTRL_EPTP_LIST_ADDR](https://developer.apple.com/documentation/hypervisor/vmcs_ctrl_eptp_list_addr)Added [VMCS_CTRL_EXECUTIVE_VMCS_PTR](https://developer.apple.com/documentation/hypervisor/1469436-virtual_machine_control_structur/vmcs_ctrl_executive_vmcs_ptr)Added [VMCS_CTRL_POSTED_INT_DESC_ADDR](https://developer.apple.com/documentation/hypervisor/1469436-virtual_machine_control_structur/vmcs_ctrl_posted_int_desc_addr)Added [VMCS_CTRL_POSTED_INT_N_VECTOR](https://developer.apple.com/documentation/hypervisor/vmcs_ctrl_posted_int_n_vector)Added [VMCS_CTRL_VIRT_EXC_INFO_ADDR](https://developer.apple.com/documentation/hypervisor/1469436-virtual_machine_control_structur/vmcs_ctrl_virt_exc_info_addr)Added [VMCS_CTRL_VMFUNC_CTRL](https://developer.apple.com/documentation/hypervisor/vmcs_ctrl_vmfunc_ctrl)Added [VMCS_CTRL_VMREAD_BITMAP_ADDR](https://developer.apple.com/documentation/hypervisor/vmcs_ctrl_vmread_bitmap_addr)Added [VMCS_CTRL_VMWRITE_BITMAP_ADDR](https://developer.apple.com/documentation/hypervisor/1469436-virtual_machine_control_structur/vmcs_ctrl_vmwrite_bitmap_addr)Added [VMCS_CTRL_XSS_EXITING_BITMAP](https://developer.apple.com/documentation/hypervisor/1469436-virtual_machine_control_structur/vmcs_ctrl_xss_exiting_bitmap)Added [VMCS_GUEST_INT_STATUS](https://developer.apple.com/documentation/hypervisor/vmcs_guest_int_status)Added [VMCS_GUEST_SMBASE](https://developer.apple.com/documentation/hypervisor/vmcs_guest_smbase)Added [VMCS_GUEST_VMX_TIMER_VALUE](https://developer.apple.com/documentation/hypervisor/vmcs_guest_vmx_timer_value)Added [VMCS_RO_IO_RCX](https://developer.apple.com/documentation/hypervisor/1469436-virtual_machine_control_structur/vmcs_ro_io_rcx)Added [VMCS_RO_IO_RDI](https://developer.apple.com/documentation/hypervisor/1469436-virtual_machine_control_structur/vmcs_ro_io_rdi)Added [VMCS_RO_IO_RIP](https://developer.apple.com/documentation/hypervisor/vmcs_ro_io_rip)Added [VMCS_RO_IO_RSI](https://developer.apple.com/documentation/hypervisor/vmcs_ro_io_rsi)Added [VMENTRY_DEACTIVATE_DUAL_MONITOR](https://developer.apple.com/documentation/hypervisor/vmentry_deactivate_dual_monitor)Added [VMENTRY_LOAD_IA32_PAT](https://developer.apple.com/documentation/hypervisor/vmentry_load_ia32_pat)Added [VMENTRY_LOAD_IA32_PERF_GLOBAL_CTRL](https://developer.apple.com/documentation/hypervisor/vmentry_load_ia32_perf_global_ctrl)Added [VMENTRY_SMM](https://developer.apple.com/documentation/hypervisor/vmentry_smm)Added [VMEXIT_LOAD_IA32_PAT](https://developer.apple.com/documentation/hypervisor/1469645-anonymous_constants/vmexit_load_ia32_pat)Added [VMEXIT_LOAD_IA32_PERF_GLOBAL_CTRL](https://developer.apple.com/documentation/hypervisor/1469645-anonymous_constants/vmexit_load_ia32_perf_global_ctrl)Added [VMEXIT_SAVE_IA32_PAT](https://developer.apple.com/documentation/hypervisor/vmexit_save_ia32_pat)Added [VMX_REASON_APIC_WRITE](https://developer.apple.com/documentation/hypervisor/1469470-vmx_exit_reasons/vmx_reason_apic_write)Added [VMX_REASON_EPT_INVEPT](https://developer.apple.com/documentation/hypervisor/1469470-vmx_exit_reasons/vmx_reason_ept_invept)Added [VMX_REASON_GDTR_IDTR](https://developer.apple.com/documentation/hypervisor/1469470-vmx_exit_reasons/vmx_reason_gdtr_idtr)Added [VMX_REASON_GETSEC](https://developer.apple.com/documentation/hypervisor/vmx_reason_getsec)Added [VMX_REASON_INVPCID](https://developer.apple.com/documentation/hypervisor/vmx_reason_invpcid)Added [VMX_REASON_INVVPID](https://developer.apple.com/documentation/hypervisor/1469470-vmx_exit_reasons/vmx_reason_invvpid)Added [VMX_REASON_IO_SMI](https://developer.apple.com/documentation/hypervisor/vmx_reason_io_smi)Added [VMX_REASON_LDTR_TR](https://developer.apple.com/documentation/hypervisor/vmx_reason_ldtr_tr)Added [VMX_REASON_MTF](https://developer.apple.com/documentation/hypervisor/vmx_reason_mtf)Added [VMX_REASON_OTHER_SMI](https://developer.apple.com/documentation/hypervisor/vmx_reason_other_smi)Added [VMX_REASON_RDRAND](https://developer.apple.com/documentation/hypervisor/1469470-vmx_exit_reasons/vmx_reason_rdrand)Added [VMX_REASON_RDSEED](https://developer.apple.com/documentation/hypervisor/vmx_reason_rdseed)Added [VMX_REASON_RDTSCP](https://developer.apple.com/documentation/hypervisor/1469470-vmx_exit_reasons/vmx_reason_rdtscp)Added [VMX_REASON_RSM](https://developer.apple.com/documentation/hypervisor/vmx_reason_rsm)Added [VMX_REASON_VIRTUALIZED_EOI](https://developer.apple.com/documentation/hypervisor/1469470-vmx_exit_reasons/vmx_reason_virtualized_eoi)Added [VMX_REASON_VMFUNC](https://developer.apple.com/documentation/hypervisor/1469470-vmx_exit_reasons/vmx_reason_vmfunc)Added [VMX_REASON_WBINVD](https://developer.apple.com/documentation/hypervisor/1469470-vmx_exit_reasons/vmx_reason_wbinvd)Added [VMX_REASON_XRSTORS](https://developer.apple.com/documentation/hypervisor/1469470-vmx_exit_reasons/vmx_reason_xrstors)Added [VMX_REASON_XSAVES](https://developer.apple.com/documentation/hypervisor/vmx_reason_xsaves)hv_vmx.hAdded [HV_VMX_CAP_EXIT](https://developer.apple.com/documentation/hypervisor/hv_vmx_cap_exit)Added [HV_VMX_CAP_PREEMPTION_TIMER](https://developer.apple.com/documentation/hypervisor/hv_vmx_cap_preemption_timer)

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
