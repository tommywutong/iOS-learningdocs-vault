---
title: 'FourInARow: Using the GameplayKit Minmax Strategist for Opponent AI'
apple_id: TP40016142
resource_type: Sample Code
platform: iOS
topic: General
technology: GameplayKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/FourInARow/Listings/README_md.html
archived_at: '2026-07-18T03:08:52.144591Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [FourInARow: Using the GameplayKit Minmax Strategist for Opponent AI](FourInARow-%20Using%20the%20GameplayKit%20Minmax%20Strategist%20for%20Opponent%20AI.md)


[Next](LICENSE.txt.md)[Previous](FourInARowTests-FourInARowTests.m.md)

# README.md

```
# FourInARow: Using the GameplayKit Minmax Strategist for Opponent AI

This sample demonstrates how to use the GKMinmaxStrategist class to implement a computer-controlled opponent for turn-based, adversarial games. As part of this demonstration, the sample shows how to structure gameplay model code for use with the minmax strategist using the GKGameModel protocol and related APIs.

## Playing the Game

Tap in a column to drop a chip of your color there. (Red moves first, Black moves second.) Get four chips in a row -- horizontally, vertically, or diagonally -- to win.

## Building a Game Model

This project builds a game in stages:
1. The `AAPLBoard` and `AAPLPlayer` classes implement a generic model for a Four-In-A-Row game. Use the `FourInARowTests` unit test case to exercise the generic game model.
2. The `AAPLViewController` class adds a UI for playing the game on an iOS device. With the `USE_AI_PLAYER` macro left undefined, the game is for two human players.
3. The classes and categories in `AAPLMinmaxStrategy.h` and `AAPLMinmaxStrategy.m` extend the generic game model to support using GameplayKit for opponent AI. 
4. With the `USE_AI_PLAYER` macro defined, the `AAPLViewController` class replaces user control for the second player (black chips) with an AI opponent using the `GKMinmaxStrategist` class.

For a more thorough discussion of this project, see the chapter "The Minmax Strategist" in [GameplayKit Programming Guide][1].

[1]: https://developer.apple.com/library/prerelease/ios/documentation/General/Conceptual/GameplayKit_Guide/index.html

## Requirements

### Build

Xcode 7.0, iOS 9.0

### Runtime

iOS 9.0

Copyright (C) 2015 Apple Inc. All rights reserved.
```

[Next](LICENSE.txt.md)[Previous](FourInARowTests-FourInARowTests.m.md)

