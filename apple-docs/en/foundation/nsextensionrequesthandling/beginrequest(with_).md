---
title: 'beginRequest(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsextensionrequesthandling/beginrequest(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsextensionrequesthandling/beginrequest(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensionrequesthandling/beginrequest%28with%3A%29.json'
content_hash: 'sha256:d634f087b80901c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionRequestHandling](../nsextensionrequesthandling.md)

# beginRequest(with:)

<sub>Instance Method</sub>

Tells the extension to prepare for a host app’s request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func beginRequest(with context: NSExtensionContext)
```

## Parameters

- `context` — An [NSExtensionContext](../nsextensioncontext.md) object that represents the context in which the host app makes the request. Typically, the context contains data that the extension can work on.

## Discussion

An extension prepares for a host app’s request by getting the context passed in this method and requesting related data items, if appropriate. This method is received after the extension is initialized, but before the principal object is asked to do anything with the context. For example, if the principal object is a view controller, it receives this message before [loadView()](<../../uikit/uiviewcontroller/loadview().md>) is called. After an extension receives this message, the [extensionContext](../../uikit/uiviewcontroller/extensioncontext.md) property of the view controller returns a non`nil` value.

If your subclass conforms to this protocol and overrides `beginRequestWithExtensionContext:`, the subclass is expected to call `[super beginRequestWithExtensionContext:]`.

## See Also

### Related Documentation

- [App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214)
