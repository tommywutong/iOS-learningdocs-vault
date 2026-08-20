---
title: 'Earthquakes: Populating a Core Data Store Using a Background Queue'
apple_id: TP40014547
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CoreData
published: '2018-05-03'
source_url: https://developer.apple.com/library/archive/samplecode/Earthquakes/Listings/README_md.html
archived_at: '2026-07-27T06:57:09.258913Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Earthquakes: Populating a Core Data Store Using a Background Queue](Earthquakes-%20Populating%20a%20Core%20Data%20Store%20Using%20a%20Background%20Queue.md)


[Previous](Earthquakes-%20Populating%20a%20Core%20Data%20Store%20Using%20a%20Background%20Queue.md)

# README.md

```
# Earthquakes: Using a private-queue context to fetch data in background

This sample demonstrates how to set up a Core Data stack with NSPersistentContainer and use a private-queue context to import data on iOS and macOS.

NSFetchedResultsController, which is newly avaiable on macOS 10.12 but extensively adopted on iOS, is used as the data source of NSTableView. How to do batch deletes with NSBatchDeleteRequest is also covered in this sample.

Note that the data locates in a remote server that is out of our control and does not offer a secure communication channel, we'll use the http version of the URL and add "earthquake.usgs.gov" to the "NSExceptionDomains" value in the  info.plist of this sample. When you commmunicate with your own servers, or when the services you use offer a secure communication option, you should always prefer to use HTTPS.

## Requirements

### Build

Xcode 9 or later, macOS 10.13 SDK or later.
Xcode 9 or later, iOS 11 SDK or later.

### Runtime

macOS 10.13 or later.
iOS 11 or later.

Copyright (C) 2016-2018 Apple Inc. All rights reserved.
```

[Previous](Earthquakes-%20Populating%20a%20Core%20Data%20Store%20Using%20a%20Background%20Queue.md)
