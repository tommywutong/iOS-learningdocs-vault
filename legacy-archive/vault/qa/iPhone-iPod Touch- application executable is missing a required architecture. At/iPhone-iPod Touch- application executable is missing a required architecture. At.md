---
title: 'iPhone/iPod Touch: application executable is missing a required architecture.
  At least one of the following architecture(s) must be present: armv6'
apple_id: DTS40011826
resource_type: QA
platform: iOS
topic: Languages & Utilities
technology: null
published: '2012-02-13'
source_url: https://developer.apple.com/library/archive/qa/qa1760/_index.html
archived_at: '2026-07-18T02:34:35.888476Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1760

# iPhone/iPod Touch: application executable is missing a required architecture. At least one of the following architecture(s) must be present: armv6

## Q:  I am getting "iPhone/iPod Touch: application executable is missing a required architecture. At least one of the following architecture(s) must be present: armv6." when submitting my application for review with Xcode 4.2 or later.

A: You are getting the " missing a required architecture." message for one or more of the following reasons:

- Your `Architecture` at the Target Level build settings does not contain the `armv6` architecture.

  Use the "Other" option in the `Architecture` pop-up menu (see Figure 1) to add `armv6` to the `Architecture` build setting as seen in Figure 2.

__Figure 1__  Other option in the Architectures pop-up menu

!

__Figure 2__  Adding armv6 to the Architectures build setting

!!

- Your `Build Active Architecture ONLY` build setting is set to YES.

  Setting `Build Active Architecture ONLY` to YES indicates that you only wish to build your application for the native architecture, which is `armv7`  in Xcode 4. Make sure that `Architecture` includes `armv6`, then set `Build Active Architecture ONLY` to NO as seen in Figure 3 to build your application for `armv6`.

__Figure 3__  Build Active Architecture ONLY set to NO

!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-02-13 | New document that describes how to resolve the "application executable is missing a required architecture" message. |

