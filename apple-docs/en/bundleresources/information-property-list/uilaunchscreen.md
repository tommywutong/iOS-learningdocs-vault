---
title: UILaunchScreen
framework: Bundle Resources
symbol_kind: dictionary
role: symbol
role_heading: Property List Key
platforms: [iOS 14.0+, iPadOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/information-property-list/uilaunchscreen
source_url: 'https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchscreen'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/information-property-list/uilaunchscreen.json'
content_hash: 'sha256:154eb0c9d94e1a2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Information Property List](../information-property-list.md)

# UILaunchScreen

<sub>Property List Key</sub>

The user interface to show while an app launches.

## Discussion

You use this key to define the launch screen that the system displays while your app launches. If you need to provide different launch screens in response to being launched by different URL schemes, use [UILaunchScreens](uilaunchscreens.md) instead.

> [!note] Note
> Use this key to configure the user interface during app launch in a way that doesn’t rely on storyboards. If you prefer to use storyboards, use [UILaunchStoryboardName](uilaunchstoryboardname.md) instead.

## Topics

### Main Interface

- [UIColorName](uilaunchscreen/uicolorname.md) — The name of a color to use as the background color on the launch screen.
- [UIImageName](uilaunchscreen/uiimagename.md) — The name of an image to display during app launch.
- [UIImageRespectsSafeAreaInsets](uilaunchscreen/uiimagerespectssafeareainsets.md) — A Boolean that specifies whether the launch image should respect the safe area insets.

### Border Elements

- [UINavigationBar](uilaunchscreen/uinavigationbar.md) — Navigation bar visibility and configuration during launch.
- [UITabBar](uilaunchscreen/uitabbar.md) — Tab bar visibility and configuration during launch.
- [UIToolbar](uilaunchscreen/uitoolbar.md) — Toolbar visibility and configuration during launch.

## See Also

### Launch interface

- [UILaunchScreens](uilaunchscreens.md) — The user interfaces to show while an app launches in response to different URL schemes.
- [UILaunchStoryboardName](uilaunchstoryboardname.md) — The filename of the storyboard from which to generate the app’s launch image.
- [UILaunchStoryboards](uilaunchstoryboards.md) — The launch storyboard to use to generate a launch image when your app opens from a supported scheme.
- [LSUIPresentationMode](lsuipresentationmode.md) — The initial user-interface mode for the app.
- [UILaunchToFullScreenByDefaultOnMac](uilaunchtofullscreenbydefaultonmac.md) — A Boolean value that indicates whether to launch your iPad app in full-screen mode when running on a Mac.
