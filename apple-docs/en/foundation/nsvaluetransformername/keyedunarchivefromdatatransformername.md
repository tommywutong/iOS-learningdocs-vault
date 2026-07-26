---
title: keyedUnarchiveFromDataTransformerName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+（12.0 起废弃）, iPadOS 3.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.3+（10.14 起废弃）, tvOS 9.0+（12.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（5.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsvaluetransformername/keyedunarchivefromdatatransformername
source_url: 'https://developer.apple.com/documentation/foundation/nsvaluetransformername/keyedunarchivefromdatatransformername'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvaluetransformername/keyedunarchivefromdatatransformername.json'
content_hash: 'sha256:2ea695b2fc64753e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValueTransformerName](../nsvaluetransformername.md)

# keyedUnarchiveFromDataTransformerName

<sub>Type Property</sub>

The name of the value transformer that attempts to unarchive data stored inside a keyed archive in an object you provide.

> [!warning] Deprecated
> Use [NSSecureUnarchiveFromDataTransformerName](secureunarchivefromdatatransformername.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let keyedUnarchiveFromDataTransformerName: NSValueTransformerName
```

## Discussion

The transformer this property references returns the [NSData](../nsdata.md) instance created by archiving the value using keyed archiving. This transformer requires that an object implement the [NSCoding](../nscoding.md) protocol using keyed archiving in order to archive and unarchive with this transformer.

## See Also

### Type Properties

- [NSIsNilTransformerName](isniltransformername.md) — This value transformer returns true if the value is nil.
- [NSIsNotNilTransformerName](isnotniltransformername.md) — This value transformer returns true if the value is non-nil.
- [NSNegateBooleanTransformerName](negatebooleantransformername.md) — This value transformer negates a boolean value, transforming true to false and false to true.
- [NSUnarchiveFromDataTransformerName](unarchivefromdatatransformername.md) — The name of the value transformer that attempts to unarchive data from an object you provide. _(deprecated)_
- [NSSecureUnarchiveFromDataTransformerName](secureunarchivefromdatatransformername.md) — The name of the value transformer that creates then returns an object by attempting to unarchive the data to a class that supports secure coding.
