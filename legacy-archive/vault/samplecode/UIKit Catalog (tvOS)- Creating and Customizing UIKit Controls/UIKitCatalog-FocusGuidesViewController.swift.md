---
title: 'UIKit Catalog (tvOS): Creating and Customizing UIKit Controls'
apple_id: TP40016433
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: UIKit
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/UICatalogFortvOS/Listings/UIKitCatalog_FocusGuidesViewController_swift.html
archived_at: '2026-07-18T03:27:28.980109Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UIKit Catalog (tvOS): Creating and Customizing UIKit Controls](UIKit%20Catalog%20%28tvOS%29-%20Creating%20and%20Customizing%20UIKit%20Controls.md)


[Next](UIKitCatalog-MenuSplitViewController.swift.md)[Previous](UIKitCatalog-AlertFormViewController.swift.md)

# UIKitCatalog/FocusGuidesViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A view controller that demonstrates how to add and update `UIFocusGuide`s.
*/

import UIKit

class FocusGuidesViewController: UIViewController {
    // MARK: Properties

    @IBOutlet var topLeftButton: UIButton!

    @IBOutlet var topRightButton: UIButton!

    @IBOutlet var bottomLeftButton: UIButton!

    private var focusGuide: UIFocusGuide!

    override var preferredFocusEnvironments: [UIFocusEnvironment] {
        return [topLeftButton]
    }

    // MARK: UIViewController

    override func viewDidLoad() {
        super.viewDidLoad()

        /*
            Create a focus guide to fill the gap below button 2 and to the right
            of button 3.
        */
        focusGuide = UIFocusGuide()
        view.addLayoutGuide(focusGuide)

        // Anchor the top left of the focus guide.
        focusGuide.leftAnchor.constraint(equalTo: topRightButton.leftAnchor).isActive = true
        focusGuide.topAnchor.constraint(equalTo: bottomLeftButton.topAnchor).isActive = true

        // Anchor the width and height of the focus guide.
        focusGuide.widthAnchor.constraint(equalTo: topRightButton.widthAnchor).isActive = true
        focusGuide.heightAnchor.constraint(equalTo: bottomLeftButton.heightAnchor).isActive = true
    }

    // MARK: UIFocusEnvironment

    override func didUpdateFocus(in context: UIFocusUpdateContext, with coordinator: UIFocusAnimationCoordinator) {
        super.didUpdateFocus(in: context, with: coordinator)

        /*
            Update the focus guide's `preferredFocusedView` depending on which
            button has the focus.
        */
        guard let nextFocusedView = context.nextFocusedView else { return }

        switch nextFocusedView {
            case topRightButton:
                focusGuide.preferredFocusEnvironments = [bottomLeftButton]

            case bottomLeftButton:
                focusGuide.preferredFocusEnvironments = [topRightButton]

            default:
                focusGuide.preferredFocusEnvironments = []
        }
    }
}
```

[Next](UIKitCatalog-MenuSplitViewController.swift.md)[Previous](UIKitCatalog-AlertFormViewController.swift.md)

