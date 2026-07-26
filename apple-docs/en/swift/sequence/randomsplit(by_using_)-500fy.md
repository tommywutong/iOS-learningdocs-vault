---
title: 'randomSplit(by:using:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/sequence/randomsplit(by:using:)-500fy'
source_url: 'https://developer.apple.com/documentation/swift/sequence/randomsplit(by:using:)-500fy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/randomsplit%28by%3Ausing%3A%29-500fy.json'
content_hash: 'sha256:9f53a8e129b9e7e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# randomSplit(by:using:)

<sub>Instance Method</sub>

Generates two generic arrays by randomly splitting the elements of the sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func randomSplit<T, Generator>(by proportion: Double, using generator: inout Generator) -> (ArraySlice<T>, ArraySlice<T>) where T == Self.Element, Generator : RandomNumberGenerator
```

## Parameters

- `proportion` — A proportion in the range `[0.0, 1.0]`.

- `generator` — A random-number generator.

## Return Value

A tuple of array slices.
