---
title: setNeedsUpdateConstraints()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/setneedsupdateconstraints()
source_url: 'https://developer.apple.com/documentation/uikit/uiview/setneedsupdateconstraints()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/setneedsupdateconstraints%28%29.json'
content_hash: 'sha256:a93d648dbfed3b49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# setNeedsUpdateConstraints()

<sub>Instance Method</sub>

Controls whether the view’s constraints need updating.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setNeedsUpdateConstraints()
```

## Discussion

When a property of your custom view changes in a way that would impact constraints, you can call this method to indicate that the constraints need to be updated at some point in the future. The system will then call [- updateConstraints](<updateconstraints().md>) as part of its normal layout pass. Use this as an optimization tool to batch constraint changes. Updating constraints all at once just before they are needed ensures that you don’t needlessly recalculate constraints when multiple changes are made to your view in between layout passes.

## See Also

### Triggering Auto Layout

- [- needsUpdateConstraints](<needsupdateconstraints().md>) — A Boolean value that determines whether the view’s constraints need updating.
- [- updateConstraints](<updateconstraints().md>) — Updates constraints for the view.
- [- updateConstraintsIfNeeded](<updateconstraintsifneeded().md>) — Updates the constraints for the receiving view and its subviews.
