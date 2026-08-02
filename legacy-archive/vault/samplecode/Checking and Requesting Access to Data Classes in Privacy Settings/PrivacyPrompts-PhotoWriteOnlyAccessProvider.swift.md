---
title: Checking and Requesting Access to Data Classes in Privacy Settings
apple_id: DTS40013410
resource_type: Sample Code
platform: iOS
topic: Security
technology: null
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/samplecode/PrivacyPrompts/Listings/PrivacyPrompts_PhotoWriteOnlyAccessProvider_swift.html
archived_at: '2026-07-18T03:19:34.630948Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Checking and Requesting Access to Data Classes in Privacy Settings](Checking%20and%20Requesting%20Access%20to%20Data%20Classes%20in%20Privacy%20Settings.md)


[Next](PrivacyPrompts-EventKitAccessProvider.swift.md)[Previous](PrivacyPrompts-BluetoothAccessProvider.swift.md)

# PrivacyPrompts/PhotoWriteOnlyAccessProvider.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Demonstrates the API to request write only access to photos.
 */

import Foundation
import UIKit

class PhotoWriteOnlyAccessProvider: NSObject, PrivateDataAccessRequestProvider {

    var requestAccessCompletionHandler: PrivacyActionRequestAccessHandler?

    func requestAccess(completionHandler: @escaping (PrivateDataRequestAccessResult) -> Void) {
        requestAccessCompletionHandler = completionHandler
        let food = #imageLiteral(resourceName: "Food.jpg")
        UIImageWriteToSavedPhotosAlbum(food, self, #selector(image(_:didFinishSaving:contextInfo:)), nil)
    }

    @objc
    private func image(_ image: UIImage, didFinishSaving error: NSError?, contextInfo: Any?) {
        if let completionHandler = requestAccessCompletionHandler {
            let result = PrivateDataRequestAccessResult(error == nil ? .granted : .denied)
            completionHandler(result)
        }

        // Breaks reference cycle so this object can deinit.
        requestAccessCompletionHandler = nil
    }
}
```

[Next](PrivacyPrompts-EventKitAccessProvider.swift.md)[Previous](PrivacyPrompts-BluetoothAccessProvider.swift.md)

