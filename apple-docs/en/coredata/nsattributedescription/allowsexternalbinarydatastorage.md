---
title: allowsExternalBinaryDataStorage
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsattributedescription/allowsexternalbinarydatastorage
source_url: 'https://developer.apple.com/documentation/coredata/nsattributedescription/allowsexternalbinarydatastorage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsattributedescription/allowsexternalbinarydatastorage.json'
content_hash: 'sha256:11a66752a1db39c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAttributeDescription](../nsattributedescription.md)

# allowsExternalBinaryDataStorage

<sub>Instance Property</sub>

A Boolean value that indicates whether the attribute allows external binary storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowsExternalBinaryDataStorage: Bool { get set }
```

## Discussion

[true](../../swift/true.md) if the attribute allows external binary storage, otherwise [false](../../swift/false.md). If this value is [true](../../swift/true.md), the corresponding attribute may be stored in a file external to the persistent store itself.

## See Also

### Configuring the behavior

- [allowsCloudEncryption](allowscloudencryption.md) — A Boolean value that determines whether to encrypt the attribute’s value.
- [defaultValue](defaultvalue.md) — The default value of the attribute.
- [preservesValueInHistoryOnDeletion](preservesvalueinhistoryondeletion.md) — A Boolean value that indicates whether the attribute records its value in the persistent history transaction for a managed object’s deletion.
- [valueTransformerName](valuetransformername.md) — The name of the transformer to use for the attribute value.
