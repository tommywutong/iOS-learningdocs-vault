---
title: tag
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/tag
source_url: 'https://developer.apple.com/documentation/uikit/uiview/tag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/tag.json'
content_hash: 'sha256:74532a27ffb29c96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# tag

<sub>Instance Property</sub>

An integer that you can use to identify view objects in your application.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var tag: Int { get set }
```

## Discussion

The default value is `0`. You can set the value of this tag and use that value to identify the view later.

## See Also

### Identifying the view at runtime

- [- viewWithTag:](<viewwithtag(__).md>) — Returns the view whose tag matches the specified value.
