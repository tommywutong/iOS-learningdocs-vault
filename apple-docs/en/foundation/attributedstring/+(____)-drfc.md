---
title: '+(_:_:)'
framework: Foundation
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/+(_:_:)-drfc'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/+(_:_:)-drfc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/%2B%28_%3A_%3A%29-drfc.json'
content_hash: 'sha256:15af35908d2afde0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# +(_:_:)

<sub>Operator</sub>

Concatenates two attributed strings or substrings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func + (lhs: AttributedString, rhs: some AttributedStringProtocol) -> AttributedString
```

## Parameters

- `lhs` — An attributed string or substring to concatenate.

- `rhs` — Another attributed string or substring to concatenate.

## Return Value

The result of concatenating `rhs` to the end of `lhs`.

## See Also

### Combining Attributed Strings

- [append(_:)](<append(__).md>) — Appends a string to the attributed string.
- [+(_:_:)](<+(____)-8sbsq.md>) — Concatenates two attributed strings.
- [+=(_:_:)](<+=(____)-4dk88.md>) — Appends an attributed string to another attributed string.
- [+=(_:_:)](<+=(____)-6yimu.md>) — Appends an attributed string or substring to another attributed string.
