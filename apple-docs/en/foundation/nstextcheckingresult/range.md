---
title: range
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstextcheckingresult/range
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/range'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/range.json'
content_hash: 'sha256:4fd1fd0cca51f24f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# range

<sub>Instance Property</sub>

Returns the range of the result that the receiver represents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var range: NSRange { get }
```

## Discussion

This property will be present for all returned `NSTextCheckingResult` instances.

## See Also

### Text Checking Type Range and Type

- [resultType](resulttype.md) — Returns the text checking result type that the receiver represents.
- [numberOfRanges](numberofranges.md) — Returns the number of ranges.
- [- rangeAtIndex:](<range(at_).md>) — Returns the result type that the range represents.
