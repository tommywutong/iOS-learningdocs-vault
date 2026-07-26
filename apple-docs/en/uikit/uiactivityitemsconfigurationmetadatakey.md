---
title: UIActivityItemsConfigurationMetadataKey
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityitemsconfigurationmetadatakey
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationmetadatakey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsconfigurationmetadatakey.json'
content_hash: 'sha256:da14ab886f6d528a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIActivityItemsConfigurationMetadataKey

<sub>Structure</sub>

A structure that defines keys for the metadata associated with an activity items configuration.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct UIActivityItemsConfigurationMetadataKey
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIActivityItemsConfigurationMetadataKeyTitle](uiactivityitemsconfigurationmetadatakey/title.md) — A key for the title.
- [UIActivityItemsConfigurationMetadataKeyMessageBody](uiactivityitemsconfigurationmetadatakey/messagebody.md) — A key for the message body.
- [UIActivityItemsConfigurationMetadataKeyLinkPresentationMetadata](uiactivityitemsconfigurationmetadatakey/linkpresentationmetadata.md)
- [UIActivityItemsConfigurationMetadataKeyShareRecipients](uiactivityitemsconfigurationmetadatakey/sharerecipients.md)
- [UIActivityItemsConfigurationMetadataKeyCollaborationModeRestrictions](uiactivityitemsconfigurationmetadatakey/collaborationmoderestrictions.md) — A key for a collaboration mode restriction, used to specify the case where Share Sheet should not support some modes of sharing even if they are supported by the items being shared The object returned for this key should be an array of UIActivityCollaborationModeRestriction instances For supported behaviour, this array should have a maximum size of one less than the amount of possible Share Sheet modes Currently at most one object should be provided

### Initializers

- [init(_:)](<uiactivityitemsconfigurationmetadatakey/init(__).md>) — Creates an activity items configuration metadata key.
- [init(rawValue:)](<uiactivityitemsconfigurationmetadatakey/init(rawvalue_).md>) — Creates an activity items configuration metadata key with the specified raw value.

## See Also

### Managing the configuration

- [localObject](uiactivityitemsconfiguration/localobject.md) — A local object that represents the configuration.
- [metadataProvider](uiactivityitemsconfiguration/metadataprovider.md) — A closure that provides metadata for the activity items.
- [perItemMetadataProvider](uiactivityitemsconfiguration/peritemmetadataprovider.md) — A closure that provides metadata for each activity item.
- [applicationActivitiesProvider](uiactivityitemsconfiguration/applicationactivitiesprovider.md) — A closure that provides application acitivites for the activity items.
