---
title: 'performEditingTransaction(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextcontentmanager/performeditingtransaction(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentmanager/performeditingtransaction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentmanager/performeditingtransaction%28_%3A%29.json'
content_hash: 'sha256:f032bd2f98b2a50e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentManager](../nstextcontentmanager.md)

# performEditingTransaction(_:)

<sub>Instance Method</sub>

Performs an editing transaction and invokes a block upon completion.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func performEditingTransaction(_ transaction: () -> Void)
```

## Parameters

- `transaction` — The editing transaction.

## Discussion

The primary [NSTextLayoutManager](../nstextlayoutmanager.md) controlling the active editing transaction invokes this method. It’s possible to nest multiple editing transactions. The outer most transaction toggles `hasEditingTransaction` and sends synchronization messages if enabled after invoking a transaction.

## See Also

### Performing transactions

- [hasEditingTransaction](haseditingtransaction.md) — Indicates there’s an active editing transaction from the primary text layout manager.
- [- recordEditActionInRange:newTextRange:](<recordeditaction(in_newtextrange_).md>) — Records information about an edit action to the transaction.
