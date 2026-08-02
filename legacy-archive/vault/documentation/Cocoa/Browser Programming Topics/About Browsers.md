---
title: Browser Programming Topics
apple_id: 10000018i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2004-08-31'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Browser/Concepts/AboutBrowsers.html
archived_at: '2026-07-15T07:11:27.873609Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Browser Programming Topics](Introduction%20to%20Browsers.md)


[Next](Browser%20Interface%20Features.md)[Previous](Introduction%20to%20Browsers.md)

# About Browsers

A browser provides a user interface for displaying and selecting items from a list of data or from hierarchically organized lists of data such as directory paths. When working with a hierarchy of data, the levels are displayed in columns, which are numbered from left to right, beginning with 0. A browser is implemented by the NSBrowser class, and each of its column consists of an NSScrollView containing an NSMatrix filled with NSBrowserCells. NSBrowser relies on a delegate to provide the data in its NSBrowserCells.

Each entry in an NSBrowser column is an NSBrowser Cell. This cell can be either a branch cell (such as a directory) or a leaf cell (such as a file). A branch cell displays an image indicating that, when the cell is clicked, the NSBrowser will display a new column of NSBrowserCells. To display the new column, the NSBrowser sends itself the `addColumn` message, which messages its delegate to load the next column. An NSBrowserCell can also be loaded or unloaded; loaded NSBrowserCells have their state set and are ready for display. If your code needs access to a specific NSBrowserCell, you can use the NSBrowser method `loadedCellAtRow:column:`.

The user’s selection can be represented as a character string; if the selection is hierarchical (for example, a filename within a directory), each component of the path to the selected node is separated by “/”. To use some other character as the delimiter, invoke the NSBrowser method `setPathSeparator:`.

An NSBrowser can be set to allow selection of multiple cells in a column, or to limit selection to a single cell. When set for multiple selection, it can also be set to limit multiple selection to leaf cells only, or to allow selection of both types of cells together.

Because NSBrowser inherits from NSControl, it has a target object and action message. Each time the user selects one or more cells in a column, the browser sends its action message to its target. NSBrowser also adds an action to be sent when the user double-clicks on an entry, which allows the user to select items without any action being taken, and then double-click to invoke some useful action such as opening a file.

Because NSBrowserCell does not inherit from NSActionCell, it doesn’t hold a target and action value and can’t directly participate in the target/action paradigm. However, an NSBrowser action method can obtain the last selected NSBrowserCell with the `selectedCell` method.

[Next](Browser%20Interface%20Features.md)[Previous](Introduction%20to%20Browsers.md)

