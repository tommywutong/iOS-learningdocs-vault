---
title: grammarDetails
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstextcheckingresult/grammardetails
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/grammardetails'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/grammardetails.json'
content_hash: 'sha256:e49a5671cba6322f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# grammarDetails

<sub>Instance Property</sub>

The details of a located grammatical type checking result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var grammarDetails: [[String : Any]]? { get }
```

## Discussion

This array of strings is suitable for presenting to the user.

## See Also

### Text Checking Results for Grammar

- [+ grammarCheckingResultWithRange:details:](<grammarcheckingresult(range_details_).md>) — Creates and returns a text checking result with the specified array of grammatical errors.
