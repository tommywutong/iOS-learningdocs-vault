---
title: isNotNilTransformerName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsvaluetransformername/isnotniltransformername
source_url: 'https://developer.apple.com/documentation/foundation/nsvaluetransformername/isnotniltransformername'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvaluetransformername/isnotniltransformername.json'
content_hash: 'sha256:91891fecaccdc681'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValueTransformerName](../nsvaluetransformername.md)

# isNotNilTransformerName

<sub>Type Property</sub>

This value transformer returns true if the value is non-nil.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let isNotNilTransformerName: NSValueTransformerName
```

## Discussion

This transformer is not reversible.

## See Also

### Type Properties

- [NSIsNilTransformerName](isniltransformername.md) — This value transformer returns true if the value is nil.
- [NSKeyedUnarchiveFromDataTransformerName](keyedunarchivefromdatatransformername.md) — The name of the value transformer that attempts to unarchive data stored inside a keyed archive in an object you provide. _(deprecated)_
- [NSNegateBooleanTransformerName](negatebooleantransformername.md) — This value transformer negates a boolean value, transforming true to false and false to true.
- [NSUnarchiveFromDataTransformerName](unarchivefromdatatransformername.md) — The name of the value transformer that attempts to unarchive data from an object you provide. _(deprecated)_
- [NSSecureUnarchiveFromDataTransformerName](secureunarchivefromdatatransformername.md) — The name of the value transformer that creates then returns an object by attempting to unarchive the data to a class that supports secure coding.
