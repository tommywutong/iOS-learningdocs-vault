---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Foundation/ArrayMethods.html
archived_at: '2026-07-15T07:46:44.698348Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Foundation.book.md) [!Previous Section](ArrayIntro.md)

# Commonly Used Array Methods

The following sections list the most commonly used NSArray and NSMutableArray methods. The methods covered are grouped in the following categories:

- [Creating Arrays](#apple-geydioi)
- [Querying Arrays](#apple-geydmoi)
- [Sorting Arrays](#apple-geydqma)
- [Adding and Removing Objects](#apple-geydqnq)
- [Storing Arrays](#apple-geytani)
- [Representing Arrays as Strings](#apple-geytcmq)

## Creating Arrays

The methods in this section are class methods, as denoted by the plus sign (+). You use class methods to send messages to a class-in this case, NSArray and NSMutableArray. For more information on class methods, see "[Messaging in WebScript](../WebScript/Messaging.md)" in the "Using WebScript" chapter.

**__+ array__**
: Returns an empty array. Usually used to create NSMutableArrays. NSArrays created with this method are permanently empty.

```
// Most common use
id mutableArray = [NSMutableArray array];

// May not be what you want
id array = [NSArray array];
```


**__+ arrayWithObject:__**
: Returns an array containing the single specified object.

**__+ arrayWithObjects:__**
: Returns an array containing the objects in the argument list. The argument list is a comma-separated list of objects ending with __nil__.

```
id array = [NSMutableArray arrayWithObjects:
        @"Plates", @"Plasticware", @"Napkins", nil];
```


**__+ arrayWithArray:__**
: Returns an array containing the contents of a specified array. Usually used to create an NSMutableArray from an immutable NSArray. For example, the following statement:

```
id mutableArray = [NSMutableArray arrayWithArray:@("A", "B", "C")];
```


creates an NSMutableArray from a constant NSArray object.

**__+ arrayWithContentsOfFile:__**
: Returns an array initialized from the contents of a specified file. The specified file can be a full or relative pathname; the file that it names must contain a string representation of an array, such as that produced by the [__writeToFile:atomically:__](DictionaryMethods.md#apple-gezdeoa) method. See also [__description__](#apple-geytcmy).

## Querying Arrays

**__- count__**
: Returns the number of objects in the array.

**__- isEqual:__**
: Returns YES if the specified object is an array and has contents equivalent to the receiver, NO otherwise. Two arrays have equal contents if they each hold the same number of objects and objects at a given index in each array satisfy the __isEqual:__ test.

**__- objectAtIndex:__**
: Returns the object located at a specified index. Arrays have a zero-based index. The first object in an array is at index 0, the second is at index 1, and so on. It is an error to specify an index that is out of bounds (greater than or equal to the array's count).

**__- indexOfObject:__**
: Returns the index of the first object in the array that is equivalent to a specified object. To determine equality, each element of the array is sent an __isEqual:__ message.

**__- indexOfObjectIdenticalTo:__**
: Returns the index of the first occurrence of the a specified object. To determine equality, the __id__s of the two objects are compared.

## Sorting Arrays

**__- sortedArrayUsingSelector:__**
: Returns an NSArray that lists the receiver's elements in ascending order, as determined by a specified method. This method is used to sort arrays containing strings and/or numbers. For example, the following code excerpt:

```
id guestArray = @("Suzy", "Alice", "John", "Peggy", "David");
id sortedArray = [guestArray sortedArrayUsingSelector:@"compare:"];
```


creates the NSArray __sortedArray__ containing the string "Alice" at index 0, "David" at index 1, and so on.

## Adding and Removing Objects

__Warning:__  The following methods are not supported by NSArray. They are only available to NSMutableArray objects.

**__- addObject:__**
: Adds a specified object at the end of the receiver. It is an error to specify __nil__ as an argument to this method. You can not add __nil__ to an array.

**__- insertObject:atIndex:__**
: Inserts an object at a specified index. If the specified index is already occupied, the objects at that index and beyond are shifted down one slot to make room. The specified index can't be greater than the receiver's count, and the specified object cannot be __nil__.
: Array objects have a zero-based index. The first object in an array is at index 0, the second is at index 1, and so on. You can only insert new objects in ascending order-with no gaps. Once you add two objects, the array's size is 2, so you can insert objects at indexes 0, 1, or 2. Index 3 is illegal and out of bounds.
: It is an error to specify __nil__ as an argument to this method. You cannot add __nil__ to an array. It is also an error to specify an index that is greater than the array's count.

**__- removeObject:__**
: Removes all objects in the array equivalent to a specified object, and moves elements up as necessary to fill any gaps. Equivalency is determined using the __isEqual:__ method.

**__- removeObjectIdenticalTo:__**
: Removes all occurrences of a specified object and moves elements up as necessary to fill any gaps.

**__- removeObjectAtIndex:__**
: Removes the object at a specified index and moves all elements beyond the index up one slot to fill the gap. Arrays have a zero-based index. The first object in an array is at index 0, the second is at index 1, and so on.
: It is an error to specify an index that is out of bounds (greater than or equal to the array's count).

**__- removeAllObjects__**
: Empties the receiver of all of its elements.

**__- setArray:__**
: Empties the receiver of all its elements, then adds the contents of a specified array.

## Storing Arrays

**__- writeToFile:atomically:__**
: Writes the array's string representation to a specified file using the __description__ method. Returns YES on success and NO on failure. If YES is specified for __atomically:__, this method attempts to write the file safely so that an existing file with the specified path is not overwritten, and it does not create a new file at the specified path unless the write is successful. The resulting file is suitable for use with [__arrayWithContentsOfFile:__](#apple-geydmny). For example, the following code excerpt:

```
id guestArray = [NSMutableArray arrayWithContentsOfFile:path];
[guestArray addObject:newGuest];
[guestArray writeToFile:path atomically:YES];
```


creates __guestArray__ with the contents of the specified file, adds a new guest, and saves the changes to the same file.

## Representing Arrays as Strings

**__- description__**
: Returns a string that represents the contents of the receiver. For example, the following code excerpt:

```
id array = [NSMutableArray arrayWithObjects:
        @"Plates", @"Plasticware", @"Napkins", nil];
id description = [array description];
```


produces the string "(Plates, Plasticware, Napkins)".

**__- componentsJoinedByString:__**
: Returns an NSString created by interposing a specified string between the elements of the receiver's objects. Each element of the array must be a string. If the receiver has no elements, an empty string is returned. See also [__componentsSeparatedByString:__](StringMethods.md#apple-he3tm) (NSString and NSMutableString). For example, the following code excerpt:

```
id commaString = @"A, B, C";
id array = [string componentsSeparatedByString:@","];
id dashString = [array componentsJoinedByString:@"-"];
```


creates the NSString __dashString__ with the contents "A-B-C".

[!Table of Contents](Foundation.book.md) [!Next Section](DictionaryIntro.md)
