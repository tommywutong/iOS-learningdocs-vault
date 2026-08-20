---
title: Using a Search Bar in a Toolbar
apple_id: DTS40009461
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2013-09-03'
source_url: https://developer.apple.com/library/archive/samplecode/ToolbarSearch/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:27:00.439484Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using a Search Bar in a Toolbar](Using%20a%20Search%20Bar%20in%20a%20Toolbar.md)


[Next](ToolbarSearch-APLAppDelegate.h.md)[Previous](Using%20a%20Search%20Bar%20in%20a%20Toolbar.md)

# ReadMe.txt

```

ToolbarSearch
=============

This sample shows how to use a search field in a toolbar. When you start a search, a table view displaying recent searches matching the current search string is displayed in a popover. 

The main view contains a toolbar with a bar button item with a search field as a custom view. If you tap the search field, the view controller presents a popover containing a list of recent searches. The list is stored in user defaults so that it persists between launches of the application, and is managed by the list's table view controller. The recents list is filtered by the current search term. If you select an item from the recents list, the item is copied to the search field and a search executed.

Main Classes:

APLToolbarSearchViewController
A view controller that manages a search bar and a recent searches controller. When the user commences a search, the search view controller presents a recent searches controller in a popover.

APLRecentSearchesController
APLRecentSearchesController defines a table view controller to manage and display a list of recent search strings. The search strings are stored in user defaults to maintain the list between launches of the application.

The view controller manages two arrays:
 * recentSearches is the array that corresponds to the full set of recent search strings stored in user defaults.
 * displayedRecentSearches is an array derived from recent searches, filtered by the current search string (if any).

 The recentSearches array is kept synchronized with user defaults, and avoids the need to query user defaults every time the search string is updated.

 The table view displays the contents of the displayedRecentSearches array.

 The view controller has a delegate that it notifies if row in the table view is selected.


=======================================================
Copyright (C) 2010-2013 Apple Inc. All rights reserved.
```

[Next](ToolbarSearch-APLAppDelegate.h.md)[Previous](Using%20a%20Search%20Bar%20in%20a%20Toolbar.md)

