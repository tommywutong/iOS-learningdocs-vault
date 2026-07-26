---
title: caseSensitive
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/scanner/casesensitive
source_url: 'https://developer.apple.com/documentation/foundation/scanner/casesensitive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/scanner/casesensitive.json'
content_hash: 'sha256:d6796889c1bef6f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Scanner](../scanner.md)

# caseSensitive

<sub>Instance Property</sub>

Flag that indicates whether the receiver distinguishes case in the characters it scans.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var caseSensitive: Bool { get set }
```

## Discussion

[true](../../swift/true.md) if the receiver distinguishes case in the characters it scans, otherwise [false](../../swift/false.md). The default value is [false](../../swift/false.md). Note that case sensitivity doesn’t apply to the characters to be skipped.

## See Also

### Configuring a Scanner

- [scanLocation](scanlocation.md) — The character position at which the receiver will begin its next scanning operation. _(deprecated)_
- [charactersToBeSkipped](characterstobeskipped.md) — Character set containing the characters the scanner ignores when looking for a scannable element.
- [locale](locale.md) — The locale to use when scanning.
