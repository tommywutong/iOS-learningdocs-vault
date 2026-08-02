---
title: 'PhotoEditor: Crafting Modern Cocoa Apps'
apple_id: TP40017384
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoEditor/Listings/Photo_Editor_EffectsAccessoryViewController_swift.html
archived_at: '2026-07-18T03:18:49.195052Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoEditor: Crafting Modern Cocoa Apps](PhotoEditor-%20Crafting%20Modern%20Cocoa%20Apps.md)


[Next](Photo%20Editor-PhotoDocumentWindowController.swift.md)[Previous](Photo%20Editor-Defaults.swift.md)

# Photo Editor/EffectsAccessoryViewController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Manages the UI for selecting and previewing effects and creates a new image when the button is clicked.
 */

import Cocoa

class EffectsAccessoryViewController: NSTitlebarAccessoryViewController, PhotoControllerConsumer {

    @IBOutlet weak var effectSelectionPopUp: NSPopUpButton!
    @IBOutlet weak var applyFilterButton: NSButton!

    var photoController: PhotoController?

    override func viewDidLoad() {
        super.viewDidLoad()

        effectSelectionPopUp.removeAllItems()
        Effect.allEffects.enumerated().forEach { index, effect in
            let item = NSMenuItem(title: effect.displayName, action: nil, keyEquivalent: "")
            item.tag = index
            effectSelectionPopUp.menu!.addItem(item)
        }
    }

    private func imageByApplying(_ filter: CIFilter, to image: NSImage) -> NSImage{
        let sourceImage = CIImage(data: image.tiffRepresentation!)
        filter.setValue(sourceImage, forKey: kCIInputImageKey)

        let outputImage = filter.outputImage!
        let result = NSImage(size: image.size)
        let imageRep = NSCIImageRep(ciImage: outputImage)
        result.addRepresentation(imageRep)

        return result
    }

    @IBAction func btnApplyClicked(_ sender: NSButton) {
        if let image = photoController?.photo.image {
            let filter = Effect.allEffects[effectSelectionPopUp.selectedTag()].createFilter()
            let newImage = imageByApplying(filter, to: image)
            photoController?.setPhotoImage(newImage)
        }
    }

}
```

[Next](Photo%20Editor-PhotoDocumentWindowController.swift.md)[Previous](Photo%20Editor-Defaults.swift.md)

