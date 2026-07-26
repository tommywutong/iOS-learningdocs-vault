---
title: 'open(_:options:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscene/open(_:options:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/open(_:options:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/open%28_%3Aoptions%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:364510a5f3670cbe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# open(_:options:completionHandler:)

<sub>Instance Method</sub>

Attempts to open the resource at the specified URL asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func open(_ url: URL, options: UIScene.OpenExternalURLOptions?, completionHandler completion: ((Bool) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func open(_ url: URL, options: UIScene.OpenExternalURLOptions?) async -> Bool
```

## Parameters

- `url` — A URL (Universal Resource Locator). The resource identified by this URL may be local to the current app or handled by a different app. UIKit supports many common schemes, including the `http`, `https`, `tel`, `facetime`, and `mailto` schemes.

- `options` — The options to use when opening the URL.

- `completion` — The block to execute with the results. Provide a value for this parameter if you want to be informed of the success or failure of opening the URL. This block is executed asynchronously on your app’s main thread. The block has no return value and takes the following parameter: - **success** — A Boolean value indicating whether the system successfully opened the URL. If no app is capable of handling the specified URL, this parameter is [false](../../swift/false.md).

## Discussion

Use this method to open the specified resource. If the specified URL scheme is handled by another app, iOS launches that app and passes the URL to it. Launching the app brings the other app to the foreground.

## See Also

### Opening URLs

- [OpenExternalURLOptions](openexternalurloptions.md) — Options you specify when asking a scene to open a URL.
