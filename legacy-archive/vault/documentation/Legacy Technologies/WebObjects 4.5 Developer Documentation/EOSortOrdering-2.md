---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOSortOrdering.html
archived_at: '2026-07-15T08:11:40.034940Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOSortOrdering

> **__Inherits
> from:__**
> : NSObject

> **__Conforms to:__**
> : NSCoding
> : NSObject (NSObject)

> __Declared in:__ : EOControl/EOSortOrdering.h

---

## Class Description

---

An EOSortOrdering object specifies the way that a group of
objects should be sorted, using a property key and a method selector
for comparing values of that property. EOSortOrderings are used
both to generate SQL when fetching rows from a database server,
and to sort objects in memory. Both the EOFetchSpecification class
and the added NSArray sorting methods accept an array of EOSortOrderings,
which are applied in series to perform sorts by more than one property.

## Sorting with SQL

When an EOSortOrdering is used to fetch data from a relational
database, it's rendered into an ORDER BY clause for a SQL SELECT
statement according to the concrete adaptor you're using. For
more information, see the class description for EOSQLExpression.
The Framework predefines symbols for four comparison selectors,
listed in the table below. The table also shows an example of how
the comparison selectors can be mapped to SQL.

|  |  |
| --- | --- |
| __Defined Name__ | __SQL Expression__ |
| [EOCompareAscending](#apple-ijbumqsejjduo) | (_key_) asc |
| [EOCompareDescending](#apple-ijbumq2cizbuo) | (_key_) desc |
| [EOCompareCaseInsensitiveAscending](#apple-ijbumq2kijauu) | upper(_key_) asc |
| [EOCompareCaseInsensitiveDescending](#apple-ijbumqsgjbcuq) | upper(_key_) desc |

Using the mapping in the table above, the array of EOSortOrderings
(__nameOrdering__) created in the following
code example:

> ```
> NSArray *nameOrdering = [NSArray arrayWithObjects:
>     [EOSortOrdering sortOrderingWithKey:@"lastName" selector:EOCompareAscending],
>     [EOSortOrdering sortOrderingWithKey:@"firstName" selector:EOCompareAscending],
>     nil];
> ```

results in this ORDER BY clause:

> ```
> order by (lastName) asc, (firstName) asc
> ```

## In-Memory Sorting

Enterprise Objects Framework adds a method each to NSArray
and NSMutableArray for sorting objects in memory. NSArray's sortedArrayUsingKeyOrderArray: returns
a new array of objects sorted according to the specified EOSortOrderings.
Similarly, NSMutableArray's sortUsingKeyOrderArray: sorts the
provided array of objects in place. This code fragment, for example,
sorts an array of Employee objects in place, by last name, then
first name using the array of EOSortOrderings created above:

> ```
> NSArray *sortedEmployees = [employees sortedArrayUsingKeyOrderArray:nameOrdering];
> ```

## Constants

---

In EOSortOrdering.h, EOControl defines
the following selector constants:

|  |  |
| --- | --- |
| __Defined Name__ | __Method__ |
| EOCompareAscending | [- compareAscending](EOSortOrderingComparison-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2tn5zhit3smrsxe2lom5bw63lqmfzgs43pnyxwg33nobqxezkbonrwk3tenfxgo) |
| EOCompareDescending | [- compareDescending](EOSortOrderingComparison-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2tn5zhit3smrsxe2lom5bw63lqmfzgs43pnyxwg33nobqxezkemvzwgzlomruw4zy) |
| EOCompareCaseInsensitiveAscending | [- compareCaseInsensitiveAscending](EOSortOrderingComparison-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2tn5zhit3smrsxe2lom5bw63lqmfzgs43pnyxwg33nobqxezkdmfzwksloonsw443joruxmzkbonrwk3tenfxgo) |
| EOCompareCaseInsensitiveDescending | [- compareCaseInsensitiveDescending](EOSortOrderingComparison-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2tn5zhit3smrsxe2lom5bw63lqmfzgs43pnyxwg33nobqxezkdmfzwksloonsw443joruxmzkemvzwgzlomruw4zy) |

The first two can be used with any value class; the second
two with NSString objects only. The sorting methods extract property
values using key-value coding and apply the selectors to the values.
If you use custom value classes, you should be sure to implement
the appropriate comparison methods to avoid exceptions when sorting
objects.

## Adopted Protocols

---

> NSCoding: __- encodeWithCoder:__
> : __- initWithCoder:__

## Method Types

---

> **Creating instances**
> : [- initWithKey:selector:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tn5zhit3smrsxe2lom4xws3tjorlws5dijnsxsottmvwgky3un5zdu)
>
> **Examining a sort ordering**
> : [- key](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tn5zhit3smrsxe2lom4xwwzlz)
> : [- selector](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tn5zhit3smrsxe2lom4xxgzlmmvrxi33s)

## Class Methods

---

### sortOrderingWithKey:selector:

`+ (EOSortOrdering *)sortOrderingWithKey:(NSString
*)key
selector:(SEL)selector`

Creates and returns an EOSortOrdering based
on _key_ and _selector_.

__See
Also:__  [- initWithKey:selector:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tn5zhit3smrsxe2lom4xws3tjorlws5dijnsxsottmvwgky3un5zdu)

---

## Instance Methods

---

### initWithKey:selector:

`- (id)initWithKey:(NSString
*)key
selector:(SEL)aSelector`

Initializes a newly allocated EOSortOrdering
based on _key_ and _selector_ and
returns __self__. This is the designated initializer
for the EOSortOrdering class.

__See Also:__  [+ EOSortOrdering](#apple-onxxe5cpojsgk4tjnztvo2lunbfwk6k7onswyzldorxxexy)

---

### key

`- (NSString *)key`

Returns the key by which the receiver orders
items.

__See Also:__  [- selector](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tn5zhit3smrsxe2lom4xxgzlmmvrxi33s)

---

### selector

`- (SEL)selector`

Returns the method selector used to compare
values when sorting.

__See Also:__  [- key](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tn5zhit3smrsxe2lom4xwwzlz)

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
