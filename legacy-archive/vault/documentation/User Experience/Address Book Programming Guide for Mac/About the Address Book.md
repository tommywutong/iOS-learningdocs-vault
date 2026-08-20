---
title: Address Book Programming Guide for Mac
apple_id: 10000117i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AddressBook
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Concepts/WhatsInAB.html
archived_at: '2026-07-18T02:09:41.156128Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Address Book Programming Guide for Mac](Introduction.md)


[Next](Managing%20Address%20Book%20Records.md)[Previous](Introduction.md)

# About the Address Book

The Address Book framework uses a centralized database for contact and other personal information for people. Users only need to enter this information once, instead of entering it repeatedly whenever it is used. Applications that support the Address Book framework share this contact information with other applications, including Mail and Messages. Every user on the computer has one and only one address book. Every application shares the address book for the currently logged-in user.

The Address Book framework supports two fundamental kinds of records: [ABPerson](https://developer.apple.com/documentation/addressbook/abperson), for individuals, and [ABGroup](https://developer.apple.com/documentation/addressbook/abgroup), for groups. Both are subclasses of the same root class, [ABRecord](https://developer.apple.com/documentation/addressbook/abrecord), and they can be used interchangeably in some places.

An `ABPerson` record contains properties such as the person’s name, company, addresses, email addresses, phone numbers, instant messaging IDs, and a comments field.

An `ABGroup` object can contain any number of people and other groups; a person can be in any number of groups. For example, suppose you are a consultant who works with two companies, Acme Co. and Ajax Inc. You could set up an Acme employees group and an Ajax employees group, and make each company’s employees members of their respective group. You could then set up a Professionals group that includes the Acme group, the Ajax group, all well as some additional people who aren’t in either group.

In addition, group and person records have these characteristics:

- __Each group and person has a unique identifier.__ It’s set when the record is created, and guaranteed never to change even if a user changes the group’s or person’s name or other information. Use this identifier if your application needs to store a reference to a group or person. For more information, see the [ABRecord](https://developer.apple.com/documentation/addressbook/abrecord) method [uniqueId](https://developer.apple.com/documentation/addressbook/abrecord/1400515-uniqueid).
- __The groups and people are stored in an extensible form.__ As such, you can add custom properties to Address Book records that other applications will ignore, without worrying about data corruption or usability issues. For more information, see [Adding Properties to Address Book Records](Adding%20Properties%20to%20Address%20Book%20Records.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgazdmlkcifbeqscjjbbq).
- __Some of these properties can contain multiple values.__ For example, a person can have any number of street addresses, phone numbers, and email addresses. For more information, see [Using Multivalue Lists](Accessing%20Address%20Book%20Records.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgazdgljrgaztambv).

The Address Book framework manages individual search queries using [ABSearchElement](https://developer.apple.com/documentation/addressbook/absearchelement) objects, which can be created using class methods of `ABGroup` and `ABPerson`. This has an important implication—because the search objects are created using the these particular classes, a custom subclass of `ABRecord` will not contain the required methods to create such an object. For this reason, you are advised not to subclass `ABRecord`.

For more information about searching Address Book records, see [Searching an Address Book](Searching%20an%20Address%20Book.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgazdilkcifbeqscjjbbq).

The Address Book framework:

- __Allows the user to control access to their contacts data.__ Before your application is allowed to access the user’s data in the Address Book database, the user is asked whether to grant it access. Your application specifies its reason for accessing the database by setting the value of the `NSContactsUsageDescription` key in its Info.plist file.

  If the user grants access, your application can access the database as usual. If the user denies access, the [addressBook](https://developer.apple.com/documentation/addressbook/abaddressbook/1529221-addressbook) and [sharedAddressBook](https://developer.apple.com/documentation/addressbook/abaddressbook/1458758-shared) methods of `ABAddressBook` return `nil`.
- __Provides transparent record locking.__ If two applications try to change the same property within a record at the same time, the application that saved its change last will succeed. The database will not be corrupted. If two applications change different properties of the same record, both changes are expected to succeed.
- __Does not provide any security above what’s provided by OS X.__ Anyone who has read and write access to a user’s home folder can also read and write that user’s address book. For that reason, the Address Book may not be an appropriate place to store confidential information, such as credit card numbers.
- __Provides localized versions of the built-in property names and labels.__ If you add properties or labels, you must provide your own way for localizing them.
- __Syncs its records to iCloud.__ The Address Book framework uses the CardDav protocol to sync the data stored in the default properties to web services such as iCloud. Applications must not try to sync this data.

[Next](Managing%20Address%20Book%20Records.md)[Previous](Introduction.md)

