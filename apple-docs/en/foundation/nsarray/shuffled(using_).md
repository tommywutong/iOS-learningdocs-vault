---
title: 'shuffled(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/shuffled(using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/shuffled(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/shuffled%28using%3A%29.json'
content_hash: 'sha256:a83c2df8b48c7849'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# shuffled(using:)

<sub>Instance Method</sub>

Returns a new array that lists this array’s elements in a random order, using the specified random source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func shuffled(using randomSource: GKRandomSource) -> [Any]
```

## Parameters

- `randomSource` — A GameplayKit random source object.

## Return Value

A new array that lists this array’s elements in a random order.

## Discussion

Use the `randomSource` parameter to influence the random shuffling. For example, to reproduce a series of shuffles for testing, you can create a [GKARC4RandomSource](../../gameplaykit/gkarc4randomsource.md) object using the [seed](../../gameplaykit/gkarc4randomsource/seed.md) value of a previously used random source.

This method is equivalent to the [GKRandomSource](../../gameplaykit/gkrandomsource.md) method [arrayByShufflingObjects(in:)](<../../gameplaykit/gkrandomsource/arraybyshufflingobjects(in_).md>), but as an [NSArray](../nsarray.md) method it preserves generic type parameters.

## See Also

### Randomly Shuffling an Array

- [- shuffledArray](<shuffled().md>) — Returns a new array that lists this array’s elements in a random order.
