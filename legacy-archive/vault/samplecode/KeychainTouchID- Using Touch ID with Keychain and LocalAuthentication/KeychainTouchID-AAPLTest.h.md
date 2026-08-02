---
title: 'KeychainTouchID: Using Touch ID with Keychain and LocalAuthentication'
apple_id: TP40014530
resource_type: Sample Code
platform: iOS
topic: null
technology: LocalAuthentication
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/samplecode/KeychainTouchID/Listings/KeychainTouchID_AAPLTest_h.html
archived_at: '2026-07-18T03:13:23.187283Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [KeychainTouchID: Using Touch ID with Keychain and LocalAuthentication](KeychainTouchID-%20Using%20Touch%20ID%20with%20Keychain%20and%20LocalAuthentication.md)


[Next](KeychainTouchID-AAPLAppDelegate.h.md)[Previous](KeychainTouchID-AAPLKeychainTestsViewController.h.md)

# KeychainTouchID/AAPLTest.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Test instance which holds the test name details and the selector which should be invoked to perform the test.
*/

@import Foundation;

@interface AAPLTest : NSObject

- (instancetype)initWithName:(NSString *)name details:(NSString *)details selector:(SEL)method;

@property (nonatomic, copy) NSString *name;
@property (nonatomic, copy) NSString *details;
@property (nonatomic) SEL method;

@end
```

[Next](KeychainTouchID-AAPLAppDelegate.h.md)[Previous](KeychainTouchID-AAPLKeychainTestsViewController.h.md)

