---
title: 'AdaptivePhotos: Using UIKit Traits and Size Classes'
apple_id: TP40014636
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AdaptivePhotos/Listings/AdaptiveStoryboard_AdaptiveStoryboard_ProfileViewController_swift.html
archived_at: '2026-07-18T03:00:44.997051Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AdaptivePhotos: Using UIKit Traits and Size Classes](AdaptivePhotos-%20Using%20UIKit%20Traits%20and%20Size%20Classes.md)


[Next](AdaptiveStoryboard-AdaptiveStoryboard-AppDelegate.swift.md)[Previous](AdaptiveStoryboard-AdaptiveStoryboard-AboutViewController.swift.md)

# AdaptiveStoryboard/AdaptiveStoryboard/ProfileViewController.swift

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
A view controller that shows a user's profile.
*/

import UIKit

class ProfileViewController: UIViewController {
    // MARK: Properties

    @IBOutlet fileprivate var imageView: UIImageView?
    @IBOutlet fileprivate var nameLabel: UILabel?
    @IBOutlet fileprivate var conversationsLabel: UILabel?
    @IBOutlet fileprivate var photosLabel: UILabel?

    var user: User? {
        didSet {
            if isViewLoaded {
                updateUser()
            }
        }
    }

    var nameText: String? {
        return user?.name
    }

    var conversationsText: String {
        let conversationCount = user?.conversations.count ?? 0

        let localizedStringFormat = NSLocalizedString("%d conversations", comment: "X conversations")

        return String.localizedStringWithFormat(localizedStringFormat, conversationCount)
    }

    var photosText: String {
        let photoCount = user?.conversations.reduce(0) { count, conversation -> Int in
            return count + conversation.photos.count
        } ?? 0

        let localizedStringFormat = NSLocalizedString("%d photos", comment: "X photos")

        return String.localizedStringWithFormat(localizedStringFormat, photoCount)
    }

    // MARK: View Controller

    override func viewDidLoad() {
        super.viewDidLoad()

        updateUser()
    }

    // MARK: IBActions

    @IBAction func closeProfileViewController(_ sender: AnyObject) {
        dismiss(animated: true, completion: nil)
    }

    // MARK: Convenience

    // Updates the user interface with the data from the current user object.
    func updateUser() {
        nameLabel?.text = nameText
        conversationsLabel?.text = conversationsText
        photosLabel?.text = photosText
        imageView?.image = user?.lastPhoto?.image
    }
}
```

[Next](AdaptiveStoryboard-AdaptiveStoryboard-AppDelegate.swift.md)[Previous](AdaptiveStoryboard-AdaptiveStoryboard-AboutViewController.swift.md)

