---
title: set()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicolor/set()
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/set()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/set%28%29.json'
content_hash: 'sha256:56b073dd85a7d41e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# set()

<sub>Instance Method</sub>

Sets the color of subsequent stroke and fill operations to the color that the receiver represents.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func set()
```

## Discussion

If you subclass `UIColor`, you must implement this method in your subclass. Your custom implementation should modify both the stroke and fill color in the current graphics context by setting them both to the color represented by the receiver.

## See Also

### Applying the color to the drawing environment

- [Customizing drawings](../customizing-drawings.md) — Create custom colors and patterns for drawing in your app.
- [- setFill](<setfill().md>) — Sets the color of subsequent fill operations to the color that the receiver represents.
- [- setStroke](<setstroke().md>) — Sets the color of subsequent stroke operations to the color that the receiver represents.
