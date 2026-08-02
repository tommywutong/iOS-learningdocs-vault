---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/NSArrayAdditions.html
archived_at: '2026-07-18T01:28:40.385792Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOUndoManager.md)
[!](NSException%20Additions.md)

---

## NSArray Additions

## Cluster Description

Enterprise Objects Framework adds some methods to the Foundation Framework's NSArray class cluster, for filtering objects according to an EOQualifier and sorting them according to a series of EOSortOrderings. It also adds methods for key-value coding, with special support for aggregates, and a convenience method for filtering an array with a specified qualifier.

# NSArray

__Inherits From:__
NSObject

__Declared in:__ EOControl/EOQualifier.h
EOControl/EOSortOrdering.h
EOControl/EOClassDescription.h
EOControl/EOKeyValueCoding.h

Enterprise Objects Framework adds two methods to the Foundation Framework's NSArray class, for filtering objects according to an EOQualifier and sorting them according to a series of EOSortOrderings.

---

#### computeAvgForKey:

- (id)`computeAvgForKey:`(NSString \*)_key_

Returns as an NSDecimalNumber the average of the values the receiver's objects have for _key_. If the array is empty, returns `nil`.

__See also:__ - __valueForKey:__ , - __computeCountForKey:__ , - __computeMaxForKey:__ , - __computeMinForKey:__ , - __computeSumForKey:__

---

#### computeCountForKey:

- (id)`computeCountForKey:`(NSString \*)_key_

Returns the number of elements in the receiver as an NSNumber; the argument _key_ is ignored.

__See also:__ - __valueForKey:__ , - __computeAvgForKey:__ , - __computeMaxForKey:__ , - __computeMinForKey:__ , - __computeSumForKey:__

---

#### computeMaxForKey:

- (id)`computeMaxForKey:`(NSString \*)_key_

Returns the value for _key_ that is the highest for all of the objects in the receiver. If the array is empty, returns `nil`.

__See also:__ - __valueForKey:__ , - __computeAvgForKey:__ , - __computeCountForKey:__ , - __computeMinForKey:__ , - __computeSumForKey:__

---

#### computeMinForKey:

- (id)`computeMinForKey:`(NSString \*)_key_

Returns the object in the receiver that has the lowest value for _key_. If the array is empty, returns `nil`.

__See also:__ - __valueForKey:__ , - __computeAvgForKey:__ , - __computeCountForKey:__ , - __computeMaxForKey:__ , - __computeSumForKey:__

---

#### computeSumForKey:

- (id)`computeSumForKey:`(NSString \*)_key_

Returns as an NSDecimalNumber the sum of the values the receiver's objects have for _key_.

__See also:__ - __valueForKey:__ ,- __computeAvgForKey:__ , - __computeCountForKey:__ , - __computeMaxForKey:__ , - __computeMinForKey:__ , - __computeSumForKey:__

---

#### filteredArrayUsingQualifier:

- (NSArray \*)__filteredArrayUsingQualifier:__ (EOQualifier \*)_aQualifier_

Returns a new NSArray that contains only the objects from the receiver matching _aQualifier_.

---

#### shallowCopy

- (NSArray \*)`shallowCopy`

Returns an NSArray that represents a shallow copy of the receiver. Used by Enterprise Objects Framework to snapshot to-many relationship properties.

---

#### sortedArrayUsingKeyOrderArray:

- (NSArray \*)__sortedArrayUsingKeyOrderArray:__ (NSArray \*)_orderings_

Creates and returns a new NSArray by sorting the objects of the receiver according to the EOSortOrderings in _orderings_. The objects are compared by extracting the sort properties using the added NSObject method __valueForKey:__ and sending them __compare:__ messages.

__See also:__ - __sortUsingKeyOrderArray:__ (NSMutableArray)

---

#### valueForKey:

- (id)`valueForKey:`(NSString \*)_key_

When passed a "normal" key, returns an array composed of the results of sending `valueForKey:` to all elements of the array. When passed a key prefixed with "@", returns a single value that is the result of invoking an aggregate function on the values of the array.

For instance, if this method were passed the key `@sum.budget`, it would invoke `computeSumForKey:@"budget"` on the array, which would add the values for the budget keys for all of the objects in the array. The returned value would be the sum of all of the objects' budgets. The following aggregates are defined: @sum, @count, @avg, @min, @max. You can extend this set by adding methods to NSArray of the form `compute`_Name_`ForKey:`.

__See also:__ - __computeAvgForKey:__ , - __computeCountForKey:__ , - __computeMaxForKey:__ , - __computeMinForKey:__ , - __computeSumForKey:__

# NSMutableArray

__Inherits From:__
NSObject

__Declared in:__ EOControl/EOSortOrdering.h

NSMutableArray has one added method for sorting its elements according to a series of EOSortOrderings.

---

#### sortUsingKeyOrderArray:

- (void)__sortUsingKeyOrderArray:__ (NSArray \*)_orderings_

Sorts the objects of the receiver according to the EOSortOrderings in _orderings_. The objects are compared by extracting the sort properties using the added NSObject method __valueForKey:__ and sending them __compare:__ messages.

__See also:__ - __sortedArrayUsingKeyOrderArray:__ (NSArray)

---

[!](EOUndoManager.md)
[!](NSException%20Additions.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
