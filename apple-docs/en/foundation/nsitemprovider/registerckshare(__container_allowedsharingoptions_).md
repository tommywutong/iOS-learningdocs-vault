---
title: 'registerCKShare(_:container:allowedSharingOptions:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/registerckshare(_:container:allowedsharingoptions:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registerckshare(_:container:allowedsharingoptions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registerckshare%28_%3Acontainer%3Aallowedsharingoptions%3A%29.json'
content_hash: 'sha256:8e47efc9dce230f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registerCKShare(_:container:allowedSharingOptions:)

<sub>Instance Method</sub>

Registers an existing collaboration object on a server.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func registerCKShare(_ share: CKShare, container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions = CKAllowedSharingOptions.standard)
```

## Parameters

- `share` — An existing [CKShare](../../cloudkit/ckshare.md) on the server.

- `container` — A [CKContainer](../../cloudkit/ckcontainer.md) the system uses to coordinate all the interactions between your app and the server.

- `allowedSharingOptions` — The [CKAllowedSharingOptions](../../cloudkit/ckallowedsharingoptions.md). The standard option is the default.

## Discussion

Use this method when a [CKShare](../../cloudkit/ckshare.md) currently exists on the server. When the system invokes the share sheet with a `CKShare` that you register with this method, it allows the owner to make modifications to the share settings, and allows a participant to view the share settings.

## See Also

### Registering CloudKit shares

- [- registerCloudKitShare:container:](<registercloudkitshare(__container_).md>) — Registers a CloudKit share for the user to modify.
- [- registerCloudKitShareWithPreparationHandler:](<registercloudkitshare(preparationhandler_).md>) — Registers a handler that prepares a new CloudKit share.
- [registerCKShare(container:allowedSharingOptions:preparationHandler:)](<registerckshare(container_allowedsharingoptions_preparationhandler_).md>) — Creates and registers a new collaboration object using a collection of records to share.
