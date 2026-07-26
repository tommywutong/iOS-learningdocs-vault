---
title: layoutManager
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/layoutmanager
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/layoutmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/layoutmanager.json'
content_hash: 'sha256:e1cf3cd875718772'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# layoutManager

<sub>Instance Property</sub>

The layout manager that lays out text for the text view’s text container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var layoutManager: NSLayoutManager { get }
```

## Discussion

This property is a convenience accessor that provides access through the text container.

## See Also

### Accessing TextKit Objects

- [textLayoutManager](textlayoutmanager.md) — The text layout manager that lays out text for the text view’s text container.
- [textContainer](textcontainer.md) — The text container object that defines the area where text displays in the text view.
- [textStorage](textstorage.md) — The text storage object holding the text that displays in the text view.
