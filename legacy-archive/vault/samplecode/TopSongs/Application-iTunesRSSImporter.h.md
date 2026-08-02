---
title: TopSongs
apple_id: DTS40008925
resource_type: Sample Code
platform: iOS
topic: Performance
technology: CoreData
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/TopSongs/Listings/Application_iTunesRSSImporter_h.html
archived_at: '2026-07-18T03:27:04.164196Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TopSongs](TopSongs.md)


[Next](Application-AppDelegate.m.md)[Previous](Controllers-SongsViewController.h.md)

# Application/iTunesRSSImporter.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Downloads, parses, and imports the iTunes top songs RSS feed into Core Data.
 */

@import UIKit;

@class iTunesRSSImporter, Song, CategoryCache;

// Protocol for the importer to communicate with its delegate.
@protocol iTunesRSSImporterDelegate <NSObject>

@optional
// Notification posted by NSManagedObjectContext when saved.
- (void)importerDidSave:(NSNotification *)saveNotification;
// Called by the importer when parsing is finished.
- (void)importerDidFinishParsingData:(iTunesRSSImporter *)importer;
// Called by the importer in the case of an error.
- (void)importer:(iTunesRSSImporter *)importer didFailWithError:(NSError *)error;

@end


// Although NSURLConnection is inherently asynchronous, the parsing can be quite CPU intensive on the device, so
// the user interface can be kept responsive by moving that work off the main thread. This does create additional
// complexity, as any code which interacts with the UI must then do so in a thread-safe manner.
//
@interface iTunesRSSImporter : NSOperation

@property (nonatomic, strong, readonly) CategoryCache *theCache;
@property (nonatomic, strong) NSURL *iTunesURL;
@property (nonatomic, assign) id <iTunesRSSImporterDelegate> delegate;
@property (nonatomic, strong) NSPersistentStoreCoordinator *persistentStoreCoordinator;

@end
```

[Next](Application-AppDelegate.m.md)[Previous](Controllers-SongsViewController.h.md)

