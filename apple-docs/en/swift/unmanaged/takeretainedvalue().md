---
title: takeRetainedValue()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unmanaged/takeretainedvalue()
source_url: 'https://developer.apple.com/documentation/swift/unmanaged/takeretainedvalue()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unmanaged/takeretainedvalue%28%29.json'
content_hash: 'sha256:530d4809e74f6c0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Unmanaged](../unmanaged.md)

# takeRetainedValue()

<sub>Instance Method</sub>

Gets the value of this unmanaged reference as a managed reference and consumes an unbalanced retain of it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func takeRetainedValue() -> Instance
```

## Return Value

The object referenced by this `Unmanaged` instance.

## Discussion

This is useful when a function returns an unmanaged reference and you know that you’re responsible for releasing the result.
