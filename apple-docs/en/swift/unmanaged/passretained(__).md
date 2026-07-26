---
title: 'passRetained(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unmanaged/passretained(_:)'
source_url: 'https://developer.apple.com/documentation/swift/unmanaged/passretained(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unmanaged/passretained%28_%3A%29.json'
content_hash: 'sha256:c721bf1a9e1f6e5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Unmanaged](../unmanaged.md)

# passRetained(_:)

<sub>Type Method</sub>

Creates an unmanaged reference with an unbalanced retain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func passRetained(_ value: Instance) -> Unmanaged<Instance>
```

## Parameters

- `value` — A class instance.

## Return Value

An unmanaged reference to the object passed as `value`.

## Discussion

The instance passed as `value` will leak if nothing eventually balances the retain.

This is useful when passing an object to an API which Swift does not know the ownership rules for, but you know that the API expects you to pass the object at +1.
