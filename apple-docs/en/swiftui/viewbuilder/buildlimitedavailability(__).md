---
title: 'buildLimitedAvailability(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/viewbuilder/buildlimitedavailability(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/viewbuilder/buildlimitedavailability(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewbuilder/buildlimitedavailability%28_%3A%29.json'
content_hash: 'sha256:e11b6893cf99a185'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ViewBuilder](../viewbuilder.md)

# buildLimitedAvailability(_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@export(implementation) static func buildLimitedAvailability(_ content: any Commands) -> some Commands

```

## See Also

### Conditionally building content

- [buildEither(first:)](<buildeither(first_).md>) — Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [buildEither(second:)](<buildeither(second_).md>) — Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [buildIf(_:)](<buildif(__).md>) — Produces optional content for conditional statements in multi-statement closures that’s only included when the condition evaluates to true.
