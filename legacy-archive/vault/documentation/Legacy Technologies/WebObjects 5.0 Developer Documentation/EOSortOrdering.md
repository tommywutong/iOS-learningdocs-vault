---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOSortOrdering.html
archived_at: '2026-07-15T08:13:47.377552Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOSortOrdering

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : EOKeyValueArchiving: NSCoding: Serializable

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

An EOSortOrdering object specifies the way that a group of objects should be sorted, using a property key and a method selector for comparing values of that property. EOSortOrderings are used both to generate SQL when fetching rows from a database server, and to sort objects in memory. EOFetchSpecification objects use an array of EOSortOrderings, which are applied in series to perform sorts by more than one property.

## Sorting with SQL

When an EOSortOrdering is used to fetch data from a relational database, it's rendered into an ORDER BY clause for a SQL SELECT statement according to the concrete adaptor you're using. For more information, see the class description for EOSQLExpression. The Framework predefines symbols for four comparison selectors, listed in the table below. The table also shows an example of how the comparison selectors can be mapped to SQL.

|  |  |
| --- | --- |
| __Defined Name__ | __SQL Expression__ |
| [CompareAscending](#apple-ijbumqsejjduo) | (_key_) asc |
| [CompareDescending](#apple-ijbumq2cizbuo) | (_key_) desc |
| [CompareCaseInsensitiveAscending](#apple-ijbumq2kijauu) | upper(_key_) asc |
| [CompareCaseInsensitiveDescending](#apple-ijbumqsgjbcuq) | upper(_key_) desc |

Using the mapping in the table above, the array of EOSortOrderings (__nameOrdering__) created in the following code example:

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

## In-Memory Sorting

The methods [sortedArrayUsingKeyOrderArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thf5zw64tumvsec4tsmf4vk43jnztuwzlzj5zgizlsifzheylz) and [sortArrayUsingKeyOrderArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thf5zw64tuifzheylzkvzws3thjnsxst3smrsxeqlsojqxs) are used to sort objects in memory. Given an array of objects and an array of EOSortOrderings, __sortedArrayUsingKeyOrderArray__ returns a new array of objects sorted according to the specified EOSortOrderings. Similarly, __sortArrayUsingKeyOrderArray__ sorts the provided array of objects in place. This code fragment, for example, sorts an array of Employee objects in place, by last name, then first name using the array of EOSortOrderings created above:

> ```
> SortOrdering.sortVectorUsingKeyOrderVector(employees, nameOrdering);
> ```

## Constants

---

EOSortOrdering defines the following NSSelector constants:

|  |  |
| --- | --- |
| __Defined Name__ | __Method__ |
| CompareAscending | compareAscending |
| CompareDescending | compareDescending |
| CompareCaseInsensitiveAscending | compareCaseInsensitiveAscending |
| CompareCaseInsensitiveDescending | compareCaseInsensitiveDescending |

The first two can be used with any value class; the second two with NSString objects only. The sorting methods extract property values using key-value coding and apply the selectors to the values. If you use custom value classes, you should be sure to implement the appropriate comparison methods to avoid exceptions when sorting objects.

## Interfaces Implemented

---

> : NSCoding: [classForCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts6y3mmfzxgrtpojbw6zdfoi): [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thf5sgky3pmrsu6ytkmvrxi): [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts6zlomnxwizkxnf2gqq3pmrsxe): : EOKeyValueArchiving: [decodeWithKeyValueUnarchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thf5sgky3pmrsvo2lunbfwk6kwmfwhkzkvnzqxey3inf3gk4q): [encodeWithKeyValueArchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts6zlomnxwizkxnf2gqs3fpflgc3dvmvaxey3inf3gk4q):

## Method Types

---

> **Constructors**
> : [EOSortOrdering](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts6rkpknxxe5cpojsgk4tjnztq)
>
> **Examining a sort ordering**
> : [key](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts623fpe): [selector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts643fnrswg5dpoi)
>
> **In-memory sorting**
> : [sortedArrayUsingKeyOrderArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thf5zw64tumvsec4tsmf4vk43jnztuwzlzj5zgizlsifzheylz): [sortArrayUsingKeyOrderArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thf5zw64tuifzheylzkvzws3thjnsxst3smrsxeqlsojqxs)

## Constructors

---

### EOSortOrdering

`public EOSortOrdering( String key, NSSelector selector)`

Creates and returns a new EOSortOrdering object. If _key_ and _selector_ are provided, the new EOSortOrdering is initialized with them.

__See Also:__ [EOSortOrdering](#apple-onxxe5cpojsgk4tjnztvo2lunbfwk6k7onswyzldorxxexy)

---

## Static Methods

---

### decodeObject

`public static Object decodeObject(NSCoder coder)`

Conformance to NSCoding.

---

### decodeWithKeyValueUnarchiver

`public static Object decodeWithKeyValueUnarchiver(EOKeyValueUnarchiver unarchiver)`

Conformance to EOKeyValueArchiving.

---

### sortArrayUsingKeyOrderArray

`public static void sortArrayUsingKeyOrderArray( NSMutableArray objects, NSArray sortOrderings)`

Sorts _objects_ in place according to the EOSortOrderings in _sortOrderings_. The objects are compared by extracting the sort properties using the NSKeyValueCoding method valueForKey and sending them __compare...__ messages. See the table in ["Sorting with SQL"](#apple-ijcuorcdizauu) for a list of the compare methods.

__See Also:__ [sortedArrayUsingKeyOrderArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thf5zw64tumvsec4tsmf4vk43jnztuwzlzj5zgizlsifzheylz)

---

### sortOrderingWithKey

`public static EOSortOrdering sortOrderingWithKey( String key, NSSelector selector)`

Creates and returns an EOSortOrdering based on _key_ and _selector_.

__See Also:__ [EOSortOrdering](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts6rkpknxxe5cpojsgk4tjnztq) constructor

---

### sortedArrayUsingKeyOrderArray

`public static NSArray sortedArrayUsingKeyOrderArray( NSArray objects, NSArray sortOrderings)`

Creates and returns a new array by sorting _objects_ according to the EOSortOrderings in _sortOrderings_. The objects are compared by extracting the sort properties using the added EOKeyValueCoding method valueForKey and sending them __compare...__ messages. See the table in ["Sorting with SQL"](#apple-ijcuorcdizauu) for a list of the compare methods.

---

## Instance Methods

---

### classForCoder

`public Class classForCoder()`

Conformance to NSCoding.

---

### encodeWithCoder

`public void encodeWithCoder(NSCoder coder)`

Conformance to NSCoding.

---

### encodeWithKeyValueArchiver

`public void encodeWithKeyValueArchiver(EOKeyValueArchiver archiver)`

Conformance to EOKeyValueArchiving.

---

### key

`public String key()`

Returns the key by which the receiver orders items.

__See Also:__ [selector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts643fnrswg5dpoi)

---

### selector

`public NSSelector selector()`

Returns the method selector used to compare values when sorting.

__See Also:__ [key](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts623fpe)

---

### __toString__

`public String toString()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
