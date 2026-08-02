---
title: 'FourInARow: Using the GameplayKit Minmax Strategist for Opponent AI'
apple_id: TP40016142
resource_type: Sample Code
platform: iOS
topic: General
technology: GameplayKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/FourInARow/Listings/FourInARow_AAPLPlayer_m.html
archived_at: '2026-07-18T03:08:51.783353Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [FourInARow: Using the GameplayKit Minmax Strategist for Opponent AI](FourInARow-%20Using%20the%20GameplayKit%20Minmax%20Strategist%20for%20Opponent%20AI.md)


[Next](FourInARow-AAPLViewController.h.md)[Previous](FourInARow-AAPLMinmaxStrategy.h.md)

# FourInARow/AAPLPlayer.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Basic class representing a player in the Four-In-A-Row game.
 */

#import "AAPLPlayer.h"

@interface AAPLPlayer ()
@property (readwrite) AAPLChip chip;
@property (nonatomic, readwrite, copy) NSString *name;
@end

@implementation AAPLPlayer

- (instancetype)initWithChip:(AAPLChip)chip {
    self = [super init];

    if (self) {
        _chip = chip;
    }

    return self;
}

+ (AAPLPlayer *)redPlayer {
    return [self playerForChip:AAPLChipRed];
}

+ (AAPLPlayer *)blackPlayer {
    return [self playerForChip:AAPLChipBlack];
}

+ (AAPLPlayer *)playerForChip:(AAPLChip)chip {
    if (chip == AAPLChipNone) {
        return nil;
    }

    // Chip enum is 0/1/2, array is 0/1.
    return [self allPlayers][chip - 1];
}

+ (NSArray<AAPLPlayer *> *)allPlayers {
    static NSArray<AAPLPlayer *> *allPlayers = nil;

    if (allPlayers == nil) {
        allPlayers = @[
           [[AAPLPlayer alloc] initWithChip:AAPLChipRed],
           [[AAPLPlayer alloc] initWithChip:AAPLChipBlack],
        ];
    }

    return allPlayers;
}

- (UIColor *)color {
    switch (self.chip) {
        case AAPLChipRed:
            return [UIColor redColor];

        case AAPLChipBlack:
            return [UIColor blackColor];

        default:
            return nil;
    }
}

- (NSString *)name {
    switch (self.chip) {
        case AAPLChipRed:
            return @"Red";

        case AAPLChipBlack:
            return @"Black";

        default:
            return nil;
    }
}

- (NSString *)debugDescription {
    switch (self.chip) {
        case AAPLChipRed:
            return @"X";

        case AAPLChipBlack:
            return @"O";

        default:
            return @" ";
    }
}

- (AAPLPlayer *)opponent {
    switch (self.chip) {
        case AAPLChipRed:
            return [AAPLPlayer blackPlayer];

        case AAPLChipBlack:
            return [AAPLPlayer redPlayer];

        default:
            return nil;
    }
}

@end
```

[Next](FourInARow-AAPLViewController.h.md)[Previous](FourInARow-AAPLMinmaxStrategy.h.md)

