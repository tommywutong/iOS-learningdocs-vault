---
title: UIView.Invalidations.Properties
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS, Swift 5.1+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/invalidations/properties
source_url: 'https://developer.apple.com/documentation/uikit/uiview/invalidations/properties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/invalidations/properties.json'
content_hash: 'sha256:2124d24f01a218da'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIView](../../uiview.md) · [Invalidations](../invalidations.md)

# UIView.Invalidations.Properties

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct Properties
```

## Relationships

- **Conforms To**: [UIViewInvalidating](../../uiviewinvalidating.md)

## Topics

### Initializers

- [init()](<properties/init().md>)

## See Also

### Views

- [- updateProperties](<../updateproperties().md>) — Configures the view’s content and styling properties before layout.
- [- setNeedsUpdateProperties](<../setneedsupdateproperties().md>) — Call to manually request a properties update for the view. Multiple requests may be coalesced into a single update alongside the next layout pass.
- [- updatePropertiesIfNeeded](<../updatepropertiesifneeded().md>) — Forces an immediate properties update for this view (and its view controller, if applicable) and any subviews, including any view controllers or views in its subtree.
- [- layoutSubviews](<../layoutsubviews().md>) — Lays out subviews.
- [- updateConstraints](<../updateconstraints().md>) — Updates constraints for the view.
- [- drawRect:](<../draw(__).md>) — Draws the view’s image within the passed-in rectangle.
