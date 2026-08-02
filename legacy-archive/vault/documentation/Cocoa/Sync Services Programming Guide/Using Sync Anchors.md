---
title: Sync Services Programming Guide
apple_id: TP40001178
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-07-06'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SyncServices/Articles/UsingSyncAnchors.html
archived_at: '2026-07-15T07:19:47.732755Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sync Services Programming Guide](Introduction%20to%20Sync%20Services%20Programming%20Guide.md)


[Next](Filtering%20Records.md)[Previous](Syncing%20with%20Other%20Clients.md)

# Using Sync Anchors

Sync anchors provide a mechanism for tracking the success or failure of phases within a sync session. Sync anchors mark when changes are successfully pushed and pulled. This information is used by the sync engine, in the next session, to select a better sync mode. A client may request a sync mode but the sync engine ultimately decides whether a client can fast sync or needs to refresh or slow sync. Using sync anchors can improve performance by fast syncing more often and avoids serious errors by forcing a refresh or slow sync when necessary.

You should use sync anchors unless you implement your own mechanism for tracking whether records are successfully pushed and pulled. A sync anchor is a string object, unique per client and per entity or data class, that is saved periodically throughout a sync session. During the next sync session, the sync engine compares the client’s locally stored sync anchors with its copies to identify discrepancies and consequently select an appropriate sync mode. For example, if the client sync anchors are not the same as the sync engine sync anchors and the client is an application (of type `ISyncClientTypeApplication`), an alert panel appears asking the user to select an appropriate sync mode. If the client is not an application, the client slow syncs.

If you do not use sync anchors, then there may be some cases where the sync engine cannot determine accurately when a client can fast sync—that is, when it is not necessary to push every record. Sync anchors help determine when a fast sync is ok and therefore, significantly improve performance of your application by fast syncing more often, especially for large data sets.

There are also some cases when the sync engine might allow a fast sync when the client should slow sync. For example, if there is a communication failure between a client and its data store, then the sync engine might assume a fast sync is ok. The local data store could also be restored from backup (independent of the application) and both the application and the sync engine might mistakenly allow a fast sync. By using sync anchors, the sync engine can detect these types of errors and take the appropriate action.

This article describes the sync anchor methods you use when managing your sync session using either the `ISyncSession` or `ISyncSessionDriver` classes. You do not need to worry about sync anchors if you are syncing Core Data objects (see [Syncing Core Data Applications](Syncing%20Core%20Data%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temzsfvjvomi) for more details).

The sync anchor methods for the `ISyncSession` and `ISyncSessionDriver` classes are similar. You are responsible for providing the sync anchors used in the previous sync session when beginning a sync session and providing new sync anchors for the current session after both the pushing and pulling phases.

The sync anchor parameter to Sync Services methods is a dictionary where the keys are the entity names and the values are the sync anchors. A sync anchor is a unique string per entity or data class.

Typically, all entities in the same data class have the same sync mode. Therefore, you can optionally create a sync anchor per one representative entity in a data class. The sync engine then uses the same sync anchor for all entities in that data class. However, if you provide sync anchors for two or more entities per data class, then you need to specify sync anchors for all entities in that data class. Otherwise, a missing sync anchor for an entity causes that entity to refresh sync.

This code sample creates one sync anchor per a single data class that an application syncs:

```
NSString *representativeEntityName = [[self entityNames] objectAtIndex:0];
NSDictionary *syncAnchors = [NSDictionary dictionaryWithObject:[[NSDate date] description] forKey:representativeEntityName];
```


To use sync anchors, you need to provide the last sync anchors when beginning a sync session and save sync anchors at various times during a sync session. Therefore, you need to decide where and how to store your sync anchors. This section provides some tips on how and when to save sync anchors.

Typically, you store the sync anchors with your local records so they are synchronized. Keeping the sync anchors with your local records is important because if you provide the wrong sync anchors, it defeats the purpose of using sync anchors. You can avoid this by saving the sync anchors in the same file as your local records or saving the sync anchors in a separate file that is in the same bundle as your local records.

It’s strongly recommended that you save your sync anchors whenever you create them during a sync session. It’s also recommended that you save your sync anchors with your local records just before committing your changes at the end of the pulling phase. This synchronizes the state of the local records with the sync anchors and avoids problems should a session be canceled.

You also need to decide what to do if a sync session is canceled. If you save local records with sync anchors as recommended during the pushing and pulling phases, then you can safely revert to the last saved state when a session is canceled. Again, it’s easier to do so if you store your local records and sync anchors together. Read [Canceling](Managing%20Your%20Sync%20Session.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrsfuyteojwgyzq) in [Managing Your Sync Session](Managing%20Your%20Sync%20Session.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrsfvbuuqsfjbaucry) for complete details on the state of the sync engine when a session is canceled.

Read [Using Sync Anchors with ISyncSession](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temzrfvjvomq) or [Using Sync Anchors with ISyncSessionDriver](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temzrfvjvomy) for details on using sync anchors for each approach to managing your sync sessions.

This section describes the sequence of steps you follow to use sync anchors when you are managing a sync session using an `ISyncSession` object. Read [Managing Your Sync Session](Managing%20Your%20Sync%20Session.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrsfvbuuqsfjbaucry) for a complete descriptions of all the steps in managing a sync session.

Invoke either the `beginSessionWithClient:entityNames:beforeDate:lastAnchors:` or `beginSessionInBackgroundWithClient:entityNames:target:selector:lastAnchors:` methods of `ISyncSession` to begin a sync session.

The `beginSessionWithClient:entityNames:beforeDate:lastAnchors:` method is synchronous—blocks until all other clients have joined the sync session—and the `beginSessionInBackgroundWithClient:entityNames:target:selector:lastAnchors:` method is asynchronous—sends a message to a target when a sync session is created.

You pass the sync anchors used in the previous successful sync as the `lastAnchors:` parameter to each of these methods. If it’s the first time your application is syncing, then pass `nil` as the `lastAnchors:` parameter and your client will refresh sync.

After pushing changes to the sync engine, create new sync anchors and save them locally just before invoking the `clientFinishedPushingChangesWithNextAnchors:` method. Pass the new sync anchors as the parameter of this method. Optionally, save your local records, too, so that the new sync anchors match. Read [Creating Sync Anchors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temzrfvjvona) for how to create sync anchors.

After pulling changes from the sync engine and applying them to your local records, create new sync anchors and save them locally just before invoking the `clientCommittedAcceptedChangesWithNextAnchors:` method. Pass the new sync anchors as the parameter. You should also save your local records before invoking this method so that your last sync anchors match. Read [Creating Sync Anchors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temzrfvjvona) for how to create sync anchors.

Using sync anchors is optional but recommended if you are using a sync session driver. All you need to do is implement the `nextAnchorForEntityName:` and `lastAnchorForEntityName:` methods of the `ISyncSessionDriverDataSource` protocol to use sync anchors.

Simply implement the `nextAnchorForEntityName:` method to return the next sync anchor for the specified entity name. Store the sync anchor locally and implement the `lastAnchorForEntityName:` method to return it the next time it is invoked during the next sync session. Note that if you implement one of these methods, you need to implement the other one, too.

In a way that is similar to using an `ISyncSession` object, you can create one sync anchor per representative entity in a data class. In this case, you implement the methods to return the same sync anchor for all entities in the same data class.

[Next](Filtering%20Records.md)[Previous](Syncing%20with%20Other%20Clients.md)

