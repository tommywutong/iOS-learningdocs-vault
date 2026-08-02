---
title: Why do I get an
apple_id: DTS40010261
resource_type: QA
platform: iOS
topic: Languages & Utilities
technology: null
published: '2011-01-20'
source_url: https://developer.apple.com/library/archive/qa/qa1707/_index.html
archived_at: '2026-07-18T02:34:14.860530Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1707

# Why do I get an

## Q:  Why do I get an "Invalid Binary Architecture" email after uploading my app to iTunes Connect?

A: If after uploading your app to iTunes Connect you receive an email or error message stating that your binary has an "`Invalid Binary Architecture`", your project is likely building as an "Optimized (armv7)" binary, and does not have the `armv7` key in the `Required Device Capabilities` (`UIRequiredDeviceCapabilities`) key in the project's Info.plist. Adding `armv7` is necessary to ensure your app is only displayed for and installed on iOS devices capable of running this optimized binary.

Figure 1 shows the Architectures setting in your Build pane. Figure 2 shows the necessary entry in Info.plist if you build an "Optimized (armv7)" binary.

__Figure 1__  This project will build an Optimized (armv7)-only binary.

!

__Figure 2__  A correctly configured Info.plist entry for projects that build as Optimized (armv7).

!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-01-20 | Fixed typo in the document. |
| 2010-08-23 | New document that explains how to set a project's UIRequiredDeviceCapabilities key correctly for optimized binaries. |

