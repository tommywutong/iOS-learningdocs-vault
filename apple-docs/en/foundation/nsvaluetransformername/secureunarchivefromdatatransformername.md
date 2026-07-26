---
title: secureUnarchiveFromDataTransformerName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsvaluetransformername/secureunarchivefromdatatransformername
source_url: 'https://developer.apple.com/documentation/foundation/nsvaluetransformername/secureunarchivefromdatatransformername'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvaluetransformername/secureunarchivefromdatatransformername.json'
content_hash: 'sha256:ef7d6d6e0dd7baed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValueTransformerName](../nsvaluetransformername.md)

# secureUnarchiveFromDataTransformerName

<sub>Type Property</sub>

The name of the value transformer that creates then returns an object by attempting to unarchive the data to a class that supports secure coding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let secureUnarchiveFromDataTransformerName: NSValueTransformerName
```

## Discussion

The transformer this property references returns the [NSData](../nsdata.md) instance created by archiving the value using secure keyed archiving. This transformer requires that an object implement the [NSSecureCoding](../nssecurecoding.md) protocol in order to archive and unarchive with this transformer.

## See Also

### Type Properties

- [NSIsNilTransformerName](isniltransformername.md) — This value transformer returns true if the value is nil.
- [NSIsNotNilTransformerName](isnotniltransformername.md) — This value transformer returns true if the value is non-nil.
- [NSKeyedUnarchiveFromDataTransformerName](keyedunarchivefromdatatransformername.md) — The name of the value transformer that attempts to unarchive data stored inside a keyed archive in an object you provide. _(deprecated)_
- [NSNegateBooleanTransformerName](negatebooleantransformername.md) — This value transformer negates a boolean value, transforming true to false and false to true.
- [NSUnarchiveFromDataTransformerName](unarchivefromdatatransformername.md) — The name of the value transformer that attempts to unarchive data from an object you provide. _(deprecated)_
