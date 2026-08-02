---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOSortOrdering.html
archived_at: '2026-07-18T01:28:27.395214Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOQualifier.ComparisonSupport.md)
[!](EOSortOrdering.ComparisonSupport.md)

---

# EOSortOrdering

__Inherits From:__
Object (Java Client)
NSObject (Yellow Box)

__Implements:__
NSCoding (Java Client only)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (Yellow Box)

## Class Description

An EOSortOrdering object specifies the way that a group of objects should be sorted, using a property key and a method selector for comparing values of that property. EOSortOrderings are used both to generate SQL when fetching rows from a database server, and to sort objects in memory. EOFetchSpecification objects use an array of EOSortOrderings, which are applied in series to perform sorts by more than one property.

---

### Sorting with SQL

When an EOSortOrdering is used to fetch data from a relational database, it's rendered into an ORDER BY clause for a SQL SELECT statement according to the concrete adaptor you're using. For more information, see the class description for EOSQLExpression. The Framework predefines symbols for four comparison selectors, listed in the table below. The table also shows an example of how the comparison selectors can be mapped to SQL.

| __`Defined Name`__ | __SQL Expression__ |
| CompareAscending | (_key_) asc |
| CompareDescending | (_key_) desc |
| CompareCaseInsensitiveAscending | upper(_key_) asc |
| CompareCaseInsensitiveDescending | upper(_key_) desc |

```
```

Using the mapping in the table above, the array of EOSortOrderings (__nameOrdering__ ) created in the following code example:

> ```
> EOSortOrdering lastNameOrdering =
>     EOSortOrdering.sortOrderingWithKey("lastName", EOSortOrdering.CompareAscending);
> EOSortOrdering firstNameOrdering =
>     (EOSortOrdering.sortOrderingWithKey("firstName", EOSortOrdering.CompareAscending);
> NSMutableArray nameOrdering = new NSMutableArray();
> nameOrdering.addObject(lastNameOrdering);
> nameOrdering.addObject(firstNameOrdering);
> ```

results in this ORDER BY clause:

> ```
> order by (lastName) asc, (firstName) asc
> ```

---

### In-Memory Sorting

The methods __sortedArrayUsingKeyOrderArray__ and __sortArrayUsingKeyOrderArray__ are used to sort objects in memory. Given an array of objects and an array of EOSortOrderings, __sortedArrayUsingKeyOrderArray__ returns a new array of objects sorted according to the specified EOSortOrderings. Similarly, __sortArrayUsingKeyOrderArray__ sorts the provided array of objects in place. This code fragment, for example, sorts an array of Employee objects in place, by last name, then first name using the array of EOSortOrderings created above:

> ```
> SortOrdering.sortVectorUsingKeyOrderVector(employees, nameOrdering);
> ```

---

### Comparison Methods

The predefined comparison methods are:

| __Defined Name__ | __Method__ |
| CompareAscending | [- compareAscending](EOSortOrdering.Comparison.md) |
| CompareDescending | [- compareDescending](EOSortOrdering.Comparison.md) |
| CompareCaseInsensitiveAscending | [- compareCaseInsensitiveAscending](EOSortOrdering.Comparison.md) |
| CompareCaseInsensitiveDescending | [- compareCaseInsensitiveDescending](EOSortOrdering.Comparison.md) |

```
```

The first two can be used with any value class; the second two with java.lang.String objects only. The sorting methods extract property values using key-value coding and apply the selectors to the values. If you use custom value classes, you should be sure to implement the appropriate comparison methods to avoid exceptions when sorting objects.

## Interfaces Implemented

**NSCoding (Java Client only)**

**encodeWithCoder**

## Method Types

**Constructors**

**EOSortOrdering**

**Creating instances**

**+ sortOrderingWithKey**

**Examining a sort ordering**

**- key

**- selector****

**In-memory sorting**

**sortedArrayUsingKeyOrderArray

**sortArrayUsingKeyOrderArray****

## Constructors

---

#### EOSortOrdering

public __EOSortOrdering__ (java.lang.String _key_, NSSelector _selector_)

Creates and returns a new EOSortOrdering object. If _key_ and _selector_ are provided, the new EOSortOrdering is initialized with them.

__See also:__ + __sortOrderingWithKey__

## Static Methods

---

#### sortArrayUsingKeyOrderArray

public static void __sortArrayUsingKeyOrderArray__ (NSMutableArray _objects_, NSArray _sortOrderings_)

Sorts _objects_ in place according to the EOSortOrderings in _sortOrderings_. The objects are compared by extracting the sort properties using the EnterpriseObject method __valueForKey__ and sending them __compare...__ messages. See the table in "Sorting with SQL" for a list of the compare methods.

__See also:__ + __sortedArrayUsingKeyOrderArray__

---

#### sortOrderingWithKey

public static EOSortOrdering __sortOrderingWithKey__ (java.lang.String _key_, NSSelector _selector_)

Creates and returns an EOSortOrdering based on _key_ and _selector_.

__See also:__ "Constructors"

---

#### sortedArrayUsingKeyOrderArray

public static NSArray __sortedArrayUsingKeyOrderArray__ (NSArray _objects_, NSArray _sortOrderings_)

Creates and returns a new array by sorting _objects_ according to the SortOrderings in _sortOrderings_. The objects are compared by extracting the sort properties using the added NSObject method __valueForKey__ and sending them __compare...__ messages. See the table in "Sorting with SQL" for a list of the compare methods.

## Instance Methods

---

#### key

public java.lang.String __key__ ()

Returns the key by which the receiver orders items.

__See also:__ - __selector__

---

#### selector

public NSSelector __selector__ ()

Returns the method selector used to compare values when sorting.

__See also:__ - __key__

---

[!](EOQualifier.ComparisonSupport.md)
[!](EOSortOrdering.ComparisonSupport.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
