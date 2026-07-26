---
title: negateBooleanTransformerName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsvaluetransformername/negatebooleantransformername
source_url: 'https://developer.apple.com/documentation/foundation/nsvaluetransformername/negatebooleantransformername'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvaluetransformername/negatebooleantransformername.json'
content_hash: 'sha256:b0a35a6801d7d68b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValueTransformerName](../nsvaluetransformername.md)

# negateBooleanTransformerName

<sub>Type Property</sub>

This value transformer negates a boolean value, transforming true to false and false to true.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let negateBooleanTransformerName: NSValueTransformerName
```

## Discussion

This transformer is reversible.

## See Also

### Type Properties

- [NSIsNilTransformerName](isniltransformername.md) — This value transformer returns true if the value is nil.
- [NSIsNotNilTransformerName](isnotniltransformername.md) — This value transformer returns true if the value is non-nil.
- [NSKeyedUnarchiveFromDataTransformerName](keyedunarchivefromdatatransformername.md) — The name of the value transformer that attempts to unarchive data stored inside a keyed archive in an object you provide. _(deprecated)_
- [NSUnarchiveFromDataTransformerName](unarchivefromdatatransformername.md) — The name of the value transformer that attempts to unarchive data from an object you provide. _(deprecated)_
- [NSSecureUnarchiveFromDataTransformerName](secureunarchivefromdatatransformername.md) — The name of the value transformer that creates then returns an object by attempting to unarchive the data to a class that supports secure coding.
