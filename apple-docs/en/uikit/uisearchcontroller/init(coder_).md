---
title: 'init(coder:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchcontroller/init(coder:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/init%28coder%3A%29.json'
content_hash: 'sha256:6b375405a071be75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchController](../uisearchcontroller.md)

# init(coder:)

<sub>Initializer</sub>

Returns an initialized search controller from data in the specified unarchiver.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init?(coder: NSCoder)
```

## Parameters

- `coder` — An unarchiver object.

## Return Value

An initialized search controller, or `nil` if the coder doesn’t define a search controller.

## See Also

### Creating a search controller

- [- initWithSearchResultsController:](<init(searchresultscontroller_).md>) — Creates and returns a search controller with the specified view controller for displaying the results.
- [- initWithNibName:bundle:](<init(nibname_bundle_).md>) — Returns an initialized view controller with the nib file in the specified bundle.
