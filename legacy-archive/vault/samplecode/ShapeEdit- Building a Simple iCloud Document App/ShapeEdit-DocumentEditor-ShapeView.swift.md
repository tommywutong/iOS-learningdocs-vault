---
title: 'ShapeEdit: Building a Simple iCloud Document App'
apple_id: TP40016100
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/ShapeEdit/Listings/ShapeEdit_DocumentEditor_ShapeView_swift.html
archived_at: '2026-07-18T03:23:43.988667Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ShapeEdit: Building a Simple iCloud Document App](ShapeEdit-%20Building%20a%20Simple%20iCloud%20Document%20App.md)


[Next](ShapeEdit-AppDelegate.swift.md)[Previous](ShapeEdit-DocumentEditor-ShapeDocument.swift.md)

# ShapeEdit/DocumentEditor/ShapeView.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the Shape View which handles displaying / user interaction when editing an individual shape document.
*/

import UIKit
import SceneKit

/**
    The `ShapeView` class interceps touch events so we know when the document has 
    been edited so we should save the changes to disk.
*/
class ShapeView: SCNView {
    // MARK: - Properties

    var document: ShapeDocument? {
        didSet {
            guard let document = document else { return }

            document.setSceneOnRenderer(self)

            self.backgroundColor = document.backgroundColor
        }
    }

    // MARK: - Initialization

    override func awakeFromNib() {
        autoenablesDefaultLighting = true
        allowsCameraControl = true
    }

    // MARK: - Override

    override func touchesEnded(touches: Set<UITouch>, withEvent event: UIEvent?) {
        /*
            The user finished interacting with the shape for now, so notify the
            document that changes happened so that it writes the new document
            state to disk.
        */
        guard let pointOfView = pointOfView else { return }

        document?.updateCameraState(pointOfView)
    }
}
```

[Next](ShapeEdit-AppDelegate.swift.md)[Previous](ShapeEdit-DocumentEditor-ShapeDocument.swift.md)

