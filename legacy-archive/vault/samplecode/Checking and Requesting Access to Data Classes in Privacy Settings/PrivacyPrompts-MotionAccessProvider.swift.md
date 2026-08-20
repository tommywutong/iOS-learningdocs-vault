---
title: Checking and Requesting Access to Data Classes in Privacy Settings
apple_id: DTS40013410
resource_type: Sample Code
platform: iOS
topic: Security
technology: null
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/samplecode/PrivacyPrompts/Listings/PrivacyPrompts_MotionAccessProvider_swift.html
archived_at: '2026-07-18T03:19:34.463672Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Checking and Requesting Access to Data Classes in Privacy Settings](Checking%20and%20Requesting%20Access%20to%20Data%20Classes%20in%20Privacy%20Settings.md)


[Next](PrivacyPrompts-ContactsAccessProvider.swift.md)[Previous](PrivacyPrompts-Data%20Types-PrivacyDataTypes.swift.md)

# PrivacyPrompts/MotionAccessProvider.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Demonstrates the APIs to request access to motion information.
 */

import Foundation
import CoreMotion

class MotionAccessProvider {
    let motionManager = CMMotionActivityManager()
    let activityQueue = OperationQueue()
}

extension MotionAccessProvider: PrivateDataAccessRequestProvider {
    func requestAccess(completionHandler: @escaping (PrivateDataRequestAccessResult) -> Void) {
        motionManager.startActivityUpdates(to: activityQueue) { (_) in
            // Do Something with the activity reported.
            self.motionManager.stopActivityUpdates()

            DispatchQueue.main.async {
                completionHandler(PrivateDataRequestAccessResult(.granted))
            }
        }
    }
}
```

[Next](PrivacyPrompts-ContactsAccessProvider.swift.md)[Previous](PrivacyPrompts-Data%20Types-PrivacyDataTypes.swift.md)

