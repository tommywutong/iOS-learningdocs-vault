---
title: 'UnicornChat: Extending Your Apps with SiriKit'
apple_id: TP40017332
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/UnicornChat/Listings/UnicornCore_INInteraction_UnicornCore_h.html
archived_at: '2026-07-18T03:27:33.161555Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnicornChat: Extending Your Apps with SiriKit](UnicornChat-%20Extending%20Your%20Apps%20with%20SiriKit.md)


[Next](LICENSE.txt.md)[Previous](UnicornCore-UCAddressBookManager.h.md)

# UnicornCore/INInteraction+UnicornCore.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Convinience category on INInteraction to get information relevant to UnicornCore.
*/

#import <Intents/Intents.h>

@interface INInteraction (UnicornCore)

@property (nonatomic, assign, readonly) BOOL representsSendMessageIntent;
@property (nonatomic, copy, readonly) NSString *recipientName;
@property (nonatomic, copy, readonly) NSString *messageContent;

@end
```

[Next](LICENSE.txt.md)[Previous](UnicornCore-UCAddressBookManager.h.md)

