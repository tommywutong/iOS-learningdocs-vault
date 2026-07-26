---
title: UILaunchScreens
framework: Bundle Resources
symbol_kind: dictionary
role: symbol
role_heading: Property List Key
platforms: [iOS 14.0+, iPadOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/information-property-list/uilaunchscreens
source_url: 'https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchscreens'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/information-property-list/uilaunchscreens.json'
content_hash: 'sha256:e577fcaacff0cdc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Information Property List](../information-property-list.md)

# UILaunchScreens

<sub>Property List Key</sub>

The user interfaces to show while an app launches in response to different URL schemes.

## Discussion

You use this key if your app supports launching in response to one or more URL schemes, and if you want to provide different launch screens for different launch triggers. If you need only one launch screen, use [UILaunchScreen](uilaunchscreen.md) instead.

To define launch screens, create an array of dictionaries, each similar to the one you might provide for [UILaunchScreen](uilaunchscreen.md), but with an added [UILaunchScreenIdentifier](uilaunchscreens/uilaunchscreendefinitions/uilaunchscreenidentifier.md) key that uniquely identifies the screen. Store the array as the value for the [UILaunchScreenDefinitions](uilaunchscreens/uilaunchscreendefinitions.md) key.

To map from URL schemes to a launch screens, create a dictionary of schemes and identifiers, and store it as the value for the [UIURLToLaunchScreenAssociations](uilaunchscreens/uiurltolaunchscreenassociations.md) key. Additionally, indicate a default launch screen by setting a value for the [UIDefaultLaunchScreen](uilaunchscreens/uidefaultlaunchscreen.md) key.

> [!note] Note
> Use this key to configure the user interface during app launch in a way that doesn’t rely on storyboards. If you prefer to use storyboards to define the launch screen, use the [UILaunchStoryboards](uilaunchstoryboards.md) key instead.

## Topics

### Launch Screen Definitions

- [UILaunchScreenDefinitions](uilaunchscreens/uilaunchscreendefinitions.md) — A collection of launch screen configuration dictionaries.

### Associations

- [UIURLToLaunchScreenAssociations](uilaunchscreens/uiurltolaunchscreenassociations.md) — The mapping of URL schemes to launch screen configurations.
- [UIDefaultLaunchScreen](uilaunchscreens/uidefaultlaunchscreen.md) — The default launch screen configuration.

## See Also

### Launch interface

- [UILaunchScreen](uilaunchscreen.md) — The user interface to show while an app launches.
- [UILaunchStoryboardName](uilaunchstoryboardname.md) — The filename of the storyboard from which to generate the app’s launch image.
- [UILaunchStoryboards](uilaunchstoryboards.md) — The launch storyboard to use to generate a launch image when your app opens from a supported scheme.
- [LSUIPresentationMode](lsuipresentationmode.md) — The initial user-interface mode for the app.
- [UILaunchToFullScreenByDefaultOnMac](uilaunchtofullscreenbydefaultonmac.md) — A Boolean value that indicates whether to launch your iPad app in full-screen mode when running on a Mac.
