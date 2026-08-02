---
title: Checking and Requesting Access to Data Classes in Privacy Settings
apple_id: DTS40013410
resource_type: Sample Code
platform: iOS
topic: Security
technology: null
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/samplecode/PrivacyPrompts/Listings/PrivacyPrompts_AdvertisingAccessProvider_swift.html
archived_at: '2026-07-18T03:19:33.659161Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Checking and Requesting Access to Data Classes in Privacy Settings](Checking%20and%20Requesting%20Access%20to%20Data%20Classes%20in%20Privacy%20Settings.md)


[Next](PrivacyPrompts-MusicAccessProvider.swift.md)[Previous](PrivacyPrompts-LocationAccessProvider.swift.md)

# PrivacyPrompts/AdvertisingAccessProvider.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Demonstrates API to check access to advertising information.
 */

import Foundation
import AdSupport

class AdvertisingAccessProvider: PrivateDataAccessStatusProvider {
    var accessLevel: PrivateDataAccessLevel {
        /*
         It is required to check the value of the property isAdvertisingTrackingEnabled before using the advertising identifier.
         If the value is NO, then identifier can only be used for the purposes enumerated in the program license agreement note
         that the advertising ID can be controlled by restrictions just like the rest of the privacy data classes.
         Applications should not cache the advertising ID as it can be changed via the reset button in Settings.
         */
        return ASIdentifierManager.shared().isAdvertisingTrackingEnabled ? .granted : .denied
    }
}
```

[Next](PrivacyPrompts-MusicAccessProvider.swift.md)[Previous](PrivacyPrompts-LocationAccessProvider.swift.md)

