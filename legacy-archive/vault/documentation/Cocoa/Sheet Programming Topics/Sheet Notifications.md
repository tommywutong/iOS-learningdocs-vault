---
title: Sheet Programming Topics
apple_id: 10000002i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-05-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Sheets/Tasks/SheetNotifications.html
archived_at: '2026-07-15T07:19:05.459956Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sheet Programming Topics](Introduction%20to%20Sheets.md)


[Next](Positioning%20Sheets.md)[Previous](Presenting%20a%20Series%20of%20Sheets.md)

# Sheet Notifications

NSWindow offers a set of notifications related to sheets, which it broadcasts on occurrences of a sheet opening or closing. Each notification is matched to a delegate method, so an NSWindow’s delegate is automatically registered for all notifications that it implements methods for.

`NSWindowWillBeginSheetNotification` is sent before a sheet is presented on a window and `NSWindowDidEndSheetNotification` after it is dismissed.

A window delegate should implement the following methods to receive the appropriate sheet notification:

- `- (void)windowWillBeginSheet:(NSNotification *)notification;`
- `- (void)windowDidEndSheet:(NSNotification *)notification;`

It is important to note that a window’s delegate is _not_ the same as the modal delegate specified as a parameter in the `NSBegin...Alert` calls. The modal delegate passed into the `NSBegin...Alert` calls is a delegate relationship that exists only until the sheet is dismissed.

[Next](Positioning%20Sheets.md)[Previous](Presenting%20a%20Series%20of%20Sheets.md)

