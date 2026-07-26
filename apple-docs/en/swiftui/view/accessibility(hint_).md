---
title: 'accessibility(hint:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/accessibility(hint:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibility(hint:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibility%28hint%3A%29.json'
content_hash: 'sha256:5990c4817c735a77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibility(hint:)

<sub>Instance Method</sub>

Communicates to the user what happens after performing the view’s action.

> [!warning] Deprecated
> Use [accessibilityHint(_:)](<accessibilityhint(__)-3rdgs.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibility(hint: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Discussion

Provide a hint in the form of a brief phrase, like “Purchases the item” or “Downloads the attachment”.

## See Also

### Accessibility modifiers

- [accessibility(label:)](<accessibility(label_).md>) — Adds a label to the view that describes its contents. _(deprecated)_
- [accessibility(value:)](<accessibility(value_).md>) — Adds a textual description of the value that the view contains. _(deprecated)_
- [accessibility(hidden:)](<accessibility(hidden_).md>) — Specifies whether to hide this view from system accessibility features. _(deprecated)_
- [accessibility(identifier:)](<accessibility(identifier_).md>) — Uses the specified string to identify the view. _(deprecated)_
- [accessibility(selectionIdentifier:)](<accessibility(selectionidentifier_).md>) — Sets a selection identifier for this view’s accessibility element. _(deprecated)_
- [accessibility(activationPoint:)](<accessibility(activationpoint_).md>) — Specifies the point where activations occur in the view. _(deprecated)_
- [accessibility(inputLabels:)](<accessibility(inputlabels_).md>) — Sets alternate input labels with which users identify a view. _(deprecated)_
- [accessibility(addTraits:)](<accessibility(addtraits_).md>) — Adds the given traits to the view. _(deprecated)_
- [accessibility(removeTraits:)](<accessibility(removetraits_).md>) — Removes the given traits from this view. _(deprecated)_
- [accessibility(sortPriority:)](<accessibility(sortpriority_).md>) — Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level. _(deprecated)_
