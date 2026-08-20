---
title: 'QuickSwitch: Supporting Quick Watch Switching with WatchConnectivity'
apple_id: TP40016647
resource_type: Sample Code
platform: watchOS|iOS
topic: null
technology: WatchConnectivity
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/QuickSwitch/Listings/QuickSwitch_WatchKit_Extension_ExtensionDelegate_swift.html
archived_at: '2026-07-18T03:21:46.337038Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QuickSwitch: Supporting Quick Watch Switching with WatchConnectivity](QuickSwitch-%20Supporting%20Quick%20Watch%20Switching%20with%20WatchConnectivity.md)


[Next](QuickSwitch%20WatchKit%20Extension-DesignatorColorController.swift.md)[Previous](QuickSwitch%20WatchKit%20Extension-InterfaceController.swift.md)

# QuickSwitch WatchKit Extension/ExtensionDelegate.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The extension delegate.
*/

import WatchKit
import WatchConnectivity

class ExtensionDelegate: NSObject, WKExtensionDelegate {
    var wcBackgroundTasks: [WKWatchConnectivityRefreshBackgroundTask]

    override init() {
        wcBackgroundTasks = []
        super.init()

        let defaultSession = WCSession.default()
        defaultSession.delegate = WatchConnectivityManager.sharedConnectivityManager

        /*
         Here we add KVO on the session properties that this class is interested in before activating 
         the session to ensure that we do not miss any value change events
         */
        defaultSession.addObserver(self, forKeyPath: "activationState", options: [], context: nil)
        defaultSession.addObserver(self, forKeyPath: "hasContentPending", options: [], context: nil)

        defaultSession.activate()
    }

    override func observeValue(forKeyPath keyPath: String?, of object: Any?, change: [NSKeyValueChangeKey : Any]?, context: UnsafeMutableRawPointer?) {
        DispatchQueue.main.async {
            self.completeAllTasksIfReady()
        }
    }

    // MARK: Background

    func handle(_ backgroundTasks: Set<WKRefreshBackgroundTask>) {
        for backgroundTask in backgroundTasks {
            if let wcBackgroundTask = backgroundTask as? WKWatchConnectivityRefreshBackgroundTask {
                // store a reference to the task objects as we might have to wait to complete them
                self.wcBackgroundTasks.append(wcBackgroundTask)
            } else {
                // immediately complete all other task types as we have not added support for them
                backgroundTask.setTaskCompleted()
            }
        }
        completeAllTasksIfReady()
    }

    // MARK: Convenience

    func completeAllTasksIfReady() {
        let session = WCSession.default()
        // the session's properties only have valid values if the session is activated, so check that first
        if session.activationState == .activated && !session.hasContentPending {
            wcBackgroundTasks.forEach { $0.setTaskCompleted() }
            wcBackgroundTasks.removeAll()
        }
    }
}
```

[Next](QuickSwitch%20WatchKit%20Extension-DesignatorColorController.swift.md)[Previous](QuickSwitch%20WatchKit%20Extension-InterfaceController.swift.md)

