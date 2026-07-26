---
title: 'init(searchResultsController:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchcontroller/init(searchresultscontroller:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/init(searchresultscontroller:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/init%28searchresultscontroller%3A%29.json'
content_hash: 'sha256:f57c5af6b4aa6b6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchController](../uisearchcontroller.md)

# init(searchResultsController:)

<sub>Initializer</sub>

Creates and returns a search controller with the specified view controller for displaying the results.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(searchResultsController: UIViewController?)
```

## Parameters

- `searchResultsController` — The view controller that displays the search results. Specify `nil` if you want to display the search results in the same view controller that displays your searchable content. For apps running in tvOS, provide a results controller because tvOS doesn’t accept `nil` as a valid argument.

## Return Value

An initialized search controller.

## Discussion

After creating the search controller, always assign an object to the [searchResultsUpdater](searchresultsupdater.md) property. The search controller uses that object to update the search results.

## See Also

### Creating a search controller

- [- initWithCoder:](<init(coder_).md>) — Returns an initialized search controller from data in the specified unarchiver.
- [- initWithNibName:bundle:](<init(nibname_bundle_).md>) — Returns an initialized view controller with the nib file in the specified bundle.
