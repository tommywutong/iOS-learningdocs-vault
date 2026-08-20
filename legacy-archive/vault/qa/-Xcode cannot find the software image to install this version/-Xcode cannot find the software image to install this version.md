---
title: '"Xcode cannot find the software image to install this version"'
apple_id: DTS40009341
resource_type: QA
platform: iOS
topic: Xcode
technology: null
published: '2009-10-28'
source_url: https://developer.apple.com/library/archive/qa/qa1569/_index.html
archived_at: '2026-07-18T02:32:18.662341Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1569

# "Xcode cannot find the software image to install this version"

## Q:  Why do I see "Xcode cannot find the software image to install this version" in Xcode's Organizer window?

A: The message "Xcode cannot find the software image to install this version" is not an error; rather it's a notification that the version of the iPhone OS installed on the plugged in device does not have a corresponding restore image for Xcode to use.

__Figure 1__  From Xcode's Organizer window.

!

This may happen on a new Mac OS X installation (when no iPhone OS updates have yet been downloaded), or when your device contains a newer version of iPhone OS that's not yet available to Xcode (for example, a newly purchased device with a later version than what's on your Mac).

It may also happen if you install an iPhone OS on your device on one machine and then plug it into a different machine that doesn't contain the matching restore image.

This message does not prevent you from using the device for development purposes. The only effect is the inability to reinstall the OS currently on the device using Xcode.

You can check which software restore images are on your Mac (that is, have been installed either through updates in iTunes or as part of the iPhone OS beta program) by looking in `~/Library/iTunes/iPhone Software Updates/`.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-10-28 | New document that explains the (non-urgent) meaning of this message. |

