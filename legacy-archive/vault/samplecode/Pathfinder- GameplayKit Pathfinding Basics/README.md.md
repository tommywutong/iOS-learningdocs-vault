---
title: 'Pathfinder: GameplayKit Pathfinding Basics'
apple_id: TP40016461
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: GameplayKit
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/Pathfinder_GameplayKit/Listings/README_md.html
archived_at: '2026-07-18T03:18:48.335036Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Pathfinder: GameplayKit Pathfinding Basics](Pathfinder-%20GameplayKit%20Pathfinding%20Basics.md)


[Next](Pathfinder%20%28OS%20X%29-GameViewController.swift.md)[Previous](Pathfinder%20%28iOS%29-AppDelegate.swift.md)

# README.md

```
# Pathfinder: Pathfinding Basics

This sample demonstrates how to use GameplayKit’s pathfinding features to map out a game world and find paths through it. 

## Playing the game

Tap anywhere (iOS), press any key (OS X), or click the Siri Remote touch surface (tvOS) to show the solution for the displayed maze. Tap/click again to generate a new maze.

## Structure

The `MazeBuilder` class implements a general algorithm for random maze generation, creating 2D mazes expressed through `GKGridGraph` objects. 

The `Maze` class represents a generated maze, and its `solution` property getter uses `GKGraph.findPathFromNode(_:toNode:)` to obtain a path through the maze.

The `GameScene` class generates a visual representation of each `Maze` object, animates the display of maze solutions, and handles events to display/solve new mazes.

## Requirements

### Build

Xcode 7 with OS X 10.11, iOS 9.0, or tvOS 9.0 SDK

### Runtime

OS X 10.11, iOS 9.0, or tvOS 9.0

Copyright (C) 2016 Apple Inc. All rights reserved.
```

[Next](Pathfinder%20%28OS%20X%29-GameViewController.swift.md)[Previous](Pathfinder%20%28iOS%29-AppDelegate.swift.md)

