---
title: iSync Manual Test Suite Guide
apple_id: TP40004484
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-06-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/iSyncManualTestSuiteRef/CalendarTests/CalendarTests.html
archived_at: '2026-07-15T05:19:23.420689Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iSync Manual Test Suite Guide](Introduction%20to%20iSync%20Manual%20Test%20Suite%20Guide.md)


[Next](Miscellaneous%20Tests.md)[Previous](Contacts%20Tests.md)

# Calendar Tests

The tests in this chapter are specific to the Calendars database. Read Common Steps for how to turn on data change alerts before running these tests.

These are common steps specific to this chapter:

- _To perform an initial merge sync_, choose “Merge data on computer and device” from the “For first sync” pop-up menu on the iSync window.
- _To force slow sync_, launch Syncrospector, select the device from the Clients table, choose Slow Sync from the Sync Mode menu, and sync the device.
- To add a _timed event_, double-click a day in Month view in iCal and choose the type of alarm from the “alarm” pop-up menu, and then set when you want the alarm to fire.
- To add a _recurrent event_, double-click a day in Month view in iCal and choose how often you want the event to occur from the “repeat” pop-up menu.
- To add a _all-day event_, double-click a day in Month view in iCal and select the all-day option in the Info drawer.
- To add a _recurrent all-day event_, add an all-day event in iCal and choose how often you want the event to occur from the "repeat" pop-up menu.
- To add a _multi-day all-day event_, double-click a day in Month view in iCal. Then select the all-day option and type the start and end dates (spanning multiple days) in the event's Info drawer.
- To _delete fields on the computer_, select an event in iCal and edit the field in the Info drawer. To delete a recurrence rule, choose None from the “repeat” pop-up menu. To delete an alarm, choose Remove Alarm from the alarm pop-up menu. To delete text in the Notes field, click in the Notes field, press Command-A, and press the Delete key.
- To _modify a repeat rule_, select the event in iCal and choose another menu item in the "repeat" pop-up menu.

Tests adding, modifying, and deleting timed events on the device and computer.

This test consolidates calendar mapping at a high level for timed events added and/or modified on the device.

1. Add a _timed event_ to the _device_.
2. Sync.
3. Modify _field values_ on the device.
4. Sync.
5. Delete _fields_ on the device.
6. Sync.
7. Delete the _timed event_ on the device.
8. Sync.
9. Repeat steps 1-8 for all types of events that the device supports—for example, memo and anniversary.

1. Add a _timed event_ to the _computer_.
2. Sync.
3. Modify _field values_ on the computer.
4. Sync.
5. Delete _fields_ on the computer.
6. Sync.
7. Delete the _timed event_ on the computer.
8. Sync.
9. Repeat steps 1-8 for all types of events that the device supports—for example, memo and anniversary.

Tests adding, modifying, and deleting recurrent events on the device and computer. Also tests changing recurrent events to timed events and vice-versa.

This test consolidates calendar mapping at a high level for recurrent events added and/or modified on the device.

1. Add a _recurrent event_ to the _device_.
2. Sync.
3. Modify _field values_ on the device.
4. Sync.
5. Delete _fields_ on the device.
6. Sync.
7. Delete the _recurrent event_ on the device.
8. Sync.

1. Add a _recurrent event_ to the _device_.
2. Sync.
3. Modify the _repeat rule_ on the device.
4. Sync.
5. Delete _fields_ on the device.
6. Sync.
7. Delete the _recurrent event_ on the device.
8. Sync.

1. Add a _recurrent event_ to the _computer_.
2. Sync.
3. Modify _field values_ on the device.
4. Sync.
5. Delete _fields_ on the device.
6. Sync.
7. Delete the _recurrent event_ on the device.
8. Sync.

1. Add a _recurrent event_ to the _computer_.
2. Sync.
3. Modify the _repeat rule_ on the device.
4. Sync.
5. Delete the _fields_ on the device.
6. Sync.
7. Delete the _recurrent event_ on the device.
8. Sync.

1. Add a _recurrent event_ to the _computer_.
2. Sync.
3. Change the _recurrent event to a timed event_ on the device.
4. Sync.
5. Delete _fields_ on the device.
6. Sync.
7. Delete the _timed event_ on the device.
8. Sync.

1. Add a _timed event_ to the _computer_.
2. Sync.
3. Change the _timed event to a recurrent event_ on the device.
4. Sync.
5. Delete _fields_ on the device.
6. Sync.
7. Delete the _recurrent event_ on the device.
8. Sync.

Tests adding, modifying and deleting all-day events on the device and computer. Also tests changing all-day events to recurrent all-day events and vice-versa.

These tests consolidate calendar mapping at a high level for all-day events added and/or modified on the device.

1. Add an _all-day event_ to the _device_.
2. Sync.
3. Modify _field values_ on the device.
4. Sync.
5. Delete _fields_ on the device.
6. Sync.
7. Delete the _all-day event_ on the device.
8. Sync.

1. Add an _all-day event_ to the _device_.
2. Sync.
3. Change _all-day event to a timed event_ on the device.
4. Sync.
5. Delete _fields_ on the device.
6. Sync.
7. Delete the _timed event_ on the device.
8. Sync.

1. Add an _all-day event_ to the _computer_.
2. Sync.
3. Change _field values_ on device,
4. Sync.
5. Delete _fields_ on the device.
6. Sync.
7. Delete the _all-day event_ on the device.
8. Sync.

1. Add an _all-day event_ to the _computer_.
2. Sync.
3. Change a _all-day event to a timed event_ on the device.
4. Sync.
5. Delete _fields_ on the device.
6. Sync.
7. Delete the _timed event_ on the device.
8. Sync.

1. Add an _all-day event_ to the _computer_.
2. Sync.
3. Change the _all-day event to a recurrent all-day event_ on the device.
4. Sync.
5. Delete _fields_ on the device.
6. Sync.
7. Delete the _recurrent all-day event_ on the device.
8. Sync.

1. Add a _recurrent all-day event_ to the computer.
2. Sync.
3. Change _recurrent all-day event to a single all-day event_ on the device.
4. Sync.
5. Delete _fields_ on the device.
6. Sync.
7. Delete the _single all-day event_ on the device.
8. Sync.

Tests adding, modifying, and deleting tasks on the device and computer.

This test consolidates task mapping at a high level for tasks added and/or modified on the device.

1. Add a _task_ to the _device_.
2. Sync.
3. Modify _field values_ on device.

   For example, modify the priority, due date, completed, and notes fields.
4. Sync.
5. Delete _fields_ on the device.
6. Sync.
7. Delete the _task_ on the device.
8. Sync.

1. Add a _task_ to the _computer_.
2. Sync.
3. Modify _field values_ on device.
4. Sync.
5. Delete _fields_ on the device.
6. Sync.
7. Delete the _task_ on the device.
8. Sync.

Tests adding, modifying, and deleting recurrent all-day events on the device and computer.

1. Add a _recurrent all-day event_ to the _device_.
2. Sync.
3. Modify _field values_ on device.
4. Sync.
5. Delete the _recurrent all-day event_ on the device.
6. Sync.

1. Add a _recurrent all-day event_  to the _computer_.
2. Sync.
3. Modify all _field values_ on device.
4. Sync.
5. Delete _fields_ on device,
6. Sync.
7. Delete the _recurrent all-day event_  on the device.
8. Sync.

Tests adding, modifying, and deleting recurrent multi-day all-day events on the device and computer.

1. Add a _recurrent multi-day all-day event_ to the _device_.
2. Sync.
3. Modify _field values_ on device.
4. Sync.
5. Delete the _recurrent multi-day all-day event_ on the device.
6. Sync.

1. Add a _recurrent multi-day all-day event_ to the _computer_.
2. Sync.
3. Modify all _field values_ on device.
4. Sync.
5. Delete _fields_ on device,
6. Sync.
7. Delete the _recurrent multi-day all-day event_ on the device.
8. Sync.

Tests adding birthday events on the device and modifying them on the computer. Run this test using only devices that support birthday events.

1. Add a _birthday event_ to the _device_.
2. Perform an initial merge sync.
3. Force a slow sync.
4. Using iCal, select the birthday event in the current year and modify the subject field of the event and all future events.
5. Sync.

Tests adding many events and tasks with large notes.

1. Add many _events and tasks_—for example, 500 events and 500 tasks—with large notes to the _computer_.
2. Sync.

[Next](Miscellaneous%20Tests.md)[Previous](Contacts%20Tests.md)

