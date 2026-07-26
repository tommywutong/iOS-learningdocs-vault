---
title: valueTransformerName
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsattributedescription/valuetransformername
source_url: 'https://developer.apple.com/documentation/coredata/nsattributedescription/valuetransformername'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsattributedescription/valuetransformername.json'
content_hash: 'sha256:ee915e66af01cb0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAttributeDescription](../nsattributedescription.md)

# valueTransformerName

<sub>Instance Property</sub>

The name of the transformer to use for the attribute value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var valueTransformerName: String? { get set }
```

## Discussion

The attribute must be of type `NSTransformedAttributeType`.

The transformer must output an `NSData` object from [transformedValue(_:)](<../../foundation/valuetransformer/transformedvalue(__).md>) and must allow reverse transformations.

If this value is `nil`, Core Data uses a default a transformer that uses [NSCoding](../../foundation/nscoding.md) to archive and unarchive the attribute value.

## See Also

### Configuring the behavior

- [allowsCloudEncryption](allowscloudencryption.md) — A Boolean value that determines whether to encrypt the attribute’s value.
- [allowsExternalBinaryDataStorage](allowsexternalbinarydatastorage.md) — A Boolean value that indicates whether the attribute allows external binary storage.
- [defaultValue](defaultvalue.md) — The default value of the attribute.
- [preservesValueInHistoryOnDeletion](preservesvalueinhistoryondeletion.md) — A Boolean value that indicates whether the attribute records its value in the persistent history transaction for a managed object’s deletion.
