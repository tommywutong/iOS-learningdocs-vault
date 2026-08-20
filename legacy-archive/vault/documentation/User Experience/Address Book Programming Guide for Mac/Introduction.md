---
title: Address Book Programming Guide for Mac
apple_id: 10000117i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AddressBook
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/AddressBook.html
archived_at: '2026-07-18T02:09:40.076755Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20the%20Address%20Book.md)

# Introduction

Address Book is a technology that encompasses a centralized database for contact and group information, an application for viewing that information, and a programmatic interface for accessing that information in your own applications. The database contains information such as user names, street addresses, email addresses, phone numbers, and distribution lists. Applications that use the Address Book framework can share this contact information with other applications, including Mail and Messages, or extend it to include application-specific information.

In addition to the Objective-C interface described in this book, the Address Book framework also provides a C interface. This document points out fundamental differences between the two as appropriate, but the majority of the code samples are written in Objective-C only. Developers using the C programming interface should refer to [Using the Address Book C API](Using%20the%20Address%20Book%20C%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgy4talkciffeosskifea) and _Address Book C Framework Reference for Mac_ for information about mapping the Objective-C code to C.

This document is designed for anyone who wants to leverage the abilities of the OS X Address Book technology in their application. You should read it to learn how to access a user’s address book, add new properties to the address book database, and create action plug-ins for the Address Book application.

It is expected that you are already familiar with Xcode and the basics of Mac app development.

The document contains the following articles:

- [About the Address Book](About%20the%20Address%20Book.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgazdclkciffeosskifea) describes what’s in the Address Book database and what you can do with it.
- [Managing Address Book Records](Managing%20Address%20Book%20Records.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgazdelkcifbeqscjjbbq) describes how to add and remove people and groups, how to arrange people into groups, and how to find the record for the logged-in user.
- [Accessing Address Book Records](Accessing%20Address%20Book%20Records.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgazdglkcifbeqscjjbbq) describes how to access data in a person or group record.
- [Searching an Address Book](Searching%20an%20Address%20Book.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgazdilkcifbeqscjjbbq) describes how to perform searches on a user’s address book.
- [Using Address Book Groups as Distribution Lists](Using%20Address%20Book%20Groups%20as%20Distribution%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgazdklkcifbeqscjjbbq) describes how to set up a group so you can use it as a mailing list, or other type of distribution list.
- [Adding Properties to Address Book Records](Adding%20Properties%20to%20Address%20Book%20Records.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgazdmlkcifbeqscjjbbq) describes how to customize an address book for your own applications by adding properties to it.
- [Creating and Using Address Book Action Plug-ins](Creating%20and%20Using%20Address%20Book%20Action%20Plug-ins.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgy4dclkcineuirsiizeq) describes how to create action plug-ins which allow users to perform custom actions on address book data viewed within the Address Book application.
- [Importing and Exporting Person and Group Records](Importing%20and%20Exporting%20Person%20and%20Group%20Records.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgazdolkcineuirsiizeq) describes how to import and export person records by using the vCard standard.
- [Using the Address Book C API](Using%20the%20Address%20Book%20C%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgy4talkciffeosskifea) contains special information for those using the Address Book C API.

- _[Identity Services Programming Guide](../../Networking/Identity%20Services%20Programming%20Guide/Introduction%20to%20Identity%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diojq)_ discusses a way to manage groups of users on a local system, including standard login accounts and sharing accounts.
[Next](About%20the%20Address%20Book.md)

