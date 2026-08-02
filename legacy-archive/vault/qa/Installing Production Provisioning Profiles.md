---
title: Installing Production Provisioning Profiles
apple_id: DTS40011373
resource_type: QA
platform: macOS
topic: Data Management
technology: AppKit
published: '2011-12-15'
source_url: https://developer.apple.com/library/archive/qa/qa1759/_index.html
archived_at: '2026-07-18T02:34:35.843091Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1759

# Installing Production Provisioning Profiles

## Q:  When I try to install my production provision profile into System Preferences, I get the alert "The profile could not be installed due to an unexpected error." How do I work around this error?

A: Production provisioning profiles cannot be installed in the Profiles system preference pane. This is by design.

Production profiles do not contain any hardware UUIDs. Production provisioning profiles are only for signing apps that use iCloud or push notifications for submission to the Mac App Store. If your app does not use iCloud or push notifications, you just sign your app without a provisioning profile.

This is similar to iOS where production builds cannot be run on a device.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-12-15 | New document that describes the error that will occur when trying to install a production provisioning profile in System Preferences. |

