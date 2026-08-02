---
title: Handling Popover Controllers During Orientation Changes
apple_id: DTS40009982
resource_type: QA
platform: iOS
topic: User Experience
technology: UIKit
published: '2010-12-10'
source_url: https://developer.apple.com/library/archive/qa/qa1694/_index.html
archived_at: '2026-07-18T02:34:12.096850Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1694

# Handling Popover Controllers During Orientation Changes

## Q:  How do I handle popover controllers when the device orientation changes?

A: How do I handle popover controllers when the device orientation changes?

When showing a popover controller, there are times when you will need to handle how the popover controller appears after a change in device orientation.

Situations when handling is required:

- If the popover controller is presented from a target rectangle using the `–presentPopoverFromRect:inView:permittedArrowDirections:animated:` method of UIPopoverController.
- If the popover controller is presented from a bar button item that is removed after the rotation has finished.

- In the `-didRotateFromInterfaceOrientation:` method of UIApplication, present the popover controller again after the rotation has finished.

  __Listing 1__  Presenting a popover controller from a target rectangle after the rotation has finished.

```objc
- (void)didRotateFromInterfaceOrientation:(UIInterfaceOrientation)fromInterfaceOrientation {     [aPopover presentPopoverFromRect:targetRect.frame inView:self.view permittedArrowDirections:UIPopoverArrowDirectionAny animated:YES]; }
```

- Do not present more than one popover controller at a time. For more information on the proper usage of UIPopoverController, read the [Popover section](https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/MobileHIG/UIElementGuidelines/UIElementGuidelines.html#//apple_ref/doc/uid/TP40006556-CH13-SW40) in the in the [iOS Human Interface Guidelines](https://developer.apple.com/library/ios/#documentation/UserExperience/Conceptual/MobileHIG/Introduction/Introduction.html).
- Do not use `self.popovercontroller` for a custom popover controller, if you are using a split-view controller. The default popover controller should be reserved for the master list view controller.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-12-10 | Updated to reflect consolidated iPad/iPhone Human Interface Guidelines. |
| 2010-05-18 | Removed situations where handling of popover controllers was not required. |
| 2010-05-17 | New document that shows best practices for handling popover controllers during device orientation changes. |

