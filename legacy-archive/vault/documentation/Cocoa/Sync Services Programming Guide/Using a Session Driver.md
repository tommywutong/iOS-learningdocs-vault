---
title: Sync Services Programming Guide
apple_id: TP40001178
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-07-06'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SyncServices/Articles/ControllingSyncSessions.html
archived_at: '2026-07-15T07:19:36.730326Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sync Services Programming Guide](Introduction%20to%20Sync%20Services%20Programming%20Guide.md)


[Next](Syncing%20Core%20Data%20Applications.md)[Previous](Formatting%20Records.md)

# Using a Session Driver

`ISyncSessionDriver` is a class that encapsulates the entire syncing process including setting up clients, registering schemas, and managing sync sessions. Applications can optionally use an `ISyncSessionDriver` object to manage their sync sessions instead of creating `ISyncClient` and `ISyncSession` objects directly. `ISyncSessionDriver` works well for typical applications that have a local data store and that push and pull records during every sync. `ISyncSessionDriver` uses a delegation model where application-specific objects implement some required and some optional methods.

The application supplies two objects to the driver to help control a sync session. The responsibility of the _data source_ is to provide client information and maintain local records—the data source conforms to the `ISyncSessionDriverDataSource` protocol. The responsibility of the _delegate_ is to optionally intervene during the syncing process and perform application-specific tasks. By default, the data source and delegate are the same object. Explicitly set the delegate object if you want a separate object to control a sync session.

The following sections describe the data source and delegate methods in the sequence they are invoked in a typical application. The process involves creating a driver, setting a delegate, and starting a sync session. Some of the data source methods are required and some are optional. All of the delegate methods are optional. The driver sends a series of messages to the data source and delegate:

1. The driver requests information from the data source, such as the client identifier and client description property list before starting a sync session.
2. The driver requests changes to local records from the data source during the pushing phase.
3. The driver sends server-side changes to the data source during the pulling phase.
4. The driver can notify the delegate before and after each phase during the syncing process. For example, notify the delegate when the pulling phase is done or when a session is about to be canceled.

The data source and delegate are also responsible for identifying client-side errors and notifying the driver. They can cancel a sync session at any time. Read [Handling Errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztmmbqfvjvomi) for details.

An `ISyncSessionDriver` object can be used for multiple sync sessions—typically, there's one `ISyncSessionDriver` object per application.

This chapter uses code fragments from the _[SimpleStickies](../../../samplecode/SimpleStickies/SimpleStickies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmbvge)_ sample code project. Also read _ISyncSessionDriverDataSource Protocol Reference_ and _ISyncSessionDriver Class Reference_ for a complete description of the data source and delegate methods.

First you create an `ISyncSessionDriver` object and set its data source as follows:

```
    // Create an ISyncSessionDriver object
    sessionDriver = [[ISyncSessionDriver sessionDriverWithDataSource:myDataSource] retain];
```

If you do not set the delegate using the `setDelegate:` method, the data source and delegate are the same object.

Some data source methods are required. For example, a data source must provide a client identifier and client description property list in order for an `ISyncSessionDriver` object to create an `ISyncClient` object. The `sessionDriverWithDataSource:` method raises an exception if required methods are not implemented. The following sections cover the different data source methods in detail.

You start a sync session by sending either `sync` or `startAsynchronousSync:` to an `ISyncSessionDriver` object. The following code fragment uses `sync` as follows:

```
    // Begin a sync session.
    NSError *syncError;
    BOOL syncSuccess = [sessionDriver sync];
    if (syncSuccess == NO){
        syncError = [sessionDriver error];
        NSAlert *theAlert = [NSAlert alertWithError:syncError];
        [theAlert runModal];
    }
```

The `sync` method sends a series of messages to the data source and delegate to create the client and session objects. The data source is required to implement some methods invoked during pushing and pulling, and the delegate can optionally implement other callback methods during the entire process.

The `sync` method returns `NO` if an error occurs in either the sync session or the application. How you handle the error is application dependent. Typically, you log or display the error message and set the next preferred sync mode accordingly. See [Handling Errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztmmbqfvjvomi) for more details.

Optionally, use the `startAsynchronousSync:` method if you need to sync asynchronously. In this case, you might implement the delegate methods to get notification when the sync session finishes or cancels.

The driver takes care of the details of registering schemas and clients with the sync engine so you don't have to. The driver sends the following messages to the data source to register the client and any schemas.

A data source must provide a client identifier—a unique string that identifies your application—by implementing the `clientIdentifier` method. Typically, the client identifier is a reverse DNS-style string that identifies your organization and application as follows:

```objc
- (NSString *)clientIdentifier
{
    return @"com.mycompany.SimpleStickies";
}
```


A data source must provide a client description property list by implementing the `clientDescriptionURL` method. In this sample code, the `ClientDescription.plist` file is located in the application `Resources` directory:

```objc
- (NSURL *)clientDescriptionURL
{
    return [NSURL fileURLWithPath:[[NSBundle mainBundle] pathForResource:@"ClientDescription" ofType:@"plist"]];
}
```

The client description property list contains additional information about the client as well as the entities and properties that it syncs. The entities and properties may be a subset of the entities and properties defined in the schemas. See [Client Description Properties](Registering%20Clients.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjvfuytgnzwhezq) for a complete description of the client description property list.

The data source must implement the `schemaBundleURLs` method to return an array of NSURL objects containing the paths to the schemas. In this sample code, the schema called `Stickies.syncschema` is located in the application's `Resource` directory:

```objc
- (NSArray *)schemaBundleURLs {
    return [NSArray arrayWithObject:[NSURL fileURLWithPath:
        [[[NSBundle mainBundle] resourcePath] stringByAppendingPathComponent:@"Stickies.syncschema"]]];
}
```

This method is invoked once before each sync session starts so it should return the paths to all the schemas used by your application. See [Creating a Sync Schema](Creating%20a%20Sync%20Schema.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjtfvbuuqsfjbaucry) for how to create your own schema or extend an existing schema.

The driver needs to know which entities from the client description property list you intend to push and pull during this sync session. The data source may optionally implement the `entityNamesToSync` method to return a subset of the entities declared in the client description property list. If the data source does not implement this method, the default is to sync all entities in the client description property list. The implementation of this method simply returns an NSArray object (containing NSString objects) and is application-specific.

The data source can optionally implement the `entityNamesToPull` method to specify a subset of entities to pull. Implement this method only if the entities are different from those returned by the `entityNamesToSync` method or declared in the client description property list.

All clients need to negotiate a sync mode before pushing and pulling records. The driver checks to see whether the data source prefers a particular sync mode.

The data source must implement the `preferredSyncModeForEntityName:` method. You may return a different result for each entity name that is passed as a parameter to this method. It is therefore the responsibility of the application to remember the previous sync mode and track errors per entity name if applicable. This method may return one of the constants described in _ISyncSessionDriverDataSource Protocol Reference_.

For example, when you first sync you might want to request a slow sync and thereafter, a fast sync. However, if you failed to save records during the last sync, you might request a refresh or slow sync. The data source maintains the state of its local records and tracks changes so it can make the appropriate request; otherwise, it should always request a slow sync.

What methods are invoked during the pushing phase depends on how the data source tracks changes to local records and what the current sync mode is.

During a slow or refresh sync, the driver requests all the client records so that it can compare them with the records in the truth database and resolve conflicts. Therefore, the data source is required to implement the `recordsForEntityName:moreComing:error:` method to return all records. Records are expected to be a dictionary representation. Read `[“Pushing Records”](SessionManagement.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrsfuytmmbvhazq)` for a description of a sync record.

During a fast sync, the driver sends a request to the data source for all changes to local records. If the data source tracks changes to individual properties then it can push just the changes. To do this the data source implements the `changesForEntityName:moreComing:error:` method to return an array of `ISyncChange` objects that describe the changes. See _ISyncChange Class Reference_ for how to create these objects.

Otherwise, if the data source knows only which records changed, it pushes all the changed records and the sync engine compares the old records with the new records to apply changes to individual properties. The data source implements the `changedRecordsForEntityName:moreComing:error:` method to return the changed records. Records are expected to be a dictionary representation. Read [Pushing Records](Managing%20Your%20Sync%20Session.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrsfuytmmbvhazq) for a description of a sync record.

The data source is required to implement one of these methods if the `preferredSyncModeForEntityName:` method may return `ISyncSessionDriverModeFast`.

During a fast sync, the driver also requests the record identifiers for records that were deleted. The data source can either pass back deletion changes using an `ISyncChange` object returned by the `changesForEntityName:moreComing:error:` method, or implement the `identifiersForRecordsToDeleteForEntityName:moreComing:error:` method to return the record identifiers.

The `identifiersForRecordsToDeleteForEntityName:moreComing:error:` method is optional.

All the pushing methods support batching. Set the value referenced by the the `moreComing:` parameter to `YES` if you want to batch changes or records. The method is invoked repeatedly until the `moreComing:` parameter is set to `NO`.

Typically, the data source just needs to apply changes during the pulling phase, but the data source can also reformat records and change record identifiers.

Typically, the driver sends changes to the data source during the pulling phase. Changes may include deletions, additions, and changes to existing records. Therefore, the data source is required to implement the `applyChange:forEntityName:remappedRecordIdentifier:formattedRecord:error:` method. The implementation should send the `type` `ISyncChange` method to the `applyChange:` parameter to determine the type of change as in this sample code:

```objc
- (ISyncSessionDriverChangeResult)applyChange:(ISyncChange *)change
                                forEntityName:(NSString *)entityName
                     remappedRecordIdentifier:(NSString **)outRecordIdentifier
                              formattedRecord:(NSDictionary **)outRecord
                                        error:(NSError **)outError
{
    // Delete a record
    if ([change type] == ISyncChangeTypeDelete){
        ...
    }

    // Add a record
    else if ([change type] == ISyncChangeTypeAdd){
        ...
    }
    // Change a record
    else {
        ...
    }
    return ISyncSessionDriverChangeAccepted;
}
```

How you apply the changes to your local records is application dependent. See _ISyncChange Class Reference_ for other methods the data source can use to get the changes.

This method returns one of the change constants described in _ISyncSessionDriverDataSource Protocol Reference_ to notify the driver if the change is successfully applied. Otherwise, the local records can become out of sync with the truth database and the client should slow sync the next time it syncs.

Occasionally, the driver requests that the data source delete all local records—for example, when due to other circumstances the client must pull the truth. Therefore, the data source is required to implement the `deleteAllRecordsForEntityName:error:` method.

When pulling records from the sync engine, the client can optionally change the format of property values without the sync engine interpreting the reformatting as changes to the values and mistakenly syncing the changes to other clients. Use the `formattedRecord:` parameter in the `applyChange:forEntityName:remappedRecordIdentifier:formattedRecord:error:` method to specify an alternate format for a record. Read [Formatting Records](Formatting%20Records.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjsfvbuuqsfjjbeqsa) for more details.

Occasionally a client needs to change the local record identifiers supplied by the sync engine, especially if the local data store uses its own record identifiers. If the data source knows the preferred record identifier when the `applyChange:forEntityName:remappedRecordIdentifier:formattedRecord:error:` method is invoked, it can use the `remappedRecordId:` parameter to pass back the new record identifier.

Otherwise, the data source can change the record identifiers later by sending `clientChangedRecordIdentifiers:` to the `ISyncSession` object as follows:

```
[[syncDriver session] clientChangedRecordIdentifiers:oldToNewDictionary];
```

The `session` method returns `nil` if the sync session is finished. Therefore, invoke this method before a sync session is finished. Read [Customizing Sync Behavior](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztmmbqfvjvomy) for methods the delegate can implement to do this.

The session driver can optionally handle sync alerts for you. A sync alert is an invitation to join a sync session with other clients that you observe. You specify the types of clients to observe in the client description property list. By default a session driver does not handle sync alerts. Send `setHandlesSyncAlerts:` to the session driver passing `YES` as the parameter to turn on this feature.

If the session driver handles sync alerts, then it registers a sync alert handler and receives notifications for requests to join sync sessions. When the session driver receives a request, it initiates a sync session. It uses the `startAsynchronousSync:` not the `sync` method to start the sync session so it doesn’t sync in the main thread.

If you prefer to handle sync alerts yourself, then you typically implement the `sessionDriver:didRegisterClientAndReturnError:` delegate method to set your own handler.

The delegate can implement any number of optional callback methods to intervene during the phases of a sync session. A client might do this to execute local database operations or monitor the progress of a sync session.

For example, the delegate might implement the `sessionDriver:didRegisterClientAndReturnError:` method to set up an application-specific sync alert handler. Read [Syncing with Other Clients](Syncing%20with%20Other%20Clients.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjzfvbecssfifeukri) for details on joining sync sessions.

The delegate might implement the `sessionDriver:didPullAndReturnError:` method to resolve relationships between local records after a pulling phase.

The delegate might implement the `sessionDriver:willFinishSessionAndReturnError:` method to save local changes and change record identifiers once they are known (typical actions if you are using a relational database to store your records).

Similarly the delegate might implement the `sessionDriverWillCancelSession:` method to revert the local records to the state before the sync session started.

Syncing records is a complex process. Errors can occur at every level during this process including client-side errors that corrupt the local data store.

Most of the delegate and data source methods invoked by the driver during a sync session have an `...Error:` or `error:` parameter that your object can use to pass back descriptions of the error that occurred. When implementing these methods, you should return `NO` if an error occurred and set the `...Error:` or `error:` parameter accordingly. Other methods that have an `...Error:` or `error:` parameter may return `ISyncSessionDriverChangeError` to indicate an error.

If an error occurs, the driver prematurely cancels the sync session. Eventually, an `NSError` object is passed back to the method that originally started the sync session. For example, the `sync` method returns `NO` if an error occurred in either Sync Services, the data source, or the delegate. Use the `lastError` method to get and handle the error. For example, the code fragment in [Starting a Sync Session](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztmmbqfvjvomq) displays an alert panel.

[Next](Syncing%20Core%20Data%20Applications.md)[Previous](Formatting%20Records.md)

