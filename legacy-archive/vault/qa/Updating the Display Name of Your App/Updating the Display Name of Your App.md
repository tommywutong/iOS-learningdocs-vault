---
title: Updating the Display Name of Your App
apple_id: DTS40014218
resource_type: QA
platform: iOS
topic: Xcode
technology: null
published: '2015-03-26'
source_url: https://developer.apple.com/library/archive/qa/qa1823/_index.html
archived_at: '2026-07-18T02:34:56.048730Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1823

# Updating the Display Name of Your App

## Q:  How do I change the name displayed underneath my app icon on my device's Home screen?

A: To change the name appearing underneath your app icon, modify the `CFBundleDisplayName` key in your `Info.plist`. Follow these steps to modify `CFBundleDisplayName`:

1. In Xcode, click the disclosure triangle next to your app folder in the project navigator to reveal its content as shown in Figure 1.

__Figure 1__  Expand your app folder to reveal its content

!!

1. Click the disclosure triangle next to the "Supporting Files" subfolder to reveal its content.
2. Select the `Info.plist` file to reveal a property list editor of keys and values.
3. By default, Xcode displays a human-readable string of a key rather than its actual name. So, search the property list for "Bundle display name". Skip to step 5 if your property list already shows `Bundle display name`. If it doesn't, add it to your list as follows:

   1. Click on any entry in your list, then click the "+" button.
   2. Choose `Bundle display name` from the ensuing pop-up menu.
4. Double-click in the Value column of `Bundle display name`.
5. Enter a new value for `Bundle display name` as shown in Figure 2.

__Figure 2__  Setting up Bundle display name to a given value for a WatchKit app

!!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-03-26 | Editorial update. |
| 2014-03-12 | New document that describes how to update the name displayed underneath your app icon. |

