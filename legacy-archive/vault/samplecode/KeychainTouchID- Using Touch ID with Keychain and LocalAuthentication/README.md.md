---
title: 'KeychainTouchID: Using Touch ID with Keychain and LocalAuthentication'
apple_id: TP40014530
resource_type: Sample Code
platform: iOS
topic: null
technology: LocalAuthentication
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/samplecode/KeychainTouchID/Listings/README_md.html
archived_at: '2026-07-18T03:13:23.352665Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [KeychainTouchID: Using Touch ID with Keychain and LocalAuthentication](KeychainTouchID-%20Using%20Touch%20ID%20with%20Keychain%20and%20LocalAuthentication.md)


[Next](LICENSE.txt.md)[Previous](KeychainTouchID-AAPLAppDelegate.h.md)

# README.md

```
# KeychainTouchID: Using Touch ID with Keychain and LocalAuthentication

The KeychainTouchID sample shows how to store Touch ID protected items to the keychain and how to query for those items with custom message prompts. You’ll see how to use the keychain item accessibility class, which invalidates items when the passcode is removed. You’ll also find out how to use the LocalAuthentication class to invoke Touch ID verification without involving the keychain.

The LocalAuthentication sample is implemented in AAPLLocalAuthenticationTestsViewController while the keychain sample is implemented in AAPLKeychainTestsViewController. Both classes are inherited from AAPLBasicTestViewController which just implements the shared table view handling and launching of the tests defined in AAPLLocalAuthenticationTestsViewController and AAPLKeychainTestsViewController.

Note that the LocalAuthentication framework requires Touch ID. You can implement your own authentication to support devices without Touch ID.

## Requirements

This sample requires a device with Touch ID and passcode enabled. The keychain test will work on devices without Touch ID; iOS will fall back to the passcode prompt in that case. The LocalAuthentication test on the other hand requires Touch ID.

This sample does not support the simulator.

### Build

Xcode 8.0, iOS 10 SDK

### Runtime

iOS 10

Copyright (C) 2016 Apple Inc. All rights reserved.
```

[Next](LICENSE.txt.md)[Previous](KeychainTouchID-AAPLAppDelegate.h.md)

