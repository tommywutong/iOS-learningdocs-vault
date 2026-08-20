---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/Connect3.html
archived_at: '2026-07-15T08:02:56.737394Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Connecting%20to%20a%20Database.md) [!Previous Section](Logging%20into%20a%20Database.md)

# Limiting the Number of Database Connections

By default, an Enterprise Objects Framework application uses one connection to the database-that is, all of an application's display groups, EODatabaseDataSources, EOEditingContexts, and EODatabaseDataSources share the same database connections. However, if an application accesses multiple databases (an Oracle database and a Sybase database, for example), Enterprise Objects Framework establishes one database connection for each database, and these connections are shared as shown in [Figure 46](#apple-gi3dc).

!

Figure 46. Sharing Database Connections

Because Enterprise Objects Framework uses the minimum number of connections by default, you don't need to do anything to limit the number of connections an application uses. However, you can close connections when they aren't in use.

## Closing Database Connections

Enterprise Objects Framework doesn't close database connections. If many copies of an application are likely to be running at the same time, you may run out of database connections. You can reduce the likelihood of running out if you close connections when they aren't in use. A good time to close an EODatabaseChannel is after a specified period of inactivity. The following method demonstrates the process:
In Java:

```
public void closeChannels() {
    int i, contextCount, j, channelCount;
    NSArray contexts;
    EOObjectStoreCoordinator coordinator;

    coordinator =
(EOObjectStoreCoordinator)EOObjectStoreCoordinator.defau
ltCoordinator();

    contexts = coordinator.cooperatingObjectStores();
    contextCount = contexts.count();
    for (i = 0; i < contextCount; i++) {
        NSArray channels =
((EODatabaseContext)contexts.objectAtIndex(i)).registere
dChannels();
        channelCount = channels.count();
        for (j = 0; j < channelCount; j++) {

((EODatabaseChannel)channels.objectAtIndex(j)).adaptorCh
annel().closeChannel();
        }
    }
}
```


In Objective-C:

```objc
- (void)closeChannels
{
    int i, contextCount, j, channelCount;
    NSArray *contexts;
    EOObjectStoreCoordinator *coordinator;

    coordinator = [EOObjectStoreCoordinator
defaultCoordinator];

    contexts = [coordinator cooperatingObjectStores];
    contextCount = [contexts count];
    for (i = 0; i < contextCount; i++) {
        NSArray *channels = [(EODatabaseContext *)
        [contexts objectAtIndex:i] registeredChannels];
        channelCount = [channels count];

        for (j = 0; j < channelCount; j++) {
            [[(EODatabaseChannel *)
                [channels objectAtIndex:j] adaptorChannel]
                closeChannel];
        }
    }
}
```


The __closeChannels__ method gets the EODatabaseContexts from the default EOObjectStoreCoordinator. Then it gets the EODatabaseChannels registered with each EODatabaseContext. To close the database connection managed by an EODatabaseChannel, __closeChannels__ sends the channel's EOAdaptorChannel a __closeChannel__ message.
The next time a channel is needed, its EODatabaseContext reopens it automatically.
The __closeChannels__ method above assumes that the application only has one EOObjectStoreCoordinator. If your application has multiple coordinators, you would repeat the process for each coordinator. It also assumes that all of the EOCooperatingObjectStores managed by the coordinator are EODatabaseContexts, which is nearly always the case. An EOObjectStoreCoordinator uses only EODatabaseContexts unless you substitute your own EOCooperatingObjectStore subclass. (For more information about EOCooperatingObjectStores, see the chapter ["Application Configurations"](Application%20Configurations.md#apple-ge2tqojy).)

[!Table of Contents](Connecting%20to%20a%20Database.md) [!Next Section](Using%20Multiple%20EODatabaseChannels.md)
