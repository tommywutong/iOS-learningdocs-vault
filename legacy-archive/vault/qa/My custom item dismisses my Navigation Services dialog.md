---
title: My custom item dismisses my Navigation Services dialog
apple_id: DTS10003410
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2004-11-22'
source_url: https://developer.apple.com/library/archive/qa/qa1381/_index.html
archived_at: '2026-07-18T02:30:29.232169Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1381

# My custom item dismisses my Navigation Services dialog

## Q:  I have a custom area in my Navigation Services dialog and each time I click some of my items, the dialog disappears. What's happening?

A: I have a custom area in my Navigation Services dialog and each time I click some of my items, the dialog disappears. What's happening?

You are probably running in Jaguar (Mac OS X 10.2.x) and those items have a control ID of 1.

This is a bug which was fixed in Panther (Mac OS X 10.3): previously, when a click was occurring in the custom area on an item which control ID was 1, no matter what the signature was, the Navigation Services dialog was incorrectly interpreting the click as a click on the default button and thus was dismissing the dialog. The Navigation Services dialog in Panther correctly checks the signature of the control in addition to its ID and thus does not confuse your items with the default button.

The best workaround for that problem is to use control IDs on your items starting higher at, for example, 100. This will work on all versions of Mac OS.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-11-22 | New document that gives a workaround for dismissive clicks on items in the custom area of Navigation Services dialogs. |

