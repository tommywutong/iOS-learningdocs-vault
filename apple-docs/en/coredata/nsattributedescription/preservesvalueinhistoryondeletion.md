---
title: preservesValueInHistoryOnDeletion
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsattributedescription/preservesvalueinhistoryondeletion
source_url: 'https://developer.apple.com/documentation/coredata/nsattributedescription/preservesvalueinhistoryondeletion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsattributedescription/preservesvalueinhistoryondeletion.json'
content_hash: 'sha256:b83e64eb42fdc326'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAttributeDescription](../nsattributedescription.md)

# preservesValueInHistoryOnDeletion

<sub>Instance Property</sub>

A Boolean value that indicates whether the attribute records its value in the persistent history transaction for a managed object’s deletion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preservesValueInHistoryOnDeletion: Bool { get set }
```

## See Also

### Configuring the behavior

- [allowsCloudEncryption](allowscloudencryption.md) — A Boolean value that determines whether to encrypt the attribute’s value.
- [allowsExternalBinaryDataStorage](allowsexternalbinarydatastorage.md) — A Boolean value that indicates whether the attribute allows external binary storage.
- [defaultValue](defaultvalue.md) — The default value of the attribute.
- [valueTransformerName](valuetransformername.md) — The name of the transformer to use for the attribute value.
