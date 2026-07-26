---
title: nibBundle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/nibbundle
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/nibbundle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/nibbundle.json'
content_hash: 'sha256:d953fe1967d06c84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# nibBundle

<sub>Instance Property</sub>

The view controller’s nib bundle if it exists.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var nibBundle: Bundle? { get }
```

## See Also

### Related Documentation

- [- initWithNibName:bundle:](<init(nibname_bundle_).md>) — Creates a view controller with the nib file in the specified bundle.

### Getting the storyboard and nib information

- [storyboard](storyboard.md) — The storyboard from which the view controller originated.
- [nibName](nibname.md) — The name of the view controller’s nib file, if one was specified.
