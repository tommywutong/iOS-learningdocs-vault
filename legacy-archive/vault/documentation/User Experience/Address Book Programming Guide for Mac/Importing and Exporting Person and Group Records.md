---
title: Address Book Programming Guide for Mac
apple_id: 10000117i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AddressBook
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/ImportingExportingPeople.html
archived_at: '2026-07-18T02:09:44.363770Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Address Book Programming Guide for Mac](Introduction.md)


[Next](Showing%20Records%20in%20the%20Contacts%20App.md)[Previous](Creating%20and%20Using%20Address%20Book%20Action%20Plug-ins.md)

# Importing and Exporting Person and Group Records

You can import and export person records using the vCard format. To create a vCard representation of a person, use the [ABPerson](https://developer.apple.com/documentation/addressbook/abperson) method [vCardRepresentation](https://developer.apple.com/documentation/addressbook/abperson/1458307-vcardrepresentation). This method creates an `NSData` structure that you can use in your program or save to a file. To enable drag and drop for this data, use a file promise as described in [Dragging Files](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/Tasks/DraggingFiles.html#//apple_ref/doc/uid/20001288).

To create a person record from a vCard representation, use the [ABPerson](https://developer.apple.com/documentation/addressbook/abperson) method [initWithVCardRepresentation:](https://developer.apple.com/documentation/addressbook/abperson/1458755-initwithvcardrepresentation).

[Next](Showing%20Records%20in%20the%20Contacts%20App.md)[Previous](Creating%20and%20Using%20Address%20Book%20Action%20Plug-ins.md)

