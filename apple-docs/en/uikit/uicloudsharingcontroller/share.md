---
title: share
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicloudsharingcontroller/share
source_url: 'https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/share'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicloudsharingcontroller/share.json'
content_hash: 'sha256:e437b7df88029197'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICloudSharingController](../uicloudsharingcontroller.md)

# share

<sub>Instance Property</sub>

A reference to the CloudKit share record used by the CloudKit sharing controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var share: CKShare? { get }
```

## Discussion

This property provides a reference to the [CKShare](../../cloudkit/ckshare.md) record used by [UICloudSharingController](../uicloudsharingcontroller.md). The property is `nil` if the controller doesn’t have a share record. This can happen when the controller is initialized with the [- initWithPreparationHandler:](<init(preparationhandler_).md>) method and the preparation handler hasn’t yet been called.
