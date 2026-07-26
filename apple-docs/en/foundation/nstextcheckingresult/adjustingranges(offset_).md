---
title: 'adjustingRanges(offset:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstextcheckingresult/adjustingranges(offset:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/adjustingranges(offset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/adjustingranges%28offset%3A%29.json'
content_hash: 'sha256:82d7d102453348cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# adjustingRanges(offset:)

<sub>Instance Method</sub>

Returns a new text checking result after adjusting the ranges as specified by the offset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func adjustingRanges(offset: Int) -> NSTextCheckingResult
```

## Parameters

- `offset` — The amount the ranges are adjusted.

## Return Value

A new `NSTextCheckingResult` instance with the adjusted range or ranges.
