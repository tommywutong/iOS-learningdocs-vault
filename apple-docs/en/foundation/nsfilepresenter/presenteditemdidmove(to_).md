---
title: 'presentedItemDidMove(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilepresenter/presenteditemdidmove(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/presenteditemdidmove(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/presenteditemdidmove%28to%3A%29.json'
content_hash: 'sha256:065278859cfa556a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# presentedItemDidMove(to:)

<sub>Instance Method</sub>

Tells your object that the presented item moved or was renamed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func presentedItemDidMove(to newURL: URL)
```

## Parameters

- `newURL` — The URL containing the new path to the presented item.

## Discussion

Use this method to update the value returned by the [presentedItemURL](presenteditemurl.md) property of your object.

## See Also

### Related Documentation

- [presentedItemURL](presenteditemurl.md) — The URL of the presented file or directory.

### Handling Changes to Files

- [- savePresentedItemChangesWithCompletionHandler:](<savepresenteditemchanges(completionhandler_).md>) — Tells your object to save any unsaved changes for the presented item.
- [- accommodatePresentedItemDeletionWithCompletionHandler:](<accommodatepresenteditemdeletion(completionhandler_).md>) — Tells your object that its presented item is about to be deleted.
- [- presentedItemDidChange](<presenteditemdidchange().md>) — Tells your object that the presented item’s contents or attributes changed.
