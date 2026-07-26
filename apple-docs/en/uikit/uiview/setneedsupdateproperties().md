---
title: setNeedsUpdateProperties()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/setneedsupdateproperties()
source_url: 'https://developer.apple.com/documentation/uikit/uiview/setneedsupdateproperties()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/setneedsupdateproperties%28%29.json'
content_hash: 'sha256:e2be2b2ddbd96ec9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# setNeedsUpdateProperties()

<sub>Instance Method</sub>

Call to manually request a properties update for the view. Multiple requests may be coalesced into a single update alongside the next layout pass.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setNeedsUpdateProperties()
```

## See Also

### Views

- [- updateProperties](<updateproperties().md>) — Configures the view’s content and styling properties before layout.
- [- updatePropertiesIfNeeded](<updatepropertiesifneeded().md>) — Forces an immediate properties update for this view (and its view controller, if applicable) and any subviews, including any view controllers or views in its subtree.
- [- layoutSubviews](<layoutsubviews().md>) — Lays out subviews.
- [- updateConstraints](<updateconstraints().md>) — Updates constraints for the view.
- [- drawRect:](<draw(__).md>) — Draws the view’s image within the passed-in rectangle.
- [Properties](invalidations/properties.md)
