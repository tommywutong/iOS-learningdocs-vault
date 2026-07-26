---
title: 'cloudSharingController(_:failedToSaveShareWithError:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicloudsharingcontrollerdelegate/cloudsharingcontroller(_:failedtosavesharewitherror:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/cloudsharingcontroller(_:failedtosavesharewitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicloudsharingcontrollerdelegate/cloudsharingcontroller%28_%3Afailedtosavesharewitherror%3A%29.json'
content_hash: 'sha256:2ed62a930cdda017'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICloudSharingControllerDelegate](../uicloudsharingcontrollerdelegate.md)

# cloudSharingController(_:failedToSaveShareWithError:)

<sub>Instance Method</sub>

Tells the delegate that the CloudKit sharing controller failed to save the share record.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func cloudSharingController(_ csc: UICloudSharingController, failedToSaveShareWithError error: any Error)
```

## Discussion

Implement this method to receive a notification from the [UICloudSharingController](../uicloudsharingcontroller.md) instance after it fails to save changes to the [CKShare](../../cloudkit/ckshare.md) record.

## See Also

### Processing shared items

- [- cloudSharingControllerDidStopSharing:](<cloudsharingcontrollerdidstopsharing(__).md>) — Tells the delegate that the user has stopped sharing the record.
- [- cloudSharingControllerDidSaveShare:](<cloudsharingcontrollerdidsaveshare(__).md>) — Tells the delegate that the CloudKit sharing controller saved the share record.
