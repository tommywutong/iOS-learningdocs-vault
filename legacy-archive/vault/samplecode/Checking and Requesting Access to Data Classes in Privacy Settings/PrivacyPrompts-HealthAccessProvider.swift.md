---
title: Checking and Requesting Access to Data Classes in Privacy Settings
apple_id: DTS40013410
resource_type: Sample Code
platform: iOS
topic: Security
technology: null
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/samplecode/PrivacyPrompts/Listings/PrivacyPrompts_HealthAccessProvider_swift.html
archived_at: '2026-07-18T03:19:34.249515Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Checking and Requesting Access to Data Classes in Privacy Settings](Checking%20and%20Requesting%20Access%20to%20Data%20Classes%20in%20Privacy%20Settings.md)


[Next](PrivacyPrompts-LocationAccessProvider.swift.md)[Previous](PrivacyPrompts-EventKitAccessProvider.swift.md)

# PrivacyPrompts/HealthAccessProvider.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Demonstrates the APIs to check and request access to health information.
 */

import Foundation
import HealthKit

class HealthAccessProvider {
    let healthStore = HKHealthStore()
}

extension HealthAccessProvider: PrivateDataAccessProvider {
    var accessLevel: PrivateDataAccessLevel {
        // Health data is not available on all devices.
        guard HKHealthStore.isHealthDataAvailable() else { return .unavailable }

        if let heartRateType = HKObjectType.quantityType(forIdentifier: .heartRate) {
            let authorizationStatus = healthStore.authorizationStatus(for: heartRateType)
            return authorizationStatus.accessLevel
        }

        return .undetermined
    }

    func requestAccess(completionHandler: @escaping (PrivateDataRequestAccessResult) -> Void) {
        // Health data is not available on all devices.
        guard HKHealthStore.isHealthDataAvailable() else {
            completionHandler(PrivateDataRequestAccessResult(.unavailable))
            return
        }

        if let heartRateType = HKObjectType.quantityType(forIdentifier: .heartRate) {
            let heartRateTypeSet: Set<HKQuantityType> = [heartRateType]

            //  Requests consent from the user to read and write heart rate data from the health store.
            healthStore.requestAuthorization(toShare: heartRateTypeSet, read: heartRateTypeSet) { (_, error) in
                if let error = error {
                    print(error)
                }

                DispatchQueue.main.async {
                    completionHandler(PrivateDataRequestAccessResult(self.accessLevel))
                }
            }
        }
    }
}

extension HKAuthorizationStatus: PrivateDataAccessLevelConvertible {
    var accessLevel: PrivateDataAccessLevel {
        switch self {
        case .notDetermined:
            return .undetermined
        case .sharingAuthorized:
            return .granted
        case .sharingDenied:
            return .denied
        }
    }
}
```

[Next](PrivacyPrompts-LocationAccessProvider.swift.md)[Previous](PrivacyPrompts-EventKitAccessProvider.swift.md)

