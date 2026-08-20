---
title: 'FourInARow: Using the GameplayKit Minmax Strategist for Opponent AI'
apple_id: TP40016142
resource_type: Sample Code
platform: iOS
topic: General
technology: GameplayKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/FourInARow/Listings/FourInARow_AAPLPlayer_h.html
archived_at: '2026-07-18T03:08:51.745025Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [FourInARow: Using the GameplayKit Minmax Strategist for Opponent AI](FourInARow-%20Using%20the%20GameplayKit%20Minmax%20Strategist%20for%20Opponent%20AI.md)


[Next](FourInARow-AAPLMinmaxStrategy.m.md)[Previous](FourInARow-main.m.md)

# FourInARow/AAPLPlayer.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Basic class representing a player in the Four-In-A-Row game.
 */

@import UIKit;

typedef NS_ENUM(NSInteger, AAPLChip) {
    AAPLChipNone = 0,
    AAPLChipRed,
    AAPLChipBlack
};

@interface AAPLPlayer : NSObject

+ (AAPLPlayer *)redPlayer;
+ (AAPLPlayer *)blackPlayer;
+ (NSArray<AAPLPlayer *> *)allPlayers;
+ (AAPLPlayer *)playerForChip:(AAPLChip)chip;

@property (nonatomic, readonly) AAPLChip chip;
@property (nonatomic, readonly) UIColor *color;
@property (nonatomic, copy, readonly) NSString *name;

@property (nonatomic, readonly) AAPLPlayer *opponent;

@end
```

[Next](FourInARow-AAPLMinmaxStrategy.m.md)[Previous](FourInARow-main.m.md)

