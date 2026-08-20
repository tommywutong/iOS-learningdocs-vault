---
title: 'Boxes: GameplayKit Entity-Component Basics'
apple_id: TP40016459
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: GameplayKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Boxes_GamePlayKit/Listings/README_md.html
archived_at: '2026-07-18T03:02:16.595721Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Boxes: GameplayKit Entity-Component Basics](Boxes-%20GameplayKit%20Entity-Component%20Basics.md)


[Next](LICENSE.txt.md)[Previous](Boxes%20%28iOS%29-AppDelegate.swift.md)

# README.md

```
# Boxes: GameplayKit Entity-Component Basics

This sample demonstrates how to use GameplayKit’s entity-component feature to create modular, scalable game architecture. It covers the classes `GKEntity`, `GKComponent`, and `GKComponentSystem`. 

## Structure

The Game object sets up the entities and their components. Each box is represented by an instance of the `GKEntity` class -- an abstract container for the `GKComponent` objects that together provide each entity's functionality.

Each box shows the effect of a different combination of the following components:
- All boxes have a `GeometryComponent` that manage their SceneKit representation for display and physics simulator.
- Boxes with a `ParticleComponent` also display a fiery or sparkly particle effect.
- Boxes with a `PlayerControlComponent` jump up into the air when you interact with the scene.

In the `Game` object's `setUpEntities` method, try adding a particle or player-control component to the purple box. 

## Playing the game

Tap anywhere (iOS), press any key (OS X), or click the Siri Remote touch surface (tvOS) to interact with the scene, causing boxes with a `PlayerControlComponent` to jump.

## Requirements

### Build

Xcode 7.1, OS X 10.11 SDK, iOS 9.0 SDK, tvOS 9.0 SDK

### Runtime

OS X 10.11, iOS 9.0, tvOS 9.0

Copyright (C) 2015-16 Apple Inc. All rights reserved.
```

[Next](LICENSE.txt.md)[Previous](Boxes%20%28iOS%29-AppDelegate.swift.md)

