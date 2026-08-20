---
title: Getting Started with Data Management
apple_id: TP40009046
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2011-01-27'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_DataManagement_MacOSX/_index.html
archived_at: '2026-07-18T02:39:21.420585Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)



## Introduction

### Overview

Most Mac apps need to manage data. Data management involves the creation and handling of the various types of data available to a program, including strings, rich text, binary data, dates, [collections](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10), [property lists](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44), and XML data. Mac apps use data management interfaces to store and access data in local databases, files, folders, and bundles. They also use data management interfaces to receive and respond appropriately to events and other types of messages, such as [notifications](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35).

OS X data management interfaces reside in several different [frameworks](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56). The principal frameworks are:

- Foundation—An Objective-C framework that defines a base layer of classes that can be used for any type of OS X program. Foundation classes provide object wrappers or equivalents for primitives such as numeric values, strings, and collections. Foundation also includes utility classes for accessing underlying system entities and services, such as ports, threads, and file systems. The Foundation API is documented in [Foundation Framework Reference](https://developer.apple.com/documentation/foundation).
- Application Kit—An Objective-C framework that provides the key infrastructure for implementing graphical, event-driven applications in OS X. Application Kit includes such classes as `NSResponder`, `NSApplication`, and `NSEvent` to manage user interface data. The Application Kit API is documented in [Application Kit Framework Reference](https://developer.apple.com/documentation/appkit).
- Core Data—A generalized framework for [object graph](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectGraph.html#//apple_ref/doc/uid/TP40008195-CH54) management and persistence. Core Data includes support for features such as undo and redo, change propagation—including maintaining the consistency of relationships among objects, and storing objects in external data repositories. The Core Data API is documented in [Core Data Framework Reference](https://developer.apple.com/documentation/coredata).
- Address Book—The Address Book framework allows you to retrieve information from and add your own properties to the people and groups in the contacts database. The Address Book API is documented in [Address Book Objective-C Framework Reference](https://developer.apple.com/documentation/addressbook).
- Core Foundation—A set of programming interfaces conceptually derived from the Foundation framework but implemented in the C language. Core Foundation defines opaque types for data objects such as strings, collections, time and dates, ports, application run loops, interprocess communication, and preferences. The Core Foundation API is documented in [Core Foundation Framework Reference](https://developer.apple.com/documentation/corefoundation).

### Data Management

The following sections describe different areas of data management and the documentation you should read to learn more about them.

#### Basic Values

Cocoa provides object abstractions for the basic data types you’re likely to use in almost any program, such as strings, dates, numbers, and even binary data. It also provides collection classes and other abstractions to group values together. To learn about these data types, read:

- [String Programming Guide](../../documentation/Cocoa/String%20Programming%20Guide/Introduction%20to%20String%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaztk2i)
- [Number and Value Programming Topics](../../documentation/Cocoa/Number%20and%20Value%20Programming%20Topics/Introduction%20to%20Numbers%20and%20Other%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaztq2i)
- [Date and Time Programming Guide](../../documentation/Cocoa/Date%20and%20Time%20Programming%20Guide/About%20Dates%20and%20Times.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazts2i)
- [Binary Data Programming Guide](../../documentation/Cocoa/Binary%20Data%20Programming%20Guide/Introduction%20to%20Binary%20Data%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazto2i)
- [Collections Programming Topics](../../documentation/Cocoa/Collections%20Programming%20Topics/About%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazti2i)
- [Property List Programming Guide](../../documentation/Cocoa/Property%20List%20Programming%20Guide/Introduction%20to%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2i)

#### Storing Application Data

Cocoa provides several ways to save your application’s data. The technology you choose depends on how much data you want to save, and what sort of data it is.

- To learn how to use property lists to save simple collections and basic values, read [Property List Programming Guide](../../documentation/Cocoa/Property%20List%20Programming%20Guide/Introduction%20to%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2i).
- To learn how to create archives of [object graphs](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectGraph.html#//apple_ref/doc/uid/TP40008195-CH54), read [Archives and Serializations Programming Guide](../../documentation/Cocoa/Archives%20and%20Serializations%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2do2i).
- To learn how you can use Core Data for persistence, as well as sophisticated object graph management, read Core Data Overview.
- To learn how to manage application preferences—also known as user defaults—read [Preferences and Settings Programming Guide](../../documentation/Cocoa/Preferences%20and%20Settings%20Programming%20Guide/About%20Preferences%20and%20Settings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2ts2i) .

#### Handling Events

In addition to input from mouse and keyboard, OS X OS supports input from tablets and, on a portable Macintosh, multi-touch using a trackpad.

- Read [Event Handling](../../documentation/General/Mac%20App%20Programming%20Guide/The%20Core%20App%20Design.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbtfvbuqmznknltcny)h in [Mac App Programming Guide](../../documentation/General/Mac%20App%20Programming%20Guide/About%20OS%20X%20App%20Design.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbt), then [Cocoa Event Handling Guide](../../documentation/Cocoa/Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i).

#### Accessing Contact Information

Address Book is a centralized database for contacts and other personal information. Contact information is important for software such as email and chat programs.

- Read [Address Book Programming Guide for Mac](../../documentation/User%20Experience/Address%20Book%20Programming%20Guide%20for%20Mac/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyto2i) to learn how to leverage the contacts database in your application. You can not only access a user’s contact data but also design and implement your own properties and actions for the data.

#### Locating Application Data

OS X provides a number of standard directories where application data might reside. Cocoa provides classes and methods to help you to locate these directories on the filesystem and as resources within your application.

- Read [Locating Directories on the System](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LowLevelFileMgmt/Articles/StandardDirectories.html#//apple_ref/doc/uid/20001279) in [Low-Level File Management Programming Topics](../../documentation/Cocoa/Low-Level%20File%20Management%20Programming%20Topics/Introduction%20to%20Low-Level%20File%20Management%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tk2i) to learn about standard directories.
- Read [Bundle Programming Guide](../../documentation/Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i) to learn how applications and file packages are stored on disk and how you can access them.

