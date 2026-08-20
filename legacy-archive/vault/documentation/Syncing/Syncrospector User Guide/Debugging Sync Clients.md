---
title: Syncrospector User Guide
apple_id: TP40004930
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-07-06'
source_url: https://developer.apple.com/library/archive/documentation/Syncing/Conceptual/SyncrospectorUserGuide/DebuggingSyncClients/DebuggingSyncClients.html
archived_at: '2026-07-18T02:07:08.200523Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Syncrospector User Guide](Introduction.md)


[Next](Registering%20and%20Viewing%20Schemas.md)[Previous](Introduction.md)

# Debugging Sync Clients

Syncrospector is an indispensable developer tool you use to debug your sync client—an application, server, or device that pushes and pulls records to the truth database. The truth database is managed by the sync engine, which is the _server_ in this client-server model. You don’t need to run your client in a debugger or even have the source code available to examine the interaction with the sync engine and the state of the truth database using Syncrospector. Syncrospector is especially useful if your client joins sync sessions when other clients sync. You can even verify whether Apple clients such as MobileMe syncs records as you expect.

Regardless of the Sync Services framework method you choose to sync your client—whether you use the low-level APIs, Core Data sync, or a sync session driver—you need to understand the phases of a sync session to debug your client. Core Data sync and the sync session driver may manage most of the sync session for you but you still need to understand when in the process a client is suppose to push changes, for example, to verify that your client is syncing correctly. You can use Syncrospector to verify whether a client performs these steps correctly:

1. Registers a custom schema.
2. Registers its client description.
3. Syncs as follows:

   1. Negotiates a sync mode.
   2. Pushes changes.
   3. Pulls changes.
   4. Finishes or cancels syncing.
4. Refresh syncs on request.
5. Joins sync sessions.

Read [Sync Services Overview](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SyncServices/Articles/SyncOverview.html#//apple_ref/doc/uid/TP40001151) and [Managing Your Sync Session](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SyncServices/Articles/SessionManagement.html#//apple_ref/doc/uid/TP40001162) to learn more about the Sync Services client-server architecture and phases of a sync session. If you are using Core Data sync or a sync session driver, you don’t need to know the API details but you should glance at the flow charts in [Managing Your Sync Session](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SyncServices/Articles/SessionManagement.html#//apple_ref/doc/uid/TP40001162) to better understand the details of the steps above.

The following chapters cover tasks you can perform using Syncrospector during each of the above steps. For example, all clients should verify whether they refresh sync correctly since this is a user-generated request, not a sync mode controlled by your client. You can use Syncrospector to force a refresh sync or any other sync mode you want to test.

[Next](Registering%20and%20Viewing%20Schemas.md)[Previous](Introduction.md)

