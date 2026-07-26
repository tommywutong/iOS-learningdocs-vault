---
title: 'stringByEvaluatingJavaScript(from:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiwebview/stringbyevaluatingjavascript(from:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/stringbyevaluatingjavascript(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/stringbyevaluatingjavascript%28from%3A%29.json'
content_hash: 'sha256:5811aca695e69cf8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# stringByEvaluatingJavaScript(from:)

<sub>Instance Method</sub>

Returns the result of running a JavaScript script.

> [!warning] Deprecated
> For more information, see [UIWebView](../uiwebview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func stringByEvaluatingJavaScript(from script: String) -> String?
```

## Parameters

- `script` — The JavaScript script to run.

## Return Value

The result of running the JavaScript script passed in the `script` parameter, or `nil` if the script fails.

## Discussion

New apps should instead use the [evaluateJavaScript(_:completionHandler:)](<../../webkit/wkwebview/evaluatejavascript(__completionhandler_).md>) method from the [WKWebView](../../webkit/wkwebview.md) class. Legacy apps should adopt that method if possible.

> [!important] Important
> The [- stringByEvaluatingJavaScriptFromString:](<stringbyevaluatingjavascript(from_).md>) method waits synchronously for JavaScript evaluation to complete. If you load web content whose JavaScript code you have not vetted, invoking this method could hang your app. Best practice is to adopt the [WKWebView](../../webkit/wkwebview.md) class and use its [evaluateJavaScript(_:completionHandler:)](<../../webkit/wkwebview/evaluatejavascript(__completionhandler_).md>) method instead.
