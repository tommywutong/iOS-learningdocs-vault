---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/font/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/font/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/init%28_%3A%29.json'
content_hash: 'sha256:605cc218eb305311'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# init(_:)

<sub>Initializer</sub>

Creates a custom font from a platform font instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ font: CTFont)
```

## Discussion

Initializing [Font](../font.md) with platform font instance (doc://com.apple.documentation/documentation/CoreText/CTFont-q6r) can bridge SwiftUI [Font](../font.md) with [NSFont](../../appkit/nsfont.md) or [UIFont](../../uikit/uifont.md), both of which are toll-free bridged to doc://com.apple.documentation/documentation/CoreText/CTFont-q6r. For example:

```swift
// Use native Core Text API to create desired ctFont.
let ctFont = CTFontCreateUIFontForLanguage(.system, 12, nil)!

// Create SwiftUI Text with the CTFont instance.
let text = Text("Hello").font(Font(ctFont))
```
