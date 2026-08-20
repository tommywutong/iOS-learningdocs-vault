---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/Connect4.html
archived_at: '2026-07-15T08:02:57.747598Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Connecting%20to%20a%20Database.md) [!Previous Section](Limiting%20the%20Number%20of%20Database%20Connections.md)

# Using Multiple EODatabaseChannels

By default, an EODatabaseContext uses one EODatabaseChannel. However, occasionally your application needs more channels. Conflicts due to "busy channels" can occur when an EODatabaseContext needs to perform a database operation and its EODatabaseChannel is already fetching. Most such conflicts are manifestations of inefficient database access and can be avoided. For more information, see the section ["Cautions in Implementing Accessor Methods"](Gotchas.md#apple-ha3to) in the chapter "[Designing Enterprise Objects](Designing%20Enterprise%20Objects.md#apple-ge2daobr)." However, if you can't eliminate fetching conflicts, using additional EODatabaseChannels is an option.

When an EODatabaseContext needs a new channel because all its current channels are busy, it posts an EODatabaseChannelNeededNotification. If you add yourself as an observer of this notification, you can create new EODatabaseChannels on demand. (For more information on registering for notifications, see the NSNotification and NSNotificationCenter class specifications in the _Foundation Reference_.)
__Note:__  You should set an upper limit on the number of EODatabaseChannels your application registers with an EODatabaseContext. It's very unusual for an EODatabaseContext to require more than two or three EODatabaseChannels.
The following code examples demonstrate creating a new EODatabaseChannel and registering it with an EODatabaseContext:
In Java:

```
EODatabaseContext context; // Assume this exists
EODatabaseChannel channel = new
EODatabaseChannel(context);
if (channel) context.registerChannel(channel);
```


In Objective-C:

```
EODatabaseContext *context; // Assume this exists
EODatabaseChannel *channel = [[EODatabaseChannel alloc]
        initWithDatabaseContext:context];
if (channel) [context registerChannel:channel];
```


The EODatabaseChannel constructor can return __null__ if no more channels can be associated with the EODatabaseContext. Similarly, in Objective-C, the EODatabaseChannel method __initWithDatabaseContext:__ can return __nil__ if no more channels can be associated with the EODatabaseContext. Some database servers and their corresponding adaptors don't support multiple channels per context. For example, the Sybase adaptor only supports one EODatabaseChannel per EODatabaseContext.

[!Table of Contents](Connecting%20to%20a%20Database.md) [!Next Section](Character%20Encodings.md)
