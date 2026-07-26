---
title: 'init(nibName:bundle:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchcontroller/init(nibname:bundle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/init(nibname:bundle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/init%28nibname%3Abundle%3A%29.json'
content_hash: 'sha256:133d6a19eeb9493e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchController](../uisearchcontroller.md)

# init(nibName:bundle:)

<sub>Initializer</sub>

Returns an initialized view controller with the nib file in the specified bundle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: Bundle?)
```

## Parameters

- `nibNameOrNil` — The name of the nib file to associate with the view controller. The nib file name shouldn’t contain any leading path information. If you specify `nil`, the `nibName` property is set to `nil`.

- `nibBundleOrNil` — The bundle in which to search for the nib file. This method looks for the nib file in the bundle’s language-specific project directories first, followed by the Resources directory.

## See Also

### Creating a search controller

- [- initWithSearchResultsController:](<init(searchresultscontroller_).md>) — Creates and returns a search controller with the specified view controller for displaying the results.
- [- initWithCoder:](<init(coder_).md>) — Returns an initialized search controller from data in the specified unarchiver.
