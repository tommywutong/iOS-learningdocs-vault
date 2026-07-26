---
title: 'randomSplit(by:seed:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/sequence/randomsplit(by:seed:)-9637d'
source_url: 'https://developer.apple.com/documentation/swift/sequence/randomsplit(by:seed:)-9637d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/randomsplit%28by%3Aseed%3A%29-9637d.json'
content_hash: 'sha256:ed8edf49323ab898'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# randomSplit(by:seed:)

<sub>Instance Method</sub>

Generates two generic arrays by randomly splitting the elements of the sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func randomSplit<T>(by proportion: Double, seed: Int? = nil) -> (ArraySlice<T>, ArraySlice<T>) where T == Self.Element
```

## Parameters

- `proportion` — A proportion in the range `[0.0, 1.0]`.

- `seed` — A seed number for a random-number generator.

## Return Value

A tuple of array slices.
