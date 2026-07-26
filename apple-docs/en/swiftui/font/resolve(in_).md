---
title: 'resolve(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/font/resolve(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/font/resolve(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/resolve%28in%3A%29.json'
content_hash: 'sha256:843c791c2efb9b23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# resolve(in:)

<sub>Instance Method</sub>

Evaluates this font to a resolved font given the current context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resolve(in context: Font.Context) -> Font.Resolved
```

## Discussion

The system resolves a font’s value at the time it uses the font in a given environment’s context because [Font](../font.md) is a late-binding token.

> [!info] See Also
> [fontResolutionContext](../environmentvalues/fontresolutioncontext.md)
