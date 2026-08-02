---
title: Missing Results in Xcode Project Find Window
apple_id: DTS10004600
resource_type: QA
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2008-03-06'
source_url: https://developer.apple.com/library/archive/qa/qa1580/_index.html
archived_at: '2026-07-18T02:32:19.916227Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1580

# Missing Results in Xcode Project Find Window

## Q:  A search using the Project Find in Xcode that worked previously now returns no results, even though I am typing into the still-open window from the prior search. How do I get my list of search results?

A: A likely reason is that some options were changed accidentally from the `Project Find` window in Xcode. The options (accessible from the `Options` button) could have been altered to modify the actual files searched or the search filters, resulting in the previously generated list of search results being invalidated and, therefore, not displayed.

If you check the `Options` dialog and everything appears correct, there are ways to address the problem. First, quit the Xcode development environment. You can then edit your Xcode preferences file - located in `~/Library/Preferences/com.apple.Xcode.plist` - in the Property List Editor to remove the `PBXGlobalFindOptionsSets` key. You can also delete the preferences file completely - however, doing so will result in more changes to your development environment than removing the single option. When you restart Xcode and go back to the `Project Find` window, the options will have been reset to the default values. Your search should now return the previously seen results.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-03-06 | New document that a workaround for when a search that previously returned results generates no files found in Xcode |

