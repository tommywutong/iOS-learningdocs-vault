---
title: 'resolveHDR(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/color/resolvehdr(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/color/resolvehdr(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/resolvehdr%28in%3A%29.json'
content_hash: 'sha256:2a18de629f55b05e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# resolveHDR(in:)

<sub>Instance Method</sub>

Evaluates this color to a resolved color with content headroom, given a set of environment values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resolveHDR(in environment: EnvironmentValues) -> Color.ResolvedHDR
```

## Parameters

- `environment` — The environment of the view displaying the color.

## Return Value

The color’s value in the sRGB color space.

## See Also

### Working with high dynamic range (HDR) colors

- [ResolvedHDR](resolvedhdr.md) — A concrete color value, including HDR headroom information.
