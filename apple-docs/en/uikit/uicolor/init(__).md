---
title: 'init(_:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolor/init(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/init%28_%3A%29.json'
content_hash: 'sha256:05c7bdc7ee8d6954'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# init(_:)

<sub>Initializer</sub>

Creates a color object that encapsulates a SwiftUI color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
convenience init(_ color: Color)
```

## Parameters

- `color` — The initial color value, which can belong to any available color space.

## See Also

### Creating a color from another color object

- [- initWithCIColor:](<init(cicolor_)-2z057.md>) — Creates a color object that encapsulates a Core Image color.
- [- initWithCGColor:](<init(cgcolor_)-27r9g.md>) — Creates a color object using the specified Quartz color reference.
- [- colorWithAlphaComponent:](<withalphacomponent(__).md>) — Creates a color object that has the same color space and component values as the receiver, but has the specified alpha component.
