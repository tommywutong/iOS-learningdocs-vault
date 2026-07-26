---
title: isAtEnd
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/scanner/isatend
source_url: 'https://developer.apple.com/documentation/foundation/scanner/isatend'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/scanner/isatend.json'
content_hash: 'sha256:d50dc62382092ce7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Scanner](../scanner.md)

# isAtEnd

<sub>Instance Property</sub>

Flag that indicates whether the receiver has exhausted all significant characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isAtEnd: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the receiver has exhausted all significant characters in its string, otherwise [false](../../swift/false.md).

If only characters from the set to be skipped remain, returns [true](../../swift/true.md).

## See Also

### Related Documentation

- [charactersToBeSkipped](characterstobeskipped.md) — Character set containing the characters the scanner ignores when looking for a scannable element.
