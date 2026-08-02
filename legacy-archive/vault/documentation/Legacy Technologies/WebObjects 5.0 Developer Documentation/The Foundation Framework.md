---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Introduction.html
archived_at: '2026-07-15T08:13:56.901195Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](FoundationTOC.md)

# The Foundation Framework

> **__Package:__**
> : com.webobjects.foundation

---

## Introduction

The Foundation Framework defines a base layer of classes written in Java. In addition to providing a set of useful primitive object classes, it introduces several paradigms that define functionality not covered by the Java language. The Foundation Framework is designed with these goals in mind:

- Provide a small set of basic utility classes
- Simplifies software development by introducing consistent conventions for things such as notifications, object persistence, key-value coding, and validation.
- Provide a level of OS independence, to enhance portability

This version of the Foundation framework is similar to the WebObjects 4.5 Foundation framework (com.apple.yellow.foundation) but does not rely on the Java Bridge because it is written in pure Java. The API for the pure Java Foundation also follows conventions in Sun's API more closely than the WebObjects 4.5 Foundation.

The pure Java Foundation resembles the WebObjects 4.5 Java Client Foundation (com.apple.client.foundation) but provides a larger set of functions.

### Foundation Framework Classes

The Foundation Framework consists of several related groups of classes as well as a few individual classes:

- Data storage. [NSData](NSData.md#apple-incuqrsjizdui) provides object-oriented storage for arrays of bytes. [NSArray](NSArray.md#apple-ijbuqr2ei5cum), [NSDictionary](NSDictionary.md#apple-incumskiiffeu), and [NSSet](NSSet.md#apple-ineeissfijauc) provide storage for objects of any class.
- Dates and times. The NSTimestamp and NSTimeZone classes store times and dates. They offer methods for calculating date and time differences, for displaying dates and times in many formats, and for adjusting times and dates based on location in the world. The NSTimestampFormatter class converts dates to user-presentable strings and back.
- Application coordination and timing. [NSNotification](NSNotification.md#apple-ijduorkhjjauu) and [NSNotificationCenter](NSNotificationCenter.md#apple-inauqrsfjbcuu) provide systems that an object can use to notify all interested observers of changes that occur. [NSDelayedCallbackCenter](NSDelayedCallbackCenter.md#apple-ineeer2fizbeq) coordinates events.
- Object distribution and persistence. The data that an object contains can be represented in an architecture-independent way using [NSCoder](NSCoder.md#apple-ijeugr2jivduo) and its subclasses, which also stores class information along with the data. The resulting representations are used for archiving and object distribution.
- Object disposal. The [NSDisposable](NSDisposable.md#apple-ijbesq2gineuc) interface together with the [NSDisposableRegistry](NSDisposableRegistry.md#apple-incumq2eifdek) ensure that unused objects are collected by Java's garbage collector.
- Key-value coding. The [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu) and [NSKeyValueCodingAdditions](NSKeyValueCodingAdditions.md#apple-inbemssiinbek) interfaces along with their support classes provide a consistent way for objects to receive and return values for keys.
- Validation. The [NSValidation](NSValidation.md#apple-infemrcejfeec) interface and support classes define and implement a consistent validation mechanism.
- Locking of objects. The [NSLock](NSLock.md#apple-ineukqsjifeeo), [NSRecursiveLock](NSRecursiveLock.md#apple-inbekrkkjffem), and [NSMultiReaderLock](NSMultiReaderLock.md#apple-incueq2kizfeu) classes together with the [NSLocking](NSLocking.md#apple-ineegssbi5euk) interface coordinate the locking of objects or graphs of objects.
- Operating system services. Several classes are designed to insulate you from the idiosyncracies of various operating systems. [NSPathUtilities](NSPathUtilities.md#apple-ijbuiscfjfaui) provides a consistent interface for working with file system paths. [NSBundle](NSBundle.md#apple-infeiq2diveuq) accesses the application's resources.
- Other utility classes. [NSRange](NSRange.md#apple-ijfeoscei5eeg) specifies a range of values. [NSComparator](NSComparator.md#apple-ijeugsshizeec) defines inequality relationships between objects for sorting. [NSUndoManager](NSUndoManager.md#apple-ijbesrcginbeo) manages an application's undo function. [NSForwardException](NSForwardException.md#apple-ijduqrkfjfcuk) wraps exceptions into a subclass of Java's RuntimeException. [NSPropertyListSerialization](NSPropertyListSerialization.md#apple-inbusscdivcec) converts between property lists and byte arrays.

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
