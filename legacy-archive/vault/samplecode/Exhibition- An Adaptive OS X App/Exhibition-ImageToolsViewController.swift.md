---
title: 'Exhibition: An Adaptive OS X App'
apple_id: TP40016178
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/Exhibition/Listings/Exhibition_ImageToolsViewController_swift.html
archived_at: '2026-07-18T03:08:01.348575Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Exhibition: An Adaptive OS X App](Exhibition-%20An%20Adaptive%20OS%20X%20App.md)


[Next](Exhibition-ImageCollectionListController.swift.md)[Previous](Exhibition-ImageCollection.swift.md)

# Exhibition/ImageToolsViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Contains the `ImageToolsViewController` class, which manages the UI of a stack of tools buttons.
*/


import Cocoa

/**
    `ImageToolsViewController` manages a list of tool controls. The controls can be
    detached from the tool stack once their contained view becomes too small and 
    displayed in an overflow menu.
*/
class ImageToolsViewController: NSViewController, NSStackViewDelegate {
    // MARK: Properties

    @IBOutlet var stackView: NSStackView!

    /**
        The button shown when the tool stack is too small to present all of its
        buttons. Clicking on the overflow button shows a menu with representations 
        of the detached buttons.
    */
    lazy var overflowRevealButton: NSButton = {
        let overflowRevealButton = NSButton()

        overflowRevealButton.bezelStyle = .shadowlessSquare

        overflowRevealButton.translatesAutoresizingMaskIntoConstraints = false

        overflowRevealButton.attributedTitle = NSAttributedString(string: "...", attributes: [
            NSFontAttributeName: NSFont.boldSystemFont(ofSize: 13.0)
        ])

        overflowRevealButton.alphaValue = 0.75

        overflowRevealButton.target = self

        overflowRevealButton.action = #selector(ImageToolsViewController.popUpOverflowMenu(_:))

        return overflowRevealButton
    }()

    // MARK: Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()

        stackView.detachesHiddenViews = true
    }


    // MARK: Overflow Menu

    /**
        Creates a menu for the detached views in the stack. The title, target, 
        and action of the menu items match the associated buttons. If there were 
        no detached items, returns nil.
    */
    var overflowMenu: NSMenu? {
        let detachedButtons = stackView.detachedViews.flatMap { $0 as? NSButton }

        if !detachedButtons.isEmpty {
            let menu = NSMenu(title: "Detached Items")

            /*
                Do not use auto-validation, the menu items will have the same 
                enabled state as their represented button.
            */
            menu.autoenablesItems = false

            /* 
                Add a menu item for each detached button, transferring the applicable
                button state to the menu item.
            */
            for button in detachedButtons {
                let menuItem = menu.addItem(withTitle: button.title, action: button.action, keyEquivalent: button.keyEquivalent)
                menuItem.target = button.target
                menuItem.isEnabled = button.isEnabled
                menuItem.representedObject = button
            }

            return menu
        }

        return nil
    }

    @objc fileprivate func popUpOverflowMenu(_ sender: AnyObject?) {
        // Show the overflow menu (if we one exists) underneath the overflow button.
        let popUpMenuLocation = NSPoint(x: overflowRevealButton.bounds.minX, y: overflowRevealButton.bounds.maxY)

        overflowMenu?.popUp(positioning: nil, at: popUpMenuLocation, in: overflowRevealButton)
    }


    // MARK: NSStackView Delegate

    func stackView(_ stackView: NSStackView, willDetach views: [NSView]) {
        /*
            If the stack view did not previously have any detached views, these 
            are the first, so the overflow button needs to be added and constrained.
        */
        if stackView.detachedViews.isEmpty {
            /*
                Add the overflow button (not as an arranged subview), and constraints 
                to position it on the trailing edge of the stack view.
            */
            stackView.addSubview(overflowRevealButton)

            overflowRevealButton.trailingAnchor.constraint(equalTo: stackView.trailingAnchor).isActive = true

            overflowRevealButton.topAnchor.constraint(equalTo: stackView.topAnchor).isActive = true

            overflowRevealButton.bottomAnchor.constraint(equalTo: stackView.bottomAnchor).isActive = true
        }
    }

    func stackView(_ stackView: NSStackView, didReattach views: [NSView]) {
        /*
            If the stack view no longer has any detached views, these were the last, 
            so the overflow button needs to be removed.
        */
        if stackView.detachedViews.isEmpty {
            // Removing the overflow button will also remove constraints associated with it.
            overflowRevealButton.removeFromSuperview()
        }
    }

}
```

[Next](Exhibition-ImageCollectionListController.swift.md)[Previous](Exhibition-ImageCollection.swift.md)

