---
title: iSync Manual Test Suite Guide
apple_id: TP40004484
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-06-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/iSyncManualTestSuiteRef/ContactsTests/ContactsTests.html
archived_at: '2026-07-15T05:19:24.094648Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iSync Manual Test Suite Guide](Introduction%20to%20iSync%20Manual%20Test%20Suite%20Guide.md)


[Next](Calendar%20Tests.md)[Previous](Stress%20Tests.md)

# Contacts Tests

The tests in this chapter pertain to the Contacts database. Read Common Steps for how to turn on data change alerts before running these tests.

There is one common step specific to this chapter:

- _To add a contact with pictures_, select the contact in Address Book and click Edit. Double-click the picture area and drag an image to the picture area.

Tests adding, modifying, and deleting contacts.

This test consolidates contact mapping at a high level for contacts created and/or changed from the device side.

1. Add a _contact_ to the _device_.
2. Sync.
3. Modify _field values_ on the device.
4. Sync.
5. Delete _fields_ on the device.
6. Sync.
7. Delete the _contact_ on the device.
8. Sync.

1. Add a _contact_ to the _computer_.
2. Sync.
3. Modify _field values_ on the device.
4. Sync.
5. Delete _fields_ on the device.
6. Sync.
7. Delete the _contact_ on the device.
8. Sync.

Tests adding many contacts with large pictures.

1. Add many _contacts with large pictures_—for example, 500 contacts—to the _computer_ .

   Pictures should be 256 x 256 pixels or larger.
2. Sync.

[Next](Calendar%20Tests.md)[Previous](Stress%20Tests.md)

