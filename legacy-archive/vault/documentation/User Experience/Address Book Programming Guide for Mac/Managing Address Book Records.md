---
title: Address Book Programming Guide for Mac
apple_id: 10000117i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AddressBook
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/ManagingGroups.html
archived_at: '2026-07-18T02:09:44.917147Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Address Book Programming Guide for Mac](Introduction.md)


[Next](Accessing%20Address%20Book%20Records.md)[Previous](About%20the%20Address%20Book.md)

# Managing Address Book Records

You can manage the people and groups within a user’s address book. This article explains how to obtain the user’s address book, add and remove people and groups from that address book, manage groups, find the record that corresponds to the logged-in user, and save your changes.

There are two ways to get a copy of the address book. The preferred way is to use the [ABAddressBook](https://developer.apple.com/documentation/addressbook/abaddressbook) method [addressBook](https://developer.apple.com/documentation/addressbook/abaddressbook/1529221-addressbook). The address book object that it returns should only be used on the same thread that it was created on, and can be used with the [ABPerson](https://developer.apple.com/documentation/addressbook/abperson) method [initWithAddressBook:](https://developer.apple.com/documentation/addressbook/abrecord/1400511-init).

If you're just making one-off lookups and edits, the [ABAddressBook](https://developer.apple.com/documentation/addressbook/abaddressbook) method [sharedAddressBook](https://developer.apple.com/documentation/addressbook/abaddressbook/1458758-shared) may be used. However, this method can cause a significant decrease in performance, especially in a tight loop.

For example, you can replace code such as the following:

```
for (id item in someDataStructure) {
    ABPerson* person = [[ABPerson alloc] init];
    // Populate the person from the item
}
[[ABAddressBook sharedAddressBook] save];
```

With code like the following, yielding a significant performance increase:

```
ABAddressBook* tempBook = [ABAddressBook addressBook];
for (id item in someDataStructure) {
    ABPerson* person = [[ABPerson alloc] initWithAddressBook:tempBook];
    // Populate the person from the item
}
[tempBook save];
```


The `ABAddressBook` class provides methods for accessing, adding, and removing group and person records. For example, use the [groups](https://developer.apple.com/documentation/addressbook/abaddressbook/1458440-groups) method to get an array of all the group records in the database, or the [people](https://developer.apple.com/documentation/addressbook/abaddressbook/1458683-people) method to get all the person records.

Adding a new person or group record takes the following steps:

- Get the address book. The preferred way to do this is with the [ABAddressBook](https://developer.apple.com/documentation/addressbook/abaddressbook) method [addressBook](https://developer.apple.com/documentation/addressbook/abaddressbook/1529221-addressbook).
- Create the person or group record . You must allocate and initialize the respective `ABPerson` or `ABGroup` object. The preferred initializer is [initWithAddressBook:](https://developer.apple.com/documentation/addressbook/abrecord/1400511-init).
- Add the record to the Address Book using the `ABAddressBook` method [addRecord:](https://developer.apple.com/documentation/addressbook/abaddressbook/1458749-add).

To remove a person or group, use the `ABAddressBook` method [removeRecord:](https://developer.apple.com/documentation/addressbook/abaddressbook/1458605-remove).

The Address Book framework lets you add people and subgroups to groups, as well as find out all groups that a person or subgroup is in.

To add and remove people from a group, use the [addMember:](https://developer.apple.com/documentation/addressbook/abgroup/1427932-addmember) and [removeMember:](https://developer.apple.com/documentation/addressbook/abgroup/1427940-removemember) methods. A person record can only be added to a group after it has been saved to the address book. To get a list of all the groups a person is in, use the [parentGroups](https://developer.apple.com/documentation/addressbook/abperson/1458380-parentgroups) methods.

You can also add groups to a group. For example, a user could have a group called Pet Lovers that contains the groups Dog Lovers and Cat Lovers. To add and remove groups from another group, use the [addSubgroup:](https://developer.apple.com/documentation/addressbook/abgroup/1427938-addsubgroup) and [removeSubgroup:](https://developer.apple.com/documentation/addressbook/abgroup/1427960-removesubgroup) methods. You cannot create a cycle. For example, if Dog Lovers is a subgroup of Pet Lovers, then Pet Lovers cannot be a subgroup of Dog Lovers, directly or indirectly. To get a list of all groups that another group is a subgroup of, use the [parentGroups](https://developer.apple.com/documentation/addressbook/abgroup/1427956-parentgroups) methods.

To get lists of what’s in a group, use the [members](https://developer.apple.com/documentation/addressbook/abgroup/1427934-members) and [subgroups](https://developer.apple.com/documentation/addressbook/abgroup/1427948-subgroups) methods.

The currently logged-in user can specify a record that contains information about himself or herself. That lets your application find the name, address, or phone number of the user, so you can use it when filling out forms, for example. To get the logged-in user’s record, use the `ABAddressBook` method [me](https://developer.apple.com/documentation/addressbook/abaddressbook/1458663-me). To set the logged-in user’s record, use the `ABAddressBook` [setMe:](https://developer.apple.com/documentation/addressbook/abaddressbook/1458403-setme) methods.

When you modify the Address Book database, those changes are made in memory, and not to the database itself. Unless you save those changes, they will be lost.

To save your changes to the database, use the `ABAddressBook` method [save](https://developer.apple.com/documentation/addressbook/abaddressbook/1458432-save) or [saveAndReturnError:](https://developer.apple.com/documentation/addressbook/abaddressbook/1458623-saveandreturnerror). To test whether there are unsaved changes, use the `ABAddressBook` method [hasUnsavedChanges](https://developer.apple.com/documentation/addressbook/abaddressbook/1458270-hasunsavedchanges).

The Address Book posts notifications if any application, including your own, makes changes to the database. Typically, you observe these notifications to update any dependent view or model objects in your application. The Address Book framework sends two notifications: [kABDatabaseChangedNotification](https://developer.apple.com/documentation/addressbook/kabdatabasechangednotification) to indicate that the current process has made a change, and [kABDatabaseChangedExternallyNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1458671-abdatabasechangedexternally) to indicate that another process has made a change. Use [NSNotificationCenter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/cl/NSNotificationCenter) to register for the notifications you are interested in. Note that these notifications are not sent until after the [sharedAddressBook](https://developer.apple.com/documentation/addressbook/abaddressbook/1458758-shared) method of the `ABAddressBook` class or the C function [ABGetSharedAddressBook](https://developer.apple.com/documentation/addressbook/1430178-abgetsharedaddressbook) has been invoked.

If your application is using the shared address book object (returned by the [sharedAddressBook](https://developer.apple.com/documentation/addressbook/abaddressbook/1458758-shared) method), the changes have already been merged in automatically and are available immediately when you receive the change notification. Non-shared address book objects (returned by the[addressBook](https://developer.apple.com/documentation/addressbook/abaddressbook/1529221-addressbook) method) are generally used only for short time, and do not process change notifications automatically.

This Objective-C example adds a person named John Doe to the current user’s address book. Take note of how the code accesses the shared address book and how it allocates a new `ABPerson` object. Also note the properties used (in this case, just first name and last name), and the final save, which sends the changes to the user’s address book:

```
ABAddressBook *addressBook;
ABPerson *newPerson;

addressBook = [ABAddressBook sharedAddressBook];

newPerson = [[ABPerson alloc] init];

[newPerson setValue:@"John"
        forProperty:kABFirstNameProperty];

[newPerson setValue:@"Doe"
        forProperty:kABLastNameProperty];

[addressBook addRecord:newPerson];
[addressBook save];
```

[Next](Accessing%20Address%20Book%20Records.md)[Previous](About%20the%20Address%20Book.md)

