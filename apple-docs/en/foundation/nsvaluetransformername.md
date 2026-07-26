---
title: NSValueTransformerName
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsvaluetransformername
source_url: 'https://developer.apple.com/documentation/foundation/nsvaluetransformername'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvaluetransformername.json'
content_hash: 'sha256:3d637f5596250d71'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSValueTransformerName

<sub>Structure</sub>

Named value transformers defined by `NSValueTransformer`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSValueTransformerName
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [NSIsNilTransformerName](nsvaluetransformername/isniltransformername.md) — This value transformer returns true if the value is nil.
- [NSIsNotNilTransformerName](nsvaluetransformername/isnotniltransformername.md) — This value transformer returns true if the value is non-nil.
- [NSKeyedUnarchiveFromDataTransformerName](nsvaluetransformername/keyedunarchivefromdatatransformername.md) — The name of the value transformer that attempts to unarchive data stored inside a keyed archive in an object you provide. _(deprecated)_
- [NSNegateBooleanTransformerName](nsvaluetransformername/negatebooleantransformername.md) — This value transformer negates a boolean value, transforming true to false and false to true.
- [NSUnarchiveFromDataTransformerName](nsvaluetransformername/unarchivefromdatatransformername.md) — The name of the value transformer that attempts to unarchive data from an object you provide. _(deprecated)_
- [NSSecureUnarchiveFromDataTransformerName](nsvaluetransformername/secureunarchivefromdatatransformername.md) — The name of the value transformer that creates then returns an object by attempting to unarchive the data to a class that supports secure coding.

### Initializers

- [init(_:)](<nsvaluetransformername/init(__).md>)
- [init(rawValue:)](<nsvaluetransformername/init(rawvalue_).md>)

## See Also

### Using the Name-Based Registry

- [+ setValueTransformer:forName:](<valuetransformer/setvaluetransformer(__forname_).md>) — Registers the provided value transformer with a given identifier.
- [+ valueTransformerForName:](<valuetransformer/init(forname_).md>) — Returns the value transformer identified by a given identifier.
- [+ valueTransformerNames](<valuetransformer/valuetransformernames().md>) — Returns an array of all the registered value transformers.
