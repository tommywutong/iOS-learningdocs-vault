---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/Connect.html
archived_at: '2026-07-15T08:02:55.287863Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Top](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

#

# Connecting to a Database

---

Normally, you don't have to worry about making connections to the database, because Enterprise Objects Framework connects to the database automatically for you. However, there are times when you may need to intervene. This chapter describes how Enterprise Objects Framework manages database connections and how you can customize the process. It's organized into the following sections:

["When Database Connections Are Opened and Closed"](When%20Database%20Connections%20Are%20Opened%20and%20Closed.md#apple-gizdi) describes when applications open and close database connections.

["Logging into a Database"](Logging%20into%20a%20Database.md#apple-gizdc) describes the process of getting and validating database connection information. It answers the questions "How do I set connection information that's not in a model?" and "How can I suppress an adaptor's login panel in an OpenStep application?"

["Limiting the Number of Database Connections"](Limiting%20the%20Number%20of%20Database%20Connections.md#apple-gi3dg) describes how to close database connections that aren't in use.

["Using Multiple EODatabaseChannels"](Using%20Multiple%20EODatabaseChannels.md#apple-gq4dony) describes how to avoid "busy channel" fetching conflicts.

["Character Encodings"](Character%20Encodings.md#apple-gm4tgoa) describes how to tell both the database and the adaptor what encoding to use.

[!First Section](When%20Database%20Connections%20Are%20Opened%20and%20Closed.md)
