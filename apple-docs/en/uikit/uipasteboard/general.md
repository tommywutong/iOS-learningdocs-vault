---
title: general
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/general
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/general'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/general.json'
content_hash: 'sha256:94825024acd7e991'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# general

<sub>Type Property</sub>

The systemwide general pasteboard, which you use for general copy-paste operations.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class var general: UIPasteboard { get }
```

## Return Value

A shared system pasteboard object with the name of [UIPasteboardNameGeneral](name-swift.struct/general.md).

## Discussion

You may use the general pasteboard for copying and pasting text, images, URLs, colors, and other data within an app or between apps. The general pasteboard is persistent across device restarts and app uninstalls.

## See Also

### Getting and removing pasteboards

- [+ pasteboardWithName:create:](<init(name_create_).md>) — Returns a pasteboard that you identify by name, optionally creating it if it doesn’t exist.
- [+ pasteboardWithUniqueName](<withuniquename().md>) — Returns an app pasteboard that you identify by a unique system-generated name.
- [+ removePasteboardWithName:](<remove(withname_).md>) — Invalidates the designated app pasteboard.
