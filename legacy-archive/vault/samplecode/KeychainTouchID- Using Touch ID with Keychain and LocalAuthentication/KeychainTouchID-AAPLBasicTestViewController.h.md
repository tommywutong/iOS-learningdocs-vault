---
title: 'KeychainTouchID: Using Touch ID with Keychain and LocalAuthentication'
apple_id: TP40014530
resource_type: Sample Code
platform: iOS
topic: null
technology: LocalAuthentication
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/samplecode/KeychainTouchID/Listings/KeychainTouchID_AAPLBasicTestViewController_h.html
archived_at: '2026-07-18T03:13:22.845046Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [KeychainTouchID: Using Touch ID with Keychain and LocalAuthentication](KeychainTouchID-%20Using%20Touch%20ID%20with%20Keychain%20and%20LocalAuthentication.md)


[Next](KeychainTouchID-AAPLBasicTestViewController.m.md)[Previous](KeychainTouchID-AAPLAppDelegate.m.md)

# KeychainTouchID/AAPLBasicTestViewController.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Test view controller parent for implementing test pages in the test application.
*/

@import UIKit;
#import "AAPLTest.h"


@interface AAPLBasicTestViewController : UIViewController <UITableViewDataSource, UITableViewDelegate>

@property (nonatomic, copy) NSArray<AAPLTest *> *tests;

- (void)printMessage:(NSString *)message inTextView:(UITextView *)textView;

@end
```

[Next](KeychainTouchID-AAPLBasicTestViewController.m.md)[Previous](KeychainTouchID-AAPLAppDelegate.m.md)

