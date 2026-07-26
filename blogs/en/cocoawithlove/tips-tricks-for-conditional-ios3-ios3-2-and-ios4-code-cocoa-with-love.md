---
title: 'Tips & Tricks for conditional iOS3, iOS3.2 and iOS4 code | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/07/tips-tricks-for-conditional-ios3-ios32.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:eb31e1e828806d3f'
translated: false
---

> 原文：[Tips & Tricks for conditional iOS3, iOS3.2 and iOS4 code | Cocoa with Love](https://www.cocoawithlove.com/2010/07/tips-tricks-for-conditional-ios3-ios32.html)　·　Cocoa with Love (Matt Gallagher)

In this post, I'll show you ways to determine which version of iOS you are running on and show you how to write a macro that can both conditionally compile and runtime switch between the code for different versions of iOS.

## A project or target that supports multiple versions of iOS

To make an application target that runs on multiple versions of iOS is relatively simple:

- Set the "Base SDK" in your projects settings to the _newest_ version number of iOS whose features you may want.
- Set the "iPhone OS Deployment Target" to the _oldest_ version number of iOS that you will support

However, getting the target settings correct is the easy part of the problem. The hard part is using new features on newer iOS versions without breaking the app on older versions.

## Running in the 3.1.3 simulator

Before getting to the actual code, it might be worthwhile to discuss how to run your projects in older versions of the simulator.

The simulator is an important part of iOS development (since it is much faster and simpler than running your code on the device). But Apple have removed SDK versions earlier than 3.2 from the current Xcode builds. This makes it hard to verify your apps on earlier devices unless you install on a physical device.

Support for 3.1.3 is relatively important since it is the last version of iOS supported by the original iPhone and iPod Touch and it will be a few months before iOS 4 exceeds 80% of the remaining iPhone and iPod Touch market.

To allow simulation in 3.1.3, you must install an old version of Xcode. If you are a registered iPhone developer, you can download [Xcode 3.1.4 for Leopard with iPhone SDK 3.1.3](http://developer.apple.com/iphone/download.action?path=/iphone/iphone_sdk_3.1.3__final/iphone_sdk_3.1.3_with_xcode_3.1.4__leopard__9m2809a.dmg) or [Xcode 3.1.4 for Snow Leopard with iPhone SDK 3.1.3](http://developer.apple.com/iphone/download.action?path=/iphone/iphone_sdk_3.1.3__final/iphone_sdk_3.1.3_with_xcode_3.2.1__snow_leopard__10m2003a.dmg). Be careful to install these in a different location to your Xcode 3.2.3 with iOS3.2/iOS4 (either select a different hard disk or rename your existing /Developer directory before you install).

Once you've got an old version of Xcode, you'll want to duplicate your main target and set the Base SDK to 3.1.3 in this duplicate (because it won't exist in this version of Xcode). You should use a second target for this because you shouldn't risk messing with your main target just to run code in the simulator.

## Using features from newer iOS versions while supporting older iOS versions

For example, if you want to start an iOS4 background task in an application that you want to run on earlier versions of iOS, then you'll need to use code like this:

```objc
#if __IPHONE_OS_VERSION_MAX_ALLOWED >= 40000
    if ([[UIApplication sharedApplication]
        respondsToSelector:@selector(beginBackgroundTaskWithExpirationHandler:)])
    {
        UIBackgroundTaskIdentifier bgTask = [[UIApplication sharedApplication]
            beginBackgroundTaskWithExpirationHandler:^{}];

        // Perform work that should be allowed to continue in background

        [[UIApplication sharedApplication] endBackgroundTask:bgTask];
    }
#endif
```

There are three important components:

1. The `#if __IPHONE_OS_VERSION_MAX_ALLOWED >= 40000` compile-time conditional. This ensures that if we choose to build this project with a Base SDK lower than 4.0, then it won't cause compile problems. This is essential for running in older versions of the simulator.
2. The runtime check that ` UIApplication ` supports the ` beginBackgroundTaskWithExpirationHandler ` method. Since the final release build will be built against the 4.0 SDK (even if users install on SDK 3.0) this runtime check ensures that the method we need is available.
3. Everything else between the `#if __IPHONE_OS_VERSION_MAX_ALLOWED >= 40000` and the `#endif` is the iPhone OS 4 code.

## Making the conditional work less ugly

The problem with the previous code is the compile-time conditional and the runtime check for the presence of methods is cumbersome since you must remember to to both.

If you want to integrate both a compile-time check and a runtime check, a better approach would look like this:

```objc
IF_IOS4_OR_GREATER
(
    UIBackgroundTaskIdentifier bgTask = [[UIApplication sharedApplication]
        beginBackgroundTaskWithExpirationHandler:^{}];

    // Perform work that should be allowed to continue in background

    [[UIApplication sharedApplication] endBackgroundTask:bgTask];
);
```

We can implement this macro as follows:

```objc
#ifndef kCFCoreFoundationVersionNumber_iPhoneOS_4_0
#define kCFCoreFoundationVersionNumber_iPhoneOS_4_0 550.32
#endif

#if __IPHONE_OS_VERSION_MAX_ALLOWED >= 40000
#define IF_IOS4_OR_GREATER(...) \
    if (kCFCoreFoundationVersionNumber >= kCFCoreFoundationVersionNumber_iPhoneOS_4_0) \
    { \
        __VA_ARGS__ \
    }
#else
#define IF_IOS4_OR_GREATER(...)
#endif
```

If we want to include something only in OS versions _prior_ to a a specific version, then we don't need the conditional compilation (since we still want the code to appear when compiled in a later version. In this case, only a runtime check is required. You can either do this directly, or for symmetry with other macros, you could use:

```objc
#define IF_PRE_IOS4(...) \
    if (kCFCoreFoundationVersionNumber < kCFCoreFoundationVersionNumber_iPhoneOS_4_0) \
    { \
        __VA_ARGS__ \
    }
```

Three interesting points to note about these macros:

1. I use the `kCFCoreFoundationVersionNumber` to determine the iPhone OS at runtime. There are many examples on the web using `[[UIDevice currentDevice] systemVersion]` but that method requires a string comparison and potentially handling of major and minor numbers within the string components. A single `double` comparison is far more straightforward.
2. I have not used the typical `do { x } while (0)` wrapper around the macro, so you _can_ simply tack an `else` onto the end if you choose (and it doesn't need conditional compilation of its own).
3. I use a variable argument list for the macro. This is so that any number of commas may appear in the contents without causing problems.

A final point... the `kCFCoreFoundationVersionNumber` definitions may not be in every version of the SDK (each SDK normally contains definitions for versions up to but not including itself), so you should conditionally define them yourself in case they're missing. Here's a handy list:

```objc
#ifndef kCFCoreFoundationVersionNumber_iPhoneOS_2_0
#define kCFCoreFoundationVersionNumber_iPhoneOS_2_0 478.23
#endif

#ifndef kCFCoreFoundationVersionNumber_iPhoneOS_2_1
#define kCFCoreFoundationVersionNumber_iPhoneOS_2_1 478.26
#endif

#ifndef kCFCoreFoundationVersionNumber_iPhoneOS_2_2
#define kCFCoreFoundationVersionNumber_iPhoneOS_2_2 478.29
#endif

#ifndef kCFCoreFoundationVersionNumber_iPhoneOS_3_0
#define kCFCoreFoundationVersionNumber_iPhoneOS_3_0 478.47
#endif

#ifndef kCFCoreFoundationVersionNumber_iPhoneOS_3_1
#define kCFCoreFoundationVersionNumber_iPhoneOS_3_1 478.52
#endif

#ifndef kCFCoreFoundationVersionNumber_iPhoneOS_3_2
#define kCFCoreFoundationVersionNumber_iPhoneOS_3_2 478.61
#endif

#ifndef kCFCoreFoundationVersionNumber_iPhoneOS_4_0
#define kCFCoreFoundationVersionNumber_iPhoneOS_4_0 550.32
#endif
```

## Better still: solutions that don't require macros

Better than a simple macro is a simple function. This is a valid solution where the contents of your conditional code does not itself contain OS specific code (only the condition itself requires OS specific logic).

A common example is handing separate layout for iPad and iPhone versions. Ordinarily, if you're compiling for iPad 3.2 and iPhone 3.1.3, you need the following code:

```objc
#if __IPHONE_OS_VERSION_MAX_ALLOWED >= 30200
    if ([[UIDevice currentDevice] respondsToSelector:@selector(userInterfaceIdiom)] &&
        [[UIDevice currentDevice] userInterfaceIdiom] == UIUserInterfaceIdiomPad)
    {
        // iPad specific layout changes
    }
    else
#endif
    {
        // iPhone layout
    }
```

You can handle this with a conditional macro like the `IF_IOS4_OR_GREATER` but a far better solution is:

```objc
if (isIPad())
{
    // iPad specific layout changes
}
else
{
    // iPhone layout
}
```

Where all the conditional pollution is tidily kept in your `isIPad()` function:

```objc
BOOL isIPad()
{
    IF_3_2_OR_GREATER
    (
        if ([[UIDevice currentDevice] userInterfaceIdiom] == UIUserInterfaceIdiomPad)
        {
            return YES;
        }
    );
    
    return NO;
}
```

## Conclusion

Apple doesn't exactly make it easy to support old versions of the iPhone SDK. I'm sure they want everyone to keep up to date or buy new devices if their current device can't be updated.

That's not always a realistic attitude for App Store developers. You can't expect all your customers to upgrade as soon as possible.

The important point when writing for multiple versions of the SDK is to keep as few conditionals as possible. You don't want to have thousands of conditionals in your code for supporting different versions. Every conditional is extra testing work since different behaviors must be fully exercised on all different platforms.

While the conditionals and functions I've talked about here will help, if you find yourself needing a lot of conditionals you may also want to consider design changes like instantiating different subclasses for different OS versions.
