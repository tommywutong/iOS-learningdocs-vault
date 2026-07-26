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
doc_path: /documentation/foundation/attributedsubstring/runs
source_url: 'https://developer.apple.com/documentation/foundation/attributedsubstring/runs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedsubstring/runs.json'
content_hash: 'sha256:529af377f89d6cfa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedSubstring](../attributedsubstring.md)

# runs

<sub>Instance Property</sub>

The attributed runs of the attributed string, as a view into the underlying string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var runs: AttributedString.Runs { get }
```

## See Also

### Accessing Views into the Attributed Substring

- [characters](characters.md) — The characters of the attributed string, as a view into the underlying string.
- [CharacterView](../attributedstring/characterview.md) — A view into the underlying storage of the attributed string, as Unicode characters.
- [unicodeScalars](unicodescalars.md) — The Unicode scalars of the attributed string, as a view into the underlying string.
- [UnicodeScalarView](../attributedstring/unicodescalarview.md) — A view into the underlying storage of the attributed string, as Unicode scalars.
- [Runs](../attributedstring/runs-swift.struct.md) — An iterable view into segments of the attributed string, each of which indicates where a run of identical attributes begins or ends.
