---
title: linkPresentationMetadata
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityitemsconfigurationmetadatakey/linkpresentationmetadata
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationmetadatakey/linkpresentationmetadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsconfigurationmetadatakey/linkpresentationmetadata.json'
content_hash: 'sha256:bdb436e6bd88410b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityItemsConfigurationMetadataKey](../uiactivityitemsconfigurationmetadatakey.md)

# linkPresentationMetadata

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let linkPresentationMetadata: UIActivityItemsConfigurationMetadataKey
```

## See Also

### Constants

- [UIActivityItemsConfigurationMetadataKeyTitle](title.md) — A key for the title.
- [UIActivityItemsConfigurationMetadataKeyMessageBody](messagebody.md) — A key for the message body.
- [UIActivityItemsConfigurationMetadataKeyShareRecipients](sharerecipients.md)
- [UIActivityItemsConfigurationMetadataKeyCollaborationModeRestrictions](collaborationmoderestrictions.md) — A key for a collaboration mode restriction, used to specify the case where Share Sheet should not support some modes of sharing even if they are supported by the items being shared The object returned for this key should be an array of UIActivityCollaborationModeRestriction instances For supported behaviour, this array should have a maximum size of one less than the amount of possible Share Sheet modes Currently at most one object should be provided
