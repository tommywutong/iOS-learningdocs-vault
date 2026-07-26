---
title: UISearchContainerViewController
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchcontainerviewcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontainerviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontainerviewcontroller.json'
content_hash: 'sha256:f7c495d92c9aa842'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISearchContainerViewController

<sub>Class</sub>

A view controller that manages the presentation of search results in your interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UISearchContainerViewController
```

## Overview

In tvOS, rather than push a [UISearchController](uisearchcontroller.md) onto a navigation controller’s stack or use one as a child of another container view controller, embed an instance of this class and let it manage the presentation of the search controller’s content.

[UISearchContainerViewController](uisearchcontainerviewcontroller.md) presents its [UISearchController](uisearchcontroller.md), instead of containing it. So implement view appearance methods, such as [- viewWillAppear:](<uiviewcontroller/viewwillappear(__).md>) and [- didMoveToParentViewController:](<uiviewcontroller/didmove(toparent_).md>) on both view controllers.

## Relationships

- **Inherits From**: [UIViewController](uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](uiappearancecontainer.md), [UIContentContainer](uicontentcontainer.md), [UIFocusEnvironment](uifocusenvironment.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UIStateRestoring](uistaterestoring.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Creating a search container view controller

- [- initWithSearchController:](<uisearchcontainerviewcontroller/init(searchcontroller_).md>) — Initializes and returns a search container view controller with the specified search controller object.

### Getting the search controller

- [searchController](uisearchcontainerviewcontroller/searchcontroller.md) — The search controller the search container view controller manages.

## See Also

### Search interface

- [UISearchController](uisearchcontroller.md) — A view controller that manages the display of search results based on interactions with a search bar.
- [UISearchBar](uisearchbar.md) — A specialized view for receiving search-related information from the user.
- [UISearchResultsUpdating](uisearchresultsupdating.md) — A set of methods that let you update search results based on information the user enters into the search bar.
- [Displaying searchable content by using a search controller](displaying-searchable-content-by-using-a-search-controller.md) — Create a user interface with searchable content in a table view.
- [Using suggested searches with a search controller](using-suggested-searches-with-a-search-controller.md) — Create a search interface with a table view of suggested searches.
