---
title: Why won't my UIViewController rotate with the device?
apple_id: DTS40009879
resource_type: QA
platform: iOS
topic: User Experience
technology: null
published: '2013-04-18'
source_url: https://developer.apple.com/library/archive/qa/qa1688/_index.html
archived_at: '2026-07-18T02:34:10.787857Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1688

# Why won't my UIViewController rotate with the device?

## Q:  Why won't my `UIViewController` rotate with the device?

A: The `UIViewController` class provides the fundamental view-management model for iOS applications. It provides automatic support for rotating the views of the view controller in response to changes to the orientation of the device. If the autoresizing properties of your view and subviews are properly configured, this behavior is automatic in most cases. Here is a fairly exhaustive list of reasons a view controller may not rotate.

- You have added your view controller's `UIView` property to `UIWindow` as a subview.

  Developers are discouraged from adding the view property of any view controller as a subview of `UIWindow`. Your application's root view controller should be assigned to the app window's `rootViewController` property either in Interface Builder, or at runtime before returning from `application:didFinishLaunchingWithOptions:`. If you need to display content from more than one view controller simultaneously, you should define your own container view controller and use it as the root view controller. See [Creating Custom Container View Controllers](https://developer.apple.com/library/ios/redirect/DTS/CustomContainerVC).

  __Beginning with iOS 6__, if a root view controller has not been assigned to the app's window, supported orientations are determined only by the `UIApplication` object. Further, view controllers will not be notified of orientation changes, which may result in unexpected behavior.
- The view controller does not support the new orientation.

  __Beginning with iOS 6__, a view controller can limit its supported orientations by overriding this method:

  `- (NSUInteger)supportedInterfaceOrientations`

  The default implementation of `supportedInterfaceOrientations` returns a rotation mask of the recommended orientation values for the current device's idiom. That is, `UIInterfaceOrientationMaskAll` is returned on iPad devices and `UIInterfaceOrientationMaskAllButUpsideDown` is returned on iPhone devices. There is little need to override this method unless the content managed by the view controller must only be displayed in a subset of these orientations. If you override this method, your implementation must return a bitwise combination of `UIInterfaceOrientationMask` values.

  __On iOS 5 and below__, a view controller can support multiple orientations by overriding this method:

  `- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation`

  Even if `shouldAutorotateToInterfaceOrientation` is implemented, you should make sure it returns `YES` for all the orientations you wish to support. The default implementation returns `YES` if `interfaceOrientation` is equal to `UIInterfaceOrientationPortrait`, locking the view controller into portrait orientation. To support all orientations, simply always return `YES`.
- The application does not support the same orientations as the view controller.

  __Beginning with iOS 6__, UIKit uses both the `UIApplication` object and the topmost view controller to determine the supported orientations. The `UISupportedInterfaceOrientations` key in the app's `Info.plist` must contain a value for each orientation your app supports. The system uses these values to derive the app's supported orientation mask. The application delegate may implement `application:supportedInterfaceOrientationsForWindow:` to return a `UIInterfaceOrientationMask` that is used in place of the values from the app's `Info.plist`.

  __On iOS 5 and below__, the values for the `UISupportedInterfaceOrientations` key in the app's `Info.plist` only serve as a hint to Springboard that it should reposition the status bar before starting your app. They do not restrict the supported orientations of your app after it has been launched.
- The view controller declined to rotate.

  __Beginning with iOS 6__, when UIKit determines that rotation may need to occur, it calls the `shouldAutorotate` method of the topmost view controller to determine whether to proceed with the rotation. The default implementation of this method returns `YES`; however, a view controller may dynamically disable automatic rotation at runtime by overriding `shouldAutorotate` to return `NO`.
- The view controller is a child of another view controller.

  __Beginning with iOS 6__, only the topmost view controller (alongside the `UIApplication` object) participates in deciding whether to rotate in response to a change of the device's orientation. More often than not, the view controller displaying your content is a child of `UINavigationController`, `UITabBarController`, or a custom container view controller. You may find yourself needing to subclass a container view controller in order to modify the values returned by its `supportedInterfaceOrientations` and `shouldAutorotate` methods.
- The view controller overrides `init` or `initWithNibName:bundle:` but does not invoke the superclass' implementation. For the object to be initialized properly, you must call super on any `init` or `initWithNibName` method you are overriding in your view controllers.
- All child view controllers in your `UITabBarController` or `UINavigationController` do not agree on a common orientation set.

  __On iOS 5 and below__, to make sure that all your child view controllers rotate correctly, you must implement `shouldAutorotateToInterfaceOrientation` for each view controller representing each tab or navigation level. Each must agree on the same orientation for that rotate to occur. That is, they all should return `YES` for the same orientation positions.
- The view controller is altering the layout of its subviews programmatically.

  Certain layouts are impossible to realize using autoresizing masks alone. A view controller can manually layout its subviews by altering their frame, bounds, or center properties. Developers should not place layout code in any of the rotation methods overridden by the view controller (e.g. `shouldAutorotateToInterfaceOrientation`). There are cases where the interface may rotate without these methods being called, leaving the view controller's subviews in an inconsistent state.

  __If the app only supports iOS 5 or later__, you should place layout code in the view controller's `viewWillLayoutSubviews:` or `viewDidLayoutSubviews:` methods.

  __If the app must support iOS 4__, you should place layout code in the `layoutSubviews` method of the view controller's view.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-04-18 | Updated to include changes to autorotation in iOS 6. |
| 2010-07-06 | Added the case of not calling super on -(id)init. |
| 2010-04-08 | New document that describes situations that can prevent view controllers from rotating. |

