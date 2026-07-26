---
title: 'shareManagedObjects:toShare:completion:'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentcloudkitcontainer/sharemanagedobjects:toshare:completion:'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/sharemanagedobjects:toshare:completion:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainer/sharemanagedobjects%3Atoshare%3Acompletion%3A.json'
content_hash: 'sha256:ee9b960a1b7bb883'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentCloudKitContainer](../nspersistentcloudkitcontainer.md)

# shareManagedObjects:toShare:completion:

<sub>Instance Method</sub>

Associates the specified managed objects with a new or existing share record.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) shareManagedObjects:(NSArray<NSManagedObject *> *) managedObjects toShare:(CKShare *) share completion:(void (^)(NSSet<NSManagedObjectID *> *sharedObjectIDs, CKShare *share, CKContainer *cloudKitContainer, NSError *sharingError)) completion;
```

## Parameters

- `managedObjects` — The managed objects to share.

- `share` — A share record that identifies an existing shared record zone to associate the managed objects with. Use `nil` to create a new shared record zone that contains only the specified managed objects and doesn’t have any participants.

- `completion` — The handler to invoke after Core Data shares the managed objects.

## Discussion

The `completion` closure returns no value and takes the following parameters:

- The IDs of the shared objects.
- The share record. For more information, see [CKShare](../../cloudkit/ckshare.md).
- The CloudKit container of the database that stores the shared record zone. For more information, see [CKContainer](../../cloudkit/ckcontainer.md).
- An error object that contains information about a problem, or `nil` if the managed objects share successfully.

When you invoke this method, Core Data performs a deep traversal among the specified managed objects and adds any related objects to the share.

Sharing fails if any of the following conditions apply:

- Any objects in `managedObjects`, or those the traversal finds, belong to an existing share record.
- Any objects in `managedObjects` belong to a persistent store that doesn’t support sharing, such as those you configure with the [CKDatabase.Scope.public](../../cloudkit/ckdatabase/scope/public.md) database scope.
- The current device state doesn’t support sharing, such as when there isn’t an active iCloud account.

You can use `completion` directly with the [init(preparationHandler:)](<../../uikit/uicloudsharingcontroller/init(preparationhandler_).md>) method of [UICloudSharingController](../../uikit/uicloudsharingcontroller.md), as the following example shows.

**Swift**

```swift
func share(_ objects: [NSManagedObjects], in container: NSPersistentCloudKitContainer) {
  // Create an instance of UICloudSharingController.
  let cloudSharingController = UICloudSharingController {
    (controller, completion: @escaping (CKShare?, CKContainer?, Error?) -> Void) in
    
    // Call the container's share method, passing the managed objects to share.
    container.share(objects, to: nil) { _, share, container, error in
      // Invoke the cloud-sharing controller's completion handler,
      // passing the share, container, and error parameters that
      // NSPersistentCloudKitContainer provides.
      completion(share, container, error)
    }
  }

  // Present the cloud-sharing controller to the user.
  present(cloudSharingController, animated: true)
}
```

**Objective-C**

```objc
- (void)shareObjects:(NSArray *)objects
         inContainer:(NSPersistentCloudKitContainer *)container {
    
    // Create an instance of UICloudSharingController.
    UICloudSharingController *cloudSharingController =
        [[UICloudSharingController alloc]
         initWithPreparationHandler:^(UICloudSharingController * _Nonnull controller,
                                      void (^ _Nonnull preparationCompletionHandler)(
                                       CKShare * _Nullable,
                                       CKContainer * _Nullable,
                                       NSError * _Nullable)) {
        
        // Call the container's share method, passing the managed objects
        // to share.
        [container shareManagedObjects:objects
                               toShare:NULL
                            completion:^(NSSet<NSManagedObjectID *>
                                         * _Nullable sharedObjectIDs,
                                         CKShare * _Nullable share,
                                         CKContainer * _Nullable cloudKitContainer,
                                         NSError * _Nullable sharingError) {
            
            // Invoke the cloud-sharing controller's completion handler,
            // passing the share, container, and error parameters that
            // NSPersistentCloudKitContainer provides.
            preparationCompletionHandler(share, cloudKitContainer, sharingError);
        }];
    }];
    
    // Present the cloud-sharing controller to the user.
    [self presentViewController:cloudSharingController
                       animated:true
                     completion:NULL];
}
```

## See Also

### Sharing Objects

- [Accepting Share Invitations in a SwiftUI App](../accepting-share-invitations-in-a-swiftui-app.md) — Adapt your app to use UIKit’s application and scene delegates so it can process CloudKit share invitations.
- [acceptShareInvitationsFromMetadata:intoPersistentStore:completion:](acceptshareinvitationsfrommetadata_intopersistentstore_completion_.md) — Accepts one or more invitations to participate in sharing using the specified metadata.
- [fetchParticipantsMatchingLookupInfos:intoPersistentStore:completion:](fetchparticipantsmatchinglookupinfos_intopersistentstore_completion_.md) — Fetches all participants that match the specified critieria.
- [fetchSharesInPersistentStore:error:](fetchsharesinpersistentstore_error_.md) — Returns an array that contains all share records in the specified persistent store.
- [fetchSharesMatchingObjectIDs:error:](fetchsharesmatchingobjectids_error_.md) — Returns a dictionary that contains the share records that CloudKit associates with specified managed object IDs.
- [persistUpdatedShare:inPersistentStore:completion:](persistupdatedshare_inpersistentstore_completion_.md) — Saves the share record and schedules it for export to iCloud.
