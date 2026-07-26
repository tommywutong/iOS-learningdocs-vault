---
title: UIPasteboardNameFind
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+（10.0 起废弃）, iPadOS 3.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uipasteboardnamefind
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboardnamefind'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboardnamefind.json'
content_hash: 'sha256:a91a3d617069b8e7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPasteboardNameFind

<sub>Global Variable</sub>

A name that identifies the Find pasteboard.

> [!warning] Deprecated
> The Find pasteboard is no longer available.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
let UIPasteboardNameFind: String
```

## Discussion

The Find pasteboard is unavailable starting in iOS 10.

The name identifying the Find pasteboard, which, prior to iOS 10, was used in search operations. In such operations, the most recent search string in the search bar was put in the Find pasteboard.

## See Also

### Constants

- [UIPasteboardNameGeneral](uipasteboard/name-swift.struct/general.md) — The name identifying the general pasteboard, which you use for general copy-cut-paste operations.
