---
title: Checking and Requesting Access to Data Classes in Privacy Settings
apple_id: DTS40013410
resource_type: Sample Code
platform: iOS
topic: Security
technology: null
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/samplecode/PrivacyPrompts/Listings/PrivacyPrompts_HomeAccessProvider_swift.html
archived_at: '2026-07-18T03:19:34.295360Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Checking and Requesting Access to Data Classes in Privacy Settings](Checking%20and%20Requesting%20Access%20to%20Data%20Classes%20in%20Privacy%20Settings.md)


[Next](PrivacyPrompts-SpeechRecognitionAccessProvider.swift.md)[Previous](PrivacyPrompts-Supporting%20Files-Localizable.swift.md)

# PrivacyPrompts/HomeAccessProvider.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Demonstrates the APIs to check and request access to home information.
 */

import Foundation
import HomeKit

class HomeAccessProvider: NSObject {
    var homeManager: HMHomeManager?
    var requestAccessCompletionHandler: PrivacyActionRequestAccessHandler?

    private func dispatchAccessResult(_ result: PrivateDataRequestAccessResult) {
        DispatchQueue.main.async {
            guard let completionHandler = self.requestAccessCompletionHandler else { return }
            completionHandler(result)

            // Breaks reference cycle so this object can deinit.
            self.requestAccessCompletionHandler = nil
        }
    }
}

extension HomeAccessProvider: PrivateDataAccessRequestProvider {
    func requestAccess(completionHandler: @escaping (PrivateDataRequestAccessResult) -> Void) {
        requestAccessCompletionHandler = completionHandler

        /*
         HMHomeManager will notify the delegate when it's ready to vend home data.
         It will ask for user permission first, if needed.
         */
        homeManager = HMHomeManager()
        homeManager?.delegate = self
    }
}

extension HomeAccessProvider: HMHomeManagerDelegate {
    func homeManagerDidUpdateHomes(_ manager: HMHomeManager) {
        if !manager.homes.isEmpty {
            // A home exists, so we have access.
            dispatchAccessResult(PrivateDataRequestAccessResult(.granted))
        } else {
            manager.addHome(withName: "Test Home", completionHandler: { (home, error) in
                guard error == nil else {
                    if let error = error as? HMError {
                        if error.code == .homeAccessNotAuthorized {
                            self.dispatchAccessResult(PrivateDataRequestAccessResult(.denied))
                        }
                    } else if let error = error as NSError? {
                        let result = PrivateDataRequestAccessResult(.undetermined, error: error, errorMessageKey: "HOME_ERROR")
                        self.dispatchAccessResult(result)
                    }

                    return
                }

                if let home = home {
                    // Clean up after ourselves, don't leave the Test Home in the HMHomeManager array.
                    manager.removeHome(home, completionHandler: { (_) in
                        // ... do something with the result of removing the home ...
                    })
                }

                self.dispatchAccessResult(PrivateDataRequestAccessResult(.granted))
            })
        }
    }
}
```

[Next](PrivacyPrompts-SpeechRecognitionAccessProvider.swift.md)[Previous](PrivacyPrompts-Supporting%20Files-Localizable.swift.md)

