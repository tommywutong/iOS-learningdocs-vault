---
title: 'CFRangeMake(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrangemake(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrangemake(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrangemake%28_%3A_%3A%29.json'
content_hash: 'sha256:b10d122ce89dcdf5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRangeMake(_:_:)

<sub>Function</sub>

Declares and initializes a `CFRange` structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRangeMake(_ loc: CFIndex, _ len: CFIndex) -> CFRange
```

## Parameters

- `loc` — The starting location of the range.

- `len` — The length of the range.

## Return Value

An initialized structure of type [CFRange](cfrange.md).

## Discussion

This is an in-line convenience function for creating initialized [CFRange](cfrange.md) structures.
