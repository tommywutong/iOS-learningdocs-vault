---
title: UICloudSharingControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicloudsharingcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicloudsharingcontrollerdelegate.json'
content_hash: 'sha256:878086c45971c89b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICloudSharingControllerDelegate

<sub>Protocol</sub>

The protocol you implement to provide additional information to, and receive notifications from, the CloudKit sharing controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UICloudSharingControllerDelegate : NSObjectProtocol
```

## Overview

Implement an object that conforms to the [UICloudSharingControllerDelegate](uicloudsharingcontrollerdelegate.md) protocol when you want to:

- Configure a [UICloudSharingController](uicloudsharingcontroller.md) instance.
- Receive notifications from a [UICloudSharingController](uicloudsharingcontroller.md) instance as it attempts to save or remove the [CKShare](../cloudkit/ckshare.md) record based on user interactions on the Invitation and People screens.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the view controller

- [- itemTitleForCloudSharingController:](<uicloudsharingcontrollerdelegate/itemtitle(for_).md>) — Asks the delegate for the title to display on the invitation screen.
- [- itemTypeForCloudSharingController:](<uicloudsharingcontrollerdelegate/itemtype(for_).md>) — Asks the delegate for the Uniform Type Identifier (UTI) of the item.
- [- itemThumbnailDataForCloudSharingController:](<uicloudsharingcontrollerdelegate/itemthumbnaildata(for_).md>) — Asks the delegate for the thumbnail image data to display on the invitation.

### Processing shared items

- [- cloudSharingController:failedToSaveShareWithError:](<uicloudsharingcontrollerdelegate/cloudsharingcontroller(__failedtosavesharewitherror_).md>) — Tells the delegate that the CloudKit sharing controller failed to save the share record.
- [- cloudSharingControllerDidStopSharing:](<uicloudsharingcontrollerdelegate/cloudsharingcontrollerdidstopsharing(__).md>) — Tells the delegate that the user has stopped sharing the record.
- [- cloudSharingControllerDidSaveShare:](<uicloudsharingcontrollerdelegate/cloudsharingcontrollerdidsaveshare(__).md>) — Tells the delegate that the CloudKit sharing controller saved the share record.

## See Also

### Customizing the cloud sharing controller behavior

- [delegate](uicloudsharingcontroller/delegate.md) — A reference to an object that conforms to the CloudKit sharing controller delegate protocol.
