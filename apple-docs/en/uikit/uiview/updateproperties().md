---
title: updateProperties()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/updateproperties()
source_url: 'https://developer.apple.com/documentation/uikit/uiview/updateproperties()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/updateproperties%28%29.json'
content_hash: 'sha256:433950f76008790e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# updateProperties()

<sub>Instance Method</sub>

Configures the view’s content and styling properties before layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updateProperties()
```

## Overview

Override this method to configure content and styling in your view subclass. Don’t call this method directly; instead, call [- setNeedsUpdateProperties](<setneedsupdateproperties().md>) to schedule an update.

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## See Also

### Observing data in views

- [- layoutSubviews](<layoutsubviews().md>) — Lays out subviews.
- [- updateConstraints](<updateconstraints().md>) — Updates constraints for the view.
- [- drawRect:](<draw(__).md>) — Draws the view’s image within the passed-in rectangle.
