---
title: Revisiting the App Launch Sequence on iOS
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/02/app-launch-sequence-ios-revisited/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:b4956547f04e0bc9'
translated: false
---

> 原文：[Revisiting the App Launch Sequence on iOS](https://oleb.net/blog/2012/02/app-launch-sequence-ios-revisited/)　·　Ole Begemann

# Revisiting the App Launch Sequence on iOS

In June 2011, I blogged about [the App Launch Sequence on iOS](https://oleb.net/blog/2011/06/app-launch-sequence-ios/) for the first time, illustrating what really happens under the hood between the launch of an iOS app and the [`application:didFinishLaunchingWithOptions:`](https://developer.apple.com/library/IOs/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/Reference/Reference.html#//apple_ref/doc/uid/TP40006786-CH3-SW18) method.

Since that time, Apple has revised the default launch sequence in their iOS app project templates, so it is time for an update to the original post.

# Flowchart

![App Launch Sequence as of Xcode 4.2 (without Storyboarding)](https://oleb.net/media/xcode-4-2-app-launch-sequence.png)

<sub>Flowchart of the default app launch sequence in iOS as of Xcode 4.2 for a non-storyboarded app. Feel free to share this image under a [Creative Commons Attribution license](http://creativecommons.org/licenses/by/3.0/) (CC-BY). In a storyboarded app, `UIApplicationMain()` would additionally initiate the loading of the app's main storyboard file, which in turn would create the window and initial view controller.</sub>

# Changes to `main()`

Let’s have a look at the changes to the `main()` function, which still is the starting point for our app. The function now looks like this:

```
int main(int argc, char *argv[])
{
    @autoreleasepool {
        return UIApplicationMain(argc, argv, nil, NSStringFromClass([AppDelegate class]));
    }
}
```

`main()` uses the new `@autoreleasepool { }` syntax introduced with LLVM 3.0, but that change doesn’t concern the app’s launch sequence. More importantly, the call to [`UIApplicationMain()`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIKitFunctionReference/Reference/reference.html#//apple_ref/doc/uid/TP40006894-CH3-SW7) changed from `UIApplicationMain(argc, argv, nil, nil);` to the one shown above. Note the change in the fourth argument.

Looking at [the documentation](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIKitFunctionReference/Reference/reference.html#//apple_ref/doc/uid/TP40006894-CH3-SW7), we learn that the fourth argument to `UIApplicationMain()` specifies

> The name of the class from which the application delegate is instantiated. … Specify `nil` if you load the delegate object from your application’s main nib file.

So apparently our app delegate, which was previously created with Interface Builder inside `MainWindow.xib`, is now created directly by the `UIApplicationMain()` function.[1](#fn:1) In fact, there isn’t even a `MainWindow.xib` file anymore in our project!

# No MainWindow.xib

Before Xcode 4.2, all default project templates did create a `MainWindow.xib` file. Because this file was specified in the app’s `Info.plist` as the main NIB file, the `UIApplicationMain()` function would load it automatically right after it had created the [`UIApplication`](https://developer.apple.com/reference/uikit/uiapplication) instance for the app.

It was then inside the NIB file that both the application delegate object and the app’s main window were created and wired together via outlets. More often than not, `MainWindow.xib` would also include the app’s root view controller, already connected to a custom outlet in the application delegate class and the window’s `rootViewController` outlet.

With so much work done inside the main NIB file, the default `application:didFinishLaunchingWithOptions:` method could be kept almost empty. All it had to do was bring the window on screen:

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    // Override point for customization after application launch.
    [self.window makeKeyAndVisible];
    return YES;
}
```

For Xcode 4.2 and later, Apple has decided to remove the main NIB file from the iOS project templates. The immediate reason for this change was most likely the introduction of [storyboarding](https://developer.apple.com/library/ios/#releasenotes/Miscellaneous/RN-AdoptingStoryboards/_index.html).

Storyboards are based around view controllers, not views or windows. Sticking to the concept of a main NIB file for a storyboard-based app would make no sense (and is impossible since the `Info.plist` keys `NSMainNibFile` and `UIMainStoryboardFile` [are mutually exclusive](https://developer.apple.com/library/ios/documentation/general/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW9)). And abandoning the main NIB file only for storyboard-based apps but keeping it for others would lead to project templates differ from each other more than necessary.

# More Work To Do in `application:didFinishLaunchingWithOptions:`

With the main NIB file gone, the tasks that were performed in the NIB file must now move elsewhere. We have already seen that `UIApplicationMain()` takes over one of them: the creation of our application delegate. Since the function now has control over both the `UIApplication` instance and its delegate, we can also safely assume that it will assign the delegate to the application instance.

At this stage, the `application:didFinishLaunchingWithOptions:` message will be sent. Since nobody has created a window or view controller yet, the method now performs these tasks in code, at least for an app that is not storyboard-based:

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    // Override point for customization after application launch.
    self.viewController = [[ViewController alloc] initWithNibName:@"ViewController" bundle:nil];
    self.window.rootViewController = self.viewController;
    [self.window makeKeyAndVisible];
    return YES;
}
```

If your app uses storyboarding (by specifying a `UIMainStoryboardFile` in `Info.plist`), the app will automatically load the main storyboard file at launch, just like the main NIB file. It will also create a window and place the storyboard’s initial view controller inside it, and bring the window on screen. Therefore, there is nothing left to do for us in `application:didFinishLaunchingWithOptions:`:

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    // Override point for customization after application launch.
    return YES;
}
```

# A Litte More Code But Clearer

Initializing our (non-storyboard) app now takes a few more lines of code than before, but I think this change made the application launch sequence a lot clearer than before. I know many iOS developers who have had problems understanding the launch process because the role the main NIB file played was not clear to them.

Im a generally a big proponent of using NIB files/storyboards but in some cases they can confuse more than they help.

1. The syntax `NSStringFromClass([AppDelegate class])` might seem a little strange. Why did Apple not just use a plain string @”AppDelegate” here? The result would be the same. They probably did it the more complicated way to simplify refactoring: if you want to rename the `AppDelegate` class, the built-in refactoring tool would detect its use in `main()` and rename it there as well. That would obviously not work if it were just a string. [↩︎](#fnref:1)
