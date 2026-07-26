---
title: pinned
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewconfigurationstate-c.class/pinned
source_url: 'https://developer.apple.com/documentation/uikit/uiviewconfigurationstate-c.class/pinned'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewconfigurationstate-c.class/pinned.json'
content_hash: 'sha256:76a640ad2628f190'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewConfigurationState](../uiviewconfigurationstate-c.class.md)

# pinned

<sub>Instance Property</sub>

A Boolean value that indicates whether the view is in a pinned state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, getter=isPinned) BOOL pinned;
```

## Discussion

This state applies to header and footer views.

## See Also

### Managing view configuration states

- [traitCollection](traitcollection.md) — The traits that describe the current layout environment of the view, such as the user interface style and layout direction.
- [selected](selected.md) — A Boolean value that indicates whether the view is in a selected state.
- [highlighted](highlighted.md) — A Boolean value that indicates whether the view is in a highlighted state.
- [focused](focused.md) — A Boolean value that indicates whether the view is in a focused state.
- [disabled](disabled.md) — A Boolean value that indicates whether the view is in a disabled state.
