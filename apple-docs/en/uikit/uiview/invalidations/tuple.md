---
title: UIView.Invalidations.Tuple
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS, Swift 5.1+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/invalidations/tuple
source_url: 'https://developer.apple.com/documentation/uikit/uiview/invalidations/tuple'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/invalidations/tuple.json'
content_hash: 'sha256:f7b35df66b27df4e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIView](../../uiview.md) · [Invalidations](../invalidations.md)

# UIView.Invalidations.Tuple

<sub>Structure</sub>

A change that invalidates a combination of factors covered by the other invalidation types.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct Tuple<Invalidation1, Invalidation2> where Invalidation1 : UIViewInvalidating, Invalidation2 : UIViewInvalidating
```

## Overview

The system uses this type when a change invalidates multiple aspects of a view. Use a tuple of the static values defined in [UIViewInvalidating](../../uiviewinvalidating.md) when more than one invalidation type applies to a change.

## Relationships

- **Conforms To**: [UIViewInvalidating](../../uiviewinvalidating.md)

## Topics

### Creating the invalidation structure

- [init(_:_:)](<tuple/init(____).md>) — Creates an invalidation structure with multiple invalidations.

## See Also

### Invalidation types

- [Configuration](configuration.md) — A change that invalidates a view’s configuration.
- [Constraints](constraints.md) — A change that invalidates a view’s constraints.
- [Display](display.md) — A change that requires the system to redraw a view’s content.
- [IntrinsicContentSize](intrinsiccontentsize.md) — A change that invalidates a view’s intrinsic size.
- [Layout](layout.md) — A change that invalidates the layout of the containing view’s subviews.
