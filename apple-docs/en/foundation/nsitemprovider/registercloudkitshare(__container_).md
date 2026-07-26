---
title: 'registerCloudKitShare(_:container:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.12+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/registercloudkitshare(_:container:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registercloudkitshare(_:container:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registercloudkitshare%28_%3Acontainer%3A%29.json'
content_hash: 'sha256:305a4f877a1930e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registerCloudKitShare(_:container:)

<sub>Instance Method</sub>

Registers a CloudKit share for the user to modify.

<sub>macOS</sub>

```swift
func registerCloudKitShare(_ share: CKShare, container: CKContainer)
```

## Parameters

- `share` — The CloudKit share to modify.

- `container` — The CloudKit container that stores the shared records.

## Discussion

Use this method when the CloudKit share already exists on the server and you want to update it. The behavior of the sharing service depends on the role of the current user. An owner can edit the share’s configuration, which includes managing participants and their permissions. A participant can view the share’s configuration and choose to stop participating.

If you’re unsure which container to use, fetch the share’s metadata using [CKFetchShareMetadataOperation](../../cloudkit/ckfetchsharemetadataoperation.md). Then initialize an instance of [CKContainer](../../cloudkit/ckcontainer.md) using the metadata’s [containerIdentifier](../../cloudkit/ckshare/metadata/containeridentifier.md) property.

Use the [NSCloudSharingServiceDelegate](../../appkit/nscloudsharingservicedelegate.md) protocol to respond to any changes the sharing service makes.

> [!note] Note
> To create a new share, use the [- registerCloudKitShareWithPreparationHandler:](<registercloudkitshare(preparationhandler_).md>) method instead.

The following example shows how to create an item provider with an existing share. It then invokes the cloud-sharing service with the provider and presents the share’s configuration to the user.

```swift
func modifyShare(_ share: CKShare, in container: CKContainer) {

    // Create an item provider and register a share that
    // already exists on the server.
    let itemProvider = NSItemProvider()
    itemProvider.registerCloudKitShare(share, container: container)
        
    // Create and invoke the cloud-sharing service to
    // present the share configuration to the user.
    if let service = NSSharingService(named: .cloudSharing),
       service.canPerform(withItems: [itemProvider]) {
        service.perform(withItems: [itemProvider])
    }
}
```

## See Also

### Registering CloudKit shares

- [- registerCloudKitShareWithPreparationHandler:](<registercloudkitshare(preparationhandler_).md>) — Registers a handler that prepares a new CloudKit share.
- [registerCKShare(_:container:allowedSharingOptions:)](<registerckshare(__container_allowedsharingoptions_).md>) — Registers an existing collaboration object on a server.
- [registerCKShare(container:allowedSharingOptions:preparationHandler:)](<registerckshare(container_allowedsharingoptions_preparationhandler_).md>) — Creates and registers a new collaboration object using a collection of records to share.
