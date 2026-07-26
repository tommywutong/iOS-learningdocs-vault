---
title: textStorage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/textstorage
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/textstorage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/textstorage.json'
content_hash: 'sha256:40f6afed7c29b656'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# textStorage

<sub>Instance Property</sub>

The text storage object holding the text that displays in the text view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var textStorage: NSTextStorage { get }
```

## Discussion

This property is a convenience accessor that provides access through the text container.

## See Also

### Accessing TextKit Objects

- [textLayoutManager](textlayoutmanager.md) — The text layout manager that lays out text for the text view’s text container.
- [layoutManager](layoutmanager.md) — The layout manager that lays out text for the text view’s text container.
- [textContainer](textcontainer.md) — The text container object that defines the area where text displays in the text view.
