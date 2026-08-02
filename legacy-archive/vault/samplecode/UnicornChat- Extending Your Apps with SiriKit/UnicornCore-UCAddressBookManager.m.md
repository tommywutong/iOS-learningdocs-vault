---
title: 'UnicornChat: Extending Your Apps with SiriKit'
apple_id: TP40017332
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/UnicornChat/Listings/UnicornCore_UCAddressBookManager_m.html
archived_at: '2026-07-18T03:27:33.372419Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnicornChat: Extending Your Apps with SiriKit](UnicornChat-%20Extending%20Your%20Apps%20with%20SiriKit.md)


[Next](UnicornCore-UCChatViewController.m.md)[Previous](UnicornCore-UCChatView.m.md)

# UnicornCore/UCAddressBookManager.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The class that manages UnicornChat's own address book.
*/

#import "UCAddressBookManager.h"
#import "UCContact.h"

@implementation UCAddressBookManager

- (NSArray<UCContact *> *)contactsMatchingName:(NSString *)name {
    NSMutableArray<UCContact *> *results = [[NSMutableArray alloc] init];
    for (UCContact *contact in [self allContacts]) {
        if ([[[contact name] lowercaseString] containsString:[name lowercaseString]]) {
            [results addObject:contact];
        }
    }
    return results;
}


- (NSArray<UCContact *> *)allContacts {
    UCContact *contact1 = [[UCContact alloc] init];
    [contact1 setName:@"Bill James"];
    [contact1 setUnicornName:@"Sparkle Sparkly"];

    UCContact *contact2 = [[UCContact alloc] init];
    [contact2 setName:@"Tom Clark"];
    [contact2 setUnicornName:@"Celestra"];

    UCContact *contact3 = [[UCContact alloc] init];
    [contact3 setName:@"Juan Chavez"];
    [contact3 setUnicornName:@"Dandelion Prince"];

    UCContact *contact4 = [[UCContact alloc] init];
    [contact4 setName:@"Anne Johnson"];
    [contact4 setUnicornName:@"Pinky Nose"];

    NSArray<UCContact *> *allContacts = @[contact1,
                                          contact2,
                                          contact3,
                                          contact4,
                                          ];
    return allContacts;
}

@end
```

[Next](UnicornCore-UCChatViewController.m.md)[Previous](UnicornCore-UCChatView.m.md)

