---
title: UIView.Invalidations.Display
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS, Swift 5.1+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/invalidations/display
source_url: 'https://developer.apple.com/documentation/uikit/uiview/invalidations/display'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/invalidations/display.json'
content_hash: 'sha256:434b7e20bd832963'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIView](../../uiview.md) · [Invalidations](../invalidations.md)

# UIView.Invalidations.Display

<sub>Structure</sub>

A change that requires the system to redraw a view’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct Display
```

## Overview

Use [display](../../uiviewinvalidating/display.md) to create an instance of this type.

## Relationships

- **Conforms To**: [UIViewInvalidating](../../uiviewinvalidating.md)

## Topics

### Creating the invalidation structure

- [init()](<display/init().md>) — Creates a display invalidation structure.

## See Also

### Invalidation types

- [Configuration](configuration.md) — A change that invalidates a view’s configuration.
- [Constraints](constraints.md) — A change that invalidates a view’s constraints.
- [IntrinsicContentSize](intrinsiccontentsize.md) — A change that invalidates a view’s intrinsic size.
- [Layout](layout.md) — A change that invalidates the layout of the containing view’s subviews.
- [Tuple](tuple.md) — A change that invalidates a combination of factors covered by the other invalidation types.
