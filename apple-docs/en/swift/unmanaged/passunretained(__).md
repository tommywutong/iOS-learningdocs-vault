---
title: 'passUnretained(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unmanaged/passunretained(_:)'
source_url: 'https://developer.apple.com/documentation/swift/unmanaged/passunretained(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unmanaged/passunretained%28_%3A%29.json'
content_hash: 'sha256:cf79dfe4da02d9e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Unmanaged](../unmanaged.md)

# passUnretained(_:)

<sub>Type Method</sub>

Creates an unmanaged reference without performing an unbalanced retain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func passUnretained(_ value: Instance) -> Unmanaged<Instance>
```

## Parameters

- `value` — A class instance.

## Return Value

An unmanaged reference to the object passed as `value`.

## Discussion

This is useful when passing a reference to an API which Swift does not know the ownership rules for, but you know that the API expects you to pass the object at +0.

```swift
CFArraySetValueAtIndex(.passUnretained(array), i,
                       .passUnretained(object))
```
