---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/menuactiondismissbehavior/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/menuactiondismissbehavior/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menuactiondismissbehavior/automatic.json'
content_hash: 'sha256:e9794d816bd9995c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MenuActionDismissBehavior](../menuactiondismissbehavior.md)

# automatic

<sub>Type Property</sub>

Use the a dismissal behavior that’s appropriate for the given context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let automatic: MenuActionDismissBehavior
```

## Discussion

In most cases, the default behavior is [enabled](enabled.md). There are some cases, like [Stepper](../stepper.md), that use [disabled](disabled.md) by default.

## See Also

### Getting dismiss behaviors

- [disabled](disabled.md) — Never dismiss the presented menu after performing an action.
- [enabled](enabled.md) — Always dismiss the presented menu after performing an action.
