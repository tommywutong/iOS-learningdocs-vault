---
title: cloudKitShareMetadata
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/connectionoptions/cloudkitsharemetadata
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/connectionoptions/cloudkitsharemetadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/connectionoptions/cloudkitsharemetadata.json'
content_hash: 'sha256:25a205bd0089c4f2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScene](../../uiscene.md) · [ConnectionOptions](../connectionoptions.md)

# cloudKitShareMetadata

<sub>Instance Property</sub>

Information about the CloudKit data that’s now available to the app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var cloudKitShareMetadata: CKShareMetadata? { get }
```

## Discussion

If an invitation to share CloudKit data is available at scene-connection time, this property contains the metadata you use to accept that invitation. Use the information in the object to create and schedule a [CKAcceptSharesOperation](../../../cloudkit/ckacceptsharesoperation.md) object. After your operation object finishes successfully, you can begin fetching records and incorporating the resulting data into your app.
