---
title: Checking and Requesting Access to Data Classes in Privacy Settings
apple_id: DTS40013410
resource_type: Sample Code
platform: iOS
topic: Security
technology: null
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/samplecode/PrivacyPrompts/Listings/PrivacyPrompts_CameraAccessProvider_swift.html
archived_at: '2026-07-18T03:19:33.776735Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Checking and Requesting Access to Data Classes in Privacy Settings](Checking%20and%20Requesting%20Access%20to%20Data%20Classes%20in%20Privacy%20Settings.md)


[Next](PrivacyPrompts-PhotoAccessProvider.swift.md)[Previous](PrivacyPrompts-SpeechRecognitionAccessProvider.swift.md)

# PrivacyPrompts/CameraAccessProvider.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Demonstrates the APIs to request access to the camera.
 */

import Foundation
import AVFoundation

class CameraAccessProvider: PrivateDataAccessProvider {
    var accessLevel: PrivateDataAccessLevel {
        return AVCaptureDevice.authorizationStatus(for: .video).accessLevel
    }

    func requestAccess(completionHandler: @escaping (PrivateDataRequestAccessResult) -> Void) {
        AVCaptureDevice.requestAccess(for: .video) { (_) in
            DispatchQueue.main.async {
                completionHandler(PrivateDataRequestAccessResult(self.accessLevel))
            }
        }
    }
}

extension AVAuthorizationStatus: PrivateDataAccessLevelConvertible {
    var accessLevel: PrivateDataAccessLevel {
        switch self {
        case .authorized:
            return .granted
        case .denied:
            return .denied
        case .notDetermined:
            return .undetermined
        case .restricted:
            return .restricted
        }
    }
}
```

[Next](PrivacyPrompts-PhotoAccessProvider.swift.md)[Previous](PrivacyPrompts-SpeechRecognitionAccessProvider.swift.md)

