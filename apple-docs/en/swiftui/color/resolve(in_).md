---
title: 'resolve(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/color/resolve(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/color/resolve(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/resolve%28in%3A%29.json'
content_hash: 'sha256:acddbc01ba91322d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# resolve(in:)

<sub>Instance Method</sub>

Evaluates this color to a resolved color given the current `context`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resolve(in environment: EnvironmentValues) -> Color.Resolved
```

## See Also

### Creating a color

- [init(_:bundle:)](<init(__bundle_).md>) — Creates a color from a color set that you indicate by name.
- [init(_:)](<init(__).md>) — Creates a constant color with the values specified by the resolved color.
