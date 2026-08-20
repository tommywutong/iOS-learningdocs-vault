---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_NotificationBar_swift.html
archived_at: '2026-07-18T03:03:29.011391Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-AppDelegate.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-MainMenuTableViewCell.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/NotificationBar.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This class describes the notification bar that is shown when a CloudKit notification is received.
*/

import UIKit
import CloudKit

class NotificationBar: UIView {

    var notification: CKNotification? {
        didSet {
            if let navigationController = window!.rootViewController as? UINavigationController {
                for viewController in navigationController.viewControllers {
                    viewController.navigationItem.hidesBackButton = (notification != nil)
                }
            }
            setNeedsLayout()
            self.superview!.layoutIfNeeded()
        }
    }

    var heightConstraint: NSLayoutConstraint!

    var label: UILabel!
    var button: UIButton!

    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        heightConstraint = NSLayoutConstraint(item: self, attribute: .Height, relatedBy: .Equal, toItem: nil, attribute: .NotAnAttribute, multiplier: 1.0, constant: 0.0)
        translatesAutoresizingMaskIntoConstraints = false

        backgroundColor = UIColor.blackColor()

        addConstraint(heightConstraint)

        label = UILabel()
        label.text = "You have a new CloudKit notification!"
        label.textColor = UIColor.whiteColor()
        label.textAlignment = .Center
        label.translatesAutoresizingMaskIntoConstraints = false
        label.hidden = true
        label.userInteractionEnabled = true

        addSubview(label)

        button = UIButton()
        button.setTitle("✕", forState: .Normal)
        button.addTarget(self, action: #selector(NotificationBar.close), forControlEvents: .TouchDown)
        button.translatesAutoresizingMaskIntoConstraints = false
        button.hidden = true

        addSubview(button)

        let rightConstraint = NSLayoutConstraint(item: self, attribute: .RightMargin, relatedBy: .Equal, toItem: button, attribute: .Right, multiplier: 1.0, constant: 0.0)
        addConstraint(rightConstraint)

        let centerConstraint = NSLayoutConstraint(item: self, attribute: .CenterY, relatedBy: .Equal, toItem: button, attribute: .CenterY, multiplier: 1.0, constant: 0.0)
        addConstraint(centerConstraint)

        let leftConstraint = NSLayoutConstraint(item: self, attribute: .LeftMargin, relatedBy: .Equal, toItem: label, attribute: .Left, multiplier: 1.0, constant: 0.0)
        addConstraint(leftConstraint)

        let rightLabelConstraint = NSLayoutConstraint(item: button, attribute: .Left, relatedBy: .Equal, toItem: label, attribute: .Right, multiplier: 1.0, constant: 8.0)
        addConstraint(rightLabelConstraint)

        let centerLabelConstraint = NSLayoutConstraint(item: self, attribute: .CenterY, relatedBy: .Equal, toItem: label, attribute: .CenterY, multiplier: 1.0, constant: 0.0)
        addConstraint(centerLabelConstraint)

        let tapGestureRecognizer = UITapGestureRecognizer(target: self, action: #selector(NotificationBar.showNotification))
        label.addGestureRecognizer(tapGestureRecognizer)

    }

    func close() {
        UIView.animateWithDuration(0.4, animations: {
            self.label.hidden = true
            self.button.hidden = true
            self.heightConstraint.constant = 0
            self.notification = nil
        })
    }

    func show() {
        UIView.animateWithDuration(0.4, animations: {
            self.heightConstraint.constant = self.superview!.frame.size.height
            self.label.hidden = false
            self.button.hidden = false
            self.superview!.layoutIfNeeded()
        })
    }

    func showNotification() {
        if let _ = notification, navigationController = window!.rootViewController as? NavigationController, mainMenuViewController = navigationController.viewControllers.first as? MainMenuTableViewController {
            close()
            if let topViewController = navigationController.topViewController as? CodeSampleViewController where topViewController.selectedCodeSample is MarkNotificationsReadSample {
                topViewController.runCode(topViewController.runButton)
            } else {
                let notificationSample = mainMenuViewController.codeSampleGroups.last!.codeSamples.first
                navigationController.performSegueWithIdentifier("ShowLoadingView", sender: notificationSample)
            }
        }
    }


}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-AppDelegate.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-MainMenuTableViewCell.swift.md)

