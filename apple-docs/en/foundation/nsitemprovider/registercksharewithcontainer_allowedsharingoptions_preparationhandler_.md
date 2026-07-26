---
title: 'registerCKShareWithContainer:allowedSharingOptions:preparationHandler:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/registercksharewithcontainer:allowedsharingoptions:preparationhandler:'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registercksharewithcontainer:allowedsharingoptions:preparationhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registercksharewithcontainer%3Aallowedsharingoptions%3Apreparationhandler%3A.json'
content_hash: 'sha256:6b45ddae705935bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registerCKShareWithContainer:allowedSharingOptions:preparationHandler:

<sub>Instance Method</sub>

Creates and registers a new collaboration object using a collection of records to share.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) registerCKShareWithContainer:(CKContainer *) container allowedSharingOptions:(CKAllowedSharingOptions *) allowedOptions preparationHandler:(CKSharePreparationHandler) preparationHandler;
```

## Parameters

- `container` — A [CKContainer](../../cloudkit/ckcontainer.md) the system uses to coordinate all the interactions between your app and the server.

- `allowedOptions` — The [CKAllowedSharingOptions](../../cloudkit/ckallowedsharingoptions.md). The standard option is the default.

- `preparationHandler` — The handler the system calls in your app to create a new [CKShare](../../cloudkit/ckshare.md).

## Discussion

Use this method to share a collection of [CKRecord](../../cloudkit/ckrecord.md) objects that aren’t assigned to an existing [CKShare](../../cloudkit/ckshare.md). When the system calls the `preparationHandler`, your app creates a new `CKShare` with the appropriate root `CKRecord` or [CKRecordZone.ID](../../cloudkit/ckrecordzone/id.md).

After the server successfully saves the share, invoke the [CKSharePreparationCompletionHandler](../../cloudkit/cksharepreparationcompletionhandler.md) with either the resulting `CKShare` or an `NSError,` if the save failed.

When the system invokes the share sheet with a `CKShare` registered with this method, it prompts the user to start sharing.

## See Also

### Registering CloudKit shares

- [- registerCloudKitShare:container:](<registercloudkitshare(__container_).md>) — Registers a CloudKit share for the user to modify.
- [- registerCloudKitShareWithPreparationHandler:](<registercloudkitshare(preparationhandler_).md>) — Registers a handler that prepares a new CloudKit share.
- [registerCKShare:container:allowedSharingOptions:](registerckshare_container_allowedsharingoptions_.md) — Registers an existing collaboration object on a server.
