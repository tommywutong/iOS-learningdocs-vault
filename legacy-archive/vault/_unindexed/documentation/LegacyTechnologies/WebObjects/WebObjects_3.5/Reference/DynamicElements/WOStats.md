---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOStats.html
archived_at: '2026-07-15T07:55:34.963865Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WOExtensionsTOC.md) [!Previous Section](WOSortOrder.md)

## WOStats

### Synopsis

WOStats is a full-paged component. To access it, use a URL such as this one:

```
    http://localhost/cgi-bin/WebObjects/MyAppName.woa/-/WOStats
```


### Description

The WOStats component is a page that displays statistics about the application. These statistics are recorded by all WebObjects applications. If you need to find out about transaction processing times or how many users are accessing your application, you can access WOStats while the application is running.
The statistics described here are actually recorded by a WOStatisticsStore object. You can use WOStatisticsStore to do things like change the moving average sample size. For more information, see its class specification in the [_WebObjects Class Reference_](../Reference.md).

The WOStats page provides this information:

**Transactions**
: Total number of transactions processed by this application instance. A _transaction_ is defined as one cycle of the WebObjects request-response loop. That is, a transaction begins when the user sends an HTTP request and ends when the user receives a response page. (Starting up the application is a transaction and accessing the WOStats page is a transaction as well.)

**Avg. Transaction Time**
: Average length of time it took to process a transaction.

**Avg. Idle Time**
: Average length of time the application sat idle between transactions.

**Moving Avg. Transaction Time**
: Average length of time it took to process the last _n_ transactions, where _n_ is the moving average sample size.

**Move Avg. Idle Time**
: Average length of time the application sat idle between the last _n_ transactions, where _n_ is the moving average sample size.

**Sample Size for Moving Avg.**
: The number of transactions used to compute moving average statistics, such as the Moving Avg. Transaction Time and the Moving Avg. Idle Time. (The sample size is set through the WOStatisticsStore class.)

**Started at**
: Time at which this application instance started running.

**Running time**
: Length of time this instance has been running.

**Avg. Transactions Per Session**
: Average number of transactions each user performed in a session.

**Total Sessions Created**
: The number of sessions this application has created in its lifetime. A session is created each time a new user accesses an application.

**Current Active Sessions**
: Number of the created sessions that are still alive.

**Peak Active Sessions**
: The maximum number of sessions that have been active at the same time.

**Avg. Session Life**
: Average length of time a session lasted.

**Peak Concurrent Sessions At**
: The date and time at which the peak number of active sessions was reached.

**Memory Usage**
: The amount of memory allocated to the application. Resident Set Size is the number of physical memory pages. Virtual is the number of virtual memory pages.

**Avg. Memory Usage Per Session**
: Average amount of memory each session took.
: The memory display differs depending on the operating system. On Windows NT, you see the amount of memory reserved for this application and the amount committed. On all other platforms, you see the Resident Set Size (the number of physical memory pages) and the Virtual memory size (number of virtual memory pages).

**Response Description for Last User**
: A list of the pages accessed by the last session that timed out. The pages are listed from first accessed to last accessed. This list is the same as the list that appears in the application log, if the application log is enabled.

**Page Statistics**
: A table that shows page generation times for each component in the application. (Only parent components, components that represent a full page, are listed; nested components that represent a portion of a page are not listed.)
: The page generation time is the amount of time it took for the request-response loop to receive the request for that page, process the request, invoke the appropriate action in the request component, and generate the page. Often, the bulk of the time it takes to generate a page happens in the action invocation and response generation phases of the request-response loop. The initial processing of the request takes a minimal amount of time.
: For example, suppose the user clicks a button in Page A that fetches items from a database and displays those items in Page B. The total amount of time it takes to handle the request on Page A, invoke the action, fetch items from the database, and generate Page B is recorded as the amount of time it took to generate Page B.

**Detailed Statistics**
: If the application supports more detailed statistics (which it does if you've overridden __descriptionForResponse:inContext:__ in the application's components), this table shows how many times a particular instance of a component was accessed. (An instance of a component might have different values for the component's instance variables.)

[!Table of Contents](WOExtensionsTOC.md) [!Next Section](WOToManyRelationship.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
