---
title: traitCollection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitenvironment/traitcollection
source_url: 'https://developer.apple.com/documentation/uikit/uitraitenvironment/traitcollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitenvironment/traitcollection.json'
content_hash: 'sha256:c21e52b6575279af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitEnvironment](../uitraitenvironment.md)

# traitCollection

<sub>Instance Property</sub>

The traits, such as the size class and scale factor, that describe the current environment of the object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var traitCollection: UITraitCollection { get }
```

## Discussion

[UIViewController](../uiviewcontroller.md) and [UIView](../uiview.md) adopt the [UITraitEnvironment](../uitraitenvironment.md) protocol and expose this property.

> [!important] Important
> Don’t implement this property in your own objects. Instead, use the [traitCollection](traitcollection.md) property associated with a view, view controller, or other object to determine the currently available trait information.
