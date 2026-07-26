---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/delegate.json'
content_hash: 'sha256:de49560ff09e78c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# delegate

<sub>Instance Property</sub>

The text view’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UITextViewDelegate)? { get set }
```

## Discussion

A text view delegate responds to editing-related messages from the text view. You can use the delegate to track changes to the text itself and to the current selection.

For information about the methods implemented by the delegate, see [UITextViewDelegate](../uitextviewdelegate.md).

## See Also

### Responding to text view changes

- [UITextViewDelegate](../uitextviewdelegate.md) — The methods for receiving editing-related messages for text view objects.
