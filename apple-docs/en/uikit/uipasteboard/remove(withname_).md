---
title: 'remove(withName:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteboard/remove(withname:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/remove(withname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/remove%28withname%3A%29.json'
content_hash: 'sha256:60dc736bc23f7513'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# remove(withName:)

<sub>Type Method</sub>

Invalidates the designated app pasteboard.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class func remove(withName pasteboardName: UIPasteboard.Name)
```

## Parameters

- `pasteboardName` — The name of the pasteboard to be invalidated.

## Discussion

Invalidation of an app pasteboard frees up all resources used by it. Once a pasteboard is invalidated, you cannot use the it; `UIPasteboard` ignores any calls to it. The method has no effect if called with the name of a system pasteboard.

## See Also

### Getting and removing pasteboards

- [generalPasteboard](general.md) — The systemwide general pasteboard, which you use for general copy-paste operations.
- [+ pasteboardWithName:create:](<init(name_create_).md>) — Returns a pasteboard that you identify by name, optionally creating it if it doesn’t exist.
- [+ pasteboardWithUniqueName](<withuniquename().md>) — Returns an app pasteboard that you identify by a unique system-generated name.
