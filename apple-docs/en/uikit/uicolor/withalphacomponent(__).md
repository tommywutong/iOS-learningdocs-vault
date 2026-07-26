---
title: 'withAlphaComponent(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolor/withalphacomponent(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/withalphacomponent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/withalphacomponent%28_%3A%29.json'
content_hash: 'sha256:2152c29e9f6614f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# withAlphaComponent(_:)

<sub>Instance Method</sub>

Creates a color object that has the same color space and component values as the receiver, but has the specified alpha component.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func withAlphaComponent(_ alpha: CGFloat) -> UIColor
```

## Parameters

- `alpha` — The opacity value of the new color object, specified as a value from 0.0 to 1.0. Alpha values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.

## Return Value

The new `UIColor` object.

## Discussion

A subclass with explicit opacity components should override this method to return a color with the specified alpha.

## See Also

### Creating a color from another color object

- [init(_:)](<init(__).md>) — Creates a color object that encapsulates a SwiftUI color.
- [- initWithCIColor:](<init(cicolor_)-2z057.md>) — Creates a color object that encapsulates a Core Image color.
- [- initWithCGColor:](<init(cgcolor_)-27r9g.md>) — Creates a color object using the specified Quartz color reference.
