---
title: UISearchBarDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchbardelegate
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbardelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbardelegate.json'
content_hash: 'sha256:d22da30dcac47543'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISearchBarDelegate

<sub>Protocol</sub>

A collection of optional methods that you implement to make a search bar control functional.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UISearchBarDelegate : UIBarPositioningDelegate
```

## Overview

A [UISearchBar](uisearchbar.md) object provides the user interface for a search field on a bar, but it’s the application’s responsibility to implement the actions when buttons are tapped. At a minimum, the delegate needs to perform the actual search when text is entered in the text field.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIBarPositioningDelegate](uibarpositioningdelegate.md)

## Topics

### Managing the search text

- [- searchBar:textDidChange:](<uisearchbardelegate/searchbar(__textdidchange_).md>) — Tells the delegate that the user changed the search text.
- [- searchBar:shouldChangeTextInRange:replacementText:](<uisearchbardelegate/searchbar(__shouldchangetextin_replacementtext_).md>) — Ask the delegate if text in a specified range should be replaced with given text. _(deprecated)_
- [- searchBarShouldBeginEditing:](<uisearchbardelegate/searchbarshouldbeginediting(__).md>) — Asks the delegate if editing should begin in the specified search bar.
- [- searchBarTextDidBeginEditing:](<uisearchbardelegate/searchbartextdidbeginediting(__).md>) — Tells the delegate when the user begins editing the search text.
- [- searchBarShouldEndEditing:](<uisearchbardelegate/searchbarshouldendediting(__).md>) — Asks the delegate if editing should stop in the specified search bar.
- [- searchBarTextDidEndEditing:](<uisearchbardelegate/searchbartextdidendediting(__).md>) — Tells the delegate that the user finished editing the search text.

### Responding to clicks in search controls

- [- searchBarBookmarkButtonClicked:](<uisearchbardelegate/searchbarbookmarkbuttonclicked(__).md>) — Tells the delegate that the bookmark button was tapped.
- [- searchBarCancelButtonClicked:](<uisearchbardelegate/searchbarcancelbuttonclicked(__).md>) — Tells the delegate that the cancel button was tapped.
- [- searchBarSearchButtonClicked:](<uisearchbardelegate/searchbarsearchbuttonclicked(__).md>) — Tells the delegate that the search button was tapped.
- [- searchBarResultsListButtonClicked:](<uisearchbardelegate/searchbarresultslistbuttonclicked(__).md>) — Tells the delegate that the search results list button was tapped.

### Responding to scope button changes

- [- searchBar:selectedScopeButtonIndexDidChange:](<uisearchbardelegate/searchbar(__selectedscopebuttonindexdidchange_).md>) — Tells the delegate that the scope button selection changed.

### Instance Methods

- [- searchBar:shouldChangeTextInRanges:replacementText:](<uisearchbardelegate/searchbar(__shouldchangetextinranges_replacementtext_).md>)

## See Also

### Handling search bar interactions

- [delegate](uisearchbar/delegate.md) — The search bar’s delegate object.
