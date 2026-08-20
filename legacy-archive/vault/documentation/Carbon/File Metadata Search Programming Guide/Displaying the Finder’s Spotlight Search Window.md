---
title: File Metadata Search Programming Guide
apple_id: TP40001841
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreServices
published: '2011-09-28'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/SpotlightWindow.html
archived_at: '2026-07-15T05:24:41.729309Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File Metadata Search Programming Guide](About%20File%20Metadata%20Queries.md)


[Next](Document%20Revision%20History.md)[Previous](File%20Metadata%20Query%20Expression%20Syntax.md)

# Displaying the Finder’s Spotlight Search Window

Applications can provide users direct interaction with Spotlight by displaying the standard Finder search interface.

The [NSWorkspace](https://developer.apple.com/documentation/appkit/nsworkspace) method [showSearchResultsForQueryString:](https://developer.apple.com/documentation/appkit/nsworkspace/1532131-showsearchresults) provides a simple interface to the Finder search window. This is the programmatic equivalent of the user switching to Finder, creating a new window, and typing the search string into the search field.

The code fragment in Displaying the Finder’s Spotlight Search Window demonstrates extracting a string value and displaying the search interface.

__Listing 4-1__  Displaying the Finder Search Window

```
resultCode=[[NSWorkspace sharedWorkspace] showSearchResultsForQueryString:[sender stringValue]];

if (resultCode == NO) {
    // failed to open the panel
    // present an error to the user
    }
```

[Next](Document%20Revision%20History.md)[Previous](File%20Metadata%20Query%20Expression%20Syntax.md)

