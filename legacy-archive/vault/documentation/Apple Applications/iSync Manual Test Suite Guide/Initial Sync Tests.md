---
title: iSync Manual Test Suite Guide
apple_id: TP40004484
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-06-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/iSyncManualTestSuiteRef/InitialSyncTests/InitialSyncTests.html
archived_at: '2026-07-15T05:19:24.107419Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iSync Manual Test Suite Guide](Introduction%20to%20iSync%20Manual%20Test%20Suite%20Guide.md)


[Next](Sync%20Mode%20Tests.md)[Previous](General%20Tests.md)

# Initial Sync Tests

The tests in this chapter cover syncing the device for the first time which is called _initial sync_. There are different types of initial syncs that need to be tested. These tests assume that you have iSync launched, the device is selected in the iSync window, and syncing is enabled for the device. Read Common Steps for set up instructions before running these tests.

In addition, you should configure the iSync preferences so an alert appears each time the device changes the state of the truth—each time the device adds, modifies, or deletes records—as follows:

- _To set the data change alert to “any” in iSync_, choose iSync > Preferences, enable the “Show Data Change Alert when” option, and select “any” from the adjacent pop-up menu.

  When a Sync Alert panel appears, click the triangle at the bottom of the panel to reveal more information about the changes. Use this panel to verify the changes and optionally, cancel the sync session.

Some of the following tests require records on the device before running an initial sync. Optionally, follow these steps to set up a device for these tests using iSync:

1. Add contacts and calendars to the computer that you want to be on the device.

   Create a group in Address Book and add the contacts to that group. Create a calendar in iCal and add the events to that calendar.
2. Launch iSync and select the device icon.
3. Choose the Contacts group from the Synchronize pop-up menu.
4. Select the Calendars group from the Calendars > Selected scroll view.
5. Choose Devices > Reset Device from the iSync menu and click Reset in the alert panel.

   Wait for iSync to sync the device, which adds the selected records to the device.
6. Click the device icon and choose Devices > Remove Device and click OK in the alert panel.
7. Delete all the records on the computer that were added to the device.
8. Reset the Sync Services server by launching Syncrospector, choosing Window > Show Sync Plans, and clicking the Reset Server button.

These are the common steps used in this chapter:

- _To perform an initial merge sync_, choose “Merge data on computer and device” from the “For first sync” pop-up menu in the iSync window.
- _To perform an initial erase sync_, choose “Erase data on device then sync” from the “For first sync” pop-up menu in the iSync window.
- _To reset the device_, choose Device > Reset Device or Device > Reset All Devices from the iSync menu.

  This is an alternate way to perform an initial erase sync.

Tests _initial syncs_ where `0` records are on the device and some records are on the computer.

1. Add a contact to the computer.
2. Add an event to the computer.
3. Add a task to the computer.
4. Make sure there are `0` contacts and `0` events on the device.
5. Perform an initial merge sync.

   Verify that the records on the computer are now on the device.

Tests initial merge syncs when records are on the device and on the computer.

1. Add some contacts and events to the device.
2. Add some different contacts and event to the computer.
3. Perform an initial merge sync.

   Verify that the records on the device are now on the computer and vice-versa.

Tests syncing with many records on the device and computer.

1. Add many _contacts and events_ (2000 or more records) to the _computer_.
2. Add many different _contacts and events_ to the _device_.
3. Perform an initial merge sync.

   Verify that the records on the device are now on the computer and vice-versa.

Tests initial erase sync when the device contains many records.

1. Add many _contacts and events_ (2000 or more records) to the _device_.
2. Add a few different _contacts and events_ to the _computer_.
3. Enable Contacts and Calendars in the iSync window.
4. Initial erase sync.

   Verify that existing records on the device are deleted and that records from the computer are added correctly.
5. Repeat steps 1-4 for the Contacts database only and Calendars database only.

Tests initial erase sync when the device contains no records and the computer contains records

1. Add many _contacts and events_ to the _computer_.
2. Enable Contacts and Calendars in the iSync window.
3. Initial erase sync.

   Verify that all the records on the computer are on the device.
4. Repeat steps 1-3 for the Contacts database only and Calendars database only.

[Next](Sync%20Mode%20Tests.md)[Previous](General%20Tests.md)

