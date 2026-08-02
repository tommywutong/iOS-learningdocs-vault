---
title: 'WARNING: The Copy Bundle Resources build phase contains this target''s Info.plist
  file ''Info.plist''.'
apple_id: DTS40009342
resource_type: QA
platform: iOS|Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-06-29'
source_url: https://developer.apple.com/library/archive/qa/qa1649/_index.html
archived_at: '2026-07-18T02:33:14.562120Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1649

# WARNING: The Copy Bundle Resources build phase contains this target's Info.plist file 'Info.plist'.

## Q:  Why am I getting "WARNING: The Copy Bundle Resources build phase contains this target's Info.plist file 'Info.plist'"? And how do I fix it?

A: You are getting this warning because you probably added your `Info.plist` file to the Copy Bundle Resources build phase as shown in Figure 1.

__Figure 1__  Remove Info.plist from the Copy Bundle Resources build phase.

!!

The INFOPLIST_FILE build setting specifies the name of the `Info.plist` associated with your target. When building a target, Xcode reads this build setting and copies the referenced `Info.plist` into your application bundle. Because Xcode automatically processes the `Info.plist`, you should not add it to your Copy Bundle Resources build phase nor make it a target member.

To resolve this warning, select your `Info.plist` from the Copy Bundle Resource build phase as shown in Figure 1, then click the Remove (–) button to delete it from the phase.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-06-29 | Editorial update. |
| 2011-09-22 | Updated for Xcode 4. |
| 2009-10-27 | New document that explains and describes how to fix the Copy Bundle Resources build phase warning. |

