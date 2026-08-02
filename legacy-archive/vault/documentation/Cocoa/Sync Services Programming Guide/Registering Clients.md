---
title: Sync Services Programming Guide
apple_id: TP40001178
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-07-06'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SyncServices/Articles/RegisteringClients.html
archived_at: '2026-07-15T07:19:38.707208Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sync Services Programming Guide](Introduction%20to%20Sync%20Services%20Programming%20Guide.md)


[Next](Syncing%20Relationships.md)[Previous](Registering%20Schemas.md)

# Registering Clients

Before you can sync any records, you need to register your client with the sync engine. You do this by specifying a unique client identifier and client description property list.

The lifetime of a sync client is dependent on the lifetime of the data you are syncing, not the lifetime of the application or tool that syncs. The sync engine keeps a snapshot of the client records that it uses when mingling in order to compute the changes that will be pulled by the client—changes that were possibly made by other clients. This information is retained until you unregister your client.

If you unregister a client, the snapshot is removed along with all other information the sync engine knew about your client. Consequently, if you unregister your client when the application terminates, you will not be able to fast sync the next time it launches.

Typically, you use one client identifier per data source or data file containing the records you want to sync, and you reuse that client identifier each time your application or tool launches. For this reason, you typically use a reverse DNS-style name as your client identifier. For example, the client identifier for the Events example application is `com.mycompany.syncexamples.events`.

You can see whether a client exists before registering it (see the sample code in [How to Register a Client](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjvfuytgobqg43q)). You unregister your client only if your data is corrupted or removed.

You register a client using the `registerClientWithIdentifier:descriptionFilePath:` method of `ISyncManager`. When you register a client, you specify a unique client identifier. For example, you can use a reverse DNS-style name such as `com.mycompany.syncexamples.MediaAssets`.

You also specify a client description property list that describes the client’s capabilities. You cannot sync any records without specifying the supported entities and properties in the client description. The client description may contain a subset of the entities and properties defined in a schema but _must_ contain all the required properties. If a client does not support required properties it will fail to register. See [Client Description Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjvfuytgnzwhezq) for a description of this property list.

You use the `clientWithIdentifier:` method of `ISyncManager` to get an existing registered client. In this sample code, the `getSyncClient` method returns a client if it exists; otherwise, it registers it:

```objc
// Returns a sync client for this application
- (ISyncClient *)getSyncClient {
    // Get an existing client
    ISyncClient *client =
         [[ISyncManager sharedManager] clientWithIdentifier:clientID];
    if (client != nil) {
        return client;
    }

    client = [[ISyncManager sharedManager] registerClientWithIdentifier:clientID
        descriptionFilePath:[[NSBundle mainBundle] pathForResource:@"ClientDescription" ofType:@"plist"]];

    return client;
}
```


The client description is a property list stored in a file so that it can be updated independent of the client process. The sync engine periodically checks the client description file for changes, and if the file changed, the sync engine updates the client’s capabilities.

The properties of a client description are listed in [Table 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjvfvjvomi).

__Table 1__  Client description properties

| Property | Description |
| `Type` | A string identifying the type of client. This string must be one of the following predefined values: `app` (an application like iCal or Address Book), `device` (a phone, PDA or iPod), `server` (MobileMe) or `peer` (a peer-to-peer client). The default is `app`. |
| `DisplayName` | A string containing the display name for this client. |
| `ImagePath` | Path to an image of the client. This must be an absolute path except when the description is taken from a file. If it is a relative path, then it is expected to be relative to the folder containing the client description file. |
| `Entities` | A dictionary mapping entity names to an array. The array contains an array of property names (both attributes and relationships) identifying the properties supported by the client on each record type. The array must include the `com.apple.syncservices.RecordEntityName` property. This key is required. |
| `NeverFormatsRelationships` | A boolean value set to `true` if the client never reformats the destination records of pulled relationships, `false` otherwise. The default value is `false`. If this property is set to `true`, then the sync engine can perform some optimizations on behalf of the client. Read [Formatting Records](Formatting%20Records.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjsfvbuuqsfjjbeqsa) for how to format records.  Deprecated in Mac OS X v10.6. |
| `FormatsRelationships` | A Boolean value set to `true` if the client might format a relationship it pulls. In Mac OS X v10.6 and later, the default value is `false`.  Available in Mac OS X v10.6 and later. |
| `PullOnlyEntities` | An array containing the names of the record types for which the client will pull changes from the engine but never push changes to the engine. |
| `PushOnlyEntities` | An array containing the names of the record types for which the client will only push changes to the engine but never pull changes from the engine. |
| `SyncsWith` | A dictionary specifying the kinds of clients this client wants to sync with. See the `setShouldSynchronize:withClientsOfType:` method of `ISyncClient` for details. |

For example, the following client description property list is used by the MediaAssets and Events example applications to describe their client capabilities. It happens that the client descriptions for each application are the same—each application supports both entities, Event and Media, and all their properties.

```xml
<plist version="1.0">
<dict>
    <key>DisplayName</key>
    <string>Events</string>
    <key>ImagePath</key>
    <string>Events.icns</string>
    <key>Entities</key>
    <dict>
        <key>com.mycompany.syncexamples.Event</key>
        <array>
            <string>com.apple.syncservices.RecordEntityName</string>
            <string>date</string>
            <string>startDate</string>
            <string>endDate</string>
            <string>title</string>
            <string>media</string>
        </array>
        <key>com.mycompany.syncexamples.Media</key>
        <array>
            <string>com.apple.syncservices.RecordEntityName</string>
            <string>date</string>
            <string>imageURL</string>
            <string>title</string>
            <string>event</string>
        </array>
    </dict>
</dict>
</plist>
```


The properties of the `SyncsWith` dictionaries are as follows:

| Property | Description |
| --- | --- |
| `SyncAlertTypes` | An array of the client types that this client wants to sync with. This key is required. |
| `SyncAlertToolPath` | The path of a tool that the engine invokes when a client of the specified type starts syncing. If it is a relative path, then it is expected to be relative to the folder containing the client description file.  The tool is passed at least two key-value pairs as arguments on the command line. The "--sync" key is followed by the client identifier. The “--entitynames” key is followed by a string containing the entity names to be synced separated by commas. The order of the key-value pairs is arbitrary. Any other command-line arguments should be ignored since they might be private.  In general, options are always prefixed with “--” and followed by an optional value. The option and value are delimited by spaces. |

See [Setting Alert Handlers Using the Client Description](Syncing%20with%20Other%20Clients.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjzfuytsmzugq4a) for an example of a client description property list that uses the `SyncsWith` property.

[Next](Syncing%20Relationships.md)[Previous](Registering%20Schemas.md)

