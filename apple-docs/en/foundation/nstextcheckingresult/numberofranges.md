---
title: numberOfRanges
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstextcheckingresult/numberofranges
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/numberofranges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/numberofranges.json'
content_hash: 'sha256:acb06838c7fc4615'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# numberOfRanges

<sub>Instance Property</sub>

Returns the number of ranges.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var numberOfRanges: Int { get }
```

## Discussion

A result must have at least one range, but may optionally have more (for example, to represent regular expression capture groups).

Passing [- rangeAtIndex:](<range(at_).md>) the value `0` always returns the value of the the [range](range.md) property.  Additional ranges, if any, will have indexes from `1` to `numberOfRanges``-1`.

## See Also

### Text Checking Type Range and Type

- [range](range.md) — Returns the range of the result that the receiver represents.
- [resultType](resulttype.md) — Returns the text checking result type that the receiver represents.
- [- rangeAtIndex:](<range(at_).md>) — Returns the result type that the range represents.
