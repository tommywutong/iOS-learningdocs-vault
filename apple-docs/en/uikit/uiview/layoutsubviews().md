---
title: layoutSubviews()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/layoutsubviews()
source_url: 'https://developer.apple.com/documentation/uikit/uiview/layoutsubviews()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/layoutsubviews%28%29.json'
content_hash: 'sha256:8710f19d003bc967'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# layoutSubviews()

<sub>Instance Method</sub>

Lays out subviews.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func layoutSubviews()
```

## Discussion

The default implementation uses any constraints you set to determine the size and position of any subviews.

Subclasses can override this method as needed to perform more precise layout of their subviews. You should override this method only if the autoresizing and constraint-based behaviors of the subviews don’t offer the behavior you want. You can use your implementation to set the frame rectangles of your subviews directly.

Don’t call this method directly. If you want to force a layout update, call the [- setNeedsLayout](<setneedslayout().md>) method instead to do so prior to the next drawing update. If you want to update the layout of your views immediately, call the [- layoutIfNeeded](<layoutifneeded().md>) method.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this view’s `traitCollection`. For more information, see [Automatic trait tracking](../automatic-trait-tracking.md).

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## See Also

### Observing data in views

- [- updateProperties](<updateproperties().md>) — Configures the view’s content and styling properties before layout.
- [- updateConstraints](<updateconstraints().md>) — Updates constraints for the view.
- [- drawRect:](<draw(__).md>) — Draws the view’s image within the passed-in rectangle.
