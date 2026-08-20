---
title: QuickContacts
apple_id: DTS40009475
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: AddressBook
published: '2014-07-17'
source_url: https://developer.apple.com/library/archive/samplecode/QuickContacts/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:21:41.789426Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QuickContacts](QuickContacts.md)


[Next](main.m.md)[Previous](QuickContacts.md)

# ReadMe.txt

```
QuickContacts demonstrates how to use the Address Book UI controllers and various properties such as displayedProperties, allowsAddingToAddressBook, and displayPerson.

This sample also shows how to: 
-Browse a list of Address Book contacts and allow users to choose a contact from that list.
-Display and edit information associated with a selected contact. 
-Prevent users from performing default actions such as dialing a phone number associated with a selected information.
-Create a new contact record.
-Update a partial contact record.
-Present and dismiss the people picker, person view controller, new-person view controller, and unknown-person view controller.


Build Requirements:
iOS SDK 6.0 or later


Runtime Requirements:
iOS 6.0 or later


Using the Sample
The application displays four cells labeled "Display Picker," "Create New Contact," "Display and Edit Contact," and "Edit Unknown Contact." Tap "Display Picker" to browse a list of contacts and choose a person from that list. Tap "Create New Contact" to create a new person. Tap "Display and Edit Contact" to display and edit a person. Tap "Edit Unknown Contact" to add data to an existing person or use them to create a new person.


Packaging List
main.m - Main source file for this sample.

QuickContactsAppDelegate.h
QuickContactsAppDelegate.m
The application's delegate to setup its window and content.

QuickContactsViewController.h
QuickContactsViewController.m
A view controller for managing the table.

Main.storyboard
The storyboard file containing a table view controller.


Changes from Previous Versions
1.0 - First version.
1.1 - Upgraded project to build with the iOS 4.0 SDK.
1.2 - Updated for iOS 6.0, now uses ARC, and shows how to check and request access to a user’s address book database.  
1.3 - Updated to support Storyboards.

Copyright (c) 2010-2014 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](QuickContacts.md)

