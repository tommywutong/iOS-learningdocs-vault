---
title: withUniqueName()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/withuniquename()
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/withuniquename()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/withuniquename%28%29.json'
content_hash: 'sha256:67e7bd2824832701'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# withUniqueName()

<sub>Type Method</sub>

Returns an app pasteboard that you identify by a unique system-generated name.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class func withUniqueName() -> UIPasteboard
```

## Return Value

An app pasteboard object with a unique name.

## Discussion

Obtain the value of the [name](name-swift.property.md) property to discover the name of the returned pasteboard. App pasteboards returned by this method are not persistent, existing only until the app quits. Starting in iOS 10, persistent named pasteboards are deprecated. Instead use a shared container, as described in the overview for the [UIPasteboard](../uipasteboard.md) class.

## See Also

### Getting and removing pasteboards

- [generalPasteboard](general.md) — The systemwide general pasteboard, which you use for general copy-paste operations.
- [+ pasteboardWithName:create:](<init(name_create_).md>) — Returns a pasteboard that you identify by name, optionally creating it if it doesn’t exist.
- [+ removePasteboardWithName:](<remove(withname_).md>) — Invalidates the designated app pasteboard.
