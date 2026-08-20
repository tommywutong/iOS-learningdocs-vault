---
title: Kiosk Mode Programming Topic
apple_id: TP40009080
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/technotes/KioskMode/Introduction/Introduction.html
archived_at: '2026-07-26T19:54:16.202025Z'
---
> 导航：[总目录](../../README.md) · [technotes](../../_indexes/technotes.md)



# Kiosk Mode Technical Note

Kiosk mode is a system-software and user-interface feature that is ideal for computer games and kiosk-style applications. It is useful when you want the user interface elements of the system to behave in custom ways when your application is active—that is, when you want a different user experience from the one that the system user interface normally offers. These customizable features include the dock, menu bar, and task switcher. In addition, with kiosk mode your customized application can observe changes in UI behavior that are made by other active applications

In OS X v10.6 and later, the [NSApplication](https://developer.apple.com/documentation/appkit/nsapplication) class supports this customization. It also serves as a replacement for the Carbon `SystemUIMode` API available in OS X v10.5 and earlier.

The main goal of kiosk mode is to lock the user into a particular application, either to allow a game to take over the entire screen (in computer game applications) or to prevent uusers at a computer from opening applications that should not be accessible to them (in a kiosk-style application).

This technical note covers several useful techniques that can be used by kiosk developers, outlines the numerous options for kiosk mode, and provides advice on how and when to successfully implement its many features.

## Features of the API

Kiosk mode lets you control the user experience by manipulating numerous system user interface elements from within your application. For example:

- You can decide whether you want users to the see the Dock and menu bar and whether the Apple menu is active.
- You can disable activities that take users out of your application, such as process switching, the Force Quit window, hiding the application, and Exposé
- You can prevent users from restarting or powering down the computer

### Choosing the Features

A set of options exists for customizing the user experience through the `NSApplication` class by using a new bitmask, `NSApplicationPresentationOptions` (this set of options serves as a replacement for the Carbon interface SystemUIMode that is available in OS X v10.5 and earlier).

The flags that comprise an application’s presentation options are as follows:

|  |  |
| --- | --- |
| __Flag__ | __Description__ |
| `NSApplicationPresentationDefault` | Default settings. No special behavior. |
| `NSApplicationPresentationAutoHideDock` | Dock appears when moused to. Spotlight menu is disabled. |
| `NSApplicationPresentationHideDock` | Dock is entirely unavailable. Spotlight menu is disabled. |
| `NSApplicationPresentationAutoHideMenuBar` | Menu Bar appears when moused to. |
| `NSApplicationPresentationHideMenuBar` | Menu Bar is entirely unavailable. |
| `NSApplicationPresentationDisableAppleMenu` | All Apple menu items are disabled. |
| `NSApplicationPresentationDisableProcessSwitching` | Cmd+Tab UI is disabled. All Exposé functionality is also disabled. |
| `NSApplicationPresentationDisableForceQuit` | Cmd+Opt+Esc panel is disabled. |
| `NSApplicationPresentationDisableSessionTermination` | PowerKey panel and Restart/Shut Down/Log Out are disabled. |
| `NSApplicationPresentationDisableHideApplication` | Application "Hide" menu item is disabled. |
| `NSApplicationPresentationDisableMenuBarTransparency` | The transparent appearance of the menu bar is disabled. |

### Getting and Setting the Features

There are a few main methods that are used for getting or setting the presentation options. The [setPresentationOptions:](https://developer.apple.com/documentation/appkit/nsapplication/1428664-presentationoptions) method sets the application’s presentation options to the specified value. When using this method, it is important to note that only certain combinations of `NSApplicationPresentationOptions` flags are allowed, as detailed in the following section, and that when given an invalid combination of option flags, this method raises an exception.

For example, in the main controller file of a simple window based application, the following code snippet in the `awakeFromNib` method hides the dock and menu bar upon your application’s launch:

```objc
-(void) awakeFromNib {
     @try {
          NSApplicationPresentationOptions options = NSApplicationPresentationHideDock + NSApplicationPresentationHideMenuBar;
          [NSApp setPresentationOptions:options];
     }
     @catch(NSException * exception) {
          NSLog(@"Error.  Make sure you have a valid combination of options.");
     }
}
```

__Note:__ You should always set the `presentationOptions` in a try/catch statement to ensure that your program does not crash from an invalid combination of options. The guidelines for valid combinations are discussed in the following section.

The `presentationOptions` method returns the set of application presentation options for that current application. The `currentSystemPresentationOptions` method returns the set of application presentation options that are currently in effect for the system. These are the presentations options that have been put into effect by the currently active application.

For most applications, the initial value of `presentationOptions` is `NSApplicationPresentationDefault`. If an application’s `Info.plist` file specifies a value for the LSUIElement key, as described in _[Creating Kiosks](../Creating%20Kiosks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzga)_, the application’s `presentationOptions` is initialized to an equivalent combination of `NSApplicationPresentationOptions` flags instead.

## Valid Combinations of Settings

When you combine settings, or option flags, to pass to the `setPresentationOptions:` method, you must do so in a way that satisfies the following requirements:

- `NSApplicationPresentationAutoHideDock` and `NSApplicationPresentationHideDock` are mutually exclusive: You may specify one or the other, but not both.
- `NSApplicationPresentationAutoHideMenuBar` and `NSApplicationPresentationHideMenuBar` are mutually exclusive: You may specify one or the other, but not both.
- If you specify `NSApplicationPresentationHideMenuBar`, it must be accompanied by `NSApplicationPresentationHideDock`. If you specify `NSApplicationPresentationAutoHideMenuBar`, it must be accompanied by either `NSApplicationPresentationHideDock` or `NSApplicationPresentationAutoHideDock`.
- If you specify any of `NSApplicationPresentationDisableProcessSwitching`, `NSApplicationPresentationDisableForceQuit`, `NSApplicationPresentationDisableSessionTermination`, or `NSApplicationPresentationDisableMenuBarTransparency`, it must be accompanied by either `NSApplicationPresentationHideDock` or `NSApplicationPresentationAutoHideDock`.

When the `setPresentationOptions:` method receives a `newOptions` parameter that does not conform to these requirements, it raises an exception (`NSInvalidArgumentException`).

## Key-Value Observing Compliance

Both `presentationOptions` and `currentSystemPresentationOptions` are key-value observing (KVO) compliant. A client that observes `currentSystemPresentationOptions` receives notifications if the following events occur:

1. The client is the active application and makes a change itself using the `setPresentationOptions:` method.
2. Another application is active and makes its own changes.
3. Making a different application active causes the active set of presentation options to change.

__Note:__ If a different application becomes active and has the same set of presentation options as the application that was previously active, no notification is sent.

For more information about KVO compliance, see _[Key-Value Observing Programming Guide](../../documentation/Cocoa/Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)_.

## Full-Screen Mode Compatibility

In OS X v10.6 and later, you can use an instance of the [NSView](https://developer.apple.com/documentation/appkit/nsview) class in full-screen mode and retain the kiosk mode functionality. The [enterFullScreenMode:withOptions:](https://developer.apple.com/documentation/appkit/nsview/1483780-enterfullscreenmode) method accepts a new option, whose key-value pair specifies the kiosk mode options to use while the view is operating in full-screen mode. The new key is the string `NSFullScreenModeApplicationPresentationOptions`. It’s value must be of type `NSApplicationPresentationOptions`.

When the options dictionary you pass to `enterFullScreenMode:withOptions:` does not contain a value for `NSFullScreenModeApplicationPresentationOptions`, AppKit does not alter the presentation options that were previously in effect before taking the view full-screen. AppKit also captures either the destination screen, or, if you specify `YES` for `NSFullScreenModeAllScreens`, all attached screens.

In OS X v10.6 and later, you can put a windowless view in full-screen mode. This means that the `enterFullScreenMode:withOptions:` method can be sent to a view for which `[view window] == nil`.

__Note:__ On OS X v10.5, calling the `enterFullScreenMode:withOptions:` method on a windowless view raises an exception. You can work around this by placing the view in an offscreen dummy window.

When the options dictionary you pass to `enterFullScreenMode:withOptions:` does contain a value for `NSFullScreenModeApplicationPresentationOptions`, AppKit does not capture any displays, because doing so would prevent the showing of `presentationOptions`-controlled UI elements such as the menu bar and Dock. AppKit puts the requested `NSApplicationPresentationOptions` value into effect when switching the view into full-screen mode, and restores the previously active `NSApplication` presentationOptions setting when the view exits from full-screen mode via the [exitFullScreenModeWithOptions:](https://developer.apple.com/documentation/appkit/nsview/1483256-exitfullscreenmode) method.
