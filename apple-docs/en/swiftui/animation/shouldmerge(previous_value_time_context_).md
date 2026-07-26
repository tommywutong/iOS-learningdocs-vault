---
title: 'shouldMerge(previous:value:time:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animation/shouldmerge(previous:value:time:context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animation/shouldmerge(previous:value:time:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/shouldmerge%28previous%3Avalue%3Atime%3Acontext%3A%29.json'
content_hash: 'sha256:f5cab0cf1e2ab9f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# shouldMerge(previous:value:time:context:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the current animation should merge with a previous animation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func shouldMerge<V>(previous: Animation, value: V, time: TimeInterval, context: inout AnimationContext<V>) -> Bool where V : VectorArithmetic
```
