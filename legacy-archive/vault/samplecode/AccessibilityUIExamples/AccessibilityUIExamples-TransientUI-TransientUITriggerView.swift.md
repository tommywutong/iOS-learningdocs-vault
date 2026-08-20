---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_TransientUI_TransientUITriggerView_swift.html
archived_at: '2026-07-18T03:00:38.876312Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-TransientUI-TransientUIViewController.swift.md)[Previous](AccessibilityUIExamples-Table-CustomTableViewController.swift.md)

# AccessibilityUIExamples/TransientUI/TransientUITriggerView.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
An example demonstrating adding accessibility to an NSView subclass that shows a hidden view
 on mouse over by implementing the NSAccessibilityContainsTransientUI protocol.
*/

import Cocoa

class TransientUITriggerView: NSView, NSAccessibilityContainsTransientUI {

    static let ShowHideTransientUIAnimationDuration = 0.2

    @IBOutlet var transientView: NSView!

    override func awakeFromNib() {
        super.awakeFromNib()
        createTrackingArea()
        transientView.alphaValue = 0.0
        transientView.isHidden = true
    }

    fileprivate func createTrackingArea() {
        // Track the mouse for enter and exit for proper highlighting.
        let trackingArea = NSTrackingArea(rect: bounds,
                                          options: [NSTrackingArea.Options.activeInActiveApp,
                                                    NSTrackingArea.Options.activeAlways,
                                                    NSTrackingArea.Options.mouseEnteredAndExited,
                                                    NSTrackingArea.Options.mouseMoved,
                                                    NSTrackingArea.Options.inVisibleRect],
                                          owner: self,
                                          userInfo: nil)
        addTrackingArea(trackingArea)
    }

    fileprivate func showTransientView() {
        setTransientViewIsHidden(hidden: false)
    }

    fileprivate func hideTransientView() {
        setTransientViewIsHidden(hidden: true)
    }

    fileprivate func setTransientViewIsHidden(hidden: Bool) {
        if hidden != transientView.isHidden {
            transientView.isHidden = hidden

            let animationContext = NSAnimationContext.current
            NSAnimationContext.beginGrouping()

            animationContext.duration = TransientUITriggerView.ShowHideTransientUIAnimationDuration
            transientView.animator().alphaValue = transientView.isHidden ? 0.0 : 1.0

            NSAnimationContext.endGrouping()

            sendTransientUIChangedNotification()
        }
    }

    // MARK: - Events

    override func mouseMoved(with event: NSEvent) {
        showTransientView()
    }

    override func mouseEntered(with event: NSEvent) {
        showTransientView()
    }

    override func mouseExited(with event: NSEvent) {
        hideTransientView()
    }

}

// MARK: -

extension TransientUITriggerView {
    // MARK: Accessibility

    override func isAccessibilityAlternateUIVisible() -> Bool {
        return !transientView.isHidden
    }

    override func accessibilityPerformShowAlternateUI() -> Bool {
        showTransientView()
        return true
    }

    override func accessibilityPerformShowDefaultUI() -> Bool {
        hideTransientView()
        return true
    }

    fileprivate func sendTransientUIChangedNotification() {
        let changedElements = NSAccessibilityUnignoredChildren(transientView.subviews)
        NSAccessibilityPostNotificationWithUserInfo(self, .layoutChanged, [NSAccessibilityNotificationUserInfoKey.uiElements: changedElements])
    }

}
```

[Next](AccessibilityUIExamples-TransientUI-TransientUIViewController.swift.md)[Previous](AccessibilityUIExamples-Table-CustomTableViewController.swift.md)

