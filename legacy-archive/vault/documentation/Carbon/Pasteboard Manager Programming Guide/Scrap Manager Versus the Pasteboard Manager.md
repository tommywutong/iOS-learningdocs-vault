---
title: Pasteboard Manager Programming Guide
apple_id: TP40001439
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: null
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Pasteboard_Prog_Guide/paste_scrap/paste_scrap.html
archived_at: '2026-07-15T05:23:55.120580Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Pasteboard Manager Programming Guide](Introduction%20to%20Pasteboard%20Manager%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Pasteboard%20Manager%20Tasks.md)

# Scrap Manager Versus the Pasteboard Manager

If your application still uses the Scrap Manager written for classic Mac OS, Apple encourages you to update your code to use the Pasteboard Manager instead.

The Pasteboard Manager is available in Mac OS X v10.3 and later.

[Table A-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimzzfvbuqmrqgmwugrkhjjeeqskc) lists the Carbon Scrap Manager functions and their Pasteboard Manager equivalents.

__Table A-1__  Scrap Manager functions and their Pasteboard Manager replacements

| Scrap Manager function | Pasteboard Manager equivalent | Comments |
| `GetScrapByName` | PasteboardCreate |  |
| `GetCurrentScrap` | `PasteboardCreate` | Specify the `kPasteboardClipboard` constant in `PasteboardCreate` to indicate you want the Clipboard. |
| `GetScrapFlavorFlags` | `PasteboardGetItemFlavorFlags` |  |
| `GetScrapFlavorSize` | No equivalent | Data is now handed to you as a CFData object, so you no longer need to allocate memory when receiving pasteboard data. |
| `GetScrapFlavorData` | `PasteboardCopyItemFlavorData` |  |
| `ClearCurrentScrap` | `PasteboardClear` | Specifically, clear the Clipboard pasteboard. |
| `ClearScrap` | `PasteboardClear` |  |
| `PutScrapFlavor` | `PasteboardPutItemFlavor` |  |
| `GetScrapFlavorCount` | `PasteboardCopyItemFlavors` | You obtain the flavors as a CFArray, and you can call `CFArrayGetCount` to obtain the number of flavors. |
| `GetScrapFlavorInfoList` | `PasteboardCopyItemFlavors` |  |
| `CallInScrapPromises` | `PasteboardResolvePromises` |  |
| `SetScrapPromiseKeeper` | `PasteboardSetPromiseKeeper` |  |
| Promise keeper UPP functions | No equivalent | UPPs not required for Mac OS X. |
| Promise keeper callback function | Promise keeper callback function | The parameter list is different for Pasteboard Manager callbacks. |

[Next](Document%20Revision%20History.md)[Previous](Pasteboard%20Manager%20Tasks.md)

