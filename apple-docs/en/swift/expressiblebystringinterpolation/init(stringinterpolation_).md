---
title: 'init(stringInterpolation:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/expressiblebystringinterpolation/init(stringinterpolation:)'
source_url: 'https://developer.apple.com/documentation/swift/expressiblebystringinterpolation/init(stringinterpolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/expressiblebystringinterpolation/init%28stringinterpolation%3A%29.json'
content_hash: 'sha256:ce2e337c8dac64c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ExpressibleByStringInterpolation](../expressiblebystringinterpolation.md)

# init(stringInterpolation:)

<sub>Initializer</sub>

Creates an instance from a string interpolation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(stringInterpolation: Self.StringInterpolation)
```

## Parameters

- `stringInterpolation` — An instance of `StringInterpolation` which has had each segment of the string literal appended to it.

## Discussion

Most `StringInterpolation` types will store information about the literals and interpolations appended to them in one or more properties. `init(stringInterpolation:)` should use these properties to initialize the instance.

## Default Implementations

### ExpressibleByStringInterpolation Implementations

- [init(stringInterpolation:)](<init(stringinterpolation_)-hhnp.md>) — Creates a new instance from an interpolated string literal.
