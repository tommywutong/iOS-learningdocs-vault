---
title: 'MediaLibraryLoader: Using MLMediaLibrary to load and display photos'
apple_id: TP40017375
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2016-11-03'
source_url: https://developer.apple.com/library/archive/samplecode/MediaLibraryLoader/Listings/MediaLibraryLoader_AppDelegate_swift.html
archived_at: '2026-07-18T03:14:33.523919Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MediaLibraryLoader: Using MLMediaLibrary to load and display photos](MediaLibraryLoader-%20Using%20MLMediaLibrary%20to%20load%20and%20display%20photos.md)


[Next](Document%20Revision%20History.md)[Previous](MediaLibraryLoader-ViewController.swift.md)

# MediaLibraryLoader/AppDelegate.swift

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
The `AppDelegate` class is a delegate to NSApplication responsible for managing the app's main functions.
*/

import Cocoa

@NSApplicationMain

class AppDelegate: NSObject, NSApplicationDelegate {

    func applicationDidFinishLaunching(_ aNotification: Notification) {
        // Insert code here to initialize your application
    }

    func applicationWillTerminate(_ aNotification: Notification) {
        // Insert code here to tear down your application
    }

    func applicationShouldTerminate(_ sender: NSApplication)-> NSApplicationTerminateReply {
        return .terminateNow
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](MediaLibraryLoader-ViewController.swift.md)

