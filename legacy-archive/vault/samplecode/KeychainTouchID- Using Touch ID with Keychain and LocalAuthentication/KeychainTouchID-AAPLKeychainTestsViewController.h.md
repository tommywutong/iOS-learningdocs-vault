---
title: 'KeychainTouchID: Using Touch ID with Keychain and LocalAuthentication'
apple_id: TP40014530
resource_type: Sample Code
platform: iOS
topic: null
technology: LocalAuthentication
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/samplecode/KeychainTouchID/Listings/KeychainTouchID_AAPLKeychainTestsViewController_h.html
archived_at: '2026-07-18T03:13:22.927560Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [KeychainTouchID: Using Touch ID with Keychain and LocalAuthentication](KeychainTouchID-%20Using%20Touch%20ID%20with%20Keychain%20and%20LocalAuthentication.md)


[Next](KeychainTouchID-AAPLTest.h.md)[Previous](KeychainTouchID-AAPLLocalAuthenticationTestsViewController.m.md)

# KeychainTouchID/AAPLKeychainTestsViewController.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Keychain with Touch ID demo implementation.
*/

@import UIKit;

#import "AAPLBasicTestViewController.h"

@interface AAPLKeychainTestsViewController : AAPLBasicTestViewController

@property (nonatomic, weak) IBOutlet UITextView *textView;
@property (nonatomic, strong) IBOutlet NSLayoutConstraint *dynamicViewHeight;
@property (nonatomic, weak) IBOutlet UITableView *tableView;

@end
```

[Next](KeychainTouchID-AAPLTest.h.md)[Previous](KeychainTouchID-AAPLLocalAuthenticationTestsViewController.m.md)

