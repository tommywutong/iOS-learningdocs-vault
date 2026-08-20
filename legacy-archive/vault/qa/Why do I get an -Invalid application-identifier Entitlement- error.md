---
title: Why do I get an "Invalid application-identifier Entitlement" error?
apple_id: DTS40010246
resource_type: QA
platform: iOS|Xcode Developer Tools|macOS
topic: Languages & Utilities
technology: null
published: '2014-03-24'
source_url: https://developer.apple.com/library/archive/qa/qa1710/_index.html
archived_at: '2026-07-18T02:34:18.707637Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1710

# Why do I get an "Invalid application-identifier Entitlement" error?

## Q:  Why do I get an "Invalid application-identifier Entitlement" error?

A: The most common cause of this error occurs when mistakenly supplying a malformed application identifier entitlement within your Xcode project's custom `Entitlements.plist`.

In modern versions of Xcode, you don't need to supply a value for this entitlement yourself, so the error can be avoided by simply removing the application identifier entitlement from your custom Entitlements.plist.

Xcode builds the application identifier entitlement for you based on the Bundle Identifier property defined in your Xcode project's Target > Info tab, so setting the correct Bundle Identifier in Xcode is imperative.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-03-24 | Editorial update, fixed links. |
| 2013-05-03 | Simplified solution for modern versions of Xcode. |
| 2011-03-28 | Minor updates. |
| 2010-08-18 | New document that explains the "Invalid application-identifier Entitlement" error. |

