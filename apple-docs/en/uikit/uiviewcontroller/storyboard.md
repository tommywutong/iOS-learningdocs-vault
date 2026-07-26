---
title: storyboard
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/storyboard
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/storyboard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/storyboard.json'
content_hash: 'sha256:061fa638bad52ad7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# storyboard

<sub>Instance Property</sub>

The storyboard from which the view controller originated.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var storyboard: UIStoryboard? { get }
```

## Discussion

If the view controller was not instantiated from a storyboard, this property is `nil`.

## See Also

### Getting the storyboard and nib information

- [nibName](nibname.md) — The name of the view controller’s nib file, if one was specified.
- [nibBundle](nibbundle.md) — The view controller’s nib bundle if it exists.
