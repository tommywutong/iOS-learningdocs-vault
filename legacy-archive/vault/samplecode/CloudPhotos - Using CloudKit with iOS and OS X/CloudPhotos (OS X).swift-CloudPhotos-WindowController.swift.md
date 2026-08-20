---
title: 'CloudPhotos : Using CloudKit with iOS and OS X'
apple_id: TP40016061
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CloudKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/CloudPhotos/Listings/CloudPhotos__OS_X__swift_CloudPhotos_WindowController_swift.html
archived_at: '2026-07-18T03:03:32.502430Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudPhotos : Using CloudKit with iOS and OS X](CloudPhotos%20-%20Using%20CloudKit%20with%20iOS%20and%20OS%20X.md)


[Next](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-MediaObjectToLocationTransformer.swift.md)[Previous](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-SplitViewController.swift.md)

# CloudPhotos (OS X).swift/CloudPhotos/WindowController.swift

```swift
/*
Copyright (C) 2017 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
View controller that shows the location of a photo in a popover.
*/

import Cocoa
import Foundation

class WindowController : NSWindowController, NSWindowRestoration {
    override func windowDidLoad() {
        super.windowDidLoad()

        // We handle the window restoration (so restore0WindowWithIdentifier can be called).
        // Note: The "restorable" and "identifier" properties are setup in IB.
        //
        window!.restorationClass = WindowController.self
    }

    /// Sent to request that this window be restored.
    static func restoreWindow(withIdentifier identifier: String, state: NSCoder, completionHandler: @escaping (NSWindow?, Error?) -> Swift.Void) {
        var restoreWindow: NSWindow? = nil
        if identifier == "CloudPhotosID" {  // This is the identifier for our NSWindow.

            // We didn't create the window, it was created from the storyboard.
            restoreWindow = NSApplication.shared().windows[0]
        }
        completionHandler(restoreWindow, nil)
    }
}
```

[Next](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-MediaObjectToLocationTransformer.swift.md)[Previous](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-SplitViewController.swift.md)

