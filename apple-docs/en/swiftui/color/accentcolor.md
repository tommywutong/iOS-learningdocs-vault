---
title: accentColor
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/color/accentcolor
source_url: 'https://developer.apple.com/documentation/swiftui/color/accentcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/accentcolor.json'
content_hash: 'sha256:8f480ee9520a1d40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# accentColor

<sub>Type Property</sub>

A color that reflects the accent color of the system or app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var accentColor: Color { get }
```

## Discussion

The accent color is a broad theme color applied to views and controls. You can set it at the application level by specifying an accent color in your app’s asset catalog.

> [!note] Note
> In macOS, SwiftUI applies customization of the accent color only if the user chooses Multicolor under General \> Accent color in System Preferences.

The following code renders a [Text](../text.md) view using the app’s accent color:

```swift
Text("Accent Color")
    .foregroundStyle(Color.accentColor)
```

## See Also

### Getting semantic colors

- [primary](primary.md) — The color to use for primary content.
- [secondary](secondary.md) — The color to use for secondary content.
