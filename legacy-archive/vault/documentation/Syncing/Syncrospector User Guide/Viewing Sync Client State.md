---
title: Syncrospector User Guide
apple_id: TP40004930
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-07-06'
source_url: https://developer.apple.com/library/archive/documentation/Syncing/Conceptual/SyncrospectorUserGuide/ViewingSyncClients/ViewingSyncClients.html
archived_at: '2026-07-18T02:07:11.983190Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Syncrospector User Guide](Introduction.md)


[Next](Viewing%20Records%20in%20the%20Truth%20Database.md)[Previous](Registering%20and%20Viewing%20Schemas.md)

# Viewing Sync Client State

After verifying that your schema is registered, you should verify that your client—an application, server, or device—successfully registered with the sync engine. Specifically, you need to verify that the client description properties are correct. You can also view the sync state of each entity synced by your client.

Download the _[SimpleStickies](../../../samplecode/SimpleStickies/SimpleStickies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmbvge)_ sample code project to follow along in this chapter.

Your client should register with the sync engine after it launches and provide it with a client description property list as described in [Registering Clients](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SyncServices/Articles/RegisteringClients.html#//apple_ref/doc/uid/TP40001155). Follow these steps to examine the client properties stored in the sync engine:

1. Launch your client.

   Build and run SimpleStickies in Xcode or your client.
2. Launch Syncrospector.
3. Choose Clients from the left-side pop-up menu to see the registered clients.

   You should see SimpleStickies listed as one of the registered clients in the Clients table below the toolbar. All the properties displayed in this table, except Last Sync, are properties you set when registering a client described in [Client Description Properties](../../Cocoa/Sync%20Services%20Programming%20Guide/Registering%20Clients.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjvfuytgnzwhezq). The Last Sync column displays the date the client last synced or `never` if it has not synced yet.
4. Select your client in the table and click Summary to view its properties.

   The Summary pane displays more client description properties, as shown in Figure 3-1.

   __Figure 3-1__  The summary pane

   !

You can examine the known state of each sync session.

1. Follow the steps in [Viewing Client Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqmjqgawvgvzs) to select your client.
2. Click Sync State to see the entities synced by this client in the table below.

   The Sync State table displays the entity name, the date it was last synced, the status of that sync, and how the sync engine plans to sync it the next time, as shown in Figure 3-2. For example, since SimpleStickies already synced at launch, the next time it syncs it will fast sync (only changes are pushed and pulled). Read [Sync Engine](../../Cocoa/Sync%20Services%20Programming%20Guide/Sync%20Services%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjrfuytimbqhaya) for a description of all the sync modes. The number in the Gen column is an identifier for the sync session where the entity was last synced.

   __Figure 3-2__  The Sync State pane

   !

You need to specify both the entities and the entity properties that a client syncs as part of the client description property list described in [Client Description Properties](../../Cocoa/Sync%20Services%20Programming%20Guide/Registering%20Clients.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjvfuytgnzwhezq). Use Syncrospector to verify that your client is syncing the correct entities and properties.

1. Follow the steps in [Viewing Client Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqmjqgawvgvzs) to select your client.
2. Click Registration to see the entities and properties that the client syncs.

   Select an entity in the column on the left in the Registration pane to view the entity properties in the column on the right, as shown in Figure 3-3.

   __Figure 3-3__  The registration pane

   !

[Next](Viewing%20Records%20in%20the%20Truth%20Database.md)[Previous](Registering%20and%20Viewing%20Schemas.md)

