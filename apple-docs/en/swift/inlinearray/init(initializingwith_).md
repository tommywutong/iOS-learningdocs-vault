---
title: 'init(initializingWith:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/inlinearray/init(initializingwith:)'
source_url: 'https://developer.apple.com/documentation/swift/inlinearray/init(initializingwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/inlinearray/init%28initializingwith%3A%29.json'
content_hash: 'sha256:aac6440bb62aae0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [InlineArray](../inlinearray.md)

# init(initializingWith:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<E>(initializingWith initializer: @_lifetime(0: copy 0) (inout OutputSpan<Element>) throws(E) -> Void) throws(E) where E : Error
```
