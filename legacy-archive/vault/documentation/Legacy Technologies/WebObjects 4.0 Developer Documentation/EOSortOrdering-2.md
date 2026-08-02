---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOSortOrdering.html
archived_at: '2026-07-18T01:28:37.373678Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOQualifier-4.md)
[!](EOTemporaryGlobalID-2.md)

---

# EOSortOrdering

__Inherits From:__
NSObject

__Conforms To:__ NSCoding
NSObject (NSObject)

__Declared in:__ EOControl/EOSortOrdering.h

An EOSortOrdering object specifies the way that a group of objects should be sorted, using a property key and a method selector for comparing values of that property. EOSortOrderings are used both to generate SQL when fetching rows from a database server, and to sort objects in memory. Both the EOFetchSpecification class and the added NSArray sorting methods accept an array of EOSortOrderings, which are applied in series to perform sorts by more than one property.

---

### Sorting with SQL

When an EOSortOrdering is used to fetch data from a relational database, it's rendered into an ORDER BY clause for a SQL SELECT statement according to the concrete adaptor you're using. For more information, see the class description for EOSQLExpression. The Framework predefines symbols for four comparison selectors, listed in the table below. The table also shows an example of how the comparison selectors can be mapped to SQL.

| __`Defined Name`__ | __SQL Expression__ |
| EOCompareAscending | (_key_) asc |
| EOCompareDescending | (_key_) desc |
| EOCompareCaseInsensitiveAscending | upper(_key_) asc |
| EOCompareCaseInsensitiveDescending | upper(_key_) desc |

```
```

Using the mapping in the table above, the array of EOSortOrderings (__nameOrdering__ ) created in the following code example:

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

---

### In-Memory Sorting

Enterprise Objects Framework adds a method each to NSArray and NSMutableArray for sorting
objects in memory. NSArray's sortedArrayUsingKeyOrderArray: returns a new array of objects
sorted according to the specified EOSortOrderings. Similarly, NSMutableArray's
sortUsingKeyOrderArray: sorts the array of objects. This code fragment, for example, sorts an array
of Employee objects by last name, then first name using the array of EOSortOrderings created above:

> ```
> NSArray *sortedEmployees = [employees sortedArrayUsingKeyOrderArray:nameOrdering];
> ```

---

### Comparison Methods

The predefined comparison selectors are:

| __Defined Name__ |  |
| EOCompareAscending | [- compareAscending:](EOSortOrderingComparison.md) |
| EOCompareDescending | [- compareDescending:](EOSortOrderingComparison.md) |
| EOCompareCaseInsensitiveAscending | [- compareCaseInsensitiveAscending:](EOSortOrderingComparison.md) |
| EOCompareCaseInsensitiveDescending | [- compareCaseInsensitiveDescending:](EOSortOrderingComparison.md) |

```
```

The first two can be used with any value class; the second two with NSString objects only. The sorting methods extract property values using key-value coding and apply the selectors to the values. If you use custom value classes, you should be sure to implement the appropriate comparison methods to avoid exceptions when sorting objects.

---

## Adopted Protocols

**NSCoding**

**- encodeWithCoder:

**- initWithCoder:****

**Creating instances**

**+ sortOrderingWithKey:selector:

**- initWithKey:selector:****

**Examining a sort ordering**

**- key

**- selector****

---

#### sortOrderingWithKey:selector:

+ (EOSortOrdering \*)__sortOrderingWithKey:__ (NSString \*)_key___selector:__ (SEL)_selector_

Creates and returns an EOSortOrdering based on _key_ and _selector_.

__See also:__ - __initWithKey:selector:__

---

#### initWithKey:selector:

- (id)__initWithKey:__ (NSString \*)_key___selector:__ (SEL)_aSelector_

Initializes a newly allocated EOSortOrdering based on _key_ and _selector_ and returns __self__ . This is the designated initializer for the EOSortOrdering class.

__See also:__ + __sortOrderingWithKey:selector:__

---

#### key

- (NSString \*)__key__

Returns the key by which the receiver orders items.

__See also:__ - __selector__

---

#### selector

- (SEL)__selector__

Returns the method selector used to compare values when sorting.

__See also:__ - __key__

---

[!](EOQualifier-4.md)
[!](EOTemporaryGlobalID-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
