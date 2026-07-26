---
title: needsUpdateConstraints()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/needsupdateconstraints()
source_url: 'https://developer.apple.com/documentation/uikit/uiview/needsupdateconstraints()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/needsupdateconstraints%28%29.json'
content_hash: 'sha256:73e516a34bd0af8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# needsUpdateConstraints()

<sub>Instance Method</sub>

A Boolean value that determines whether the view’s constraints need updating.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func needsUpdateConstraints() -> Bool
```

## Return Value

[true](../../swift/true.md) if the view’s constraints need updating, [false](../../swift/false.md) otherwise.

## Discussion

The constraint-based layout system uses the return value of this method to determine whether it needs to call [- updateConstraints](<updateconstraints().md>) on your view as part of its normal layout pass.

## See Also

### Triggering Auto Layout

- [- setNeedsUpdateConstraints](<setneedsupdateconstraints().md>) — Controls whether the view’s constraints need updating.
- [- updateConstraints](<updateconstraints().md>) — Updates constraints for the view.
- [- updateConstraintsIfNeeded](<updateconstraintsifneeded().md>) — Updates the constraints for the receiving view and its subviews.
