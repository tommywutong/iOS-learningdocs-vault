---
title: Checking and Requesting Access to Data Classes in Privacy Settings
apple_id: DTS40013410
resource_type: Sample Code
platform: iOS
topic: Security
technology: null
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/samplecode/PrivacyPrompts/Listings/PrivacyPrompts_FaceIDAccessProvider_swift.html
archived_at: '2026-07-18T03:19:34.124567Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Checking and Requesting Access to Data Classes in Privacy Settings](Checking%20and%20Requesting%20Access%20to%20Data%20Classes%20in%20Privacy%20Settings.md)


[Next](PrivacyPrompts-BluetoothAccessProvider.swift.md)[Previous](PrivacyPrompts-User%20Interface-PrivacyActionsViewController.swift.md)

# PrivacyPrompts/FaceIDAccessProvider.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Demonstrates the APIs to request FaceID access from LocalAuthentication.
 */

import Foundation
import LocalAuthentication

class FaceIDAccessProvider: PrivateDataAccessRequestProvider {

    func requestAccess(completionHandler: @escaping (PrivateDataRequestAccessResult) -> Void) {
        let authenticationContext = LAContext()
        let reason = NSLocalizedString("FACE_ID_REASON", comment: "Reset password prompt for FaceID")        

        var authenticationError: NSError?
        if authenticationContext.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: &authenticationError) {

            guard authenticationContext.biometryType == .faceID else {
                DispatchQueue.main.async {
                    let result = PrivateDataRequestAccessResult(.unavailable,
                                                                error:nil,
                                                                errorMessageKey: "LOCAL_AUTHENTICATION_REQUIRES_FACE_ID")
                    completionHandler(result)
                }
                return
            }

            authenticationContext.evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, localizedReason: reason) { success, evaluateError in
                if success {
                    DispatchQueue.main.async {
                        let result = PrivateDataRequestAccessResult(.granted)
                        completionHandler(result)
                    }
                } else {
                    DispatchQueue.main.async {
                        let result = PrivateDataRequestAccessResult(.denied,
                                                                    error: evaluateError as NSError?,
                                                                    errorMessageKey: "LOCAL_AUTHENTICATION_ERROR")
                        completionHandler(result)
                    }
                }
            }
        } else {
            DispatchQueue.main.async {
                let result = PrivateDataRequestAccessResult(.undetermined,
                                                            error: authenticationError,
                                                            errorMessageKey: "LOCAL_AUTHENTICATION_ERROR")
                completionHandler(result)
            }
        }
    }
}
```

[Next](PrivacyPrompts-BluetoothAccessProvider.swift.md)[Previous](PrivacyPrompts-User%20Interface-PrivacyActionsViewController.swift.md)

