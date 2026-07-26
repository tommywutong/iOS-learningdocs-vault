---
title: 'recordEditAction(in:newTextRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextcontentmanager/recordeditaction(in:newtextrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentmanager/recordeditaction(in:newtextrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentmanager/recordeditaction%28in%3Anewtextrange%3A%29.json'
content_hash: 'sha256:ab2cbb7b56ab2641'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentManager](../nstextcontentmanager.md)

# recordEditAction(in:newTextRange:)

<sub>Instance Method</sub>

Records information about an edit action to the transaction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func recordEditAction(in originalTextRange: NSTextRange, newTextRange: NSTextRange)
```

## Parameters

- `originalTextRange` — The range before the action.

- `newTextRange` — The corresponding range after the action.

## Discussion

The concrete subclass invokes this method for each edit action.

## See Also

### Performing transactions

- [hasEditingTransaction](haseditingtransaction.md) — Indicates there’s an active editing transaction from the primary text layout manager.
- [- performEditingTransactionUsingBlock:](<performeditingtransaction(__).md>) — Performs an editing transaction and invokes a block upon completion.
