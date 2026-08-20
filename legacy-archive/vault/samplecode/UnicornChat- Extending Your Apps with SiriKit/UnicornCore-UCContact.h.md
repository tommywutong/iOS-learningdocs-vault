---
title: 'UnicornChat: Extending Your Apps with SiriKit'
apple_id: TP40017332
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/UnicornChat/Listings/UnicornCore_UCContact_h.html
archived_at: '2026-07-18T03:27:33.562397Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnicornChat: Extending Your Apps with SiriKit](UnicornChat-%20Extending%20Your%20Apps%20with%20SiriKit.md)


[Next](UnicornCore-UCContact.m.md)[Previous](UnicornCore-INInteraction%2BUnicornCore.m.md)

# UnicornCore/UCContact.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Data model class for contact object in UnicornChat.
*/

#import <Foundation/Foundation.h>

@class INPerson;

NS_ASSUME_NONNULL_BEGIN

@interface UCContact : NSObject

@property (nonatomic, copy, nullable) NSString *name;
@property (nonatomic, copy, nullable) NSString *unicornName;

@property (nonatomic) BOOL favorite;

- (INPerson *)inPerson;

@end

NS_ASSUME_NONNULL_END
```

[Next](UnicornCore-UCContact.m.md)[Previous](UnicornCore-INInteraction%2BUnicornCore.m.md)

