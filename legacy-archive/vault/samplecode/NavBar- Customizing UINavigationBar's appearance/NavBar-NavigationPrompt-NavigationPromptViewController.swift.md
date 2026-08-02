---
title: 'NavBar: Customizing UINavigationBar''s appearance'
apple_id: DTS40007418
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2017-12-07'
source_url: https://developer.apple.com/library/archive/samplecode/NavBar/Listings/NavBar_NavigationPrompt_NavigationPromptViewController_swift.html
archived_at: '2026-07-18T03:16:53.383408Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NavBar: Customizing UINavigationBar's appearance](NavBar-%20Customizing%20UINavigationBar%27s%20appearance.md)


[Next](NavBar-CitiesDataSource.swift.md)[Previous](NavBar-CustomAppearance-CustomAppearanceViewController.swift.md)

# NavBar/NavigationPrompt/NavigationPromptViewController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Demonstrates displaying text above the navigation bar.
 */

import UIKit

class NavigationPromptViewController: UIViewController {

    override var supportedInterfaceOrientations: UIInterfaceOrientationMask {
        return .portrait
    }

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)

        // There is a bug in iOS 7.x (fixed in iOS 8) which causes the
        // topLayoutGuide to not be properly resized if the prompt is set before
        // -viewDidAppear: is called. This may result in the navigation bar
        // improperly overlapping your content.  For this reason, you should
        // avoid configuring the prompt in your storyboard and instead configure
        // it programmatically in -viewDidAppear: if your application deploys to iOS 7.
        //
        navigationItem.prompt = "Navigation prompts appear at the top."
    }
}
```

[Next](NavBar-CitiesDataSource.swift.md)[Previous](NavBar-CustomAppearance-CustomAppearanceViewController.swift.md)

