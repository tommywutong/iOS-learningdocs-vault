---
title: preferredFocusEnvironments
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusenvironment/preferredfocusenvironments
source_url: 'https://developer.apple.com/documentation/uikit/uifocusenvironment/preferredfocusenvironments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusenvironment/preferredfocusenvironments.json'
content_hash: 'sha256:81d2858c28ba0e26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusEnvironment](../uifocusenvironment.md)

# preferredFocusEnvironments

<sub>Instance Property</sub>

An array of focus environments, ordered by priority, to which this environment prefers focus to be directed during a focus update.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredFocusEnvironments: [any UIFocusEnvironment] { get }
```

## Discussion

The preferred focus environments listed in this property define where to search for the default focused item in an environment, such as when focus updates programmatically. Starting from the target environment, each preferred focus environment is recursively searched in the order it appears in the array until an eligible, focusable item is found. Preferred focus environments can include focusable and nonfocusable items, in addition to nonitem environments. Returning an empty array is equivalent to returning an array containing only `self`.

## See Also

### Controlling user-generated focus movements

- [preferredFocusedView](preferredfocusedview.md) — Specifies the view that should be focused if this environment is focused. _(deprecated)_
