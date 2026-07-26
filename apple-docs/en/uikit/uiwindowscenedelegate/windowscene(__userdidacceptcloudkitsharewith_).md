---
title: 'windowScene(_:userDidAcceptCloudKitShareWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwindowscenedelegate/windowscene(_:userdidacceptcloudkitsharewith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscenedelegate/windowscene(_:userdidacceptcloudkitsharewith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscenedelegate/windowscene%28_%3Auserdidacceptcloudkitsharewith%3A%29.json'
content_hash: 'sha256:e6d7931d760a7abb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowSceneDelegate](../uiwindowscenedelegate.md)

# windowScene(_:userDidAcceptCloudKitShareWith:)

<sub>Instance Method</sub>

Tells the delegate that the window scene now has access to shared information in CloudKit.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func windowScene(_ windowScene: UIWindowScene, userDidAcceptCloudKitShareWith cloudKitShareMetadata: CKShareMetadata)
```

## Parameters

- `windowScene` — The window scene object receiving the metadata.

- `cloudKitShareMetadata` — Information about the CloudKit data that is now available to the app. Use this object to retrieve information about the [CKShare](../../cloudkit/ckshare.md) object and the associated records.

## Discussion

Use this method to respond to a CloudKit Sharing invitation. In your implementation, accept the share by scheduling a [CKAcceptSharesOperation](../../cloudkit/ckacceptsharesoperation.md) object that contains the metadata object in the `cloudKitShareMetadata` parameter. After your operation object finishes successfully, you can begin fetching records and incorporating the resulting data into your app. Alternatively, if your app uses Core Data and [NSPersistentCloudKitContainer](../../coredata/nspersistentcloudkitcontainer.md), accept the share by calling the container’s [acceptShareInvitationsFromMetadata:intoPersistentStore:completion:](../../coredata/nspersistentcloudkitcontainer/acceptshareinvitationsfrommetadata_intopersistentstore_completion_.md) method.

> [!note] Note
> To use this method in a SwiftUI app, you must first add scene and application delegates to your project and configure your app to use them. For more information, see [Accepting Share Invitations in a SwiftUI App](../../coredata/accepting-share-invitations-in-a-swiftui-app.md).

The system calls this method only when your app is running and has an existing scene. If your app isn’t running, the system includes the share metadata in the [ConnectionOptions](../uiscene/connectionoptions.md) object it passes to the [- initWithSession:connectionOptions:](<../uiscene/init(session_connectionoptions_).md>) method when it creates your app’s first scene.

## See Also

### Performing tasks

- [- windowScene:performActionForShortcutItem:completionHandler:](<windowscene(__performactionfor_completionhandler_).md>) — Asks the delegate to perform the user-selected action.
