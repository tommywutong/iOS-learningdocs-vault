---
title: What's New in macOS
apple_id: TP40001812
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/WhatsNewInOSX/Articles/macOSSierra10.12.html
archived_at: '2026-07-18T02:58:54.987704Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [What's New in macOS](Introduction.md)


[Next](macOS%20Sierra%2010.12.md)[Previous](macOS%2010.13.md)

# macOS Sierra 10.12.1

This article summarizes the key technology changes and improvements in macOS 10.12.1. The information about these changes is organized into sections by technology area.

Please file any bug reports about this release or this documentation at [http://bugreport.apple.com/](http://bugreport.apple.com/).

macOS 10.12.1 contains enhancements related to new hardware capabilities and the MediaPlayer API.

The Touch Bar, a multi-touch retina display at the top of the MacBook Pro keyboard that replaces the function row, changes depending on what users are doing in your app, allowing you to surface context-specific features, tools, actions, and controls.

Apps can take advantage of the Touch Bar to make everything from content browsing to formatting easier. For example, your app can add:

- Toolbars: context-sensitive toolbars that augment the keyboard
- Inspectors: Secondary display of inspector panels
- Sliders: select and adjust colors, gradients, styles and widths
- Media controls and scrubbers
- Action Buttons
- Custom items for your app
- Customization: Your users can customize what appears in the Touch Bar for your app. You can allow them to add the buttons, controls and tools they use most right into the keyboard for easy access.

Adoption is accomplished using AppKit objects, controllers, controls, and responders. Developers adopting the Touch Bar in their apps will find an extension of the concepts that power `NSToolbar`.

Touch Bar items are similar to AppKit items your app may already have, such as buttons, pickers, popovers, sliders, and custom items for your app. There is also a new control, `NSScrubber`, which provides scrub and wheel selection behavior controlled by taps and horizontal pan gestures.

The new MacBook Pro has Touch ID, which allows users to securely and easily log in to their Macs, purchase items from the iTunes, iBooks, and App Stores with a touch, and authenticate Apple Pay purchases in Safari. Third-party apps can adopt Touch ID so users can unlock features with the same security and convenience.

You add Touch ID support to your app using the same APIs used for Touch ID support on iOS.

The MediaPlayer API is now available on macOS, providing universal remote control support. This is the same API used on iOS, so your app can interact with media controls in Control Center, the Lock Screen, CarPlay, bluetooth devices, and others.

By adopting this API, your app will appear in the Touch Bar Now Playing UI, and will work with new wireless accessories, such as AirPods.

The MediaPlayer API on Mac is identical to the iOS API, except for one additional task you need to implement so that the correct playback state is conveyed throughout the system. Because there is no central media server on macOS like there is on iOS, you need to report your playback state every time the state changes (for example, when playback pauses). This API is part of `MPNowPlayingInfoCenter`:

```objc
/// The current playback state of the app.
/// This only applies on macOS, where playback state cannot be determined by
/// the application's audio session. This property must be set every time
/// the app begins or halts playback, otherwise remote control functionality may
/// not work as expected.
@property (assign) MPNowPlayingPlaybackState playbackState NS_AVAILABLE_MAC(10_12_1);
```

You can test that your adoption of the API is working by interacting with the Now Playing Touch UI located in the Touch Bar system tray.

The Now Playing UI will appear if any media apps are playing content in the background. This button will disappear after an app has not been playing any media for eight minutes.

[Next](macOS%20Sierra%2010.12.md)[Previous](macOS%2010.13.md)

