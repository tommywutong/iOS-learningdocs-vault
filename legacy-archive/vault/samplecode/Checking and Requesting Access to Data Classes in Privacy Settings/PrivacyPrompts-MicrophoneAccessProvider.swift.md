---
title: Checking and Requesting Access to Data Classes in Privacy Settings
apple_id: DTS40013410
resource_type: Sample Code
platform: iOS
topic: Security
technology: null
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/samplecode/PrivacyPrompts/Listings/PrivacyPrompts_MicrophoneAccessProvider_swift.html
archived_at: '2026-07-18T03:19:34.424632Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Checking and Requesting Access to Data Classes in Privacy Settings](Checking%20and%20Requesting%20Access%20to%20Data%20Classes%20in%20Privacy%20Settings.md)


[Next](PrivacyPrompts-User%20Interface-PrivacyClassesTableViewController.swift.md)[Previous](Checking%20and%20Requesting%20Access%20to%20Data%20Classes%20in%20Privacy%20Settings.md)

# PrivacyPrompts/MicrophoneAccessProvider.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Demonstrates the APIs to check and request access to the microphone.
 */

import Foundation
import AVFoundation

class MicrophoneAccessProvider: NSObject {
    let audioSession = AVAudioSession.sharedInstance()
}

extension MicrophoneAccessProvider: PrivateDataAccessProvider {
    var accessLevel: PrivateDataAccessLevel {
        return audioSession.recordPermission().accessLevel
    }

    func requestAccess(completionHandler: @escaping (PrivateDataRequestAccessResult) -> Void) {
        audioSession.requestRecordPermission { (granted) in
            if granted {
                // Setting the category will also request access from the user.
                do {
                    try self.audioSession.setCategory(AVAudioSessionCategoryPlayAndRecord)
                    // Do something with the audio session.
                } catch let error {
                    debugPrint(error)
                }
            } else {
                // Handle denied access gracefully.
            }

            DispatchQueue.main.async {
                completionHandler(PrivateDataRequestAccessResult(self.accessLevel))
            }
        }
    }
}

extension AVAudioSessionRecordPermission: PrivateDataAccessLevelConvertible {
    var accessLevel: PrivateDataAccessLevel {
        switch self {
        case .denied:
            return .denied
        case .undetermined:
            return .undetermined
        case .granted:
            return .granted
        }
    }
}
```

[Next](PrivacyPrompts-User%20Interface-PrivacyClassesTableViewController.swift.md)[Previous](Checking%20and%20Requesting%20Access%20to%20Data%20Classes%20in%20Privacy%20Settings.md)

