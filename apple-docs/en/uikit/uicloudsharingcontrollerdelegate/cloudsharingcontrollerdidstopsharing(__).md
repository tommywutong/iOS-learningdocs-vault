---
title: 'cloudSharingControllerDidStopSharing(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicloudsharingcontrollerdelegate/cloudsharingcontrollerdidstopsharing(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/cloudsharingcontrollerdidstopsharing(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicloudsharingcontrollerdelegate/cloudsharingcontrollerdidstopsharing%28_%3A%29.json'
content_hash: 'sha256:1ef2f3e398987c0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICloudSharingControllerDelegate](../uicloudsharingcontrollerdelegate.md)

# cloudSharingControllerDidStopSharing(_:)

<sub>Instance Method</sub>

Tells the delegate that the user has stopped sharing the record.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func cloudSharingControllerDidStopSharing(_ csc: UICloudSharingController)
```

## Discussion

Implement this method to receive a notification from the [UICloudSharingController](../uicloudsharingcontroller.md) instance after the user who owns the [CKShare](../../cloudkit/ckshare.md) record stops sharing it with all participants.

## See Also

### Processing shared items

- [- cloudSharingController:failedToSaveShareWithError:](<cloudsharingcontroller(__failedtosavesharewitherror_).md>) — Tells the delegate that the CloudKit sharing controller failed to save the share record.
- [- cloudSharingControllerDidSaveShare:](<cloudsharingcontrollerdidsaveshare(__).md>) — Tells the delegate that the CloudKit sharing controller saved the share record.
