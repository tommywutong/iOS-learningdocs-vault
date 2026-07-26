---
title: runs
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstringprotocol/runs
source_url: 'https://developer.apple.com/documentation/foundation/attributedstringprotocol/runs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstringprotocol/runs.json'
content_hash: 'sha256:5dbf677c34717d57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedStringProtocol](../attributedstringprotocol.md)

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
- [unicodeScalars](unicodescalars.md) — The Unicode scalars of the attributed string, as a view into the underlying string.
