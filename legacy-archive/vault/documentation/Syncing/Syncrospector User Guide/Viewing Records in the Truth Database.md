---
title: Syncrospector User Guide
apple_id: TP40004930
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-07-06'
source_url: https://developer.apple.com/library/archive/documentation/Syncing/Conceptual/SyncrospectorUserGuide/ViewingnSyncSessions/ViewingnSyncSessions.html
archived_at: '2026-07-18T02:07:18.723797Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Syncrospector User Guide](Introduction.md)


[Next](Viewing%20the%20Call%20History.md)[Previous](Viewing%20Sync%20Client%20State.md)

# Viewing Records in the Truth Database

After the schema and client are registered correctly, your client is ready to sync its first records. Whether you use the low-level APIs, Core Data sync, or a sync session driver to sync, the sync process is the same. First your client negotiates a sync mode, then it pushes and pulls changes, and then it finishes or cancels the sync session.

Your client can request a sync mode, but the actual mode used is negotiated with the sync engine because it depends on the state of the sync engine and whether there are any other clients syncing the same entities. The sync mode that the sync engine expects to use is displayed in the Will Sync column when viewing the sync state as described in [Viewing Sync Session State](Viewing%20Sync%20Client%20State.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqmjqgawvgvzw). For example, the sync engine expects to fast sync the Note entity the next time SimpleStickies syncs. This mode can change if, for example, the user requests a refresh sync as described in [Testing Sync Modes](Testing%20Sync%20Modes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqmjqgqwvgvzr).

In most cases, your client fast syncs by just pushing and pulling the changes since the last sync. After it does this, you can use Syncrospector to verify if the changes were applied correctly to the truth database.

Download the _[SimpleStickies](../../../samplecode/SimpleStickies/SimpleStickies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmbvge)_ sample code projects to follow along in this chapter.

You can check to see whether your records are pushed by examining the contents of the truth database. Of course, you’ll need to run your client, create some records, and sync them first.

If you are using your own client, add some records and sync them. Otherwise, add a few Note records using SimpleStickies as follows:

1. Launch SimpleStickies and click the Add button below the table.
2. Select a note record in the table, and set a few properties of the note records in the detail interface—for example, enter some text in the Text field, and change the color of each note record, as shown in Figure 4-1.

   __Figure 4-1__  Modify records

   !
3. Choose Sync from the File menu to save a local copy of the records and push them to the sync engine.
4. If a Sync Alert dialog appears asking whether you would like to sync StickiesWithCoreData changes too, click Sync Stickies.

Then check to see if the records were pushed to the sync engine as follows:

1. Using Syncrospector, choose Truth from the left-side pop-up menu.
2. Click Reload if Syncrospector was running when you synced and the table is empty.
3. Display the Note entities by entering `com.mycompany.stickies.Note` in the search field.

   The records you created should appear in the table.
4. Select a record and click Properties in the detail view to see whether the property values are correct, as shown in Figure 4-2.

   __Figure 4-2__  Displaying record properties

   !!

The truth database keeps track of the state of each record per client that synced it. Most notably, each client has a different local record identifier for each record it syncs. When you sync records for the first time, you can use the local record identifiers provided by the sync engine or optionally generate your own local identifiers. Local record identifiers need to be unique for the lifetime of the record. Read [Managing Your Sync Session](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SyncServices/Articles/SessionManagement.html#//apple_ref/doc/uid/TP40001162) and [Changing Record Identifiers](../../Cocoa/Sync%20Services%20Programming%20Guide/Using%20a%20Session%20Driver.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztmmbqfvjvomrq) to learn more about assigning local record identifiers.

To view the different clients that synced a record, follow the steps in [Viewing Record Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqmrnknlte) and click Client States. Note that the truth database uses a global record identifier that is different from the SimpleStickies local record identifier shown in Figure 4-3.

__Figure 4-3__  Displaying record sync states

!!

The History pane is described in [Viewing the Call History](Viewing%20the%20Call%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqobnknlti).

[Next](Viewing%20the%20Call%20History.md)[Previous](Viewing%20Sync%20Client%20State.md)

