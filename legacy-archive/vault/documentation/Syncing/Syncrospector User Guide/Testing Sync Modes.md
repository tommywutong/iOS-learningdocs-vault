---
title: Syncrospector User Guide
apple_id: TP40004930
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-07-06'
source_url: https://developer.apple.com/library/archive/documentation/Syncing/Conceptual/SyncrospectorUserGuide/RefreshSyncing/RefreshSyncing.html
archived_at: '2026-07-18T02:07:09.508339Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Syncrospector User Guide](Introduction.md)


[Next](Debugging%20Multiple%20Clients.md)[Previous](Viewing%20the%20Call%20History.md)

# Testing Sync Modes

Your application needs to be robust enough to recover from unexpected events such as the loss of a local data file. Using MobileMe preferences, the user can also request various sync modes such as “Push the Truth” and “Pull the Truth.” You can use Syncrospector to test whether your client can handle these situations.

For example, suppose the user creates some data and syncs it and then inadvertently removes the local data file. At this point, the sync engine assumes that the client has copies of the records and does not send them to the client on the next sync. The client needs to explicitly request a refresh sync—that is, remove all local records and “Pull the Truth”—to correct the problem. If this is not done, the sync engine may issue false deletes to other clients. Follow these steps to test whether your application properly handles this case:

1. If you haven’t created any records with SimpleStickies, launch SimpleStickies, create some records, save the file (which syncs the records), and quit.
2. Remove the `com.mycompany.SimpleStickies.xml` file, located in the `~/Library/Application Support/SyncExamples` folder, which contains the local copy of the client’s records.
3. Using Syncrospector, choose Clients from the pop-up menu to view the state of SimpleStickies—select SimpleStickies from the table and click Sync State in the detail view.

   If SimpleStickies fast syncs the next time it syncs and it fails to load the local records when launching, it fails to apply any changes pulled from the sync engine, except adds. If it slow syncs the next time, SimpleStickies does not push any records, and the sync engine assumes that the client deleted those records. This may result in the unintentional loss of data.
4. Force SimpleStickies to slow sync by selecting SimpleStickies from the list of clients and choosing Slow Sync from the right-hand side pop-up menu.

   Now when you click Sync State, the Will Sync mode reads “slow.”
5. Launch SimpleStickies again.

   SimpleStickies syncs immediately after launching. Fortunately, it detects that the local data file is missing and requests a refresh sync. If SimpleStickies did not request a refresh sync, it won’t push any records and the sync engine will issue delete changes to StickiesUsingCoreData and all its sticky windows disappear.

You can simulate other sync modes by choosing other menu items from the Sync Mode pop-up menu. For example, simulate the user pulling the truth by choosing “Pull the Truth” from the Sync Mode pop-up menu.

[Next](Debugging%20Multiple%20Clients.md)[Previous](Viewing%20the%20Call%20History.md)

