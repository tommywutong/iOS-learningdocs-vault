---
title: 'cancelRequest(withError:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsextensioncontext/cancelrequest(witherror:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsextensioncontext/cancelrequest(witherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensioncontext/cancelrequest%28witherror%3A%29.json'
content_hash: 'sha256:244b243f5c55e46e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionContext](../nsextensioncontext.md)

# cancelRequest(withError:)

<sub>Instance Method</sub>

Tells the host app to cancel the app extension request, with a supplied error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancelRequest(withError error: any Error)
```

## Parameters

- `error` — The error object to return. It must be non-`nil`.

## Discussion

On return, the `userInfo` dictionary of the [NSError](../nserror.md) object contains a key named [NSExtensionItemsAndErrorsKey](../nsextensionitemsanderrorskey.md) which has as its value a dictionary of [NSExtensionItem](../nsextensionitem.md) objects and associated [NSError](../nserror.md) instances.

## See Also

### Related Documentation

- [App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214)

### Handling requests

- [- completeRequestReturningItems:completionHandler:](<completerequest(returningitems_completionhandler_).md>) — Tells the host app to complete the app extension request with an array of result items.
- [NSExtensionItemsAndErrorsKey](../nsextensionitemsanderrorskey.md) — The extension items and errors key.
