---
title: 'ForceTouchCatalog: Using the Force Touch Trackpad API'
apple_id: TP40016148
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/ForceTouchCatalog/Listings/ForceTouchCatalog_SquireViewController_swift.html
archived_at: '2026-07-18T03:08:48.927999Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ForceTouchCatalog: Using the Force Touch Trackpad API](ForceTouchCatalog-%20Using%20the%20Force%20Touch%20Trackpad%20API.md)


[Next](ForceTouchCatalog-KnightViewController.swift.md)[Previous](ForceTouchCatalog-ForceTouchCatalog-MasterViewController.swift.md)

# ForceTouchCatalog/SquireViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    View controller for the Squire tab. Examples of high-level Force Touch API. Uses Force Touch and spring loaded buttons.
*/

import Cocoa

class SquireViewController: NSViewController {
    // MARK: Properties

    @IBOutlet weak var nextPhotoButton: NSButton!
    @IBOutlet weak var imageView: NSImageView!
    @IBOutlet weak var pressureIndicator: NSLevelIndicator!
    @IBOutlet weak var levelIndicator: NSLevelIndicator!

    static let imageBaseName = "Lola"
    static let maxPhotoIndex = 4

    var photoIndex = 1

    // MARK: View Controller

    override func viewDidLoad() {
        super.viewDidLoad()

        /*
            This is how you manually set a continuous accelerator button.
            The other buttons are set in the IB Attributes Inspector for that button.
        */
        nextPhotoButton.setButtonType(.accelerator)
        nextPhotoButton.isContinuous = true
    }

    func nextPhotoName() -> String {
        photoIndex += 1

        if photoIndex > SquireViewController.maxPhotoIndex {
            photoIndex = 1
        }

        return "\(SquireViewController.imageBaseName)\(photoIndex)"
    }

    // MARK: IBActions

    @IBAction func nextPhotoAction(_ sender: NSButton) {
        var startFrame = imageView.frame
        let nextPhoto = NSImage(named: nextPhotoName())
        startFrame.origin.x = -startFrame.size.width

        let newImageView = NSImageView(frame: startFrame)
        newImageView.image = nextPhoto

        view.addSubview(newImageView)

        NSAnimationContext.runAnimationGroup({ context in
            context.duration = 0.1
            newImageView.animator().frame = self.imageView.frame
        }, completionHandler: {
            self.imageView.image = nextPhoto
            newImageView.removeFromSuperviewWithoutNeedingDisplay()
        })
    }

    @IBAction func acceleratorChanged(_ sender: NSButton) {
        if sender.doubleValue >= 1 {
            pressureIndicator.integerValue = Int((sender.doubleValue - 1.0) * 1000.0)
        }
        else {
            pressureIndicator.integerValue = 0
        }
    }

    @IBAction func multiLevelAcceleratorChanged(_ sender: NSButton) {
        levelIndicator.integerValue = sender.integerValue
    }

    @IBAction func beepAction(_ sender: NSButton) {
        NSBeep()
    }
}
```

[Next](ForceTouchCatalog-KnightViewController.swift.md)[Previous](ForceTouchCatalog-ForceTouchCatalog-MasterViewController.swift.md)

