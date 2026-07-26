---
title: unarchiveFromDataTransformerName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+（12.0 起废弃）, iPadOS 3.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.3+（10.14 起废弃）, tvOS 9.0+（12.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（5.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsvaluetransformername/unarchivefromdatatransformername
source_url: 'https://developer.apple.com/documentation/foundation/nsvaluetransformername/unarchivefromdatatransformername'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvaluetransformername/unarchivefromdatatransformername.json'
content_hash: 'sha256:d8b89f153cda2c9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValueTransformerName](../nsvaluetransformername.md)

# unarchiveFromDataTransformerName

<sub>Type Property</sub>

The name of the value transformer that attempts to unarchive data from an object you provide.

> [!warning] Deprecated
> Use [NSSecureUnarchiveFromDataTransformerName](secureunarchivefromdatatransformername.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let unarchiveFromDataTransformerName: NSValueTransformerName
```

## Discussion

The transformer this property references returns the [NSData](../nsdata.md) instance created by archiving the value. This transformer requires that an object supports [NSCoding](../nscoding.md) in order for the transformer to archive and unarchive.

## See Also

### Type Properties

- [NSIsNilTransformerName](isniltransformername.md) — This value transformer returns true if the value is nil.
- [NSIsNotNilTransformerName](isnotniltransformername.md) — This value transformer returns true if the value is non-nil.
- [NSKeyedUnarchiveFromDataTransformerName](keyedunarchivefromdatatransformername.md) — The name of the value transformer that attempts to unarchive data stored inside a keyed archive in an object you provide. _(deprecated)_
- [NSNegateBooleanTransformerName](negatebooleantransformername.md) — This value transformer negates a boolean value, transforming true to false and false to true.
- [NSSecureUnarchiveFromDataTransformerName](secureunarchivefromdatatransformername.md) — The name of the value transformer that creates then returns an object by attempting to unarchive the data to a class that supports secure coding.
