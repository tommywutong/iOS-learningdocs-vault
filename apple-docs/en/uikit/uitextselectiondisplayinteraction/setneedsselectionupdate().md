---
title: setNeedsSelectionUpdate()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextselectiondisplayinteraction/setneedsselectionupdate()
source_url: 'https://developer.apple.com/documentation/uikit/uitextselectiondisplayinteraction/setneedsselectionupdate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextselectiondisplayinteraction/setneedsselectionupdate%28%29.json'
content_hash: 'sha256:181aa331b525a95c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSelectionDisplayInteraction](../uitextselectiondisplayinteraction.md)

# setNeedsSelectionUpdate()

<sub>Instance Method</sub>

Tells the system to update the selection UI to match the current selection state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setNeedsSelectionUpdate()
```

## Discussion

When the selection state changes in your text input view, call this method to notify the system of the change. The system fetches the current selection state from your text input view and updates the system UI to match.

## See Also

### Reporting changes to the selection

- [- layoutManagedSubviews](<layoutmanagedsubviews().md>) — Loads the selection from the text input view and lays out the selection-related views.
