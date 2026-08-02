---
title: Keeping macro definitions out of the Xcode editor window's function pop-up
apple_id: DTS40009344
resource_type: QA
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2009-10-27'
source_url: https://developer.apple.com/library/archive/qa/qa1670/_index.html
archived_at: '2026-07-18T02:33:36.175583Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1670

# Keeping macro definitions out of the Xcode editor window's function pop-up

## Q:  How can I keep Xcode from listing macro definitions in the editor window's function pop-up?

A: Although the Xcode preferences panel does not have an interface for this configuration, you can set it by accessing the user defaults for Xcode from the command line, as shown in Listing 1.

__Listing 1__  Setting Xcode's user default value for macro definitions in the editor pop-up.

```
defaults write com.apple.Xcode PBXMethodPopupIncludeDefinesDefault NO
```

The change will take effect the next time you launch Xcode.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-10-27 | New document that describes how to configure Xcode so that it does not display macro definitions in the editor window's function pop-up. |

