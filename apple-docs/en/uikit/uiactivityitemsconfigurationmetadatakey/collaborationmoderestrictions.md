---
title: collaborationModeRestrictions
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityitemsconfigurationmetadatakey/collaborationmoderestrictions
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationmetadatakey/collaborationmoderestrictions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsconfigurationmetadatakey/collaborationmoderestrictions.json'
content_hash: 'sha256:e4b34cac93ba5157'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityItemsConfigurationMetadataKey](../uiactivityitemsconfigurationmetadatakey.md)

# collaborationModeRestrictions

<sub>Type Property</sub>

A key for a collaboration mode restriction, used to specify the case where Share Sheet should not support some modes of sharing even if they are supported by the items being shared The object returned for this key should be an array of UIActivityCollaborationModeRestriction instances For supported behaviour, this array should have a maximum size of one less than the amount of possible Share Sheet modes Currently at most one object should be provided

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let collaborationModeRestrictions: UIActivityItemsConfigurationMetadataKey
```

## See Also

### Constants

- [UIActivityItemsConfigurationMetadataKeyTitle](title.md) — A key for the title.
- [UIActivityItemsConfigurationMetadataKeyMessageBody](messagebody.md) — A key for the message body.
- [UIActivityItemsConfigurationMetadataKeyLinkPresentationMetadata](linkpresentationmetadata.md)
- [UIActivityItemsConfigurationMetadataKeyShareRecipients](sharerecipients.md)
