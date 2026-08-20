---
title: 'HelloGameKit: A skeleton app for turn based games on watchOS'
apple_id: TP40017337
resource_type: Sample Code
platform: watchOS
topic: null
technology: GameCenter
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/HelloGameKit/Listings/README_md.html
archived_at: '2026-07-18T03:11:49.301181Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HelloGameKit: A skeleton app for turn based games on watchOS](HelloGameKit-%20A%20skeleton%20app%20for%20turn%20based%20games%20on%20watchOS.md)


[Next](LICENSE.txt.md)[Previous](HelloGameKit-AppDelegate.swift.md)

# README.md

```
# HelloGameKit: A skeleton app for turn based games on watchOS

This sample is an implementation of a simple turn based game for watchOS. It demonstrates the following technologies:

  * Game Center turn based multiplayer
  * SpriteKit Scenes/Nodes/Actions
  * Haptic Feedback
  * WatchKit gestures


## Description

This is a simple turn based game that lets the user record tap and pan gestures.  A turn consists of recording any number of gestures followed by a long press gesture to indicate the end of a turn.

A turn consists of recording a series of taps and pan gestures and ending with a long tap.  

If you tap on Pick Opponent it will bring up an interface that lets you choose to Auto-Match (let Game Center pick a player) or choose from a list of players that you recently played.  When you pick a player they get assigned to the opponent field.  However the turn based game does not actually start until you create a match

Swiping left accesses the match list giving you the option to create a new match or choose an opponent.  If you choose create a new match it will a player that you have chosen as an opponent or Auto-Match if you have not.   


## App Structure

The app is structured using the Model/View/Controller design pattern

### InterfaceController
The top level controller that presents the main game scene it responds to various gestures

### GameModel
This contains a list of moves which are a collection of points recorded as part of a single gesture.  It implements logic for making a move and ending a turn.  It also provides means for loading and saving data to a GKTurnBasedMatch.

### GameScene
This provides the main user interface.  It has label nodes indicating you and your opponent on the top and bottom.  It has a green counter that indicates the total number of gestures recorded.

### ListWithButtonInterfaceController
This is a base class that provides a simple tableview that provides a single action button row plus displays a lists of items with title/detail information.  You adopt ListDataSource for loading data and to provide text for the button table.  You adopt the ListItem protocol for your items

### PlayersInterfaceController

Specializes ListWithButtonInterfaceController to load a list of recent players

### MatchesInterfaceController

Specializes ListWithButtonInterfaceController to load a list of turn based matches


## Requirements 

iOS/watchOS device only.  Simulator is not supported at this time.

### Build

Xcode 8.0 or later; iOS 10.0 SDK or later; watchOS 3.0 SDK or later

### Runtime

iOS 10.0 or later; watchOS 3.0 or later

Copyright (C) 2016 Apple Inc. All rights reserved.
```

[Next](LICENSE.txt.md)[Previous](HelloGameKit-AppDelegate.swift.md)

