---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOSortOrdering.html
archived_at: '2026-07-15T08:11:37.970042Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOSortOrdering

> **__Inherits from:__**
> : (com.apple.client.eocontrol) Object
>
> (com.apple.yellow.eocontrol) NSObject

> **__Implements:__**
> : (com.apple.client.eocontrol only) NSCoding

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Class Description

---

An EOSortOrdering object specifies the way that a group of
objects should be sorted, using a property key and a method selector
for comparing values of that property. EOSortOrderings are used
both to generate SQL when fetching rows from a database server,
and to sort objects in memory. EOFetchSpecification objects use an
array of EOSortOrderings, which are applied in series to perform sorts
by more than one property.

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
| [CompareAscending](#apple-ijbumqsejjduo) | ( _key_) asc |
| [CompareDescending](#apple-ijbumq2cizbuo) | ( _key_) desc |
| [CompareCaseInsensitiveAscending](#apple-ijbumq2kijauu) | upper( _key_) asc |
| [CompareCaseInsensitiveDescending](#apple-ijbumqsgjbcuq) | upper( _key_) desc |

Using the mapping in the table above, the array of EOSortOrderings
(`nameOrdering`) created in the following
code example:

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

The methods [sortedArrayUsingKeyOrderArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thf5zw64tumvsec4tsmf4vk43jnztuwzlzj5zgizlsifzheylz) and [sortArrayUsingKeyOrderArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thf5zw64tuifzheylzkvzws3thjnsxst3smrsxeqlsojqxs) are
used to sort objects in memory. Given an array of objects and an
array of EOSortOrderings, `sortedArrayUsingKeyOrderArray` returns
a new array of objects sorted according to the specified EOSortOrderings.
Similarly, `sortArrayUsingKeyOrderArray` sorts
the provided array of objects in place. This code fragment, for example,
sorts an array of Employee objects in place, by last name, then
first name using the array of EOSortOrderings created above:

> ```
> SortOrdering.sortVectorUsingKeyOrderVector(employees, nameOrdering);
> ```

## Constants

---

EOSortOrdering defines the following NSSelector constants:

|  |  |
| --- | --- |
| __Defined Name__ | __Method__ |
| CompareAscending | [compareAscending](EOSortOrderingComparison.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknxxe5cpojsgk4tjnztug33nobqxe2ltn5xc6y3pnvygc4tfifzwgzlomruw4zy) |
| CompareDescending | [compareDescending](EOSortOrderingComparison.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknxxe5cpojsgk4tjnztug33nobqxe2ltn5xc6y3pnvygc4tfirsxgy3fnzsgs3th) |
| CompareCaseInsensitiveAscending | [compareCaseInsensitiveAscending](EOSortOrderingComparison.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknxxe5cpojsgk4tjnztug33nobqxe2ltn5xc6y3pnvygc4tfinqxgzkjnzzwk3ttnf2gs5tfifzwgzlomruw4zy) |
| CompareCaseInsensitiveDescending | [compareCaseInsensitiveDescending](EOSortOrderingComparison.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknxxe5cpojsgk4tjnztug33nobqxe2ltn5xc6y3pnvygc4tfinqxgzkjnzzwk3ttnf2gs5tfirsxgy3fnzsgs3th) |

The first two can be used with any value class; the second
two with String objects only. The sorting methods extract property
values using key-value coding and apply the selectors to the values.
If you use custom value classes, you should be sure to implement
the appropriate comparison methods to avoid exceptions when sorting
objects.

## Interfaces Implemented

---

> NSCoding
> (com.apple.client.eocontrol only): `encodeWithCoder`

## Method Types

---

> **Constructors**
> : [EOSortOrdering](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts6rkpknxxe5cpojsgk4tjnztq)
>
> **Examining a sort ordering**
> : [key](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts623fpe)
> : [selector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts643fnrswg5dpoi)
>
> **In-memory sorting**
> : [sortedArrayUsingKeyOrderArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thf5zw64tumvsec4tsmf4vk43jnztuwzlzj5zgizlsifzheylz)
> : [sortArrayUsingKeyOrderArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thf5zw64tuifzheylzkvzws3thjnsxst3smrsxeqlsojqxs)

## Constructors

---

### EOSortOrdering

`public EOSortOrdering(
String key,
NSSelector selector)`

Creates and returns a new EOSortOrdering object.
If _key_ and _selector_ are
provided, the new EOSortOrdering is initialized with them.

__See
Also:__  [EOSortOrdering](#apple-onxxe5cpojsgk4tjnztvo2lunbfwk6k7onswyzldorxxexy)

---

## Static Methods

---

### sortArrayUsingKeyOrderArray

`public static void sortArrayUsingKeyOrderArray(
NSMutableArray objects,
NSArray sortOrderings)`

Sorts _objects_ in
place according to the EOSortOrderings in _sortOrderings._
The objects are compared by extracting the sort properties using
the EOKeyValueCoding method [valueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe) and sending them `compare...` messages.
See the table in ["Sorting with SQL"](#apple-ijcuorcdizauu) for a list of the compare methods.

__See
Also:__  [sortedArrayUsingKeyOrderArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thf5zw64tumvsec4tsmf4vk43jnztuwzlzj5zgizlsifzheylz)

---

### sortOrderingWithKey

`public static EOSortOrdering sortOrderingWithKey(
String key,
NSSelector selector)`

Creates and returns an EOSortOrdering based
on _key_ and _selector._

__See
Also:__  [EOSortOrdering](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts6rkpknxxe5cpojsgk4tjnztq) constructor

---

### sortedArrayUsingKeyOrderArray

`public static NSArray sortedArrayUsingKeyOrderArray(
NSArray objects,
NSArray sortOrderings)`

Creates and returns a new array by sorting _objects_ according
to the EOSortOrderings in _sortOrderings._
The objects are compared by extracting the sort properties using
the added EOKeyValueCoding method [valueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe) and sending them `compare...` messages.
See the table in ["Sorting with SQL"](#apple-ijcuorcdizauu) for a list of the compare methods.

---

## Instance Methods

---

### key

`public String key()`

Returns the key by which the receiver orders
items.

__See Also:__  [selector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts643fnrswg5dpoi)

---

### selector

`public NSSelector selector()`

Returns the method selector used to compare
values when sorting.

__See Also:__  [key](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts623fpe)

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
