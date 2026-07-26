---
title: runs
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/runs-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/runs-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/runs-swift.property.json'
content_hash: 'sha256:41360a0daba829ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# runs

<sub>Instance Property</sub>

The attributed runs of the attributed string, as a view into the underlying string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var runs: AttributedString.Runs { get }
```

## Discussion

Runs begin and end when the attributes for the characters change. Use this property to iterate over the runs with `for`-`in` syntax.

## See Also

### Accessing Views into the Attributed String

- [characters](characters.md) — The characters of the attributed string, as a view into the underlying string.
- [CharacterView](characterview.md) — A view into the underlying storage of the attributed string, as Unicode characters.
- [unicodeScalars](unicodescalars.md) — The Unicode scalars of the attributed string, as a view into the underlying string.
- [UnicodeScalarView](unicodescalarview.md) — A view into the underlying storage of the attributed string, as Unicode scalars.
- [Runs](runs-swift.struct.md) — An iterable view into segments of the attributed string, each of which indicates where a run of identical attributes begins or ends.
