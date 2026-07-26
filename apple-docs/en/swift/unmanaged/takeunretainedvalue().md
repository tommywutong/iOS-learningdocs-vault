---
title: takeUnretainedValue()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unmanaged/takeunretainedvalue()
source_url: 'https://developer.apple.com/documentation/swift/unmanaged/takeunretainedvalue()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unmanaged/takeunretainedvalue%28%29.json'
content_hash: 'sha256:dd04e18de5fa9151'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Unmanaged](../unmanaged.md)

# takeUnretainedValue()

<sub>Instance Method</sub>

Gets the value of this unmanaged reference as a managed reference without consuming an unbalanced retain of it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func takeUnretainedValue() -> Instance
```

## Return Value

The object referenced by this `Unmanaged` instance.

## Discussion

This is useful when a function returns an unmanaged reference and you know that you’re not responsible for releasing the result.
