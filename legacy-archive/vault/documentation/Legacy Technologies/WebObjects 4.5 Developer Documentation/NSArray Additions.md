---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/NSArrayAdditions.html
archived_at: '2026-07-15T08:11:42.110535Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# NSArray Additions

> __Category
> of:__ NSArray

> __Declared in:__ : EOControl/EOQualifier.h
> : EOControl/EOSortOrdering.h
> : EOControl/EOClassDescription.h
> : EOControl/EOKeyValueCoding.h

---

## Category Description

---

Enterprise Objects Framework adds some methods to the Foundation
Framework's NSArray class cluster, for filtering objects according
to an EOQualifier and sorting them according to a series of EOSortOrderings.
It also adds methods for key-value coding, with special support
for aggregates, and a convenience method for filtering an array
with a specified qualifier.

## Method Types

---

> **Filtering and sorting
> objects**
> : [- filteredArrayUsingQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu4u2bojzgc6jaifsgi2lunfxw44zpmzuwy5dfojswiqlsojqxsvltnfxgoulvmfwgsztjmvzdu)
> : [- sortedArrayUsingKeyOrderArray:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu4u2bojzgc6jaifsgi2lunfxw44zponxxe5dfmraxe4tbpfkxg2lom5fwk6kpojsgk4sbojzgc6j2)
>
> **Aggregate functions**
> : [- computeAvgForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu4u2bojzgc6jaifsgi2lunfxw44zpmnxw24dvorsuc5thizxxes3fpe5a)
> : [- computeCountForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu4u2bojzgc6jaifsgi2lunfxw44zpmnxw24dvorsug33vnz2em33sjnsxsoq)
> : [- computeMaxForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu4u2bojzgc6jaifsgi2lunfxw44zpmnxw24dvorsu2ylyizxxes3fpe5a)
> : [- computeMinForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu4u2bojzgc6jaifsgi2lunfxw44zpmnxw24dvorsu22loizxxes3fpe5a)
> : [- computeSumForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu4u2bojzgc6jaifsgi2lunfxw44zpmnxw24dvorsvg5lnizxxes3fpe5a)
>
> **Key Value Coding**
> : [- valueForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu4u2bojzgc6jaifsgi2lunfxw44zpozqwy5lfizxxes3fpe5a)
>
> **Making copies**
> : [- shallowCopy](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu4u2bojzgc6jaifsgi2lunfxw44zponugc3dmn53ug33qpe)

## Instance Methods

---

### computeAvgForKey:

`- (id)computeAvgForKey:(NSString
*)key`

Returns as an NSDecimalNumber the average of
the values the receiver's objects have for _key_.
If the array is empty, returns nil.

---

### computeCountForKey:

`- (id)computeCountForKey:(NSString
*)key`

Returns the number of elements in the receiver
as an NSNumber; the argument _key_ is
ignored.

---

### computeMaxForKey:

`- (id)computeMaxForKey:(NSString
*)key`

Returns the value for _key_ that
is the highest for all of the objects in the receiver. If the array
is empty, returns nil.

---

### computeMinForKey:

`- (id)computeMinForKey:(NSString
*)key`

Returns the object in the receiver that has
the lowest value for _key_. If the
array is empty, returns nil.

__See Also:__  [- valueForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu4u2bojzgc6jaifsgi2lunfxw44zpozqwy5lfizxxes3fpe5a), [- computeAvgForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu4u2bojzgc6jaifsgi2lunfxw44zpmnxw24dvorsuc5thizxxes3fpe5a), [- computeCountForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu4u2bojzgc6jaifsgi2lunfxw44zpmnxw24dvorsug33vnz2em33sjnsxsoq), [- computeMaxForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu4u2bojzgc6jaifsgi2lunfxw44zpmnxw24dvorsu2ylyizxxes3fpe5a), [- computeSumForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu4u2bojzgc6jaifsgi2lunfxw44zpmnxw24dvorsvg5lnizxxes3fpe5a)

---

### computeSumForKey:

`- (id)computeSumForKey:(NSString
*)key`

Returns as an NSDecimalNumber the sum of the
values the receiver's objects have for _key_.

---

### filteredArrayUsingQualifier:

`- (NSArray *)filteredArrayUsingQualifier:(EOQualifier
*)aQualifier`

Returns a new NSArray that contains only the
objects from the receiver matching _aQualifier_.

---

### shallowCopy

`- (NSArray *)shallowCopy`

Returns an NSArray that represents a shallow
copy of the receiver. Used by Enterprise Objects Framework to snapshot
to-many relationship properties.

---

### sortedArrayUsingKeyOrderArray:

`- (NSArray *)sortedArrayUsingKeyOrderArray:(NSArray
*)orderings`

Creates and returns a new NSArray by sorting
the objects of the receiver according to the EOSortOrderings in _orderings_.
The objects are compared by extracting the sort properties using
the added NSObject method __valueForKey:__ and
sending them __compare:__ messages.

__See
Also:__  [- sortUsingKeyOrderArray:](NSMutableArray%20Additions.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu4u2nov2gcytmmvaxe4tbpeqeczdenf2gs33oomxxg33sorkxg2lom5fwk6kpojsgk4sbojzgc6j2) ( [NSMutableArray Additions](NSMutableArray%20Additions.md#apple-ijbeurcfirfeq))

---

### valueForKey:

`- (id)valueForKey:(NSString
*)key`

When passed a "normal" key, returns an array
composed of the results of sending valueForKey: to all elements
of the array. When passed a key prefixed with "@", returns a
single value that is the result of invoking an aggregate function
on the values of the array.

For instance, if this method were
passed the key @sum.budget, it would invoke `computeSumForKey:@"budget"` on
the array, which would add the values for the budget keys for all
of the objects in the array. The returned value would be the sum
of all of the objects' budgets. The following aggregates are defined:
@sum, @count, @avg, @min, @max. You can extend this set by adding
methods to NSArray of the form compute_Name_ForKey:.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
