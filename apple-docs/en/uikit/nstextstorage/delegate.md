---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextstorage/delegate
source_url: 'https://developer.apple.com/documentation/uikit/nstextstorage/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstorage/delegate.json'
content_hash: 'sha256:9c85b0d9808b0a7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextStorage](../nstextstorage.md)

# delegate

<sub>Instance Property</sub>

The delegate for the text storage object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any NSTextStorageDelegate)? { get set }
```

## Discussion

Use a delegate object to monitor edits occurring to the text contents. Your delegate object must conform to the [NSTextStorageDelegate](../nstextstoragedelegate.md) protocol.

## See Also

### Processing the editing actions

- [NSTextStorageDelegate](../nstextstoragedelegate.md) — The optional methods that delegates of text storage objects implement to handle text-edit processing.
