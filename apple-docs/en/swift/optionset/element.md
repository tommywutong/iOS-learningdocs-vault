---
title: Element
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/optionset/element
source_url: 'https://developer.apple.com/documentation/swift/optionset/element'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/optionset/element.json'
content_hash: 'sha256:6603f0932d4d3a70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OptionSet](../optionset.md)

# Element

<sub>Associated Type</sub>

The element type of the option set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Element = Self
```

## Discussion

To inherit all the default implementations from the `OptionSet` protocol, the `Element` type must be `Self`, the default.
