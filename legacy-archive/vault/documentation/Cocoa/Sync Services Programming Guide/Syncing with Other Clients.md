---
title: Sync Services Programming Guide
apple_id: TP40001178
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-07-06'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SyncServices/Articles/AlertHandlers.html
archived_at: '2026-07-15T07:19:36.181935Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sync Services Programming Guide](Introduction%20to%20Sync%20Services%20Programming%20Guide.md)


[Next](Using%20Sync%20Anchors.md)[Previous](Syncing%20Relationships.md)

# Syncing with Other Clients

Your client _trickle syncs_ if it syncs frequently and simultaneously when other related clients sync—clients that share the same entities as your client. This article explains how to configure your client to sync with other clients.

Your client syncs with other clients by setting alert handlers to be invoked when clients of a certain type or types sync. Clients can be one of these types: application, device, server or peer (see [Clients](Sync%20Services%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjrfuytenztgq3a)). Your client is assumed to be an application unless you specify otherwise in the client description property list (see [Client Description Properties](Registering%20Clients.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjvfuytgnzwhezq) for details).

Typically, a slow client, such as a device client, alerts a fast client, such as the MobileMe server, to sync. However, a fast client never invites slow clients to join its sync session. For example, if the user syncs the MobileMe server, the user expects it to sync quickly, not be delayed because every slow device hooked up to the computer suddenly wants to join the sync session (unless the user specifically requested that those devices be included). Conversely, if a phone client periodically syncs, then it might alert MobileMe to sync without any performance penalty.

You can specify alert handlers programmatically or by modifying the client description property list. However, delays can occur when syncing with other clients. Therefore, Sync Services offers a nonblocking API so that your applications can still be responsive to the user when syncing.

The first step is to specify the types of clients your client is interested in syncing with. You can send `setShouldSynchronize:withClientsOfType:` multiple times to an `ISyncClient` object to set multiple types. For example, the MediaAssets and Events example applications are configured to sync with any application and server clients that share the same entities as follows:

```
// Specify client types
[client setShouldSynchronize:YES
           withClientsOfType:ISyncClientTypeApplication];
[client setShouldSynchronize:YES
           withClientsOfType:ISyncClientTypeServer];
```

Next you set an alert handler to be invoked when related clients sync. For example, in this code fragment from the MediaAssets example application, `client:mightWantToSyncEntityNames:` is invoked when any application or server client syncs the Media or Event entities:

```
// Specify alert handler
[client setSyncAlertHandler:self selector:
    @selector(client:mightWantToSyncEntityNames:)];
```


Alternatively, you can specify the alert types and an alert tool using the client description property list described in [Client Description Properties](Registering%20Clients.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjvfuytgnzwhezq). For example, the following fragment of a client description property list specifies that an alert tool, called MySyncTool, should be launched whenever an application or server begins syncing entities used by your application.

```
    <key>SyncsWith</key>
    <dict>
        <key>SyncAlertToolPath</key>
        <string>MySyncTool</string>
        <key>SyncAlertTypes</key>
        <array>
            <string>app</string>
            <string>server</string>
        </array>
    </dict>
```

Note that the sync tool path is typically relative to the location of the client description file. Also, if you register both an alert handler programmatically and an alert tool, as show above, then only the alert handler is invoked.

Delays may occur while your client is waiting for related clients to join its sync session. Consequently, Sync Services provides a blocking and nonblocking API when beginning a sync session. See [Starting a Sync Session](Managing%20Your%20Sync%20Session.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrsfuytgojxgu3q) for code examples of the `beginSession...` class methods of ISyncSession.

If you use the blocking API, you can specify how long you are willing to wait for the session to begin. Because unknown events may occur between multiple processes, you should never wait indefinitely for a session to begin. For example, if you have a Cocoa application and a session doesn’t begin after 5 seconds, you might return to the main run loop to process any user events and sync later.

Another delay can occur when the sync session enters the mingling state. Mingling begins when all clients have finished pushing their records and invoked one of the `prepareToPullChanges...` methods of `ISyncSession`. Your client may be delayed if a slower client is still pushing changes. Consequently, Sync Services provides a blocking and nonblocking API to begin the mingling state. See [Mingling](Managing%20Your%20Sync%20Session.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrsfuytimzsgm4q) for code examples of the different `ISyncSession` `prepareToPullChanges...` methods.

[Next](Using%20Sync%20Anchors.md)[Previous](Syncing%20Relationships.md)

