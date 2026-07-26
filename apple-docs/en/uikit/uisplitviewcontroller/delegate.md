---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/delegate.json'
content_hash: 'sha256:2375e9e3f4581ebc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# delegate

<sub>Instance Property</sub>

The delegate you use to manage changes to a split view interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UISplitViewControllerDelegate)? { get set }
```

## Discussion

The split view controller uses its delegate to manage showing and hiding related view controllers. For more information about the methods you can implement in your delegate, see [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md).

## See Also

### Customizing the split view transitions

- [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md) — The methods adopted by the object you use to manage changes to a split view interface.
