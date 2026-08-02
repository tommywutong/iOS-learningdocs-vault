---
title: FireWire Release Notes
apple_id: TP40007716
resource_type: Release Note
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2008-06-05'
source_url: https://developer.apple.com/library/archive/releasenotes/Darwin/RN-FireWire/index.html
archived_at: '2026-07-18T02:50:23.076928Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# FireWire Release Notes

This Release Note describes FireWire services available in Snow Leopard.

#### Contents:

- [64-Bit Kernel Support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tomjwfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Integrated FireWire KDP](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tomjwfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [New Buffer-Fill Isochronous Receive Service](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tomjwfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)

### 64-Bit Kernel Support

64-bit FireWire kernel (and user) services are fully functional in Snow Leopard. Some layers above FireWire do not yet work, such as the audio driver `AppleFWAudio.kext`. All other major services are available, including IOFireWireIP, Mass Storage (SBP-2), iSight, and DV/MPEG. The stack should be fully usable for both kernel and user space driver development. However, some high-level applications that use DV or MPEG on FireWire may not work, due to support issues in other software layers.

FireWire sample code and tools (such as in AVS) are functional for DV and MPEG. FireWire hard drives should be reliable, though some user-interface quirks may be present. For example, the drive may not be visible in Finder or System Profiler, but works correctly in Terminal.

FireWire kernel programming interfaces are basically identical in the 64-bit and 32-bit kernels, except that pointers are 64 bits wide in the 64-bit kernel. FireWire user space programming interfaces should be 100% compatible with the 32-bit and 64-bit user space programming interfaces in OS X v10.5.

FireWire `kprintf` and FireWire KDP (kernel debugger protocol) are both available in 64-bit kernel mode.

### Integrated FireWire KDP

FireWire KDP (kernel debugger protocol) allows developers to perform two-machine debugging over FireWire. In Snow Leopard FireWire KDP is now built in, so installing `AppleFireWireKDP.kext` is no longer required (however, you can still find `AppleFireWireKDP.kext` at `/Developer/Extras/Kernel Debugging`).

To enable FireWire KDP on a target machine, enter this command in Terminal:

```
sudo nvram boot-args="debug=146 kdp_match_name=firewire"
```

For more information on FireWire KDP, including the `FireWireKDPProxy`, see the files at `/Developer/Extras/Kernel Debugging` or download the latest FireWire SDK from [ADC Development Kits](https://developer.apple.com/sdk).

### New Buffer-Fill Isochronous Receive Service

The FireWire Family now has kernel programming interfaces that provide an alternate isochronous receive service. This new service uses the multi-channel buffer-fill DMA mode of the 1394 OpenHCI (Open Host Controller Interface). It allows for receiving packets on more isochronous channels then there are available DMA contexts. It also eliminates the need to write a DCL program to receive isochronous packets. (The old isochronous receive services are unchanged and still fully supported.)

The new programming interfaces are part of the `IOFireWireController` object. For more details, see `IOFireWireMultiIsochReceive.h`. Note that user-space access to these programming interfaces is not yet available.
