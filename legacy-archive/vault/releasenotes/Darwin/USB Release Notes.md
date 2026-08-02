---
title: USB Release Notes
apple_id: TP40007739
resource_type: Release Note
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2008-06-04'
source_url: https://developer.apple.com/library/archive/releasenotes/Darwin/RN_USB/index.html
archived_at: '2026-07-18T02:50:23.476645Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# USB Release Notes

This Release Note describes USB services available in Snow Leopard.

### 64-Bit Kernel Support

64-bit USB kernel (and user) core services are fully functional in Snow Leopard. Some layers above USB do not yet work, such as the audio, serial, (USB) Ethernet, and modem drivers. All other major services are available, including HID (keyboards and mice), hubs, mass storage, scanning, printing, and still cameras. Video camera operation may or may not work, depending on higher-level and graphics support issues.

The USB stack should be fully usable for both kernel and user space driver development. USB flash and hard drives should be reliable, though some user-interface quirks may be present. For example, the drive may not be visible in Finder or System Profiler, but works correctly in Terminal.

USB kernel programming interfaces are basically identical between the 64-bit and 32-bit kernels, except that pointers are 64 bits wide in the 64-bit kernel. USB user space programming interfaces should be 100% compatible with the 32-bit and 64-bit user space programming interfaces in OS X v10.5.
