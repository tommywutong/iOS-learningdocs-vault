---
title: 'Color Gamut Showcase: Using wide color gamut in Cocoa and Cocoa Touch applications
  with SceneKit'
apple_id: TP40017308
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: SceneKit
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/ColorGamutShowcase/Listings/iOS_ViewController_swift.html
archived_at: '2026-07-18T03:03:56.700642Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Color Gamut Showcase: Using wide color gamut in Cocoa and Cocoa Touch applications with SceneKit](Color%20Gamut%20Showcase-%20Using%20wide%20color%20gamut%20in%20Cocoa%20and%20Cocoa%20Touch%20applicatio.md)


[Next](iOS-AppDelegate.swift.md)[Previous](Common-composite.metal.md)

# iOS/ViewController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The app's view controller class.
 */

import SceneKit

class ViewController: UIViewController, UITabBarDelegate {

    @IBOutlet private weak var sceneView: SCNView!
    @IBOutlet private weak var tabBar: UITabBar!
    @IBOutlet private weak var configBarButtonItem: UIBarButtonItem!

    private var controller: Controller!

    override func viewDidLoad() {
        super.viewDidLoad()

        controller = Controller(view: sceneView)
        controller.selectScene(at: 0)
        navigationItem.title = controller.sceneTitles[0]

        configureTabBar()
    }

    // MARK: UI for Visualization Type

    @IBAction func pickVisualization(_ sender: AnyObject?) {
        let alert = UIAlertController(title: "Left Side Visualization", message: nil, preferredStyle: .actionSheet)
        let clampAction = UIAlertAction(title: "Clamp to sRGB", style: .default) { [weak self] action in
            self?.controller.visualizationType = .gamutClamp
        }
        if controller.visualizationType == .gamutClamp {
            clampAction.isEnabled = false
        }
        alert.addAction(clampAction)
        let wideGamutHighlightAction = UIAlertAction(title: "Highlight Wide Gamut", style: .default) { [weak self] action in
            self?.controller.visualizationType = .wideGamutHighlight
        }
        if controller.visualizationType == .wideGamutHighlight {
            wideGamutHighlightAction.isEnabled = false
        }
        alert.addAction(wideGamutHighlightAction)
        alert.popoverPresentationController?.barButtonItem = configBarButtonItem

        self.present(alert, animated: true, completion: nil)
    }

    // MARK: UI for Image Selection

    private func configureTabBar() {
        var items = [UITabBarItem]()

        for i in 0 ..< controller.sceneTitles.count {
            let item = UITabBarItem(title: controller.sceneTitles[i], image: nil, tag: i)
            items.append(item)
        }

        tabBar.items = items
        tabBar.delegate = self
    }

    // MARK: UITabBarDelegate Conformance

    func tabBar(_ tabBar: UITabBar, didSelect item: UITabBarItem) {
        controller.selectScene(at: item.tag)
        navigationItem.title = controller.sceneTitles[item.tag]
    }

    // MARK: Split View Handle and Touch Events

    private func updateHandlePosition(_ touch: UITouch) {
        let location = touch.location(in: view)
        let splitFraction = Float(location.x / view.bounds.size.width)
        controller.splitFraction = splitFraction
    }

    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        super.touchesBegan(touches, with: event)
        updateHandlePosition(touches.first!)
    }

    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        super.touchesMoved(touches, with: event)
        updateHandlePosition(touches.first!)
    }

    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        super.touchesEnded(touches, with: event)
        updateHandlePosition(touches.first!)
    }

}
```

[Next](iOS-AppDelegate.swift.md)[Previous](Common-composite.metal.md)

