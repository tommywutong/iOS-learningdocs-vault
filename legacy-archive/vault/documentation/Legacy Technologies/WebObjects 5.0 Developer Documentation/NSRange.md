---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSRange.html
archived_at: '2026-07-15T08:13:56.460719Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSRange

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : Cloneable: Serializable

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

An NSRange represents a range, a measurement of a segment of something linear, such as a byte stream. An NSRange has two primary values, a location and a length. The methods of NSRange give access to these values, convert between NSRanges and their string representations, test and compare ranges, and create ranges based on operations involving the union, intersection, and subtraction of two ranges.

[Table 0-12](#apple-ijbuqskkincec) describes the NSRange methods that provide the basis for all NSRange's other methods; that is, all other methods are implemented in terms of these two. If you create a subclass of NSRange, you need only ensure that these base methods work properly. Having done so, you can be sure that all your subclass's inherited methods operate properly.

__Table 0-12 NSRange's Base API__

| __Method__ | __Description__ |
| [length](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5wgk3thorua) | Returns the length of the receiver from its starting location. |
| [location](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5wg6y3boruw63q) | Returns the starting location of the receiver. |

## Constants

---

NSRange provides the following constant as a convenience; you can use it to compare values returned by some NSRange methods:

|  |  |  |
| --- | --- | --- |
| __Constant__ | __Type__ | __Description__ |
| ZeroRange | NSRange | An NSRange set to zero in location and length. |

## Interfaces Implemented

---

> : Cloneable
>
> : [clone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5rwy33omu)
>
> :

## Method Types

---

> **Constructors**
>
> : [NSRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5hfgutbnztwk)
>
> **Accessing range elements**
>
> : [length](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5wgk3thorua): [location](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5wg6y3boruw63q)
>
> **Manipulating ranges**
>
> : [rangeByIntersectingRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5zgc3thmvbhssloorsxe43fmn2gs3thkjqw4z3f): [rangeByUnioningRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5zgc3thmvbhsvlonfxw42lom5jgc3thmu): [subtractRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5zxkytuojqwg5csmfxgozi)
>
> **Testing ranges**
>
> : [containsLocation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5rw63tumfuw442mn5rwc5djn5xa): [intersectsRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5uw45dfojzwky3uonjgc3thmu): [isEmpty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5uxgrlnob2hs): [isEqualToRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5uxgrlrovqwyvdpkjqw4z3f): [isSubrangeOfRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5uxgu3vmjzgc3thmvhwmutbnztwk): [locationInRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5wg6y3boruw63sjnzjgc3thmu): [maxRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5wwc6csmfxgozi)
>
> **Methods inherited from Object**
>
> : [equals](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5sxc5lbnrzq): [hashCode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5ugc43iinxwizi): [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff52g6u3uojuw4zy)
>
> **Converting Strings to NSRanges**
>
> : [fromString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgutbnztwkl3gojxw2u3uojuw4zy)

## Constructors

---

### NSRange

`public NSRange()`

Creates an NSRange with zero location and length. For better performance, use the `ZeroRange` shared instance. See [Constants](#apple-infeqskiineui).

`public NSRange(NSRange aRange)`

Creates a new NSRange with the location and length values of _aRange_.

`public NSRange( int location, int length)`

Creates a new NSRange with the range elements of _location_ and _length_. Throws an IllegalArgumentException if either integer is negative.

---

## Static Methods

---

### fromString

`public static NSRange fromString(String rangeAsString)`

Creates an NSRange from the string _rangeAsString_. The string must be of the form "{loc,len}" where loc is a number representing the starting location of the range and len is the range's length. Throws an IllegalArgumentException if the string is improperly formatted.

__See Also:__ [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff52g6u3uojuw4zy)

---

## Instance Methods

---

### clone

`public Object clone()`

Simply returns the receiver. Since NSRange objects are immutable, there's no need to make an actual clone.

---

### containsLocation

`public boolean containsLocation(int aLocation)`

Returns whether the location _aLocation_ falls within the limits specified by the receiver.

__See Also:__ [intersectsRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5uw45dfojzwky3uonjgc3thmu), [location](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5wg6y3boruw63q)

---

### equals

`public boolean equals(Object otherObject)`

Returns whether _otherObject_ is an NSRange and is equal in location and length to the receiver.

__See Also:__ [isEqualToRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5uxgrlrovqwyvdpkjqw4z3f), [isSubrangeOfRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5uxgu3vmjzgc3thmvhwmutbnztwk)

---

### hashCode

`public int hashCode()`

Provide an appropriate hash code useful for storing the receiver in a hash-based data structure.

---

### intersectsRange

`public boolean intersectsRange(NSRange aRange)`

Returns whether the range _aRange_ intersects the receiver.

__See Also:__ [rangeByIntersectingRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5zgc3thmvbhssloorsxe43fmn2gs3thkjqw4z3f)

---

### isEmpty

`public boolean isEmpty()`

Returns whether the length of the receiver is zero.

__See Also:__ [maxRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5wwc6csmfxgozi)

---

### isEqualToRange

`public boolean isEqualToRange(NSRange aRange)`

Returns whether the range _aRange_ is equal in both location and length to the receiver.

__See Also:__ [equals](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5sxc5lbnrzq), [isSubrangeOfRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5uxgu3vmjzgc3thmvhwmutbnztwk)

---

### isSubrangeOfRange

`public boolean isSubrangeOfRange(NSRange aRange)`

Returns whether the receiver's end points match or fall within those of range _aRange_.

__See Also:__ [intersectsRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5uw45dfojzwky3uonjgc3thmu)

---

### length

`public int length()`

Returns the length of the receiver from its starting location.

__See Also:__ [location](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5wg6y3boruw63q)

---

### location

`public int location()`

Returns the starting location of the receiver.

__See Also:__ [length](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5wgk3thorua)

---

### locationInRange

`public boolean locationInRange(int aLocation)`

This method is deprecated. Use [containsLocation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5rw63tumfuw442mn5rwc5djn5xa) instead.

---

### maxRange

`public int maxRange()`

Returns the extent of the receiver (its starting location plus its length). This number is one greater than the last location in the range.

__See Also:__ [isEmpty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5uxgrlnob2hs), [length](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5wgk3thorua), [location](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5wg6y3boruw63q)

---

### rangeByIntersectingRange

`public NSRange rangeByIntersectingRange(NSRange aRange)`

Returns an NSRange that is the intersection of _aRange_ and the receiver. If the ranges do not intersect, returns an empty range (see [isEmpty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5uxgrlnob2hs)).

__See Also:__ [rangeByUnioningRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5zgc3thmvbhsvlonfxw42lom5jgc3thmu), [subtractRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5zxkytuojqwg5csmfxgozi)

---

### rangeByUnioningRange

`public NSRange rangeByUnioningRange(NSRange aRange)`

Returns an NSRange that is the union of _aRange_ and the receiver (a range constructed from the lowest starting location and the highest ending location of both NSRanges).

__See Also:__ [rangeByIntersectingRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5zgc3thmvbhssloorsxe43fmn2gs3thkjqw4z3f), [subtractRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5zxkytuojqwg5csmfxgozi)

---

### subtractRange

`public void subtractRange( NSRange otherRange, NSMutableRange resultRange1, NSMutableRange resultRange2)`

Returns the ranges resulting from the subtraction of _otherRange_ from the receiver by modifying the mutable ranges _resultRange1_ and _resultRange2_ (provided by the caller). Either or both of the the result ranges might be empty when this method returns.

__See Also:__ [rangeByIntersectingRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5zgc3thmvbhssloorsxe43fmn2gs3thkjqw4z3f), [rangeByUnioningRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjqw4z3ff5zgc3thmvbhsvlonfxw42lom5jgc3thmu)

---

### toString

`public String toString()`

Returns a string representing the receiver. The string is in the form "{loc,len}" where loc is the starting location of the range and len is its length.

__See Also:__ [fromString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgutbnztwkl3gojxw2u3uojuw4zy)

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
