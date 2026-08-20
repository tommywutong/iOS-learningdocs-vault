---
title: 'UnicornChat: Extending Your Apps with SiriKit'
apple_id: TP40017332
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/UnicornChat/Listings/UnicornCore_UCChatView_h.html
archived_at: '2026-07-18T03:27:33.487440Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnicornChat: Extending Your Apps with SiriKit](UnicornChat-%20Extending%20Your%20Apps%20with%20SiriKit.md)


[Next](UnicornCore-UCChatViewController.h.md)[Previous](UnicornCore-UCChatViewController.m.md)

# UnicornCore/UCChatView.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The view that displays messages in UnicornChat.
*/

#import <UIKit/UIKit.h>

@interface UCChatView : UIView

@property (nonatomic, copy) NSString *recipientName;
@property (nonatomic, copy) NSString *content;
@property (nonatomic, assign, getter=isSent) BOOL sent;

@end
```

[Next](UnicornCore-UCChatViewController.h.md)[Previous](UnicornCore-UCChatViewController.m.md)

