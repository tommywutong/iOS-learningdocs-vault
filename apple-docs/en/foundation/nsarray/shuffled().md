---
title: shuffled()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsarray/shuffled()
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/shuffled()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/shuffled%28%29.json'
content_hash: 'sha256:b5da93d3169f7938'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# shuffled()

<sub>Instance Method</sub>

Returns a new array that lists this array’s elements in a random order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func shuffled() -> [Any]
```

## Return Value

A new array that lists this array’s elements in a random order.

## Discussion

Calling this method is equivalent to calling the [- shuffledArrayWithRandomSource:](<shuffled(using_).md>) method and passing the system [sharedRandom()](<../../gameplaykit/gkrandomsource/sharedrandom().md>) random source. To influence the random shuffling or to be able to deterministically reproduce a series of shuffles, create your own [GKRandomSource](../../gameplaykit/gkrandomsource.md) object.

## See Also

### Randomly Shuffling an Array

- [- shuffledArrayWithRandomSource:](<shuffled(using_).md>) — Returns a new array that lists this array’s elements in a random order, using the specified random source.
