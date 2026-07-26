---
title: addressComponents
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstextcheckingresult/addresscomponents
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/addresscomponents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/addresscomponents.json'
content_hash: 'sha256:b7f18dce45c05574'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# addressComponents

<sub>Instance Property</sub>

The address dictionary of a type checking result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var addressComponents: [NSTextCheckingKey : String]? { get }
```

## Discussion

The dictionary keys are described in [Keys for Address Components](../keys-for-address-components.md).

## See Also

### Text Checking Results for Addresses

- [+ addressCheckingResultWithRange:components:](<addresscheckingresult(range_components_).md>) — Creates and returns a text checking result with the specified address components.
