---
title: 'Color Gamut Showcase: Using wide color gamut in Cocoa and Cocoa Touch applications
  with SceneKit'
apple_id: TP40017308
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: SceneKit
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/ColorGamutShowcase/Listings/OS_X_ViewController_swift.html
archived_at: '2026-07-18T03:03:56.506616Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Color Gamut Showcase: Using wide color gamut in Cocoa and Cocoa Touch applications with SceneKit](Color%20Gamut%20Showcase-%20Using%20wide%20color%20gamut%20in%20Cocoa%20and%20Cocoa%20Touch%20applicatio.md)


[Next](OS%20X-AppDelegate.swift.md)[Previous](README.md.md)

# OS X/ViewController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The app's view controller class.
 */

import SceneKit

class ViewController: NSViewController {

    @IBOutlet private weak var sceneView: SCNView!
    @IBOutlet private weak var popupButton: NSPopUpButton!
    @IBOutlet private var configButton: NSButton!

    private var controller: Controller!

    override func viewDidLoad() {
        super.viewDidLoad()

        controller = Controller(view: sceneView)
        controller.selectScene(at: 0)

        configurePopupButton()
    }

    override func viewWillAppear() {
        guard let window = view.window else { return }

        window.appearance = NSAppearance(named: NSAppearanceNameVibrantDark)

        let accessoryViewController = NSTitlebarAccessoryViewController()
        accessoryViewController.view = configButton
        accessoryViewController.layoutAttribute = .trailing
        window.addTitlebarAccessoryViewController(accessoryViewController)
    }

    // MARK: UI for Image Selection

    private func configurePopupButton() {
        for i in 0 ..< controller.sceneTitles.count {
            let item = NSMenuItem(title: controller.sceneTitles[i], action: #selector(sceneDidChange), keyEquivalent: "")
            item.tag = i
            popupButton.menu?.addItem(item)
        }
    }

    private dynamic func sceneDidChange(_ sender: AnyObject?) {
        let menuItem = sender as! NSMenuItem
        controller.selectScene(at: menuItem.tag)
    }

    // MARK: Split View Handle and Mouse Events

    private func updateHandlePosition(with event: NSEvent) {
        let location = sceneView.convert(event.locationInWindow, from: nil)
        let splitFraction = Float(location.x / view.bounds.size.width)
        controller.splitFraction = splitFraction
    }

    override func mouseDragged(with event: NSEvent) {
        updateHandlePosition(with: event)
    }

    override func mouseUp(with event: NSEvent) {
        updateHandlePosition(with: event)
    }

    override func prepare(for segue: NSStoryboardSegue, sender: Any?) {
        if let destination = segue.destinationController as? ConfigViewController, segue.identifier == "ConfigPopover" {
            destination.visualizationType = controller.visualizationType
            destination.didChangeVisualizationTypeHandler = { [weak self] type in
                self?.controller.visualizationType = type
            }
        }
    }
}

class ConfigViewController : NSViewController {
    @IBOutlet private weak var gamutClampButton: NSButton!
    @IBOutlet private weak var wideGamutHighlightButton: NSButton!

    var didChangeVisualizationTypeHandler: (Controller.VisualizationType) -> (Void) = { _ in }
    var visualizationType: Controller.VisualizationType = .gamutClamp {
        didSet {
            updateSelectedRadioButton()
        }
    }
    override func viewDidLoad() {
        updateSelectedRadioButton()
    }

    private func updateSelectedRadioButton() {
        if isViewLoaded {
            gamutClampButton.state = visualizationType == .gamutClamp ? NSOnState : NSOffState
            wideGamutHighlightButton.state = visualizationType == .wideGamutHighlight ? NSOnState : NSOffState
        }
    }

    @IBAction private func pickVisualizationMode(_ sender: NSButton) {
        let visualizationType = Controller.VisualizationType(rawValue: sender.tag)!
        didChangeVisualizationTypeHandler(visualizationType)
    }
}
```

[Next](OS%20X-AppDelegate.swift.md)[Previous](README.md.md)

