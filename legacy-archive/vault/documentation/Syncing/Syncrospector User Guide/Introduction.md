---
title: Syncrospector User Guide
apple_id: TP40004930
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-07-06'
source_url: https://developer.apple.com/library/archive/documentation/Syncing/Conceptual/SyncrospectorUserGuide/Introduction/Introduction.html
archived_at: '2026-07-18T02:07:09.471447Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Debugging%20Sync%20Clients.md)

# Introduction

Syncrospector is a developer tool you can use to help debug your Sync Services applications. Sync Services is a framework containing all the components you need to sync your applications and devices. By using Sync Services, user data can be synced with other applications and devices on the same computer, or other computers over the network via MobileMe. The process of syncing client records is complex. Syncrospector helps you verify that your client is syncing correctly every step of the way.

For many reasons, designing, implementing, and debugging your syncing application can be challenging—for example, multiple applications may join a sync session, your application may crash, your local data file may be missing when your application launches, and you might want to trickle sync. This user guide focuses on the responsibilities of the application and how to use Syncrospector to debug your application.

This book uses two sample applications, _[SimpleStickies](../../../samplecode/SimpleStickies/SimpleStickies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmbvge)_ and _[StickiesWithCoreData](../../../samplecode/StickiesWithCoreData/StickiesWithCoreData.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmbvgi)_, to show you how to debug your sync client. Before reading further, download these sample code projects or follow along using your own sync client.

You should read this document if you are developing an application or tool that uses Sync Services. This document contains information on debugging your Sync Services _client_ using Syncrospector.

The following articles cover several aspects of developing a Sync Services application:

- [Debugging Sync Clients](Debugging%20Sync%20Clients.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqojnknltc) describes the overall process of syncing and what phases you should test.
- [Registering and Viewing Schemas](Registering%20and%20Viewing%20Schemas.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqmjqgywvgvzr) describes how to check whether your schema is registered correctly.
- [Viewing Sync Client State](Viewing%20Sync%20Client%20State.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqmjqgawvgvzr) explains how to set up the Syncrospector tool and view status about clients and sync sessions.
- [Viewing Records in the Truth Database](Viewing%20Records%20in%20the%20Truth%20Database.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqmrnknltc) shows how to examine the contents of the truth database after syncing.
- [Viewing the Call History](Viewing%20the%20Call%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqobnknlti) describes how to view the call history of a sync session.
- [Testing Sync Modes](Testing%20Sync%20Modes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqmjqgqwvgvzr) describes how to emulate different sync modes.
- [Debugging Multiple Clients](Debugging%20Multiple%20Clients.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqmjqgiwvgvzr) describes how to view the call history of two clients that join the same sync session.

For a complete description of the Sync Services classes and methods, read:

- _[Sync Services Programming Guide](../../Cocoa/Sync%20Services%20Programming%20Guide/Introduction%20to%20Sync%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnzy)_, which discusses Sync Services concepts such as the architecture, components, creating a schema, and managing a sync session.
- _Sync Services Framework Reference_, which contains a description of each class, method, and type.

If you are using or extending an Apple Applications schema, such as contacts, bookmarks, or calendars, read:

- _Apple Applications Schema Reference_, which describes the different Apple Applications schemas that you can use in your applications.
[Next](Debugging%20Sync%20Clients.md)

