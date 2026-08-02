---
title: Sync Services Programming Guide
apple_id: TP40001178
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-07-06'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SyncServices/Articles/Formatting.html
archived_at: '2026-07-15T07:19:38.174463Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sync Services Programming Guide](Introduction%20to%20Sync%20Services%20Programming%20Guide.md)


[Next](Using%20a%20Session%20Driver.md)[Previous](Filtering%20Records.md)

# Formatting Records

When pulling records from the sync engine, the client can change the format of property values without the sync engine interpreting the reformatting as changes to the values and mistakenly syncing the changes to other clients.

For example, a device that has limited capacity may truncate strings to save space—limit all strings to 12 characters or less—or reformat phone numbers to a preferred style. Records that are changed in this way are called _formatted records_. Typically, you do not want the sync engine to interpret format changes as changes to actual property values and push them to all other clients.

Therefore, if you change the format of a pulled record, you need to notify the sync engine when accepting the record as follows. First you create an NSDictionary containing the key-value pairs of the formatted properties and add the `ISyncRecordEntityNameKey` key to specify the record’s entity name. Then you pass this dictionary as the _formattedRecord_ argument to `clientAcceptedChangesForRecordWithIdentifier:formattedRecord:newRecordIdentifier:`. Thereafter, the sync engine remembers the client’s formatted values and does not generate false changes during a slow sync.

```
NSDictionary *formattedRecord =
    [NSDictionary dictionaryWithObjectsAndKeys:
        entityName, ISyncRecordEntityNameKey,
        [myRecord valueForKey:@"title"], @"title", nil];
[session clientAcceptedChangesForRecordWithIdentifier:recordIdentifier
                                     formattedRecord:formattedRecord
                                  newRecordIdentifier:nil];
```

[Next](Using%20a%20Session%20Driver.md)[Previous](Filtering%20Records.md)

