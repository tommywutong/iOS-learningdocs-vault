---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/springloadingbehavior/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/springloadingbehavior/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/springloadingbehavior/automatic.json'
content_hash: 'sha256:9757ba6d90243351'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SpringLoadingBehavior](../springloadingbehavior.md)

# automatic

<sub>Type Property</sub>

The automatic spring loading behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let automatic: SpringLoadingBehavior
```

## Discussion

This defers to default component behavior for spring loading. Some components, such as `TabView`, will default to allowing spring loading; while others do not.

## See Also

### Getting the behaviors

- [enabled](enabled.md) — Spring loaded interactions will be enabled for applicable views.
- [disabled](disabled.md) — Spring loaded interactions will be disabled for applicable views.
