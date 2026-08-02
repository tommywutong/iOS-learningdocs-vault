---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/Java/util/Description.html
archived_at: '2026-07-15T07:55:41.440975Z'
---
> 导航：[总目录](../../../../../../../../../README.md) · 未编入索引的页面


# Package next.util

## PACKAGE DESCRIPTION

Package __next.util__ brings to Java some of the most useful classes from NeXT's Foundation Framework. The Foundation Framework, in turn, defines a base layer of classes for OpenStep.

The Foundation Framework includes the root object class, classes representing basic data types such as numbers and byte arrays, collections of other objects, and classes representing system information such as dates.

### next.util Classes and Interfaces

The OpenStep class hierarchy is rooted in the NextObject class. The remainder of the package consists of several related groups of classes as well as a few individuals.
Many of these classes have closely related functionality:

**Data storage**
: ImmutableBytes provides object-oriented storage for arrays of bytes. DecimalNumber provides object-oriented storage for decimal data values. ImmutableVector, MutableVector, ImmutableHashtable, and MutableHashtable provide storage for objects of any class.

**Dates and times**
: The Date and CalendarDate classes store times and dates. They offer methods for calculating date and time differences, for displaying dates and times in many formats, and for adjusting times and dates based on location in the world.

**Object  persistence**
: Coder and its subclasses allow the data that an object contains, along with class information, to be stored  in an architecture-independent way.
