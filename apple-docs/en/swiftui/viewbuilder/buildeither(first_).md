---
title: 'buildEither(first:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/viewbuilder/buildeither(first:)'
source_url: 'https://developer.apple.com/documentation/swiftui/viewbuilder/buildeither(first:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewbuilder/buildeither%28first%3A%29.json'
content_hash: 'sha256:7db405172bba55f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ViewBuilder](../viewbuilder.md)

# buildEither(first:)

<sub>Type Method</sub>

Produces content for a conditional statement in a multi-statement closure when the condition is true.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalContent<TrueContent, FalseContent>
```

## See Also

### Conditionally building content

- [buildEither(second:)](<buildeither(second_).md>) — Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [buildIf(_:)](<buildif(__).md>) — Produces optional content for conditional statements in multi-statement closures that’s only included when the condition evaluates to true.
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>)
