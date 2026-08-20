---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSComparator.html
archived_at: '2026-07-15T08:13:55.852408Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSComparator

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

NSComparator is an abstract class that defines an API for comparing two objects for the purpose of sorting them. The class defines one method, [compare](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxw24dbojqxi33sf5rw63lqmfzgk), which compares two parameters and returns one of `OrderedAscending`, [OrderedSame](#apple-ijeugsciirfeo), or [OrderedDescending](#apple-ijeugrsejjaue).

Instead of invoking __compare__ directly on a comparator, you typically use the NSArray method [sortedArrayUsingComparator](NSArray.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5zw64tumvsec4tsmf4vk43jnztug33nobqxeylun5za), which sorts the elements of the receiving array into a new array, or the NSMutableArray method [sortUsingComparator](NSMutableArray.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s643poj2fk43jnztug33nobqxeylun5za), which sorts the elements of an array in place. NSComparator provides default comparators to use with these sorting methods. See the section ["Constants" (page 54)](#apple-ijeugq2kjfbee).

## Constants

---

NSComparator defines the following `int` constants as the possible return values for [compare](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxw24dbojqxi33sf5rw63lqmfzgk):

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| OrderedAscending | Returned when the object arguments are in ascending order (the value of the first argument is less than the value of the second). |
| OrderedSame | Returned when the values of the object arguments are equal. |
| OrderedDescending | Returned when the object arguments are in descending order (the value of the first argument is less than the value of the second). |

Additionally, NSComparator defines the following NSComparator constants to be used for comparing objects of the specified class:

|  |  |
| --- | --- |
| __Constant__ | __Compares Objects of Class__ |
| AscendingStringComparator | String |
| DescendingStringComparator | String |
| AscendingCaseInsensitiveStringComparator | String |
| DescendingCaseInsensitiveStringComparator | String |
| AscendingNumberComparator | Number |
| DescendingNumberComparator | Number |
| AscendingTimestampComparator | NSTimestamp |
| DescendingTimestampComparator | NSTimestamp |

## Constructors

---

### NSComparator

`public NSComparator()`

The no-arg constructor. Don't use this method; because NSComparator is an abstract class, you can never create an instance of it.

---

## Instance Methods

---

### compare

`public abstract int compare( Object first, Object second) throws NSComparator.ComparisonException`

Compares the values of _first_ and _second_ and returns the result, one of [OrderedAscending](#apple-ijeugq2bizbuo), [OrderedSame](#apple-ijeugsciirfeo), or [OrderedDescending](#apple-ijeugrsejjaue). Specifically, for non-null _x_, _y_, and _z_:

- `compare(x, x)` returns `OrderedSame`.
- If `compare(x, y)` returns `OrderedSame`, then `compare(y, x)` returns `OrderedSame`
- If `compare(x, y)` returns `OrderedAscending`, then `compare(y, x)` returns `OrderedDescending`.
- If `compare(x, y)` returns `OrderedDescending`, then `compare(y, x)` returns `OrderedAscending`.
- If `compare(x, y)` returns `OrderedAscending` and `compare(y, z)` returns `OrderedAscending`, then `compare(x, z)` returns `OrderedAscending`.
- Exactly one of the following is true: `compare(x, x)` == `OrderedSame`, `compare(x, x)` == `OrderedAscending`, or `compare(x, x)` == `OrderedDescending`.
- The result of `compare(x, y)` must be the same in all invocations.

Throws an [NSComparator.ComparisonException](NSComparator.ComparisonException.md#apple-ijaucrcji5eeo) if a comparison between _first_ and _second_ is impossible or undefined; for example, if either argument is `null`.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
