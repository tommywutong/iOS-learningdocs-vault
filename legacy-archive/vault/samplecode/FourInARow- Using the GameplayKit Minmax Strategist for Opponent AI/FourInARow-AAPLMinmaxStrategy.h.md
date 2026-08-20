---
title: 'FourInARow: Using the GameplayKit Minmax Strategist for Opponent AI'
apple_id: TP40016142
resource_type: Sample Code
platform: iOS
topic: General
technology: GameplayKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/FourInARow/Listings/FourInARow_AAPLMinmaxStrategy_h.html
archived_at: '2026-07-18T03:08:51.626363Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [FourInARow: Using the GameplayKit Minmax Strategist for Opponent AI](FourInARow-%20Using%20the%20GameplayKit%20Minmax%20Strategist%20for%20Opponent%20AI.md)


[Next](FourInARow-AAPLPlayer.m.md)[Previous](FourInARow-AAPLBoard.m.md)

# FourInARow/AAPLMinmaxStrategy.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Additions to the game model classes adding GameplayKit protocols for use with the minmax strategist.
 */

@import GameplayKit;

#import "AAPLPlayer.h"
#import "AAPLBoard.h"

@interface AAPLMove : NSObject <GKGameModelUpdate>

// Required by GKGameModelUpdate for storing move ratings during GKMinmaxStrategist move selection.
@property (nonatomic) NSInteger value;

// Identifies the column in which to make a move.
@property (nonatomic) NSInteger column;

+ (AAPLMove *)moveInColumn:(NSInteger)column;

@end

@interface AAPLPlayer (AAPLMinmaxStrategy) <GKGameModelPlayer>
@end

@interface AAPLBoard (AAPLMinmaxStrategy) <GKGameModel>
@end
```

[Next](FourInARow-AAPLPlayer.m.md)[Previous](FourInARow-AAPLBoard.m.md)

