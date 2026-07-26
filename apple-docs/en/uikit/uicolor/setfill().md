---
title: setFill()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicolor/setfill()
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/setfill()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/setfill%28%29.json'
content_hash: 'sha256:6f1e6d97ef2d4814'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# setFill()

<sub>Instance Method</sub>

Sets the color of subsequent fill operations to the color that the receiver represents.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func setFill()
```

## Discussion

If you subclass `UIColor`, you must implement this method in your subclass. Your custom implementation should modify the fill color in the current graphics context by setting it to the color represented by the receiver.

## See Also

### Applying the color to the drawing environment

- [Customizing drawings](../customizing-drawings.md) — Create custom colors and patterns for drawing in your app.
- [- set](<set().md>) — Sets the color of subsequent stroke and fill operations to the color that the receiver represents.
- [- setStroke](<setstroke().md>) — Sets the color of subsequent stroke operations to the color that the receiver represents.
