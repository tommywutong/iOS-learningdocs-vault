---
title: 'SpeedySloth: Using HealthKit to build a workout app for Apple Watch'
apple_id: TP40017338
resource_type: Sample Code
platform: watchOS
topic: null
technology: HealthKit
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/SpeedySloth/Listings/SpeedySloth_SpeedySloth_WatchKit_Extension_ParentConnector_swift.html
archived_at: '2026-07-18T03:25:18.355890Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SpeedySloth: Using HealthKit to build a workout app for Apple Watch](SpeedySloth-%20Using%20HealthKit%20to%20build%20a%20workout%20app%20for%20Apple%20Watch.md)


[Next](SpeedySloth-SpeedySloth%20WatchKit%20Extension-WorkoutInterfaceController.swift.md)[Previous](SpeedySloth-SpeedySloth%20WatchKit%20Extension-ConfigurationInterfaceController.swif.md)

# SpeedySloth/SpeedySloth WatchKit Extension/ParentConnector.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utilites class to encapsulate messaging with parent application on iPhone.
 */

import WatchConnectivity


class ParentConnector : NSObject, WCSessionDelegate {
    // MARK: Properties

    var wcSession: WCSession?

    var statesToSend = [String]()

    // MARK: Utility methods

    func send(state: String) {
        if let session = wcSession {
            if session.isReachable {
                session.sendMessage(["State": state], replyHandler: nil)
            }
        } else {
            WCSession.default().delegate = self
            WCSession.default().activate()
            statesToSend.append(state)
        }
    }

    // MARK : WCSessionDelegate

    func session(_ session: WCSession, activationDidCompleteWith activationState: WCSessionActivationState, error: Error?) {
        if activationState == .activated {
            wcSession = session
            sendPending()
        }
    }

    private func sendPending() {
        if let session = wcSession {
            if session.isReachable {
                for state in statesToSend {
                    session.sendMessage(["State": state], replyHandler: nil)
                }
                statesToSend.removeAll()
            }
        }
    }
}
```

[Next](SpeedySloth-SpeedySloth%20WatchKit%20Extension-WorkoutInterfaceController.swift.md)[Previous](SpeedySloth-SpeedySloth%20WatchKit%20Extension-ConfigurationInterfaceController.swif.md)

