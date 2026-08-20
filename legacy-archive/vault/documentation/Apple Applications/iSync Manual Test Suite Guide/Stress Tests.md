---
title: iSync Manual Test Suite Guide
apple_id: TP40004484
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-06-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/iSyncManualTestSuiteRef/StressTests/StressTests.html
archived_at: '2026-07-15T05:19:24.129648Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iSync Manual Test Suite Guide](Introduction%20to%20iSync%20Manual%20Test%20Suite%20Guide.md)


[Next](Contacts%20Tests.md)[Previous](Cancellation%20Tests.md)

# Stress Tests

Tests in this chapter involve hardware states such as power loss and the computer going to sleep. Read Common Steps for how to turn on data change alerts before running these tests.

Tests syncing while the device is low on power.

1. Add contacts and events in the computer.
2. Start a sync.
3. During sync, power off device (turn off the device or remove the battery).
4. After iSync reports a failed sync due to connection loss or not being able to connect, turn device on.
5. Sync.

   Verify that the new contacts and events are on the device.

Tests syncing when the computer goes to sleep.

1. Sync.
2. Put computer to sleep while syncing.
3. Wake up computer.
4. Sync.

   Verify that the device recovers from the lost connection and syncs correctly.

Tests syncing when the device is low on memory.

1. Fill up the memory on the device to it’s capacity.

   It should have no space for additional contacts or events.
2. Add contacts and events to the computer that exceeds the available memory on the device.
3. Sync.

   iSync should report that the device is out of memory. If it fails to do so, it probably means that the device did not acknowledge the changes coming from the computer with the appropriate SyncML status code.

Tests syncing when the device is moved out of Bluetooth range.

1. Add contacts and events to the computer.
2. Start a sync.
3. During the sync, move the device out of Bluetooth range.

   Verify that iSync displays an alert panel saying the device is out of Bluetooth range.
4. After a few moments, bring the device into Bluetooth range.
5. Sync.

   Verify that the device recovers from the lost connection and syncs correctly.

[Next](Contacts%20Tests.md)[Previous](Cancellation%20Tests.md)

