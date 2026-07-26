---
title: primaryPresentedItemURL
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilepresenter/primarypresenteditemurl
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/primarypresenteditemurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/primarypresenteditemurl.json'
content_hash: 'sha256:cb00a828023e1032'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# primaryPresentedItemURL

<sub>Instance Property</sub>

The URL of a secondary item’s primary presented file or directory.

<sub>macOS</sub>

```swift
optional var primaryPresentedItemURL: URL? { get }
```

## Discussion

This property supports App Sandbox in macOS.

Some apps require access to secondary files or directories with names that are related to the primary, user-selected file. For example, a subtitle file, by convention, has the same name as its corresponding movie file, but with a different filename extension. If a movie player is sandboxed, an [NSOpenPanel](../../appkit/nsopenpanel.md) object will grant access only to the user-selected movie file (the primary item) and not its associated subtitle file (the secondary item).

To gain access to a secondary item, first register an [NSFilePresenter](../nsfilepresenter.md) object for it. At any point in its existence, a secondary item must be able to return an [NSURL](../nsurl.md) object to its primary item. This is done by using this property.  When done accessing the secondary item, unregister the file presenter object.

## See Also

### Accessing File Presenter Attributes

- [presentedItemURL](presenteditemurl.md) — The URL of the presented file or directory.
- [presentedItemOperationQueue](presenteditemoperationqueue.md) — The operation queue in which to execute presenter-related messages.
