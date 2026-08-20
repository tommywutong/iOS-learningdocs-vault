---
title: iSync Manual Test Suite Guide
apple_id: TP40004484
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-06-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/iSyncManualTestSuiteRef/GeneralTests/GeneralTests.html
archived_at: '2026-07-15T05:19:24.100721Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iSync Manual Test Suite Guide](Introduction%20to%20iSync%20Manual%20Test%20Suite%20Guide.md)


[Next](Initial%20Sync%20Tests.md)[Previous](Common%20Steps.md)

# General Tests

The tests in this section are basic and apply to all devices. Read Common Steps for how to turn on data change alerts before running these tests.

These tests, except Add Device, assume that you have iSync launched, the device is selected in the iSync window, and syncing is enabled for the device. These are some common steps specific to this chapter:

- _To enable syncing for a device_, select the device and select the “Turn on <device> synchronization” option in the iSync window.

  Device syncing is turned on by default.
- _To sync the device_, add the device (if it is not already added), and click the Sync Devices button. Bluetooth devices should already be paired using System Preferences before running any of these tests.

Tests adding the device to iSync—for example, tests that the correct icon appears.

If the device uses Bluetooth, then all of the tests in this document assume that you already paired the device with the computer. This step needs to be done only once per device. Use the Bluetooth pane in System Preferences to pair a Bluetooth device. Choose Help > System Preferences Help to learn more about setting up a Bluetooth connection.

If you are testing a USB connection, plug in the device via USB before following these steps.

1. Add device in iSync.

   Verify that the device appears with the correct name and icon in the Add Device and iSync windows.

Tests syncing after powering off the device. Verifies that the Sync Alert panel appears when the connection is lost.

1. Sync.
2. Power off device.
3. Sync.

   An Sync Alert panel should appear saying that it cannot connect to the device.
4. Power on device.
5. Sync.

   This sync should succeed.

Tests enabling and disabling different databases in iSync.

1. Add a contact to the computer and to the device.
2. Add an event to the computer and to the device.
3. Enable Contacts and disable Calendars in the iSync window.
4. Sync.

   Verify that changes are made to Contacts only.
5. Disable Contacts and enable Calendars in the iSync window.
6. Add a contact to the computer and to the device.
7. Sync.

   Verify that changes are made to Calendars only.

[Next](Initial%20Sync%20Tests.md)[Previous](Common%20Steps.md)

