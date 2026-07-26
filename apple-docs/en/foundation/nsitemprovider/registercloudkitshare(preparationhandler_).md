---
title: 'registerCloudKitShare(preparationHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.12+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/registercloudkitshare(preparationhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registercloudkitshare(preparationhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registercloudkitshare%28preparationhandler%3A%29.json'
content_hash: 'sha256:1b7c4bd4109564b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registerCloudKitShare(preparationHandler:)

<sub>Instance Method</sub>

Registers a handler that prepares a new CloudKit share.

<sub>macOS</sub>

```swift
func registerCloudKitShare(preparationHandler: @escaping (@escaping (CKShare?, CKContainer?, (any Error)?) -> Void) -> Void)
```

## Parameters

- `preparationHandler` — The handler the service invokes when it requires the CloudKit share.

## Discussion

Use this method to share a hierarchy of CloudKit records with other iCloud users. When the service invokes the handler, create an instance of [CKShare](../../cloudkit/ckshare.md) with a root record. Save the share to the server using [CKModifyRecordsOperation](../../cloudkit/ckmodifyrecordsoperation.md). The root record (and its hierarchy) must already exist on the server or be part of the same save operation. After the share saves, call `preparationCompletionHandler` with the saved share and its container. If the save fails, pass the error to the completion handler instead. Invoking the sharing service with a share you register using this method prompts the user to begin sharing.

Use the [NSCloudSharingServiceDelegate](../../appkit/nscloudsharingservicedelegate.md) protocol to respond to any changes the sharing service makes.

> [!note] Note
> To modify an existing share, use the [- registerCloudKitShare:container:](<registercloudkitshare(__container_).md>) method instead.

The following example shows how to create an item provider with a handler that saves a share. It then invokes the cloud-sharing service with that provider.

```swift
func beginSharing(_ record: CKRecord) {
    let itemProvider = NSItemProvider()
        
    // Register a handler that creates a CloudKit share using
    // the provided record, and saves them both to the server
    // before passing them to the sharing service.
    itemProvider.registerCloudKitShare(preparationHandler: { completion in
        let container = CKContainer.default()
            
        // Create a share and use the record the caller provides as 
        // its root record. 
        let share = CKShare(rootRecord: record)

        // Create an operation that saves both the record and the 
        // share to CloudKit.
        let records = [record, share]
        let operation = CKModifyRecordsOperation(recordsToSave: records, 
                                                 recordIDsToDelete: nil)
            
        // If the save fails, pass the error to the completion handler.
        // Otherwise, pass the new share and its container.
        operation.modifyRecordsCompletionBlock = { _, _, error in
            if let error = error {
                completion(nil, nil, error)
            } else {
                completion(share, container, nil)
            }
        }
            
        // Set an appropriate QoS and add the operation to the
        // container's queue to execute it.
        operation.qualityOfService = .userInitiated
        container.privateCloudDatabase.add(operation)
    })
        
    let items = [itemProvider]
        
    // Create a cloud-sharing service and invoke it to begin sharing.
    if let service = NSSharingService(named: .cloudSharing), 
       service.canPerform(withItems: items) {
        service.perform(withItems: items)
    }
}
```

## See Also

### Registering CloudKit shares

- [- registerCloudKitShare:container:](<registercloudkitshare(__container_).md>) — Registers a CloudKit share for the user to modify.
- [registerCKShare(_:container:allowedSharingOptions:)](<registerckshare(__container_allowedsharingoptions_).md>) — Registers an existing collaboration object on a server.
- [registerCKShare(container:allowedSharingOptions:preparationHandler:)](<registerckshare(container_allowedsharingoptions_preparationhandler_).md>) — Creates and registers a new collaboration object using a collection of records to share.
