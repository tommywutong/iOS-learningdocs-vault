---
title: defaultValue
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsattributedescription/defaultvalue
source_url: 'https://developer.apple.com/documentation/coredata/nsattributedescription/defaultvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsattributedescription/defaultvalue.json'
content_hash: 'sha256:d3c9a90cb3f060f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAttributeDescription](../nsattributedescription.md)

# defaultValue

<sub>Instance Property</sub>

The default value of the attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var defaultValue: Any? { get set }
```

## Discussion

Default values are retained by a managed object model, not copied. This means that attribute values do not have to implement the `NSCopying` protocol, however it also means that you should not modify any objects after they have been set as default values.

### Special Considerations

Setting the default value raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Configuring the behavior

- [allowsCloudEncryption](allowscloudencryption.md) — A Boolean value that determines whether to encrypt the attribute’s value.
- [allowsExternalBinaryDataStorage](allowsexternalbinarydatastorage.md) — A Boolean value that indicates whether the attribute allows external binary storage.
- [preservesValueInHistoryOnDeletion](preservesvalueinhistoryondeletion.md) — A Boolean value that indicates whether the attribute records its value in the persistent history transaction for a managed object’s deletion.
- [valueTransformerName](valuetransformername.md) — The name of the transformer to use for the attribute value.
