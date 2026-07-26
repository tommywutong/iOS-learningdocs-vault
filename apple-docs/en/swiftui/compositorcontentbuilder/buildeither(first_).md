---
title: 'buildEither(first:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/compositorcontentbuilder/buildeither(first:)'
source_url: 'https://developer.apple.com/documentation/swiftui/compositorcontentbuilder/buildeither(first:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/compositorcontentbuilder/buildeither%28first%3A%29.json'
content_hash: 'sha256:8d673d24a3c7066b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CompositorContentBuilder](../compositorcontentbuilder.md)

# buildEither(first:)

<sub>Type Method</sub>

Produces content for a conditional statement in a multi-statement closure when the condition is true.

<sub>macOS, visionOS</sub>

```swift
@export(implementation) static func buildEither<F>(first: _ConditionalContent<_LimitedAvailabilityCompositorContent, _LimitedAvailabilityCompositorContent>) -> _ConditionalContent<_LimitedAvailabilityCompositorContent, F> where F : CompositorContent
```

## Discussion

Conditional statements in a [CompositorContentBuilder](../compositorcontentbuilder.md) must contain both an `if` statement and an `else` statement, and the condition can only perform a compiler check for availability, like in the following code:

```swift
var body: some CompositorContent {
    if #available(visionOS 100, *) {
        MyNewContent()
    } else {
        MyOldContent()
    }
}
```
