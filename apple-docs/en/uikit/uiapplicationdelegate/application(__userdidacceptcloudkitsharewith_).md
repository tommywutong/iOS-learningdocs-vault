---
title: 'application(_:userDidAcceptCloudKitShareWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+（26.0 起废弃）, iPadOS 10.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 10.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:userdidacceptcloudkitsharewith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:userdidacceptcloudkitsharewith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Auserdidacceptcloudkitsharewith%3A%29.json'
content_hash: 'sha256:84653832ea8de030'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:userDidAcceptCloudKitShareWith:)

<sub>Instance Method</sub>

Tells the delegate that the app now has access to shared information in CloudKit.

> [!warning] Deprecated
> Use UIScene lifecycle and windowScene(_:userDidAcceptCloudKitShareWith:) from UIWindowSceneDelegate instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func application(_ application: UIApplication, userDidAcceptCloudKitShareWith cloudKitShareMetadata: CKShareMetadata)
```

## Parameters

- `application` — The shared app object.

- `cloudKitShareMetadata` — Information about the CloudKit data that is now available to the app. Use this object to retrieve information about the [CKShare](../../cloudkit/ckshare.md) object and the associated records that are now available.

## Discussion

If your app doesn’t support scenes, use this method to respond to a CloudKit Sharing invitation. In your implementation, accept the share by scheduling a [CKAcceptSharesOperation](../../cloudkit/ckacceptsharesoperation.md) object that contains the metadata object in the `cloudKitShareMetadata` parameter. After the share has been accepted, you can begin fetching records and incorporating the resulting data into your app. For a scene-based app, accept the invitation in your window scene delegate’s [- windowScene:userDidAcceptCloudKitShareWithMetadata:](<../uiwindowscenedelegate/windowscene(__userdidacceptcloudkitsharewith_).md>) method.

The system launches the app, as needed, before calling this method.
