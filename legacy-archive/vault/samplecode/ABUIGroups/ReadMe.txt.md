---
title: ABUIGroups
apple_id: DTS40011307
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: AddressBook
published: '2013-07-29'
source_url: https://developer.apple.com/library/archive/samplecode/ABUIGroups/Listings/ReadMe_txt.html
archived_at: '2026-07-18T02:59:23.460610Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ABUIGroups](ABUIGroups.md)


[Next](main.m.md)[Previous](ABUIGroups.md)

# ReadMe.txt

```
ABUIGroups shows how to check and request access to a user’s address book database. It also demonstrates how to retrieve, add, and remove group records from the address book database using AddressBook APIs. It displays groups organized by their source in the address book. This sample also shows how to retrieve the name of a group and of a source.


Build Requirements:
iOS SDK 6.0 or later



Runtime Requirements:
iOS 6.0 or later



Using the Sample
The application displays a list of groups organized by sources in the address book. It first prompts a user for access to their address book database. It displays existing groups and the Add and Edit buttons if the user has granted access. Tap the Add button to add a group to the default source in the address book. Tap the Edit button to delete a group from a source. 


Packaging List

ABUIGroupsAppDelegate
The application's delegate to setup its window and content.


GroupViewController
A view controller for managing access to the address book. It is also used to display, add, and remove groups from the address book. 


AddGroupViewController
A view controller that lets the user enter a name for a new group.


MySource
A simple class to represent a source.


CHANGES FROM PREVIOUS VERSIONS:

 1.1 - Updated for iOS 6.0. Now uses ARC and storyboard. Shows how to check and request access to a user’s address book database.  
 1.0 - First version.

Copyright (c) 2011-2013 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](ABUIGroups.md)

