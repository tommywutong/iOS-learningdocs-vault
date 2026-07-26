---
title: 'bold(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/font/bold(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/font/bold(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/bold%28_%3A%29.json'
content_hash: 'sha256:f9baa8fb85906e8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# bold(_:)

<sub>Instance Method</sub>

Adds or removes bold or emphasized styling on the font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func bold(_ isActive: Bool) -> Font
```

## Discussion

For fonts created from text styles, passing `true` could mean applying emphasized styling, which does not necessarily mean the bold weight specifically, so this modifier is not to be confused with [weight(_:)](<weight(__).md>).

For example:

```swift
Font.body.bold(true)
```

will most likely get you the emphasized version of body text style, which is often in [semibold](weight/semibold.md) weight. While

```swift
Font.body.weight(.bold)
```

will specifically get you the body text style font in the [bold](weight/bold.md) weight.

Using:

```swift
Font.body.bold(false)
```

will remove any emphasized styling from the font returning to its default weight which is most likely but not guaranteed to be 0.0 or [regular](weight/regular.md).
