---
title: messageBody
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityitemsconfigurationmetadatakey/messagebody
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationmetadatakey/messagebody'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsconfigurationmetadatakey/messagebody.json'
content_hash: 'sha256:20c2dd2a23bbfca1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityItemsConfigurationMetadataKey](../uiactivityitemsconfigurationmetadatakey.md)

# messageBody

<sub>Type Property</sub>

A key for the message body.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let messageBody: UIActivityItemsConfigurationMetadataKey
```

## Discussion

The value of this key is an [NSString](../../foundation/nsstring.md) or [NSAttributedString](../../foundation/nsattributedstring.md) that contains the message body.

## See Also

### Constants

- [UIActivityItemsConfigurationMetadataKeyTitle](title.md) — A key for the title.
- [UIActivityItemsConfigurationMetadataKeyLinkPresentationMetadata](linkpresentationmetadata.md)
- [UIActivityItemsConfigurationMetadataKeyShareRecipients](sharerecipients.md)
- [UIActivityItemsConfigurationMetadataKeyCollaborationModeRestrictions](collaborationmoderestrictions.md) — A key for a collaboration mode restriction, used to specify the case where Share Sheet should not support some modes of sharing even if they are supported by the items being shared The object returned for this key should be an array of UIActivityCollaborationModeRestriction instances For supported behaviour, this array should have a maximum size of one less than the amount of possible Share Sheet modes Currently at most one object should be provided
