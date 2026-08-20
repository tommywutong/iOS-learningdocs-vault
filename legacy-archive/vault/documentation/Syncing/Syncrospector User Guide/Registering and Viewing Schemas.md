---
title: Syncrospector User Guide
apple_id: TP40004930
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-07-06'
source_url: https://developer.apple.com/library/archive/documentation/Syncing/Conceptual/SyncrospectorUserGuide/ExaminingtheSchema/ExaminingtheSchema.html
archived_at: '2026-07-18T02:07:08.232410Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Syncrospector User Guide](Introduction.md)


[Next](Viewing%20Sync%20Client%20State.md)[Previous](Debugging%20Sync%20Clients.md)

# Registering and Viewing Schemas

If your client uses a custom schema or a schema extension, the first step is to register it with the sync engine. You can then view it using Syncrospector. You can also view existing schemas—for example, those used by Address Book, iCal, Mail, and other Apple applications. Using Syncrospector to view schemas is an easy way to verify that the sync engine is using the same entities and properties as your client.

Schemas used by Apple applications are also described in _Apple Applications Schema Reference_. Read [Registering Schemas](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SyncServices/Articles/RegisteringSchemas.html#//apple_ref/doc/uid/TP40001154) to programmatically register schemas.

Download the _[SimpleStickies](../../../samplecode/SimpleStickies/SimpleStickies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmbvge)_ sample code project to follow along in this chapter.

Occasionally during development you might need to register a schema manually. For example, you might do this if your client relies on another client to register the schema and it has not done so. You can also unregister a schema if you change it during development. You can also unregister the clients that use that schema.

Follow these steps to register a schema:

1. Launch your client which registers your schema.

   Open `SimpleStickies.xcode`, located in the `SyncServices_SimpleStickies` folder and click Build and Go in Xcode to launch the application or follow launch your own client.
2. Launch Syncrospector, located in the `/Developer/Applications/Utilities` folder.
3. Choose Schema from the left-side pop-up menu.
4. Click Register in the toolbar.
5. Select the schema file in the dialog that appears and click Register.

   If successful, the schema appears in the table below the toolbar.

Follow these steps to unregister a schema (this unregisters all the clients that use the schema too):

1. Launch Syncrospector.
2. Choose Schema from the left-side pop-up menu.
3. Select the schema you want to unregister from the table below the toolbar.
4. Click Unregister in the toolbar.

Follow these steps if you want to just unregister clients that use a schema:

1. Launch Syncrospector.
2. Choose Clients from the left-side pop-up menu.
3. Select the client from the table below the toolbar.
4. Click Unregister in the toolbar.

If you use a custom schema or a schema extension, follow these steps to view the schema using Syncrospector:

1. If necessary, launch your client to register the new schema or schema extension.
2. Launch Syncrospector.
3. Choose Schema from the left-side pop-up menu.
4. Select the schema from the table below, as shown in Figure 2-1.

   __Figure 2-1__  The schema master-detail interface

   !
5. View the entities in the schema in the detail pane below the table.
6. Double-click an entity or click Show Details to view the properties in a separate window, as shown in Figure 2-2.

   __Figure 2-2__  The entity inspector

   !

   A key appears in the first column if the property is an identity key. A checkmark appears in the R column if the property is required. If a “>” character appears in the O column, then the property is a relationship; otherwise, it’s an attribute. A checkmark appears in the X column if the property is excluded from data change alerts (see [Displaying Data Change Alerts](Debugging%20Multiple%20Clients.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzqfvbuqmjqgiwtembrgy2de) for how to turn on data change alerts for all clients). If the property is an attribute, the type is displayed in the Type/Destination column; otherwise, the destination entity name is displayed for a relationship.
7. Click General to view other details such as property dependencies. Read [Property Dependencies](../../Cocoa/Sync%20Services%20Programming%20Guide/Creating%20a%20Sync%20Schema.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjtfuytkojzgm4a) for how to specify property dependencies in a schema.

[Next](Viewing%20Sync%20Client%20State.md)[Previous](Debugging%20Sync%20Clients.md)

