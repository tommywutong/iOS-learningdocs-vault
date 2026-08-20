---
title: 'Earthquakes: Populating a Core Data Store Using a Background Queue'
apple_id: TP40014547
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CoreData
published: '2018-05-03'
source_url: https://developer.apple.com/library/archive/samplecode/Earthquakes/Introduction/Intro.html
archived_at: '2026-07-27T06:57:09.254556Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](README.md.md)

# Earthquakes: Populating a Core Data Store Using a Background Queue

|  |  |
| --- | --- |
| __Last Revision:__ | Version 2.0, 2018-05-03 Added iOS support. Upgraded to Swift 4. [(Full Revision History)](https://developer.apple.com/library/archive/samplecode/Earthquakes/History/History.html#//apple_ref/doc/uid/TP40014547-RevisionHistory-DontLinkElementID_1) |
| __Build Requirements:__ | macOS 10.13 SDK or later; iOS 11 SDK or later. |
| __Runtime Requirements:__ | macOS 10.13; iOS 11 |

Earthquakes demonstrates how to set up a Core Data stack with NSPersistentContainer and use a private-queue context to import a bunch of data retrieved from a remote server. NSFetchedResultsController, which is newly avaiable on macOS 10.12 but extensively adopted on iOS, is used as the data source of the table view. How to do batch deletes with NSBatchDeleteRequest is also covered in this sample.

[Next](README.md.md)
