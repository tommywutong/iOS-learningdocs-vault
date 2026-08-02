---
title: Address Book Programming Guide for iOS
apple_id: TP40007744
resource_type: Guide
platform: iOS
topic: Data Management
technology: AddressBookUI
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/ContactData/Conceptual/AddressBookProgrammingGuideforiPhone/Introduction.html
archived_at: '2026-07-15T07:22:03.671665Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](Quick%20Start%20Tutorial.md)

# Introduction

The Address Book technology for iOS provides a way to store people’s contact information and other personal information in a centralized database, and to share this information between applications. The technology has several parts:

- The Address Book framework provides access to the contact information.
- The Address Book UI framework provides the user interface to display the information.
- The Address Book database stores the information.
- The Contacts application provides a way for users to access their contact information.

This document covers the key concepts of the Address Book technology and explains the basic operations you can perform. When you add this technology to your application, users will be able to use the contact information that they use in other applications, such as Mail and Text, in your application. This document tells you how to do the following:

- Access the user’s Address Book database
- Prompt the user for contact information
- Display contact information to the user
- Make changes to the user’s Address Book database

To get the most out of this document, you should already understand navigation controllers and view controllers, and understand delegation and protocols.

This document contains the following chapters:

- [Quick Start Tutorial](Quick%20Start%20Tutorial.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tonbufvbuqmrnknltc) gets you up and running by showing you how to create a simple application that uses the Address Book technology.
- [Building Blocks: Working with Records and Properties](Building%20Blocks-%20Working%20with%20Records%20and%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tonbufvbuqmznknltc) describes how to create an address book object, how to create person and group records, and how to get and set properties.
- [User Interaction: Prompting for and Displaying Data](User%20Interaction-%20Prompting%20for%20and%20Displaying%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tonbufvbuqnjnknltc) describes how to use the views provided by the Address Book UI framework to display a contact, let the user select a contact, create a new contact, and edit a contact.
- [Direct Interaction: Programmatically Accessing the Database](Direct%20Interaction-%20Programmatically%20Accessing%20the%20Database.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tonbufvbuqnrnknltc) describes the ways your application can read and write contact information directly.

The following documents discuss some of the fundamental concepts you should understand in order to get the most out of this document:

- _[App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072)_ guides developers who are new to the iOS platform through the available technologies and how to use them to build applications. It includes relevant discussion of windows, views, and view controllers.
- _[Interface Builder User Guide](../Developer%20Tools/Interface%20Builder%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbu)_ explains how to use Interface Builder to create applications. It includes relevant discussion of the user interface for an application and making connections from the interface to the code.
- _[Programming with Objective-C](../Cocoa/Programming%20with%20Objective-C/About%20Objective-C.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjq)_ discuss many basic concepts you will need to write any application. It includes relevant discussion of delegation and protocols.

The following documents contain additional information about the Address Book frameworks:

- _Address Book Framework Reference for iOS_ describes the API for direct interaction with records in the Address Book database.
- _[Address Book UI Framework Reference for iOS](https://developer.apple.com/documentation/addressbookui)_ describes the controllers that facilitate displaying, editing, selecting, and creating records in the Address Book database, and their delegate protocols.
[Next](Quick%20Start%20Tutorial.md)

