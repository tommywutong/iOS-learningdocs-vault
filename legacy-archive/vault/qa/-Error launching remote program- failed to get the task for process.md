---
title: '"Error launching remote program: failed to get the task for process"'
apple_id: DTS40009554
resource_type: QA
platform: iOS
topic: Xcode
technology: null
published: '2010-02-23'
source_url: https://developer.apple.com/library/archive/qa/qa1682/_index.html
archived_at: '2026-07-18T02:33:47.429466Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1682

# "Error launching remote program: failed to get the task for process"

## Q:  Why am I getting "Error launching remote program: failed to get the task for process" when debugging an iPhone application on the device?

A: Why am I getting "Error launching remote program: failed to get the task for process" when debugging an iPhone application on the device?

You are getting the "Error launching remote program: failed to get the task for process" error message because you are either using your Ad Hoc or Distribution Provisioning profile when debugging your iPhone application on your device or you specified a code signing entitlements property list in your build settings which does not include a `get-task-allow` or "Can be debugged" property.

Distribution profiles don't have a `get-task-allow` entitlement property, which is needed for debugging iPhone applications. However, this property is available and enabled for Development Provisioning profiles. So, use your Development profile rather than your Distribution profile when debugging your iPhone application on the device.

If you specified a code signing entitlements property list in your build settings, make sure that your property list contains the `get-task-allow` property.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-02-23 | New document that explains and describes how to resolve the "failed to get the task for process" error message. |

