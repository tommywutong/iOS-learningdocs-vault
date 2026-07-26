---
title: 'cloudSharingControllerDidSaveShare(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicloudsharingcontrollerdelegate/cloudsharingcontrollerdidsaveshare(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/cloudsharingcontrollerdidsaveshare(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicloudsharingcontrollerdelegate/cloudsharingcontrollerdidsaveshare%28_%3A%29.json'
content_hash: 'sha256:bd992a98aa8907d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICloudSharingControllerDelegate](../uicloudsharingcontrollerdelegate.md)

# cloudSharingControllerDidSaveShare(_:)

<sub>Instance Method</sub>

Tells the delegate that the CloudKit sharing controller saved the share record.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func cloudSharingControllerDidSaveShare(_ csc: UICloudSharingController)
```

## Discussion

Implement this method to receive a notification from the [UICloudSharingController](../uicloudsharingcontroller.md) instance after it saves changes to the [CKShare](../../cloudkit/ckshare.md) record.

## See Also

### Processing shared items

- [- cloudSharingController:failedToSaveShareWithError:](<cloudsharingcontroller(__failedtosavesharewitherror_).md>) — Tells the delegate that the CloudKit sharing controller failed to save the share record.
- [- cloudSharingControllerDidStopSharing:](<cloudsharingcontrollerdidstopsharing(__).md>) — Tells the delegate that the user has stopped sharing the record.
