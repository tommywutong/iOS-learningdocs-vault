---
title: clear
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/glass/clear
source_url: 'https://developer.apple.com/documentation/swiftui/glass/clear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/glass/clear.json'
content_hash: 'sha256:fc5dae4f35fd2184'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Glass](../glass.md)

# clear

<sub>Type Property</sub>

The clear variant of glass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
static var clear: Glass { get }
```

## Discussion

When using clear glass, ensure content remains legible by adding a dimming layer or other treatment beneath the glass.

For example, you could add a transparent black color beneath your glass to ensure content remains legible above the glass.

```swift
Label("Flag", systemImage: "flag.fill")
    .padding()
    .glassEffect(.clear)
    .background(.black.opacity(0.3))
```
