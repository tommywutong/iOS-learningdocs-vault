---
title: locale
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/scanner/locale
source_url: 'https://developer.apple.com/documentation/foundation/scanner/locale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/scanner/locale.json'
content_hash: 'sha256:f0b6eee2bd0a34c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Scanner](../scanner.md)

# locale

<sub>Instance Property</sub>

The locale to use when scanning.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var locale: Any? { get set }
```

## Discussion

A scanner’s locale affects the way it interprets numeric values from the string. In particular, a scanner uses the locale’s decimal separator to distinguish the integer and fractional parts of floating-point representations. A scanner with no locale set uses non-localized values. New scanners have no locale by default.

## See Also

### Configuring a Scanner

- [scanLocation](scanlocation.md) — The character position at which the receiver will begin its next scanning operation. _(deprecated)_
- [caseSensitive](casesensitive.md) — Flag that indicates whether the receiver distinguishes case in the characters it scans.
- [charactersToBeSkipped](characterstobeskipped.md) — Character set containing the characters the scanner ignores when looking for a scannable element.
