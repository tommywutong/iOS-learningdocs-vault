---
title: 'SpeedySloth: Using HealthKit to build a workout app for Apple Watch'
apple_id: TP40017338
resource_type: Sample Code
platform: watchOS
topic: null
technology: HealthKit
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/SpeedySloth/Listings/SpeedySloth_SpeedySloth_WorkoutViewController_swift.html
archived_at: '2026-07-18T03:25:18.561026Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SpeedySloth: Using HealthKit to build a workout app for Apple Watch](SpeedySloth-%20Using%20HealthKit%20to%20build%20a%20workout%20app%20for%20Apple%20Watch.md)


[Next](SpeedySloth-SpeedySloth-AppDelegate.swift.md)[Previous](SpeedySloth-Utilities-Utilities.swift.md)

# SpeedySloth/SpeedySloth/WorkoutViewController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View controller for the active workout screen.
 */

import Foundation

import UIKit
import HealthKit
import WatchConnectivity

class WorkoutViewController: UIViewController, WCSessionDelegate {
    // MARK: Properties

    var configuration : HKWorkoutConfiguration?
    let healthStore = HKHealthStore()
    var wcSessionActivationCompletion : ((WCSession)->Void)?

    @IBOutlet var workoutSessionState : UILabel!

    // MARK: UIViewController

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)

        startWatchApp()
    }

    // MARK: Convenience

    func startWatchApp() {
        guard let workoutConfiguration = configuration else { return }

        getActiveWCSession { (wcSession) in
            if wcSession.activationState == .activated && wcSession.isWatchAppInstalled {
                self.healthStore.startWatchApp(with: workoutConfiguration, completion: { (success, error) in
                    // Handle errors
                })
            }
        }
    }

    func getActiveWCSession(completion: @escaping (WCSession)->Void) {
        guard WCSession.isSupported() else { return }

        let wcSession = WCSession.default()
        wcSession.delegate = self

        if wcSession.activationState == .activated {
            completion(wcSession)
        } else {
            wcSession.activate()
            wcSessionActivationCompletion = completion
        }
    }

    func updateSessionState(_ state: String) {
        DispatchQueue.main.async {
            self.workoutSessionState.text = state
        }
    }

    // MARK: WCSessionDelegate

    func session(_ session: WCSession, activationDidCompleteWith activationState: WCSessionActivationState, error: Error?) {
        if activationState == .activated {
            if let activationCompletion = wcSessionActivationCompletion {
                activationCompletion(session)
                wcSessionActivationCompletion = nil
            }
        }
    }

    func session(_ session: WCSession, didReceiveMessage message: [String : Any]) {
        if let state = message["State"] as? String {
            updateSessionState(state)
        }
    }

    func sessionDidBecomeInactive(_ session: WCSession) {
    }

    func sessionDidDeactivate(_ session: WCSession) {
    }
}
```

[Next](SpeedySloth-SpeedySloth-AppDelegate.swift.md)[Previous](SpeedySloth-Utilities-Utilities.swift.md)

