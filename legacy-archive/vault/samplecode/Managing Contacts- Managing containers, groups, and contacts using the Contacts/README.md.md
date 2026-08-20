---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/README_md.html
archived_at: '2026-07-18T03:14:29.378615Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](LICENSE.txt.md)[Previous](ManagingContacts-ManagingContacts-MainViewController.swift.md)

# README.md

```
# Managing Contacts
Managing containers, groups, and contacts using the Contacts framework
This sample demonstrates how to manage containers, groups, and contacts using the Contacts framework. It implements the following features:
+ Check and request access to the Contacts application and observe changes using CNContactStoreDidChangeNotification.
+ Fetch the default container, all containers, all groups per container, all contacts per container, and the container with a given identifier.
+ Fetch all groups, all contacts per group, the group with a given identifier, and the container that contains a given group.
+ Fetch all contacts, contacts matching a given name, and a contact with a given identifier.
+ Add, update, and delete contacts and groups. Describes best practices when updating and deleting them.
+ Add and remove an existing contact from an existing group.
+ Perform batching multiple changes into a single save request.
+ Show how to use CNContact's isKeyAvailable.
+ Retrieve and update the following properties of a contact: familyName, givenName,organizationName, emailAddresses, imageData, thumbnailImageData, phoneNumbers, and postalAddresses.


## Requirements

### Build

Xcode 8.0 or later; iOS 10.0 SDK or later

### Runtime

iOS 9.3 or later

## Usage
This sample requires access to Contacts and Photos services.
ManagingContacts consists of three tabs: Containers, Groups, and Contacts.
Containers allows you to fetch the default container, all containers, groups per container, and contacts per container.
Groups allows you to fetch all groups, contacts per group, add a group, update a group, delete a group, add a contact to a group, and remove a contact from a group.
Contacts allows you to fetch all contacts, contacts matching a name, add a contact, update a contact, and delete a contact.
ManagingContacts uses data from the Menu.plist file and the availability of contact, container, and group information to provide a navigation menu for each of the above tabs.
Grant access to Contacts when prompted upon launching the app. Doing so ensures that you would able to access these data. The app will not show any data if you have denied access to
Contacts. To enable Contacts access for ManagingContacts, navigate to Settings > Privacy > Contacts on your device then tap its associated switch.
See [CNContactViewController](https://developer.apple.com/reference/contactsui/cncontactviewcontroller), if you wish to add, edit, or remove your contacts via a UI.

Copyright (C) 2017 Apple Inc. All rights reserved.
```

[Next](LICENSE.txt.md)[Previous](ManagingContacts-ManagingContacts-MainViewController.swift.md)

