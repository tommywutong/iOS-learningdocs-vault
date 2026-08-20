---
title: Syncrospector User Guide
apple_id: TP40004930
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-07-06'
source_url: https://developer.apple.com/library/archive/documentation/Syncing/Conceptual/SyncrospectorUserGuide/SyncingMultipleApplications/SyncingMultipleApplications.html
archived_at: '2026-07-18T02:07:09.573105Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Syncrospector User Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Testing%20Sync%20Modes.md)

# Debugging Multiple Clients

The sync engine supports multiple sync clients joining the same sync session. That is, when one client begins a sync session, other clients that sync the same entities can optionally join the sync session. All the information on multiple clients—for example, which records each client pushes and pulls in the sync session—is available in Syncrospector. You can also compare the call history of each client and view other details in the truth database.

Read [Managing Your Sync Session](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SyncServices/Articles/SessionManagement.html#//apple_ref/doc/uid/TP40001162) to understand the phases and sequence of methods called during a sync session.

Download the _[SimpleStickies](../../../samplecode/SimpleStickies/SimpleStickies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmbvge)_ and _[StickiesWithCoreData](../../../samplecode/StickiesWithCoreData/StickiesWithCoreData.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmbvgi)_ sample code projects to follow along in this chapter.

It’s useful to turn on data change alerts when you debug multiple clients. A data change alert is the window that appears to users during a sync session confirming whether or not a set of changes should be applied. Normally, data change alerts appear for MobileMe and device clients only. However, using Syncrospector, you can turn on data change alerts for all clients. The data change alerts appear just before the pulling phase of a sync session.

Follow these steps to turn on data change alerts:

1. Launch Syncrospector.
2. Choose Preferences from the Syncrospector menu to open Preferences.
3. Select the “Always show Data Change Alert for all client types” option, as shown in Figure 7-1.

   __Figure 7-1__  Setting data change alert preferences

   !
4. You can optionally set the threshold for when data change alerts appear by choosing a percentage from the Data Change Alert Threshold pop-up menu. For example, if you choose “more than 25%”, then a data change alert appears only when more than 25% of the total records change. If you are debugging your clients, set the threshold to “any.”

To view the history of multiple clients in the same sync session, launch clients that not only use the same scheme but sync the same entities. At least one client needs to be configured to sync when other clients sync. For example, both SimpleStickies and StickiesWithCoreData sync only when you save local records but they both join other sync sessions. If you turn on data change alerts as described in [Displaying Data Change Alerts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqmjqgiwtembrgy2de) and save the call history as described in [Viewing the Call History](Viewing%20the%20Call%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqobnknlti), then you get a clear picture of what happens when multiple clients sync. Specifically turn on the call history of sync clients to see more details as described in [Viewing the Client Call History](Viewing%20the%20Call%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqobnknltk).

Then follow these steps to view the results of two clients syncing together:

1. Build and launch the SimpleStickies and StickiesWithCoreData sample projects or other clients that sync together.

   StickiesUsingCoreData syncs at startup so you don’t need to save local records to start the sync session.
2. If data change alerts are turned on as described in [Displaying Data Change Alerts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqmjqgiwtembrgy2de), alerts appear in each application before the changes are applied, as show in Figure 7-2. Verify that the data change alert shows the correct changes and click “Sync Stickies” (where “Stickies” is the localized data class display name defined in the schema).

   You should now see a sticky window appear for each Note record you created using SimpleStickies. (Move the windows in StickiesUsingCoreData to see them all.)

   __Figure 7-2__  Data change alert

   !
3. After the clients sync, launch Syncrospector and choose Clients from the left-side pop-up menu.

   Both clients should now appear in the table below the toolbar.
4. Next choose History from the left-side pop-up menu.

   All of the sync sessions are displayed in the table below chronologically.
5. Click the carat in the Generation column of the last sync session to reveal the clients.

   You should see SimpleStickies and StickiesWithCoreData listed in the Client column.
6. Follow the instruction in [Viewing the Client Call History](Viewing%20the%20Call%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqobnknltk) for each client to view both client call histories in separate windows.

You can also view the sync plans of multiple clients during a sync session. The sync plans list the participants and entities each client tells the sync engine it wants to sync during the negotiation phase.

1. Using Syncrospector, select Show Sync Plans from the Window menu.
2. Again, modify some records using one client and sync it to push the changes.
3. If a sync alert appears in the second client, click “Sync <data class display name>” to continue.
4. View the sync plans in the Sync Server window in Syncrospector by selecting the last sync session in the table below the toolbar when the status changes to “done.”

   Both clients should be listed in the Participants column in the detail view. The Entities column should show the entities each client synced, as shown in Figure 7-3.

   __Figure 7-3__  Viewing sync plans

   !

[Next](Document%20Revision%20History.md)[Previous](Testing%20Sync%20Modes.md)

