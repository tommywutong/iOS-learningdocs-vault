---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Description.html
archived_at: '2026-07-15T07:55:47.978742Z'
---
> 导航：[总目录](../../../../../../../../../README.md) · 未编入索引的页面


#  The Foundation Framework

__Framework:__
NextLibrary/Frameworks/Foundation.framework

__Header File Directories:__
NextLibrary/Frameworks/Foundation.framework/Headers

##  Introduction

The Foundation Framework defines a base layer of Objective-C classes for OpenStep. In addition to providing a set of useful primitive object classes, it introduces several paradigms that define functionality not covered by the Objective-C language. The Foundation Framework is designed with these goals in mind:

- Provide a small set of basic utility classes
- Make software development easier by introducing consistent conventions for things such as deallocation
- Support Unicode strings, object persistence, and object distribution
- Provide a level of OS independence, to enhance portability

The Foundation Framework includes the root object class, classes representing basic data types such as strings and byte arrays, collection classes for storing other objects, classes representing system information such as dates, and classes representing communication ports. See XREF for a list of those classes that make up the Foundation Framework.

The Foundation Framework introduces several paradigms to avoid confusion in common situations, and to introduce a level of consistency across class hierarchies. This is done with some standard policies, such as that for object ownership (that is, who is responsible for disposing of objects), and with abstract classes like NSEnumerator. These new paradigms reduce the number of special and exceptional cases in API and allow you to code more efficiently by reusing the same mechanisms with various kinds of objects.

###  Foundation Framework Classes

The OpenStep class hierarchy is rooted in the Foundation Framework's NSObject class (see [Figure 1](#apple-gy2a)). The remainder of the Foundation Framework consists of several related groups of classes as well as a few individual classes. Many of the groups form what are called class clusters-abstract classes that work as umbrella interfaces to a versatile set of private subclasses. NSString and NSMutableString, for example, act as brokers for instances of various private subclasses optimized for different kinds of storage needs. Depending on the method you use to create a string, an instance of the appropriate optimized class will be returned to you.

__Figure 1__
The Foundation Framework class hierarchy

!

Many of these classes have closely related functionality:

- `Data storage`. NSData and NSString provide object-oriented storage for arrays of bytes. NSValue and NSNumber provide object-oriented storage for arrays of simple C data values. NSArray, NSDictionary, NSPPL, and NSSet provide storage for Objective-C objects of any class.
- `Text and strings`. NSCharacterSet represents various groupings of characters which are used by the NSString and NSScanner classes. The NSString classes represent text strings and provide methods for searching, combining, and comparing strings. An NSScanner object is used to scan numbers and words from an NSString object.
- `Dates and times`. The NSDate and NSTimeZone classes store times and dates. They offer methods for calculating date and time differences, for displaying dates and times in many formats, and for adjusting times and dates based on location in the world.
- `Application coordination and timing`. NSNotification, NSNotificationCenter, and NSNotificationQueue provide systems that an object can use to notify all interested observers of changes that occur. You can use a NSTimer object to send a message to another object at specific intervals.
- `Object creation and disposal`. NSAutoreleasePools are used to implement the delayed-release feature of the Foundation Framework.
- `Object distribution and persistence`. The data that an object contains can be represented in an architecture-independent way using NSSerializer. The NSCoder and its subclasses take this process a step further by allowing class information to be stored along with the data. The resulting representations are used for archiving and for object distribution.
- `Operating system services`. Several classes are designed to insulate you from the idiosynccracies of various operating systems. NSFileManager provides a consistent interface for file operations (creating, renaming, deleting, and so on). NSThread and NSProcessInfo let you create multi-threaded applications and query the environment in which an application runs.

_Copyright © 1997, Apple Computer, Inc. All rights
reserved._
