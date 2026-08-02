---
title: Checking and Requesting Access to Data Classes in Privacy Settings
apple_id: DTS40013410
resource_type: Sample Code
platform: iOS
topic: Security
technology: null
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/samplecode/PrivacyPrompts/Listings/PrivacyPrompts_User_Interface_PrivacyClassesTableViewController_swift.html
archived_at: '2026-07-18T03:19:34.948294Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Checking and Requesting Access to Data Classes in Privacy Settings](Checking%20and%20Requesting%20Access%20to%20Data%20Classes%20in%20Privacy%20Settings.md)


[Next](PrivacyPrompts-User%20Interface-AppDelegate.swift.md)[Previous](PrivacyPrompts-MicrophoneAccessProvider.swift.md)

# PrivacyPrompts/User Interface/PrivacyClassesTableViewController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Tableview controller that displays all the privacy data classes in the system.
 */

import UIKit

class PrivacyClassesTableViewController: UITableViewController {

    let serviceTypes: [PrivacyDataType] = [
        .advertising,
        .appleMusic,
        .bluetooth,
        .calendars,
        .camera,
        .contacts,
        .faceID,
        .health,
        .home,
        .location,
        .microphone,
        .motion,
        .nfc,
        .photosLibrary,
        .photosLibraryWriteOnly,
        .reminders,
        .siri,
        .speechRecognition
    ]

    // MARK: - Segues

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "takeAction" {
            if let destinationController = segue.destination as? PrivacyActionsViewController, let row = self.tableView.indexPathForSelectedRow?.row {
                let selectedService = serviceTypes[row]
                destinationController.actions = PrivateDataAccessActions(for: selectedService)
            }
        }
    }
}

// MARK: - UITableViewDataSource

extension PrivacyClassesTableViewController {
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return serviceTypes.count
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "privacyClassCell", for: indexPath)
        cell.textLabel?.text = serviceTypes[indexPath.row].localizedValue()

        return cell
    }
}
```

[Next](PrivacyPrompts-User%20Interface-AppDelegate.swift.md)[Previous](PrivacyPrompts-MicrophoneAccessProvider.swift.md)

