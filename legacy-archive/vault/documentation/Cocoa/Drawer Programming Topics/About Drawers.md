---
title: Drawer Programming Topics
apple_id: 10000001i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2003-02-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Drawers/Concepts/AboutDrawers.html
archived_at: '2026-07-15T07:15:21.586294Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Drawer Programming Topics](Introduction%20to%20Drawers.md)


[Next](Positioning%20and%20Sizing%20a%20Drawer.md)[Previous](Introduction%20to%20Drawers.md)

# About Drawers

NSDrawer is a user interface element that contains and displays view objects including NSTextView, NSScrollView, NSBrowserView, and other classes that inherit from NSView. A drawer is associated with a window, called its parent, and can only appear while its parent is visible on screen. A drawer cannot be moved or ordered independently of a window, but is instead attached to one edge of its parent and moves along with it. Drawers may be resized, but a drawer can never be larger than its parent. A given window may have any number of drawers; it is the developer’s responsibility to make sure drawers do not overlap.

A drawer may be either open or closed, or in the process of opening or closing. When a drawer is closed, it does not appear on screen. A drawer may be opened on a particular edge of its parent depending on, for instance, the window’s position on screen. Each drawer may also have a preferred edge which is used when an edge is not specified programmatically. If a closed drawer is told to open without a preferred edge specified, the drawer attempts to choose an edge on which to open based on the space available to display the drawer on screen. If you need to ensure that a drawer opens on a specific edge, use `openOnEdge:`.

The opening and closing of a drawer does not happen instantaneously, so a notification is sent whenever a drawer has finished opening or closing. A drawer may be told to open or close at any time, with the expectation that the command will eventually be carried out. If a rapid series of open and close commands is issued, the last one will override the others and will determine what state the drawer finally ends up in.

A drawer can only be associated with one parent window at a time, but the parent window can be changed at anytime using `setParentWindow:` (however, the change is only made when the drawer is closed). Each drawer has its own `keyViewLoop` separate from its parent.

[Next](Positioning%20and%20Sizing%20a%20Drawer.md)[Previous](Introduction%20to%20Drawers.md)

