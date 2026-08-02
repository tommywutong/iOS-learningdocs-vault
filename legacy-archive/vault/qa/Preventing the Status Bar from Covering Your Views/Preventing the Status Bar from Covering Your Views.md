---
title: Preventing the Status Bar from Covering Your Views
apple_id: DTS40013765
resource_type: QA
platform: iOS
topic: User Experience
technology: null
published: '2014-01-09'
source_url: https://developer.apple.com/library/archive/qa/qa1797/_index.html
archived_at: '2026-07-18T02:34:45.621741Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1797

# Preventing the Status Bar from Covering Your Views

## Q:  How do I prevent the status bar from covering my views in iOS 7?

A: You need to use Auto Layout and apply a vertical spacing anchored to the "Top Layout Guide" of your view controller.

Beginning with iOS 7 view controllers are displayed full screen, by default, as shown in Figure 1. This means they will cover the entire screen including the area underneath the status bar.

__Figure 1__  Full screen view controller underneath the status bar

!!

__Figure 2__  Shows the view below the status bar, similar to the pre-iOS 7 behavior.

!!

Applications that use an opaque UINavigationController or UITabBarController automatically keep their content below the status bar.

Any view that needs to be anchored to the top and just below the status bar (i.e., UIToolbar, UIButton, etc.) requires additional work for proper placement. This Q&A takes you through a process showing how to properly place a UIToolbar using Auto Layout and Interface Builder. When you are done with this tutorial, you will have the necessary knowledge and tools to keep the content from appearing under the status bar.

For clarity, this Q&A begins with a new Xcode project and uses a UIToolbar for the top most view. At a high level, there are four major activities in this Q&A tutorial:

1. Create your project
2. Add top most view
3. Add vertical constraint to top most view
4. Add remaining constraints to top most view

1. Launch Xcode 5.0
2. Choose File menu > New > Project…
3. Among the choices for template project, select "Single View Application"
4. Click Next
5. Fill in the Product Name
6. Set Devices to "iPad"
7. Click Next
8. Pick a location to save the project, click Create.

Your Xcode project window should now appear.

1. Select the "Main.storyboard".
2. Show the "Utilities" pane on the right.
3. Open Object Library (found in lower right of the window) by selecting menu View > Utilities > Show Object Library
4. Search for UIToolbar.
5. Drag a UIToolbar to the View Controller's view.

1. Show the Document Outline for this storyboard (if not already) by selecting menu Editor > Show Document Outline. This will allow to you see the Top Layout Guide in your view controller scene.

2. Control drag from the UIToolbar to the "Top Layout Guide" as shown in figure 3.

__Figure 3__  Control drag

!

3. In the popover, choose "Vertical Spacing" as shown in figure 4.

__Figure 4__  Vertical Spacing

!

A vertical constraint is now added to your UIToolbar.

4. Select the "Vertical Space" constraint for that UIToolbar (it should be titled "Vertical Space …")

5. Open the Utilities pane by selecting menu View > Utilities > Show Attributes Inspector.

6. Change the "Vertical Space Constraint" Constant to 0 (zero) as shown in figure 6.

__Figure 5__  Vertical Space Constraint

!

Finally, to apply the missing constraints for the UIToolbar:

1. Select the UIToolbar.

2. Select menu Editor > Resolve Autolayout Issues > Add Missing Constraints

The remaining constraints should appear for that UIToolbar, thus eliminating any Auto Layout warnings in your project.

Run the app, and the toolbar should be properly placed just below the status bar. This is compatible with both iOS 6 and iOS 7.

For more detailed information about how to programmatically add a vertical constraint to the topLayoutGuide, refer to [UIViewController Class Reference](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIViewController_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40006926).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-01-09 | Editorial updates. |
| 2013-09-09 | New document that shows how to automatically place your subviews below the status bar with iOS 7, using Xcode 5.0. |

