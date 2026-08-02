---
title: 'UnicornChat: Extending Your Apps with SiriKit'
apple_id: TP40017332
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/UnicornChat/Listings/UnicornCore_INInteraction_UnicornCore_m.html
archived_at: '2026-07-18T03:27:33.203240Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnicornChat: Extending Your Apps with SiriKit](UnicornChat-%20Extending%20Your%20Apps%20with%20SiriKit.md)


[Next](UnicornCore-UCContact.h.md)[Previous](UnicornCore-UCAccount.h.md)

# UnicornCore/INInteraction+UnicornCore.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Convinience category on INInteraction to get information relevant to UnicornCore.
*/

#import "INInteraction+UnicornCore.h"

@interface INIntent (UnicornCore)

- (BOOL)isSendMessageIntent;
- (INSendMessageIntent *)sendMessageIntent;

@end

@implementation INIntent (UnicornCore)

- (BOOL)isSendMessageIntent {
    return NO;
}

- (INSendMessageIntent *)sendMessageIntent {
    return nil;
}

@end

@implementation INSendMessageIntent (UnicornCore)

- (BOOL)isSendMessageIntent {
    return YES;
}

- (INSendMessageIntent *)sendMessageIntent {
    return self;
}

@end

@implementation INInteraction (UnicornCore)

- (BOOL)representsSendMessageIntent {
    return [[self intent] isSendMessageIntent];
}

- (NSString *)messageContent {
    return [[[self intent] sendMessageIntent] content];
}

- (NSString *)recipientName {
    return [[[[[self intent] sendMessageIntent] recipients] firstObject] displayName];
}

@end
```

[Next](UnicornCore-UCContact.h.md)[Previous](UnicornCore-UCAccount.h.md)

