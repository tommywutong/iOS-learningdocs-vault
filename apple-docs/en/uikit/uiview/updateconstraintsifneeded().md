---
title: updateConstraintsIfNeeded()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/updateconstraintsifneeded()
source_url: 'https://developer.apple.com/documentation/uikit/uiview/updateconstraintsifneeded()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/updateconstraintsifneeded%28%29.json'
content_hash: 'sha256:1fb25b4b3aa7e797'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# updateConstraintsIfNeeded()

<sub>Instance Method</sub>

Updates the constraints for the receiving view and its subviews.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updateConstraintsIfNeeded()
```

## Discussion

Whenever a new layout pass is triggered for a view, the system invokes this method to ensure that any constraints for the view and its subviews are updated with information from the current view hierarchy and its constraints. This method is called automatically by the system, but may be invoked manually if you need to examine the most up to date constraints.

Subclasses should not override this method.

## See Also

### Triggering Auto Layout

- [- needsUpdateConstraints](<needsupdateconstraints().md>) — A Boolean value that determines whether the view’s constraints need updating.
- [- setNeedsUpdateConstraints](<setneedsupdateconstraints().md>) — Controls whether the view’s constraints need updating.
- [- updateConstraints](<updateconstraints().md>) — Updates constraints for the view.
