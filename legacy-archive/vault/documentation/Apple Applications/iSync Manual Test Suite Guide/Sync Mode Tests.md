---
title: iSync Manual Test Suite Guide
apple_id: TP40004484
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-06-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/iSyncManualTestSuiteRef/SyncModeTests/SyncModeTests.html
archived_at: '2026-07-15T05:19:24.135163Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iSync Manual Test Suite Guide](Introduction%20to%20iSync%20Manual%20Test%20Suite%20Guide.md)


[Next](Cancellation%20Tests.md)[Previous](Initial%20Sync%20Tests.md)

# Sync Mode Tests

The tests in this chapter cover the different sync modes. Read Common Steps for how to turn on data change alerts before running these tests.

These are the common steps specific to this chapter:

- _To perform an initial erase sync_, choose “Erase data on device then sync” from the “For first sync” pop-up menu on the iSync window.
- _To perform a master reset device_, follow the instructions in the device manufacturer’s manual.
- _To force a slow sync_, launch Syncrospector, select the device from the Clients table, choose Slow Sync from the Sync Mode menu, and sync the device.

Tests syncing after a master reset of the device.

At the SyncML level, the device should reset its anchors for all the data classes. If it fails to do this properly, then iSync cannot determine if the device was reset and assumes that the user deliberately deleted all the records and iSync deletes all the records on the computer.

1. Add contacts, events, and tasks to the computer.
2. Perform an initial erase sync.
3. Perform a master reset of the device.
4. Force a slow sync.

   No data change alert panels should appear during syncing.

Tests slow syncing.

1. Add some contacts and events to the computer.
2. Sync.
3. Add a contact and an event to the device.
4. Sync.

   Verify that a data change alert panel appears during syncing.
5. Force a slow sync.

   Verify that _no_ data change alert panel appears during syncing.

Tests the ability to refresh sync one data class or database while fast syncing the other.

1. Add contacts and events to the computer.
2. Sync.
3. Add contacts and events to the device.
4. Add contacts and events to the computer.
5. Launch Syncrospector.
6. Select the device in the Clients table.
7. Click Sync State in the lower pane and select all the Contacts entities—entity names that begin with `com.apple.contacts`.
8. Choose Sync Mode > Pull the Truth.
9. Click the Sync button in Syncrospector.

   The device should reset its contacts but not its calendars. The contacts on the device should be deleted and the changes to the calendars should be correctly applied to the computer. All the changes from the computer should be applied to the device.
10. Repeat steps 1-9 except select all the Calendars entities—entity names that begin with `com.apple.calendars`.

[Next](Cancellation%20Tests.md)[Previous](Initial%20Sync%20Tests.md)

