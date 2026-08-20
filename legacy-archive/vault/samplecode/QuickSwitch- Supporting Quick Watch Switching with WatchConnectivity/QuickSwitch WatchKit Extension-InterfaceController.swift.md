---
title: 'QuickSwitch: Supporting Quick Watch Switching with WatchConnectivity'
apple_id: TP40016647
resource_type: Sample Code
platform: watchOS|iOS
topic: null
technology: WatchConnectivity
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/QuickSwitch/Listings/QuickSwitch_WatchKit_Extension_InterfaceController_swift.html
archived_at: '2026-07-18T03:21:46.377815Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QuickSwitch: Supporting Quick Watch Switching with WatchConnectivity](QuickSwitch-%20Supporting%20Quick%20Watch%20Switching%20with%20WatchConnectivity.md)


[Next](QuickSwitch%20WatchKit%20Extension-ExtensionDelegate.swift.md)[Previous](Shared-WatchConnectivityManager.swift.md)

# QuickSwitch WatchKit Extension/InterfaceController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The `InterfaceController` class serves as the root view for QuickSwitch displaying currently selected values.
*/

import WatchKit
import WatchConnectivity

class InterfaceController: WKInterfaceController, WatchConnectivityManagerWatchDelegate, DesignatorColorControllerDelegate, DesignatorControllerDelegate {
    // MARK: Properties

    @IBOutlet var morseButton: WKInterfaceButton!
    @IBOutlet var designatorButton: WKInterfaceButton!
    @IBOutlet var colorImage: WKInterfaceImage!
    @IBOutlet var colorLabel: WKInterfaceLabel!

    var morseCodes: [String] {
        didSet {
            UserDefaults.standard.set(morseCodes, forKey: "MorseCodes")
        }
    }

    var designator: String {
        didSet {
            UserDefaults.standard.set(designator, forKey: "Designator")
        }
    }

    var designatorColor: String {
        didSet {
            UserDefaults.standard.set(designatorColor, forKey: "DesignatorColor")
        }
    }

    override init() {
        morseCodes = UserDefaults.standard.array(forKey: "MorseCodes") as? [String] ?? []
        designator = UserDefaults.standard.string(forKey: "Designator") ?? "-"
        designatorColor = UserDefaults.standard.string(forKey: "DesignatorColor") ?? "Blue"

        super.init()
    }

    override func awake(withContext context: Any?) {
        super.awake(withContext: context)

        // The `WatchConnectivityManager` will provide tailored callbacks to its delegate.
        WatchConnectivityManager.sharedConnectivityManager.delegate = self
    }

    override func contextForSegue(withIdentifier segueIdentifier: String) -> Any? {
        if segueIdentifier == "MorseCode" {
            return MorseContext(morseCodes: morseCodes)
        }
        else if segueIdentifier == "SelectDesignator" {
            return DesignatorContext(currentDesignator: designator, delegate: self)
        }
        else if segueIdentifier == "SelectDesignatorColor" {
            return DesignatorColorContext(selectedRow: designatorColor, delegate: self)
        }

        return nil
    }

    override func willActivate() {
        morseButton.setTitle(morseCodes.first ?? "")
        colorLabel.setText(designatorColor)
        colorImage.setImageNamed("\(designatorColor.lowercased())-checked")

        designatorButton.setTitle(designator)
    }

    // MARK: Convenience

    func updateDesignatorApplicationContext() {
        let defaultSession = WCSession.default()

        do {
            try defaultSession.updateApplicationContext([
                "designator": designator,
                "designatorColor": designatorColor
            ])
        }
        catch let error as NSError {
            print("\(error.localizedDescription)")
        }
    }

    // MARK: WatchConnectivityManagerWatchDelegate

    func watchConnectivityManager(_ watchConnectivityManager: WatchConnectivityManager, updatedWithMorseCode morseCode: String) {
        var morseCodes = self.morseCodes
        morseCodes.insert(morseCode, at: 0)
        self.morseCodes = Array(morseCodes[0..<min(10, morseCodes.count)]) // max 10 entries
        morseButton.setTitle(morseCodes.first ?? "")
    }

    // MARK: DesignatorColorControllerDelegate

    func colorController(_ controller: DesignatorColorController, didSelect designatorColor: String) {
        pop()
        self.designatorColor = designatorColor
        updateDesignatorApplicationContext()
    }

    // MARK: DesignatorControllerDelegate

    func designatorController(_ controller: DesignatorController, didSelect designator: String) {
        pop()
        self.designator = designator
        updateDesignatorApplicationContext()
    }
}
```

[Next](QuickSwitch%20WatchKit%20Extension-ExtensionDelegate.swift.md)[Previous](Shared-WatchConnectivityManager.swift.md)

