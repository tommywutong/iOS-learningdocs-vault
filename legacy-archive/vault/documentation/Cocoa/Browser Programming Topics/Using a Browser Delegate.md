---
title: Browser Programming Topics
apple_id: 10000018i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2004-08-31'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Browser/Tasks/UsingBrowserDelegate.html
archived_at: '2026-07-15T07:11:29.877565Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Browser Programming Topics](Introduction%20to%20Browsers.md)


[Next](Document%20Revision%20History.md)[Previous](Browser%20Interface%20Features.md)

# Using a Browser Delegate

NSBrowser requires a delegate to provide it with data to display.
The delegate is responsible for providing the data and for setting
each item as a branch or leaf node, enabled or disabled. It can
also receive notification of events like scrolling and requests
for validation of columns that may have changed.

You can implement one of two delegate types: Active or passive.
An active delegate creates a column’s rows (that is, the NSBrowserCells)
itself, while a passive one leaves that job to the NSBrowser. Normally,
passive delegates are preferable, because they’re easier to implement.
An active delegate must implement `browser:createRowsForColumn:` to
create the rows of the specified column. A passive delegate, on
the other hand, must implement `browser:numberOfRowsInColumn:` to
let the NSBrowser know how many rows to create. These two methods
are mutually exclusive; you can implement one or the other, but
not both. (The NSBrowser ascertains what type of delegate it has
by which method the delegate responds to.)

Both types of delegate implement `browser:willDisplayCell:atRow:column:` to
set up state (such as the cell’s string value and whether the
cell is a leaf or a branch) before an individual cell is displayed.
(This delegate method doesn’t need to invoke NSBrowserCell’s `setLoaded:` method,
because the NSBrowser can determine that state by itself.) An active
delegate can instead set all the cells’ state at the time the
cells are created, in which case it doesn’t need to implement `browser:willDisplayCell:atRow:column:`. However,
a passive delegate must always implement this method.

[Next](Document%20Revision%20History.md)[Previous](Browser%20Interface%20Features.md)

