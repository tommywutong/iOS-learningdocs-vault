---
title: 'completeRequest(returningItems:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsextensioncontext/completerequest(returningitems:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsextensioncontext/completerequest(returningitems:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensioncontext/completerequest%28returningitems%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:faa0b34a3293fe29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionContext](../nsextensioncontext.md)

# completeRequest(returningItems:completionHandler:)

<sub>Instance Method</sub>

Tells the host app to complete the app extension request with an array of result items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func completeRequest(returningItems items: [Any]?, completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

## Parameters

- `items` — An array of result items, each an [NSExtensionItem](../nsextensionitem.md) object, to return to the host app.

- `completionHandler` — An optional block to be called when the request completes, performed as a background priority task. The block takes the following parameter: - **expired** — A Boolean value that indicates whether the system is terminating a previous invocation of the `completionHandler` block. This parameter is [true](../../swift/true.md) when the system prematurely terminates a `completionHandler` block that was previously invoked and had not otherwise expired. > [!important] Important > If the system calls your block with an `expired` value of [true](../../swift/true.md), you must immediately suspend your app extension. If you fail to do this, the system terminates your extension’s process. > > When your app extension exits, all concurrent requests being handled by the extension, serving the same or other host apps, are terminated.

## Discussion

Calling this method eventually dismisses the app extension’s view controller.

## See Also

### Handling requests

- [- cancelRequestWithError:](<cancelrequest(witherror_).md>) — Tells the host app to cancel the app extension request, with a supplied error.
- [NSExtensionItemsAndErrorsKey](../nsextensionitemsanderrorskey.md) — The extension items and errors key.
