---
title: allowsCloudEncryption
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsattributedescription/allowscloudencryption
source_url: 'https://developer.apple.com/documentation/coredata/nsattributedescription/allowscloudencryption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsattributedescription/allowscloudencryption.json'
content_hash: 'sha256:7b109b4479867c08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAttributeDescription](../nsattributedescription.md)

# allowsCloudEncryption

<sub>Instance Property</sub>

A Boolean value that determines whether to encrypt the attribute’s value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowsCloudEncryption: Bool { get set }
```

## Discussion

Set this property to [true](../../swift/true.md) to store the attribute’s value in an encrypted form in iCloud. Only use this property with new attributes. Core Data doesn’t support encrypting attributes that already exist in your CloudKit schema, or attributes that represent relationships between entities.

You can also set this property using the Allow Cloud Encryption attribute in the Attributes inspector of the Core Data model editor.

> [!important] Important
> Attributes can’t change their encryption state after you promote them to your production CloudKit schema. If you choose to encrypt an attribute, it always remains that way.

## See Also

### Configuring the behavior

- [allowsExternalBinaryDataStorage](allowsexternalbinarydatastorage.md) — A Boolean value that indicates whether the attribute allows external binary storage.
- [defaultValue](defaultvalue.md) — The default value of the attribute.
- [preservesValueInHistoryOnDeletion](preservesvalueinhistoryondeletion.md) — A Boolean value that indicates whether the attribute records its value in the persistent history transaction for a managed object’s deletion.
- [valueTransformerName](valuetransformername.md) — The name of the transformer to use for the attribute value.
