---
title: components
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstextcheckingresult/components
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/components'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/components.json'
content_hash: 'sha256:7df530e2b84560b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# components

<sub>Instance Property</sub>

A dictionary containing the components of a type checking result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var components: [NSTextCheckingKey : String]? { get }
```

## Discussion

Currently used by the transit checking result. The supported keys are located in [Keys for Transit Components](../keys-for-transit-components.md).

## See Also

### Related Documentation

- [+ transitInformationCheckingResultWithRange:components:](<transitinformationcheckingresult(range_components_).md>) — Creates and returns a text checking result with the specified transit information.
