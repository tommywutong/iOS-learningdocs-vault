---
title: Checking and Requesting Access to Data Classes in Privacy Settings
apple_id: DTS40013410
resource_type: Sample Code
platform: iOS
topic: Security
technology: null
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/samplecode/PrivacyPrompts/Listings/PrivacyPrompts_EventKitAccessProvider_swift.html
archived_at: '2026-07-18T03:19:34.077741Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Checking and Requesting Access to Data Classes in Privacy Settings](Checking%20and%20Requesting%20Access%20to%20Data%20Classes%20in%20Privacy%20Settings.md)


[Next](PrivacyPrompts-HealthAccessProvider.swift.md)[Previous](PrivacyPrompts-PhotoWriteOnlyAccessProvider.swift.md)

# PrivacyPrompts/EventKitAccessProvider.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Demonstrates the APIs to check and request access to calendar events and reminders.
 */

import Foundation
import EventKit

class EventKitAccessProvider {
    let eventStore = EKEventStore()
    let type: EKEntityType

    init(type: EKEntityType) {
        self.type = type
    }
}

extension EventKitAccessProvider: PrivateDataAccessProvider {
    var accessLevel: PrivateDataAccessLevel {
        let authorizationStatus = EKEventStore.authorizationStatus(for: type)
        return authorizationStatus.accessLevel
    }

    func requestAccess(completionHandler: @escaping (PrivateDataRequestAccessResult) -> Void) {
        eventStore.requestAccess(to: type) { (_, error) in
            if let error = error {
                print(error)
            }

            DispatchQueue.main.async {
                completionHandler(PrivateDataRequestAccessResult(self.accessLevel))
            }
        }
    }
}

extension EKAuthorizationStatus: PrivateDataAccessLevelConvertible {
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

[Next](PrivacyPrompts-HealthAccessProvider.swift.md)[Previous](PrivacyPrompts-PhotoWriteOnlyAccessProvider.swift.md)

