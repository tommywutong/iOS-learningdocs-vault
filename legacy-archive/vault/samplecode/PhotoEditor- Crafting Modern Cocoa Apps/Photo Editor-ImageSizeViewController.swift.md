---
title: 'PhotoEditor: Crafting Modern Cocoa Apps'
apple_id: TP40017384
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoEditor/Listings/Photo_Editor_ImageSizeViewController_swift.html
archived_at: '2026-07-18T03:18:49.277443Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoEditor: Crafting Modern Cocoa Apps](PhotoEditor-%20Crafting%20Modern%20Cocoa%20Apps.md)


[Next](Photo%20Editor-AppDelegate.swift.md)[Previous](Photo%20Editor-Effects.swift.md)

# Photo Editor/ImageSizeViewController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The ImageSizeViewController has two text fields to set the image width and height. The text fields are bound in IB to the dynamic properties of the same name.
 */

import Cocoa

class ImageSizeViewController: NSViewController {

    @IBOutlet weak var widthField: NSTextField!
    @IBOutlet weak var heightField: NSTextField!
    @IBOutlet weak var constrainCheckbox: NSButton!

    dynamic var width: CGFloat = 0 // for bindings
    dynamic var height: CGFloat = 0  // for bindings

    var completionHandler: ((NSSize, NSModalResponse) -> Void)?

    private var ratio: CGFloat = 1

    var imageSize: NSSize {
        get {
            return NSSize(width: width, height: height)
        }
        set {
            (width, height) = (newValue.width, newValue.height)
            ratio = (height > 0) ? width / height : 1.0
        }
    }

    override func viewDidLoad() {
        super.viewDidLoad()
    }

    @IBAction func didEditField(_ sender: NSTextField!) {
        guard constrainCheckbox.state == NSOnState else { return }

        switch sender {
            case widthField:
                height = width / ratio

            case heightField:
                width = height * ratio

            default:
                break
        }
    }

    @IBAction func cancel(_ sender: AnyObject!) {
        dismiss(sender)
        completionHandler?(NSZeroSize, NSModalResponseCancel)
    }

    @IBAction func ok(_ sender: AnyObject!) {
        dismiss(sender)
        completionHandler?(imageSize, NSModalResponseOK)
    }

}
```

[Next](Photo%20Editor-AppDelegate.swift.md)[Previous](Photo%20Editor-Effects.swift.md)

