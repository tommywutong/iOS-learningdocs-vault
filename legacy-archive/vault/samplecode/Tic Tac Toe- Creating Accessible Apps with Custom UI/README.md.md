---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/README_md.html
archived_at: '2026-07-18T03:00:39.271265Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](LICENSE.txt.md)[Previous](TicTacToe-main.m.md)

# README.md

```
# Accessible Tic Tac Toe

This sample contains a game with several custom controls and code to make them accessible, including using the accessibility methods of NSControl subclasses and implementing accessibility protocols for custom elements.

## Requirements

### Build

Xcode 6.0 or later; OS X 10.10 SDK or later

### Runtime

OS X 10.10 or later

Copyright (C) 2014-16 Apple Inc. All rights reserved.

## Major files and folders

### Models

This folder contains all the files that define a game of tic tac toe. There is no accessibility code in these files.

### Views

This folder contains all the files that define the UI for the game. Most of the accessibility code for this application can be found in these files under the section marked `#pragma mark - Accessibility`.

#### AAPLTicTacToeButtonView

An NSView that behaves like a button and implements the NSAccessibilityButton protocol.

#### AAPLTicTacToeCheckboxView

An NSView that behaves like a checkbox and implements the NSAccessibilityCheckbox protocol.

#### AAPLTicTacToeBoardView

An NSView that draws many individual items and implements the NSAccessibilityGroup protocol.

#### AAPLTicTacToeSquareAccessibilityElement

An NSAccessibilityElement subclass that demonstrates how to create an interactive accessibility object for UI with no backing view.

### Controllers

#### AAPLTicTacToeViewController

View controller demonstrating accessibility announcements.

### MainMenu.xib

#### Tic Tac Toe Circle Plus and Minus Button Views

NSButton subclasses that demonstrate adding an accessibility information in Interface Builder by editing the Accessibiliity Identity section of the Indentity Inspector.
```

[Next](LICENSE.txt.md)[Previous](TicTacToe-main.m.md)

