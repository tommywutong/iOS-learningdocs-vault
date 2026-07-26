---
title: Color.Resolved
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/color/resolved
source_url: 'https://developer.apple.com/documentation/swiftui/color/resolved'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/resolved.json'
content_hash: 'sha256:572541d4e6b6f3e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# Color.Resolved

<sub>Structure</sub>

A concrete color value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Resolved
```

## Overview

`Color.Resolved` is a set of RGBA values that represent a color that can be shown. The values are stored in the Linear sRGB color space, using extended range. This is a low-level type, most colors are represented by the `Color` type.

> [!info] See Also
> `Color.ResolvedHDR`, `Color`.

## Relationships

- **Conforms To**: [Animatable](../animatable.md), [BitwiseCopyable](../../swift/bitwisecopyable.md), [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [ShapeStyle](../shapestyle.md)

## Topics

### Initializers

- [init(colorSpace:red:green:blue:opacity:)](<resolved/init(colorspace_red_green_blue_opacity_).md>) — Creates a resolved color from red, green, and blue component values.

### Instance Properties

- [blue](resolved/blue.md) — The amount of blue in the color in the sRGB color space.
- [cgColor](resolved/cgcolor.md) — A Core Graphics representation of the color.
- [green](resolved/green.md) — The amount of green in the color in the sRGB color space.
- [linearBlue](resolved/linearblue.md) — The amount of blue in the color in the sRGB linear color space.
- [linearGreen](resolved/lineargreen.md) — The amount of green in the color in the sRGB linear color space.
- [linearRed](resolved/linearred.md) — The amount of red in the color in the sRGB linear color space.
- [opacity](resolved/opacity.md) — The degree of opacity in the color, given in the range `0` to `1`.
- [red](resolved/red.md) — The amount of red in the color in the sRGB color space.
