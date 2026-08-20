---
title: iSync Manual Test Suite Guide
apple_id: TP40004484
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-06-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/iSyncManualTestSuiteRef/CancellationTests/CancellationTests.html
archived_at: '2026-07-15T05:19:23.433043Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iSync Manual Test Suite Guide](Introduction%20to%20iSync%20Manual%20Test%20Suite%20Guide.md)


[Next](Stress%20Tests.md)[Previous](Sync%20Mode%20Tests.md)

# Cancellation Tests

Tests canceling syncs during different states. Read Common Steps for how to turn on data change alerts before running these tests.

These are common steps specific to this chapter:

- _To perform an initial merge sync_, choose “Merge data on computer and device” from the “For first sync” menu in the iSync window.
- _To perform an initial erase sync_, choose “Erase data on device and then sync” from the “For first sync” menu in the iSync window.

Tests canceling an initial erase sync with contacts and events on the computer.

1. Add contacts to the computer.
2. Add events to the computer.
3. Perform an initial erase sync.
4. When a connection is made to the device, immediately cancel the sync using iSync.
5. Add a contact to the device.
6. Sync.

   The device should recover from the first sync—that is, from the device’s point of view, abort between SyncML package 1 and package 3.

Tests canceling an initial merge sync with contacts and events on the computer.

1. Add contacts to the computer.
2. Add events to the computer.
3. Perform an initial merge sync.
4. When a connection is made to the device, immediately cancel the sync using iSync.
5. Add a contact to the device.
6. Sync.

   The device should recover from the first sync—that is, from the device’s point of view, abort between SyncML package 1 and package 3.

Tests canceling a merge sync with records on both the device and the computer.

1. Add contacts and events to the device.
2. Add contacts and events to the computer.
3. Perform an initial merge sync.
4. When the data change alert (DCA) panel appears, press the Cancel button.
5. Sync.

   The device should recover from the first sync that is, from the device’s point of view, aborted after the end of the SyncML package 3 but before receiving package 4.

Tests what should happen when a user cancels an initial merge sync from the device.

1. Add contacts and events to the computer.
2. Perform an initial merge sync.
3. When a connection is made to the device, immediately cancel the sync from the device (if possible).
4. Add a contact to the device.
5. Sync.

   The device should recover and correctly perform the last sync.
6. Repeat steps 1-6 and cancel at various stages during the sync.

[Next](Stress%20Tests.md)[Previous](Sync%20Mode%20Tests.md)

