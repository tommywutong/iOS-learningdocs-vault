---
title: Sync Services Programming Guide
apple_id: TP40001178
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-07-06'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SyncServices/Articles/RegisteringSchemas.html
archived_at: '2026-07-15T07:19:39.180546Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sync Services Programming Guide](Introduction%20to%20Sync%20Services%20Programming%20Guide.md)


[Next](Registering%20Clients.md)[Previous](Creating%20a%20Sync%20Schema.md)

# Registering Schemas

Typically, schemas are owned by one client and possibly used by multiple clients, although this approach is not enforced. Usually a schema owner registers the schema with the sync manager. Otherwise, multiple clients must coordinate registering a shared schema. It is highly recommended that you register the schema periodically even if it does not change—for example, register the schema each time your application launches. However, if a schema changes, update it with caution because changing a schema may cause records to be deleted and cause some clients to slow sync.

You register schemas with the shared `ISyncManager` using the `registerSchemaWithBundlePath:` method. Typically, a schema is stored in a bundle along with other related files such as images. The following code fragment gets the schema bundle and registers the schema property list:

```
[[ISyncManager sharedManager] registerSchemaWithBundlePath:@"/Library/SyncServices/Schemas/SyncExamples.syncschema"];
```

You can register a schema multiple times. The sync engine compares the old and new schema and updates the schema only if it changed. If it changed, the new schema replaces the old one, records in the truth database may be deleted, and clients that use the schema may slow sync.

You can also unregister a schema, but doing so removes all records associated with the entities defined in that schema. You unregister a schema using the `unregisterSchemaWithName:` method.

Typically, you do not need to register Apple application schemas. See _Apple Applications Schema Reference_ for more information on Apple application schemas.

Read [Creating a Sync Schema](Creating%20a%20Sync%20Schema.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjtfvbuuqsfjbaucry) for more information on designing your own schemas.

[Next](Registering%20Clients.md)[Previous](Creating%20a%20Sync%20Schema.md)

