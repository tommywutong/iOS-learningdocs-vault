---
title: Why doesn't the keyboard show when my text input view is tapped?
apple_id: DTS40014522
resource_type: QA
platform: iOS
topic: Data Management
technology: null
published: '2014-05-14'
source_url: https://developer.apple.com/library/archive/qa/qa1813/_index.html
archived_at: '2026-07-18T02:34:55.811996Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1813

# Why doesn't the keyboard show when my text input view is tapped?

## Q:  Why doesn’t the keyboard show when my text input view is tapped?

A: There are several reasons why the keyboard doesn't show:

- First, it may be because the keyboard is covered by a higher-level window (see [windowLevel](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIWindow_Class/UIWindowClassReference/UIWindowClassReference.html#//apple_ref/occ/instp/UIWindow/windowLevel) for more information). In iOS, the keyboard is a subview of an independent window. The window has a higher level than the application's key window, so it is always displayed in the front. If you create another window in the overlapped position and make its level higher than that of the keyboard window, then the keyboard would be covered, thus becoming invisible to your users. You can confirm this by checking the relevant attributes of your application windows, as shown in Listing 1:

  __Listing 1__  Printing out the relevant attributes of windows

```
for (UIWindow *window in [[UIApplication sharedApplication] windows]) {
    NSLog(@"isKeyWindow = %d window level = %.1f frame = %@ class = %@\n",
          window.isKeyWindow, window.windowLevel,
          NSStringFromCGRect(window.frame), window.class.description);
}
```

  Listing 2 provides an example log when the keyboard is covered by a higher-level window (`MyCustomWindow`) in the overlapped position.

  __Listing 2__  An example log when the keyboard is covered by a higher-level window

```
TheApp[22892:60b] isKeyWindow = 1 window level = 0.0 frame = {{0, 0}, {320, 480}}
class = UIWindow
TheApp[22892:60b] isKeyWindow = 0 window level = 1.0 frame = {{0, 0}, {320, 480}}
class = UITextEffectsWindow
TheApp[22892:60b] isKeyWindow = 0 window level = 2000.0 frame = {{0, 200}, {320, 280}}
class = MyCustomWindow
```

  The solution is to avoid using multiple windows by replacing the extra window with a view or view hierarchy. In iOS, an application should only have one window unless it needs to display content on an external device screen (in this case, the extra window is normally displayed on a new screen). This ensures the keyboard, when shown, is always in the front of the screen.
- Secondly, your keyboard may not show because your text input view failed to become the first responder. This may be due to any of the following reasons:

  - Your text input view is not allowed to become the first responder. The implementation of `-` `(BOOL)canBecomeFirstResponder` method in `UIView` returns `NO` by default; thus, preventing view instances from becoming the first responder. Therefore, if your view class is directly derived from `UIView`, then you need to override the above method to return `YES` as shown in Listing 3. Doing so will ensure that your text input view is allowed to become the first responder.

    __Listing 3__  Allowing a custom view to become the first responder

```objc
- (BOOL)canBecomeFirstResponder {
    return YES;
}
```
  - Your text input view refuses to become the first responder. This may happen when the `-` `(BOOL)becomeFirstResponder` method of your view class returns `NO`. If you override this method for some reasons, be sure that it returns `YES` when the text input view is interactive.
- Lastly, the issue may be related to the auto-rotation support of view controllers. Since iOS 6, `UIViewController`'s subclasses support auto-rotation by returning an orientation bit mask in the [- (NSUInteger)supportedInterfaceOrientations](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIViewController_Class/Reference/Reference.html#//apple_ref/occ/instm/UIViewController/supportedInterfaceOrientations) method. `UIKit` uses the bit mask to calculate the keyboard frame for current user interface orientation. Returning a wrong bit mask may cause the keyboard to be placed outside the screen. So if your application supports auto-rotation, be sure that the `-` `(NSUInteger)supportedInterfaceOrientations` method is implemented and returns the right bit mask. See [UIInterfaceOrientationMask](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/Reference/Reference.html#//apple_ref/c/tdef/UIInterfaceOrientationMask) for valid bit-mask values.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-05-14 | New document that explains why the keyboard doesn't show when a text input view is tapped. |

