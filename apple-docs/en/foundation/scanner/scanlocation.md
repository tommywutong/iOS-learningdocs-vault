---
title: scanLocation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.15 起废弃）, tvOS 9.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（6.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/scanner/scanlocation
source_url: 'https://developer.apple.com/documentation/foundation/scanner/scanlocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/scanner/scanlocation.json'
content_hash: 'sha256:0b654f25fe924912'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Scanner](../scanner.md)

# scanLocation

<sub>Instance Property</sub>

The character position at which the receiver will begin its next scanning operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var scanLocation: Int { get set }
```

## Discussion

Raises an `NSRangeException` if `index` is beyond the end of the string being scanned.

This property is useful for backing up to rescan after an error.

Rather than setting the scan location directly to skip known sequences of characters, use [- scanString:intoString:](<scanstring(__into_).md>) or [- scanCharactersFromSet:intoString:](<scancharacters(from_into_).md>), which allow you to verify that the expected substring (or set of characters) is in fact present.

## See Also

### Configuring a Scanner

- [caseSensitive](casesensitive.md) — Flag that indicates whether the receiver distinguishes case in the characters it scans.
- [charactersToBeSkipped](characterstobeskipped.md) — Character set containing the characters the scanner ignores when looking for a scannable element.
- [locale](locale.md) — The locale to use when scanning.
