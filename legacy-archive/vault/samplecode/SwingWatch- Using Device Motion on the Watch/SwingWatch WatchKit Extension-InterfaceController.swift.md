---
title: 'SwingWatch: Using Device Motion on the Watch'
apple_id: TP40017286
resource_type: Sample Code
platform: watchOS
topic: null
technology: CoreMotion
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/SwingWatch/Listings/SwingWatch_WatchKit_Extension_InterfaceController_swift.html
archived_at: '2026-07-18T03:25:51.740850Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SwingWatch: Using Device Motion on the Watch](SwingWatch-%20Using%20Device%20Motion%20on%20the%20Watch.md)


[Next](SwingWatch%20WatchKit%20Extension-ExtensionDelegate.swift.md)[Previous](README.md.md)

# SwingWatch WatchKit Extension/InterfaceController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This class is responsible for managing interactions with the interface.
 */

import WatchKit
import Foundation
import Dispatch

class InterfaceController: WKInterfaceController, WorkoutManagerDelegate {
    // MARK: Properties

    let workoutManager = WorkoutManager()
    var active = false
    var forehandCount = 0
    var backhandCount = 0

    // MARK: Interface Properties

    @IBOutlet weak var titleLabel: WKInterfaceLabel!
    @IBOutlet weak var backhandCountLabel: WKInterfaceLabel!
    @IBOutlet weak var forehandCountLabel: WKInterfaceLabel!

    // MARK: Initialization

    override init() {
        super.init()

        workoutManager.delegate = self
    }

    // MARK: WKInterfaceController

    override func willActivate() {
        super.willActivate()
        active = true

        // On re-activation, update with the cached values.
        updateLabels()
    }

    override func didDeactivate() {
        super.didDeactivate()
        active = false
    }

    // MARK: Interface Bindings

    @IBAction func start() {
        titleLabel.setText("Workout started")
        workoutManager.startWorkout()
    }

    @IBAction func stop() {
        titleLabel.setText("Workout stopped")
        workoutManager.stopWorkout()
    }

    // MARK: WorkoutManagerDelegate

    func didUpdateForehandSwingCount(_ manager: WorkoutManager, forehandCount: Int) {
        /// Serialize the property access and UI updates on the main queue.
        DispatchQueue.main.async {
            self.forehandCount = forehandCount
            self.updateLabels()
        }
    }

    func didUpdateBackhandSwingCount(_ manager: WorkoutManager, backhandCount: Int) {
        /// Serialize the property access and UI updates on the main queue.
        DispatchQueue.main.async {
            self.backhandCount = backhandCount
            self.updateLabels()
        }
    }

    // MARK: Convenience

    func updateLabels() {
        if active {
            forehandCountLabel.setText("\(forehandCount)")
            backhandCountLabel.setText("\(backhandCount)")
        }
    }

}
```

[Next](SwingWatch%20WatchKit%20Extension-ExtensionDelegate.swift.md)[Previous](README.md.md)

