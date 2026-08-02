---
title: Backwards Compatibility With libxml2 and iPhone SDK
apple_id: DTS40009074
resource_type: QA
platform: iOS
topic: Xcode
technology: null
published: '2009-08-05'
source_url: https://developer.apple.com/library/archive/qa/qa1659/_index.html
archived_at: '2026-07-18T02:33:17.561858Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1659

# Backwards Compatibility With libxml2 and iPhone SDK

## Q:  Why does my application crash with an "Incompatible library version" error message?

A: Why does my application crash with an "Incompatible library version" error message?

If the following conditions are met:

- your application links directly to libxml2, and
- is built using the iPhone SDK 3.0 or later, and
- has iPhone OS 2.x as a deployment target

then the application will crash when run on 2.x devices. This is due to a compatibility version change in libxml2 between iPhone OS 2.2.1 and iPhone OS 3.0 and later. You can work around this issue by linking directly to the older version of libxml2.

You can link directly to a library by modifying the "Other Linker Flags" entry for your Xcode project. To do so, open the project's Build settings and search for "Other Linker Flags". Then find the full path to libxml2 in the appropriate 2.x SDK and add that to the flags. For example, if you have the 2.2.1 SDK installed, you can use the following:

`$(DEVELOPER_DIR)/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS2.2.1.sdk/usr/lib/libxml2.dylib`.

Xcode will replace the `$(DEVELOPER_DIR)` variable with the directory where your developer tools are installed, which makes this more portable in case the project is later opened on a machine with the tools installed in a non-default directory.

__Figure 1__  Linking directly to the iPhone OS 2.2.1 SDK version of libxml2.

!!

The setting described above will solve the problem when building the application for the Device, but because the library path is fully specified, Xcode cannot switch to the appropriate version when building for the Simulator. It is necessary to add a "Build Setting Condition" to the "Other Linker Flags" entry. One condition will specify the "Other Linker Flags" when building for the Device, the other condition will do so when building for the Simulator. You can add build setting conditions by selecting the setting, and then clicking the menu in the bottom left of the window.

__Figure 2__  Adding a build setting condition.

!

This will create a child entry for linker flags that is only enabled when the rules specified in the build setting condition are true. You will need to add two conditions - one for the Device and one for the Simulator. Set the linker flag for the device as described above. For the Simulator, you should use the Base SDK version by specifying `-lxml2`. If you had previously set the linker flag without a build condition, you should remove that flag.

__Figure 3__  Separate linker flags for Device and Simulator.

!!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-08-05 | New document that describes how to work around the "Incompatible library version" link error when using libxml2. |

