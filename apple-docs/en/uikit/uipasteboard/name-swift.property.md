---
title: name
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/name-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/name-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/name-swift.property.json'
content_hash: 'sha256:917b97ccc6a1b13c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# name

<sub>Instance Property</sub>

The name of the pasteboard.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var name: UIPasteboard.Name { get }
```

## Discussion

Names of app pasteboard objects should be unique across installed apps. If the object is a system pasteboard, this property returns one of the constants described in [Pasteboard Names](../pasteboard-names.md).

## See Also

### Related Documentation

- [+ pasteboardWithName:create:](<init(name_create_).md>) — Returns a pasteboard that you identify by name, optionally creating it if it doesn’t exist.
- [+ pasteboardWithUniqueName](<withuniquename().md>) — Returns an app pasteboard that you identify by a unique system-generated name.

### Getting and setting pasteboard attributes

- [changeCount](changecount.md) — The number of times the pasteboard’s contents change.
