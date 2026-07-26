---
title: unicodeScalars
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedsubstring/unicodescalars
source_url: 'https://developer.apple.com/documentation/foundation/attributedsubstring/unicodescalars'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedsubstring/unicodescalars.json'
content_hash: 'sha256:d3b50a52c735b21e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedSubstring](../attributedsubstring.md)

# unicodeScalars

<sub>Instance Property</sub>

The Unicode scalars of the attributed string, as a view into the underlying string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var unicodeScalars: AttributedString.UnicodeScalarView { get }
```

## See Also

### Accessing Views into the Attributed Substring

- [characters](characters.md) — The characters of the attributed string, as a view into the underlying string.
- [CharacterView](../attributedstring/characterview.md) — A view into the underlying storage of the attributed string, as Unicode characters.
- [UnicodeScalarView](../attributedstring/unicodescalarview.md) — A view into the underlying storage of the attributed string, as Unicode scalars.
- [runs](runs.md) — The attributed runs of the attributed string, as a view into the underlying string.
- [Runs](../attributedstring/runs-swift.struct.md) — An iterable view into segments of the attributed string, each of which indicates where a run of identical attributes begins or ends.
