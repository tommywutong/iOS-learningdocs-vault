---
title: Simple UISearchBar with State Restoration
apple_id: DTS40007848
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2013-05-23'
source_url: https://developer.apple.com/library/archive/samplecode/TableSearch/Listings/ReadMe_md.html
archived_at: '2026-07-18T03:26:12.152499Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Simple UISearchBar with State Restoration](Simple%20UISearchBar%20with%20State%20Restoration.md)


[Next](LICENSE.txt.md)[Previous](TableSearch-main.m.md)

# ReadMe.md

```

TableSearch
===========

This sample demonstrates how to use the UISearchDisplayController object in conjunction with a UISearchBar, effectively filtering in and out the contents of that table. If an iOS application has large amounts of table data, this sample shows how to filter it down to a manageable amount so that users to scroll through less content in a table.

It shows how you can:
- Create a UISearchDisplayController.
- Use scopes on UISearchBar with a search display controller.
- Manage the interaction between the search display controller and a containing UINavigationController
    (there is no code for this -- the navigation bar is moved around as necessary).
- Return different results for the main table view and the search display controller's table view.
- Handle the destruction and re-creation of a search display controller when receiving a memory warning.

Using the Sample

Tap the search field and as you enter case insensitive text the list shinks/expands based on the filter text. An empty string will show the entire contents.  To get back the entire contents once you have filtered the content, touch the search bar again, tap the clear ('x') button and then tap cancel.


Main Classes
----------

APLViewController
Manages a table view to display a list of products, and manages a search bar to filter the product list.


APLProduct
A simple model file to represent a product with a name and type.

=======================================================
Copyright (C) 2008-2013 Apple Inc. All rights reserved.
```

[Next](LICENSE.txt.md)[Previous](TableSearch-main.m.md)

