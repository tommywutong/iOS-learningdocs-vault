---
title: 'init(cgColor:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolor/init(cgcolor:)-27r9g'
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/init(cgcolor:)-27r9g'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/init%28cgcolor%3A%29-27r9g.json'
content_hash: 'sha256:6fd5d763b31a6c74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# init(cgColor:)

<sub>Initializer</sub>

Creates a color object using the specified Quartz color reference.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(cgColor: CGColor)
```

## Parameters

- `cgColor` — A reference to a Quartz color.

## Return Value

An initialized color object. The color information represented by this object is in the native colorspace of the specified Quartz color.

## See Also

### Creating a color from another color object

- [init(_:)](<init(__).md>) — Creates a color object that encapsulates a SwiftUI color.
- [- initWithCIColor:](<init(cicolor_)-2z057.md>) — Creates a color object that encapsulates a Core Image color.
- [- colorWithAlphaComponent:](<withalphacomponent(__).md>) — Creates a color object that has the same color space and component values as the receiver, but has the specified alpha component.
