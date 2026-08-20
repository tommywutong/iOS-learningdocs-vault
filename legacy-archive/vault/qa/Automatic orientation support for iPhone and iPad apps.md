---
title: Automatic orientation support for iPhone and iPad apps
apple_id: DTS40009983
resource_type: QA
platform: iOS
topic: User Experience
technology: null
published: '2013-08-06'
source_url: https://developer.apple.com/library/archive/qa/qa1588/_index.html
archived_at: '2026-07-18T02:32:21.835561Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1588

# Automatic orientation support for iPhone and iPad apps

## Q:  What is needed to support multiple orientations in my iPhone and iPad apps?

A: There are two things you must implement to automatically support multiple orientations in your iPhone and iPad apps: provide launch images, and update your app's `Information Property List`. To support multiple orientations on iOS 5 and below, your app's view controllers need to implement the `-shouldAutorotateToInterfaceOrientation:` method.

iPhone-only applications may only include one launch image. This is because all applications on iPhone are launched in portrait to match the home screen orientation. If your iPhone app is designed to start in landscape, see [Q&A: Launch Image Doesn't Show Up for iPhone Apps](https://developer.apple.com/library/ios/#qa/qa1700/_index.html) for information about preparing your launch images.

iPad-only applications should include launch images for each supported orientation.

Universal applications should include both iPhone and iPad specific launch images.

Refer to the [App Launch Images](https://developer.apple.com/library/etc/redirect/DTS/ios/AppLaunchImages) section in the [iOS App Programming Guide](https://developer.apple.com/library/etc/redirect/devcenter/ios/app_programming_guide) for launch image dimensions and names.

For information about designing launch images, refer to the [Launch Images](https://developer.apple.com/library/etc/redirect/DTS/ios/HIGLaunchImages) section in the [iOS Human Interface Guidelines](https://developer.apple.com/library/etc/redirect/devcenter/ios/hig).

In your app's `Information Property List` (`Info.plist`), add values to the `Supported interface orientations` (`UISupportedInterfaceOrientations`) key for the supported orientations.

See the [Information Property List Key Reference](https://developer.apple.com/library/etc/redirect/DTS/ios/UISupportedInterfaceOrientations) for possible values.

To support multiple interface orientation on iOS 6 and later, your view controller classes do not need to implement any additional methods. Beginning with iOS 6, view controllers support all orientations on iPad and all orientations except portrait upside-down on iPhone by default.

__If your app supports iOS 5 and below__

In each of your `UIViewController` classes, implement the `-(BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation` method to return YES for the supported `UIInterfaceOrientation` constants. This method should return `YES` to support all orientations.

See [Q&A: Why won't my UIViewController rotate with the device?](https://developer.apple.com/library/ios/#qa/qa1688/_index.html) for possible reasons your view controller does not rotate.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-08-06 | Added information about iOS 6. |
| 2011-03-17 | Corrected the dimensions for iPad launch images. |
| 2010-08-06 | Included more information on launch images for iPhone-only and universal apps. |
| 2010-06-01 | Corrected the dimension for iPad portrait launch image. Changed the context to apply only for automatic orientation support. |
| 2010-05-17 | New document that describes the required steps to automatically support orientations for iPhone and iPad apps. |

