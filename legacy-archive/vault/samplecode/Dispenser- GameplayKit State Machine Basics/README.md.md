---
title: 'Dispenser: GameplayKit State Machine Basics'
apple_id: TP40016460
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: GameplayKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Dispenser_GameplayKit/Listings/README_md.html
archived_at: '2026-07-18T03:07:04.347970Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Dispenser: GameplayKit State Machine Basics](Dispenser-%20GameplayKit%20State%20Machine%20Basics.md)


[Next](LICENSE.txt.md)[Previous](Dispenser%20%28iOS%29-AppDelegate.swift.md)

# README.md

```objc
# Dispenser: GameplayKit State Machine Basics

This sample demonstrates how to use GameplayKit’s state machines to achieve fine control over your game. 

## Playing the game

This game simulates a water dispenser. To serve water:
- (OS X) click anywhere or press any key
- (iOS) tap anywhere
- (tvOS) swipe the Siri Remote touch surface

To refill the dispenser:
- (OS X) click the Refill button in the scene
- (iOS) tap the Refill button in the scene
- (tvOS) click the Siri Remote touch surface

## Structure

Most of this game's behavior is driven by a state machine: the state machine tracks whether the dispenser is serving water or being refilled, and whether the dispenser is full, partially full, or empty. 

The GameScene class sets up the state machine and translates user input into actions that drive the state machine. Then, each state class manages the game's behavior during each state:

- FullState: Ensures the indicator light on the dispenser is green.
- ServeState: Runs an animation for serving water, then automatically transitions to the PartiallyFull or Empty state.
- PartiallyFullState: No effects -- this state exists only to validate state transitions.
- EmptyState: Flashes the light on the dispenser to indicate that it needs a refill.
- RefillingState: Animates refilling the dispenser tank with water, then automatically transitions to the Full state.

## Requirements

### Build

Xcode 8.0 with OS X 10.11, iOS 9.0, or tvOS 9.0 SDK

### Runtime

OS X 10.11, iOS 9.0, or tvOS 9.0

Copyright (C) 2015-16 Apple Inc. All rights reserved.
```

[Next](LICENSE.txt.md)[Previous](Dispenser%20%28iOS%29-AppDelegate.swift.md)

