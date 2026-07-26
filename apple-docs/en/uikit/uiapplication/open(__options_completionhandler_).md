---
title: 'open(_:options:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplication/open(_:options:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/open(_:options:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/open%28_%3Aoptions%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:c2fc0fd61ad9ca86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# open(_:options:completionHandler:)

<sub>Instance Method</sub>

Attempts to asynchronously open the resource at the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func open(_ url: URL, options: [UIApplication.OpenExternalURLOptionsKey : Any] = [:], completionHandler completion: (@MainActor @Sendable (Bool) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func open(_ url: URL, options: [UIApplication.OpenExternalURLOptionsKey : Any] = [:]) async -> Bool
```

## Parameters

- `url` — A URL (Universal Resource Locator). The resource identified by this URL may be local to the current app or it may be one that must be provided by a different app. UIKit supports many common schemes, including the `http`, `https`, `tel`, `facetime`, and `mailto` schemes. You can also employ custom URL schemes associated with apps installed on the device.

- `options` — A dictionary of options to use when opening the URL. For a list of possible keys to include in this dictionary, see [OpenExternalURLOptionsKey](openexternalurloptionskey.md).

- `completion` — The block to execute with the results. Provide a value for this parameter if you want to be informed of the success or failure of opening the URL. This block is executed asynchronously on your app’s main thread. The block has no return value and takes the following parameter: - **success** — A Boolean value that indicates whether the URL was opened successfully.

## Discussion

Use this method to open the specified resource. If the specified URL scheme is handled by another app, iOS launches that app and passes the URL to it. (Launching the app brings the other app to the foreground.)  If no app is capable of handling the specified scheme, the completion handler is called with the _success_ parameter set to [false](../../swift/false.md).

To determine whether an app is installed that is capable of handling the URL, call the [- canOpenURL:](<canopenurl(__).md>) method before calling this one. Be sure to read the description of that method for an important note about registering the schemes you want to employ.

## See Also

### Opening a URL resource

- [- canOpenURL:](<canopenurl(__).md>) — Returns a Boolean value that indicates whether an app is available to handle a URL scheme. _(deprecated)_
- [OpenExternalURLOptionsKey](openexternalurloptionskey.md) — Options for opening a URL.
