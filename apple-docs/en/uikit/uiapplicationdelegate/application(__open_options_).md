---
title: 'application(_:open:options:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（26.0 起废弃）, iPadOS 9.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:open:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:open:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Aopen%3Aoptions%3A%29.json'
content_hash: 'sha256:e5717b58383dd6cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:open:options:)

<sub>Instance Method</sub>

Asks the delegate to open a resource specified by a URL, and provides a dictionary of launch options.

> [!warning] Deprecated
> Use UIScene lifecycle and scene(_:openURLContexts:) from UISceneDelegate instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool
```

## Parameters

- `app` — Your singleton app object.

- `url` — The URL resource to open. This resource can be a network resource or a file. For information about the Apple-registered URL schemes, see [Apple URL Scheme Reference](https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007899).

- `options` — A dictionary of URL handling options. For information about the possible keys in this dictionary and how to handle them, see `UIApplicationOpenURLOptionsKey`. By default, the value of this parameter is an empty dictionary.

## Return Value

[true](../../swift/true.md) if the delegate successfully handled the request or [false](../../swift/false.md) if the attempt to open the URL resource failed.

## Discussion

This method is not called if your implementations return [false](../../swift/false.md) from both the [- application:willFinishLaunchingWithOptions:](<application(__willfinishlaunchingwithoptions_).md>) and [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) methods. (If only one of the two methods is implemented, its return value determines whether this method is called.) If your app implements the [- applicationDidFinishLaunching:](<applicationdidfinishlaunching(__).md>) method instead of [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>), this method is called to open the specified URL after the app has been initialized.

If a URL arrives while your app is suspended or running in the background, the system moves your app to the foreground prior to calling this method.

There is no equivalent notification for this delegation method.

## See Also

### Opening a URL-specified resource

- [OpenURLOptionsKey](../uiapplication/openurloptionskey.md) — Keys you use to access values in the options dictionary when opening a URL. _(deprecated)_
