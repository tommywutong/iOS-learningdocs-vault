---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_BaseScene_Focus_swift.html
archived_at: '2026-07-18T03:06:15.511273Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](LICENSE.txt.md)[Previous](DemoBots-SceneOperation.swift.md)

# DemoBots/BaseScene+Focus.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An extension of `BaseScene` to allow focus based navigation of buttons
                with game controllers and the keyboard on OS X.
*/

extension BaseScene {
    // MARK: Properties

    /// The currently focused button, if any.
    var focusedButton: ButtonNode? {
        get {
            for button in currentlyFocusableButtons where button.isFocused {
                return button
            }
            return nil
        }

        set {
            focusedButton?.isFocused = false
            newValue?.isFocused = true
        }
    }

    /// A computed property to determine which buttons are focusable.
    var currentlyFocusableButtons: [ButtonNode] {
        return buttons.filter { !$0.isHidden && $0.isUserInteractionEnabled }
    }

    /**
        A private property used to determine the priority for initially focusing 
        on each button.

        i.e. when a `BaseScene` is initially presented there may be a number of
        different buttons in the scene, this array determines which button should
        be focused on first.
    */
    private var buttonIdentifiersOrderedByInitialFocusPriority: [ButtonIdentifier] {
        return [
            .resume,
            .proceedToNextScene,
            .replay,
            .retry,
            .home,
            .cancel,
            .viewRecordedContent,
            .screenRecorderToggle
        ]
    }

    // MARK: Focus Based Navigation

    /**
        Establishes vertical bidirectional connections for all `currentlyFocusableButtons`.

        Note: This only establishes the vertical relationship between buttons, but 
        could be expanded to include horizontal navigation if necessary.
    */
    func createButtonFocusGraph() {
        let sortedFocusableButtons = currentlyFocusableButtons.sorted { $0.position.y > $1.position.y }

        // Clear any existing connections.
        sortedFocusableButtons.forEach { $0.focusableNeighbors.removeAll() }

        // Connect the adjacent button nodes.
        for i in 0..<sortedFocusableButtons.count - 1 {
            let node = sortedFocusableButtons[i]
            let nextNode = sortedFocusableButtons[i + 1]

            // Create a bidirectional connection between the nodes.
            node.focusableNeighbors[.down] = nextNode
            nextNode.focusableNeighbors[.up] = node
        }
    }

    /**
        Reset focus to the `ButtonNode` with the highest priority specified by 
        `buttonIdentifiersOrderedByInitialFocusPriority`.

        If playing on iOS, focus is only used when a game controller is connected.
    */
    func resetFocus() {
        #if os(iOS)
        // On iOS, ensure a game controller is connected otherwise return without providing focus.
        guard sceneManager.gameInput.isGameControllerConnected else { return }
        #endif

        // Reset focus to the `buttonNode` with the maximum initial focus priority.
        focusedButton = currentlyFocusableButtons.max { lhsButton, rhsButton in
            // The initial focus priority is the index within the `buttonIdentifiersOrderedByInitialFocusPriority` array.
            let lhsPriority = buttonIdentifiersOrderedByInitialFocusPriority.index(of: lhsButton.buttonIdentifier)!
            let rhsPriority = buttonIdentifiersOrderedByInitialFocusPriority.index(of: rhsButton.buttonIdentifier)!

            return lhsPriority > rhsPriority
        }
    }
}
```

[Next](LICENSE.txt.md)[Previous](DemoBots-SceneOperation.swift.md)

