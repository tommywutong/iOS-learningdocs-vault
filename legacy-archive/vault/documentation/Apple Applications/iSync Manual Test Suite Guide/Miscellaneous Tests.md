---
title: iSync Manual Test Suite Guide
apple_id: TP40004484
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-06-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/iSyncManualTestSuiteRef/MiscellaneousTests/MiscellaneousTests.html
archived_at: '2026-07-15T05:19:24.119691Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iSync Manual Test Suite Guide](Introduction%20to%20iSync%20Manual%20Test%20Suite%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Calendar%20Tests.md)

# Miscellaneous Tests

This chapter contains miscellaneous tests that do not fit into any of the previous categories. Read Common Steps for how to turn on data change alerts before running these tests.

Tests adding a birthday to a calendar on the device.

1. Add a contact to the device.
2. Add a birthday field to the contact on the device.
3. Save the changes.
4. If an “Add birthday to calendar?“ prompt appears on the device, click Yes.
5. Sync.

   Verify that the event appears in iCal and is a yearly recurrent event.

Tests adding and removing emoticons on a device that supports the display of emoticons with some special glyphs or pictures.

1. Add an emoticon—for example, a smiley—to each event on the device.
2. Sync.
3. Remove the emoticons from some events on the device.
4. Remove the emoticons from some different events on the computer.
5. Sync.

   Verify that the events are correctly modified in iCal and that each emoticon is displayed in iCal using the corresponding ASCII text.

[Next](Document%20Revision%20History.md)[Previous](Calendar%20Tests.md)

