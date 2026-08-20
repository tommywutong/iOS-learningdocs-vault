---
title: Viewing iOS-Optimized PNGs
apple_id: DTS40009883
resource_type: QA
platform: iOS
topic: Languages & Utilities
technology: null
published: '2013-08-13'
source_url: https://developer.apple.com/library/archive/qa/qa1681/_index.html
archived_at: '2026-07-18T02:33:47.271172Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1681

# Viewing iOS-Optimized PNGs

## Q:  When I build my iOS application, Xcode optimizes the PNG files within my application's bundle, meaning that Preview can't display them. How can I view these optimized files?

A: This optimization is done by the `pngcrush` tool, which you can find inside Xcode. The `pngcrush` tool supports a command line option, `-revert-iphone-optimizations`, that undoes the optimizations done during the Xcode build process. So, to view an optimized PNG file, you should first undo the optimization and then open it with Preview.

Listing 1 shows how you can use the `pngcrush` tool to convert an iOS-optimized PNG file (`Local.png`) to a standard PNG file (`Local-standard.png`). It uses xcrun to run the tool from within your currently selected Xcode (as determined by xcode-select).

__Listing 1__  Undoing iOS PNG optimization

```
$ xcrun -sdk iphoneos pngcrush \
-revert-iphone-optimizations -q Local.png Local-standard.png
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-08-13 | Updated to use xcrun (r. 13698179). |
| 2012-05-16 | Updated to account for Xcode being packaged as an application (r. 11396673). |
| 2010-04-09 | New document that explains how you can view a PNG file that's been optimized for iOS by the pngcrush tool. |

