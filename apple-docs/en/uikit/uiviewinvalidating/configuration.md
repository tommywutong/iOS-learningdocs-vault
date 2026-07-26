---
title: configuration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS, Swift 5.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewinvalidating/configuration
source_url: 'https://developer.apple.com/documentation/uikit/uiviewinvalidating/configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewinvalidating/configuration.json'
content_hash: 'sha256:a46584af91acc3b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewInvalidating](../uiviewinvalidating.md)

# configuration

<sub>Type Property</sub>

A change that invalidates a view’s configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var configuration: UIView.Invalidations.Configuration { get }
```

## Discussion

Use this invalidation type to call [- setNeedsUpdateConfiguration](<../uibutton/setneedsupdateconfiguration().md>) when a change in property value should cause the containing view to update the configuration.

> [!note] Note
> You only use this invalidation type on [UIView](../uiview.md) subclasses that support a configuration pattern, using [- setNeedsUpdateConfiguration](<../uibutton/setneedsupdateconfiguration().md>) and [- updateConfiguration](<../uibutton/updateconfiguration().md>) pattern. For example, use this type on [UIButton](../uibutton.md), [UICollectionViewCell](../uicollectionviewcell.md), [UITableViewCell](../uitableviewcell.md), or [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md). This type has no effect on [UIView](../uiview.md) subclasses that don’t use a configuration pattern.

## See Also

### Specifying invalidation types

- [constraints](constraints.md) — A change that invalidates a view’s constraints.
- [display](display.md) — A change that requires the system to redraw a view’s content.
- [intrinsicContentSize](intrinsiccontentsize.md) — A change that invalidates a view’s intrinsic size.
- [layout](layout.md) — A change that invalidates the layout of the containing view’s subviews.
