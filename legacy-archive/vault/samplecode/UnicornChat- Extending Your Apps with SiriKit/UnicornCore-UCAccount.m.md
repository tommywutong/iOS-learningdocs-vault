---
title: 'UnicornChat: Extending Your Apps with SiriKit'
apple_id: TP40017332
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/UnicornChat/Listings/UnicornCore_UCAccount_m.html
archived_at: '2026-07-18T03:27:33.303549Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnicornChat: Extending Your Apps with SiriKit](UnicornChat-%20Extending%20Your%20Apps%20with%20SiriKit.md)


[Next](UnicornCore-UCAddressBookManager.h.md)[Previous](UnicornCore-UnicornCore.h.md)

# UnicornCore/UCAccount.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The class that manages the current user account status, and sending/receiving messages.
*/

#import "UCAccount.h"

@implementation UCAccount

+ (instancetype)sharedAccount {
    UCAccount *shared = [[UCAccount alloc] init];
    [shared setHasValidAuthentication:YES];
    return shared;
}

- (BOOL)sendMessage:(NSString *)message toRecipients:(NSArray *)recipients {
    // Sending a message here...

    return YES;
}

@end
```

[Next](UnicornCore-UCAddressBookManager.h.md)[Previous](UnicornCore-UnicornCore.h.md)

