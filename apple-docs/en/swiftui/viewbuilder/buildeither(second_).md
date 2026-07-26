---
title: 'buildEither(second:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/viewbuilder/buildeither(second:)'
source_url: 'https://developer.apple.com/documentation/swiftui/viewbuilder/buildeither(second:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewbuilder/buildeither%28second%3A%29.json'
content_hash: 'sha256:7316cf9aa189f281'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ViewBuilder](../viewbuilder.md)

# buildEither(second:)

<sub>Type Method</sub>

Produces content for a conditional statement in a multi-statement closure when the condition is false.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalContent<TrueContent, FalseContent>
```

## See Also

### Conditionally building content

- [buildEither(first:)](<buildeither(first_).md>) — Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [buildIf(_:)](<buildif(__).md>) — Produces optional content for conditional statements in multi-statement closures that’s only included when the condition evaluates to true.
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>)
