---
title: Syncrospector User Guide
apple_id: TP40004930
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-07-06'
source_url: https://developer.apple.com/library/archive/documentation/Syncing/Conceptual/SyncrospectorUserGuide/ViewingtheHistory/ViewingtheHistory.html
archived_at: '2026-07-18T02:07:24.073237Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Syncrospector User Guide](Introduction.md)


[Next](Testing%20Sync%20Modes.md)[Previous](Viewing%20Records%20in%20the%20Truth%20Database.md)

# Viewing the Call History

You can use Syncrospector to control the level of logging during a sync session and then view the results. This feature is extremely useful if you are managing your own sync session and may be invoking methods out of order. You can also examine the parameters and return values of each Sync Services method invoked without having to set break points in your code.

Download the _[SimpleStickies](../../../samplecode/SimpleStickies/SimpleStickies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmbvge)_ sample code project to follow along in this chapter.

By default, none of the history preferences are turned on. Choose Preferences from the Syncrospector menu to open the SyncServices Preferences. The history settings are near the bottom of the window, as shown in Figure 5-1. Turn history logging on only when debugging a client; otherwise, it should be turned off to conserve resources. The history preferences are ordered from least to the most detailed. When you select the first option, the second option is enabled revealing more levels of detail in Syncrospector, and so forth. The rest of this chapter describes each history setting in more detail.

__Figure 5-1__  Setting preferences

!

The first history preference takes a snapshot of the Sync Services data after each sync that is then viewable in Syncrospector. Just knowing which records were pushed and pulled in a sync session can be helpful. Follow these steps to turn on this level of detail:

1. Open Preferences in Sycrospector and select the “Save Sync Services history” option. (Click the Cleanup History button if enabled.)
2. Make some changes to your client records and sync it.

   For example, add or remove a Note record in SimpleStickies and select Sync from the File menu.
3. Using Syncrospector, choose History from the left-side pop-up menu.
4. Click the Reload button in the toolbar.
5. Select the last sync session from the list and reveal the contents.

   The list expands to show the clients that participated in the sync session, as shown in Figure 5-2. Currently it just shows SimpleStickies but if you run _[StickiesWithCoreData](../../../samplecode/StickiesWithCoreData/StickiesWithCoreData.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmbvgi)_ at the same time as SimpleStickies, both clients appear in the list as described in [Debugging Multiple Clients](Debugging%20Multiple%20Clients.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqmjqgiwvgvzr).

   __Figure 5-2__  Viewing client history

   !!
6. Select your client from the list—for example, select `com.mycompany.SimpleStickies`.

   If changes were pushed to the sync engine, they are listed in the detail view below. In Figure 5-2, the SimpleStickies client pushed a new Note record.

The second history preference, “Save call history of sync clients”, allows you to view each method call, the parameters passed, and the return values to and from the sync engine.

1. Open Preferences in Syncrospector and select the “Save Sync Services history” option if it is not already selected.
2. Select the “Save call history of sync clients” option (enabled only if “Save Sync Services history” is selected).
3. Click the Cleanup History button.
4. Make some changes to your client records and sync them.
5. Follow steps 3-6 in [Taking a Snapshot](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqobnknlto) to select your client that participated in the last sync session.
6. Click Open Call History to see the history of messages sent from the client to the sync engine during the session.

   The call history window appears, as shown in Figure 5-3. The upper pane displays the trace of Sync Services method calls. When META-INFO is selected in the upper pane, the lower pane displays summary information about the sync session. If you select a method in the upper pane, the lower pane displays the details of that call such as the parameters—often the records that were pushed or pulled—and return value.

   __Figure 5-3__  Viewing call history

   !!

Normally, the call history is saved after the sync session is finished or canceled. If your client is crashing in the middle of a sync session and you need the call history logged after each method call, open Preferences and select the “Save call history after each method call” option. This setting is resource intensive so slows down your client.

[Next](Testing%20Sync%20Modes.md)[Previous](Viewing%20Records%20in%20the%20Truth%20Database.md)

