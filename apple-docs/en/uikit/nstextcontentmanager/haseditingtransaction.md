---
title: hasEditingTransaction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontentmanager/haseditingtransaction
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentmanager/haseditingtransaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentmanager/haseditingtransaction.json'
content_hash: 'sha256:3e85c666e13da90f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentManager](../nstextcontentmanager.md)

# hasEditingTransaction

<sub>Instance Property</sub>

Indicates there’s an active editing transaction from the primary text layout manager.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var hasEditingTransaction: Bool { get }
```

## Discussion

When this property is `true`, there’s an active editing transaction from the `primaryTextLayoutManager`. The synchronization operations to nonprimary text layout managers and the backing store block (or fail when synchronous) while this property is `true`. Avoid accessing the elements from a nonprimary text layout manager while this values is `true`.

This property is KVO-compliant.

## See Also

### Performing transactions

- [- performEditingTransactionUsingBlock:](<performeditingtransaction(__).md>) — Performs an editing transaction and invokes a block upon completion.
- [- recordEditActionInRange:newTextRange:](<recordeditaction(in_newtextrange_).md>) — Records information about an edit action to the transaction.
