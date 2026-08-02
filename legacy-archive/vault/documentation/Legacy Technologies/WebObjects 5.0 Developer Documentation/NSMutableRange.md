---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSMutableRange.html
archived_at: '2026-07-15T08:13:56.281505Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

# NSMutableRange

> **__Inherits from:__**
> : [NSRange](NSRange.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpjzjveylom5sq): Object

> **__Implements:__**
> : Cloneable

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

An NSMutableRange is an object representing a range that can be changed. A range is a measurement of a segment of something linear, such as a byte stream. You can change an NSMutableRange's two primary values, its location and its length. The methods of NSMutableRange also enable you to alter an NSMutableRange based on its union or intersection with another NSRange object.

The main purpose for NSMutableRange is to provide a way for methods to return range values in an "out" parameter. A client creates and passes in one or more NSMutableRanges to a method and gets back changed objects when the method returns. NSMutableRanges are also useful for performance reasons; instead of creating multiple NSRanges in a loop, you can create just one NSMutableRange and reuse it.

[Table 0-10](#apple-ijbuqskkincec) describes the NSMutableRange methods that provide the basis for all NSMutableRange's other methods; that is, all other methods are implemented in terms of these four. If you create a subclass of NSMutableRange, you need only ensure that these base methods work properly. Having done so, you can be sure that all your subclass's inherited methods operate properly.

__Table 0-10 NSMutableRange's Base API__

| __Method__ | __Description__ |
| [location](NSRange.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5wg6y3boruw63q) | Returns the starting location of the receiver. Inherited from [NSRange](NSRange.md#apple-ijfeoscei5eeg). |
| [length](NSRange.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5wgk3thorua) | Returns the length of the receiver from its starting location. Inherited from [NSRange](NSRange.md#apple-ijfeoscei5eeg). |
| [setLength](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsveylom5ss643forggk3thorua) | Sets the length of the receiver. |
| [setLocation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsveylom5ss643forgg6y3boruw63q) | Sets the starting location of the receiver. |

## Interfaces Implemented

---

> : Cloneable
>
> : [clone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsveylom5ss6y3mn5xgk)
>
> :

## Method Types

---

> **Constructors**
>
> : [NSMutableRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsveylom5ss6tstjv2xiylcnrsveylom5sq)
>
> **Accessing and setting range elements**
>
> : [setLength](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsveylom5ss643forggk3thorua): [setLocation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsveylom5ss643forgg6y3boruw63q)
>
> **Transforming ranges**
>
> : [intersectRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsveylom5ss62loorsxe43fmn2feylom5sq): [unionRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsveylom5ss65lonfxw4utbnztwk)
>
> **Methods inherited from Object**
>
> : [clone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsveylom5ss6y3mn5xgk)

## Constructors

---

### NSMutableRange

`public NSMutableRange()`

Creates and returns an empty NSMutableRange.

`public NSMutableRange(NSRange aRange)`

Creates a new NSMutableRange with the location and length values of _aRange_. This constructor is used in cloning the receiver.

`public NSMutableRange( int location, int length)`

Creates a new NSMutableRange with the range elements of _location_ and _length_. Throws an IllegalArgumentException if either integer is negative.

---

## Instance Methods

---

### clone

`public Object clone()`

Returns a copy (a NSMutableRange object) of the receiver.

---

### intersectRange

`public void intersectRange(NSRange aRange)`

Changes the receiver to the range resulting from the intersection of _aRange_ and the receiver before the operation. Sets the receiver to an empty range if they do not intersect.

__See Also:__ [unionRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsveylom5ss65lonfxw4utbnztwk)

---

### setLength

`public void setLength(int newLength)`

Sets the length of the receiver to _newLength_. Throws an IllegalArgumentException if _newLength_ is a negative value.

__See Also:__ [setLocation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsveylom5ss643forgg6y3boruw63q)

---

### setLocation

`public void setLocation(int newLocation)`

Sets the starting location of the receiver to _newLocation_. Throws an IllegalArgumentException if _newLocation_ is a negative value.

__See Also:__ [setLength](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsveylom5ss643forggk3thorua)

---

### unionRange

`public void unionRange(NSRange aRange)`

Changes the receiver to the range resulting from the union of _aRange_ and the receiver before the operation. This is the lowest starting location and the highest ending location of the two NSRanges.

__See Also:__ [intersectRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsveylom5ss62loorsxe43fmn2feylom5sq)

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
