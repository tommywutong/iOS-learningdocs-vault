---
title: 'range(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstextcheckingresult/range(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/range(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/range%28at%3A%29.json'
content_hash: 'sha256:2330b289439f516e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# range(at:)

<sub>Instance Method</sub>

Returns the result type that the range represents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func range(at idx: Int) -> NSRange
```

## Parameters

- `idx` — The index of the result.

## Return Value

The range of the result.

## Discussion

A result must have at least one range, but may optionally have more, for example, to represent regular expression capture groups.

Passing [- rangeAtIndex:](<range(at_).md>) the value `0` always returns the value of the [range](range.md) property. Additional ranges, if any, will have indexes from `1` to `numberOfRanges``-1`.

## See Also

### Text Checking Type Range and Type

- [range](range.md) — Returns the range of the result that the receiver represents.
- [resultType](resulttype.md) — Returns the text checking result type that the receiver represents.
- [numberOfRanges](numberofranges.md) — Returns the number of ranges.
