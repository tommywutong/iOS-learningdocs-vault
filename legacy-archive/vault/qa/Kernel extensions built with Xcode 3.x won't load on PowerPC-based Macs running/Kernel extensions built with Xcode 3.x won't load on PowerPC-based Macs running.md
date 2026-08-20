---
title: Kernel extensions built with Xcode 3.x won't load on PowerPC-based Macs running
  Mac OS X 10.4.x
apple_id: DTS40008802
resource_type: QA
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: null
published: '2009-05-19'
source_url: https://developer.apple.com/library/archive/qa/qa1628/_index.html
archived_at: '2026-07-18T02:33:00.654035Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1628

# Kernel extensions built with Xcode 3.x won't load on PowerPC-based Macs running Mac OS X 10.4.x

## Q:  I built a kernel extension with Xcode 3.x and the 10.4 SDK. When I try to load this kext on a PowerPC-based Mac running Mac OS X 10.4.x, it fails with the message `kld(): <path to kext> load command 2 unknown cmd field`. Why do I get this error and what can I do about it?

A: I built a kernel extension with Xcode 3.x and the 10.4 SDK. When I try to load this kext on a PowerPC-based Mac running Mac OS X 10.4.x, it fails with the message `kld(): <path to kext> load command 2 unknown cmd field`.

Why do I get this error and what can I do about it?

Xcode 3.x automatically adds a UUID load command to the executable file inside your kernel extension. However, the kernel linker in Mac OS X 10.4.x on PowerPC-based systems doesn't know how to handle this UUID load command, so the linker rejects the load request.

You can work around this by adding `-Xlinker -no_uuid` to the `Other Linker Flags` build setting for the PowerPC side only of your kext using the following steps.

1. Set the Configuration menu at the top of the window to All Configurations.
2. Select the Other Linker Flags build setting, then choose Add Per-Architecture Setting For from the Action pop-up menu at the lower left corner of the window and choose PowerPC from the submenu. Finally, change the value of the just-added PowerPC setting to `-Xlinker -no_uuid`.

__Figure 1__  Other Linker Flags for Xcode 3.0

!!

1. Set the Configuration menu at the top of the window to All Configurations.
2. Select the Other Linker Flags build setting, then choose Add Build Setting Condition from the Action pop-up menu at the lower left corner of the window. Choose 10.4 from the Any SDK pop-up menu and choose PowerPC from the Any Architecture pop-up menu. Finally, set the value of this build setting to `-Xlinker -no_uuid`.

__Figure 2__  Other Linker Flags for Xcode 3.1

!!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-05-19 | New document that kernel extension load failure on PowerPC-based Macs running Mac OS X 10.4 |

