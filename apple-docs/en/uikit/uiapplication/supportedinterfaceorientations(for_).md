---
title: 'supportedInterfaceOrientations(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+（27.0 起废弃）, iPadOS 6.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplication/supportedinterfaceorientations(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/supportedinterfaceorientations(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/supportedinterfaceorientations%28for%3A%29.json'
content_hash: 'sha256:afa5e3a313eab6df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# supportedInterfaceOrientations(for:)

<sub>Instance Method</sub>

Returns the default set of interface orientations to use for the view controllers in the specified window.

> [!warning] Deprecated
> Use [- supportedInterfaceOrientationsForWindowScene:](<../uiwindowscenedelegate/supportedinterfaceorientations(for_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func supportedInterfaceOrientations(for window: UIWindow?) -> UIInterfaceOrientationMask
```

## Parameters

- `window` — The window whose default interface orientations you want to retrieve.

## Return Value

A bit mask specifying which orientations are supported. See [UIInterfaceOrientationMask](../uiinterfaceorientationmask.md) for valid bit-mask values. The value returned by this method must not be `0`.

## Discussion

Starting in iOS 8, you should employ the [UITraitCollection](../uitraitcollection.md) and [UITraitEnvironment](../uitraitenvironment.md) APIs, and size class properties as used in those APIs, instead of using this method or otherwise writing your app in terms of interface orientation.

This method returns the default interface orientations for the app. These orientations are used only for view controllers that do not specify their own. If your app delegate implements the [- application:supportedInterfaceOrientationsForWindow:](<../uiapplicationdelegate/application(__supportedinterfaceorientationsfor_).md>) method, the system does not call this method.

The default implementation of this method returns the app’s default set of supported interface orientations, as you define them in the [UISupportedInterfaceOrientations](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW10) key of the `Info.plist` file in your Xcode project. If the file does not contain that key, this method returns all interface orientations for the iPad idiom and returns all interface orientations except the portrait upside-down orientation for the iPhone idiom.
