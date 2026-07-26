---
title: NSDictionary
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdictionary
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary.json'
content_hash: 'sha256:8a811f5f97fde06f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDictionary

<sub>Class</sub>

A static collection of objects associated with unique keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSDictionary
```

## Overview

You can use this type in Swift instead of a [Dictionary](../swift/dictionary.md) in cases that require reference semantics.

The `NSDictionary` class declares the programmatic interface to objects that manage immutable associations of keys and values. For example, an interactive form could be represented as a dictionary, with the field names as keys, corresponding to user-entered values.

Use this class or its subclass [NSMutableDictionary](nsmutabledictionary.md) when you need a convenient and efficient way to retrieve data associated with an arbitrary key. `NSDictionary` creates static dictionaries, and `NSMutableDictionary` creates dynamic dictionaries. (For convenience, the term _dictionary_ refers to any instance of one of these classes without specifying its exact class membership.)

A key-value pair within a dictionary is called an entry. Each entry consists of one object that represents the key and a second object that is that key’s value. Within a dictionary, the keys are unique. That is, no two keys in a single dictionary are equal (as determined by [isEqual(_:)](<../objectivec/nsobjectprotocol/isequal(__).md>)). In general, a key can be any object (provided that it conforms to the `NSCopying` protocol—see below), but note that when using key-value coding the key must be a string (see [Accessing Object Properties](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/BasicPrinciples.html#//apple_ref/doc/uid/20002170)). Neither a key nor a value can be `nil`; if you need to represent a null value in a dictionary, you should use [NSNull](nsnull.md).

`NSDictionary` is “toll-free bridged” with its Core Foundation counterpart, [CFDictionary](../corefoundation/cfdictionary.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

### Creating NSDictionary Objects Using Dictionary Literals

In addition to the provided initializers, such as [- initWithObjects:forKeys:](<nsdictionary/init(objects_forkeys_).md>), you can create an `NSDictionary` object using a _dictionary literal_.

**Swift**

```swift
let dictionary: NSDictionary = [
    "anObject" : someObject,
    "helloString" : "Hello, World!",
    "magicNumber" : 42,
    "aValue" : someValue
]
```

**Objective-C**

```objc
NSDictionary *dictionary = @{
       @"anObject" : someObject,
    @"helloString" : @"Hello, World!",
    @"magicNumber" : @42,
         @"aValue" : someValue
};
```

In Objective-C, the compiler generates code that makes an underlying call to the [dictionaryWithObjects:forKeys:count:](nsdictionary/dictionarywithobjects_forkeys_count_.md) method.

```objc
id objects[] = { someObject, @"Hello, World!", @42, someValue };
id keys[] = { @"anObject", @"helloString", @"magicNumber", @"aValue" };
NSUInteger count = sizeof(objects) / sizeof(id);
NSDictionary *dictionary = [NSDictionary dictionaryWithObjects:objects
                                                       forKeys:keys
                                                         count:count];
```

Unlike [dictionaryWithObjectsAndKeys:](nsdictionary/dictionarywithobjectsandkeys_.md) and other initializers, dictionary literals specify entries in key-value order. You should not terminate the list of objects with `nil` when using this literal syntax, and in fact `nil` is an invalid value. For more information about object literals in Objective-C, see [Working with Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/WorkingwithObjects/WorkingwithObjects.html#//apple_ref/doc/uid/TP40011210-CH4) in [Programming with Objective-C](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011210).

In Swift, the `NSDictionary` class conforms to the `DictionaryLiteralConvertible` protocol, which allows it to be initialized with dictionary literals. For more information about object literals in Swift, see [Literal Expression](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/Expressions.html#//apple_ref/doc/uid/TP40014097-CH32-ID390) in [The Swift Programming Language (Swift 4.1)](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/index.html#//apple_ref/doc/uid/TP40014097).

### Accessing Values Using Subscripting

In addition to the provided instance methods, such as [- objectForKey:](<nsdictionary/object(forkey_).md>), you can access `NSDictionary` values by their keys using _subscripting_.

**Swift**

```swift
let value = dictionary["helloString"]
```

**Objective-C**

```objc
id value = dictionary[@"helloString"];
```

### Enumerating Entries Using for-in Loops

In addition to the provided instance methods, such as [- enumerateKeysAndObjectsUsingBlock:](<nsdictionary/enumeratekeysandobjects(__).md>), you can enumerate `NSDictionary` entries using _for-in loops_.

**Swift**

```swift
for (key, value) in dictionary {
    print("Value: \(value) for key: \(key)")
}
```

**Objective-C**

```objc
for (NSString *key in dictionary) {
    id value = dictionary[key];
    NSLog(@"Value: %@ for key: %@", value, key);
}
```

In Objective-C, `NSDictionary` conforms to the [NSFastEnumeration](nsfastenumeration.md) protocol.

In Swift, `NSDictionary` conforms to the `SequenceType` protocol.

### Subclassing Notes

You generally shouldn’t need to subclass `NSDictionary`. Custom behavior can usually be achieved through composition rather than subclassing.

#### Methods to Override

If you do need to subclass `NSDictionary`, take into account that it is a [Class cluster](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassCluster.html#//apple_ref/doc/uid/TP40008195-CH7). Any subclass must override the following primitive methods:

- [- initWithObjects:forKeys:count:](<nsdictionary/init(objects_forkeys_count_).md>)
- [count](nsdictionary/count.md)
- [- objectForKey:](<nsdictionary/object(forkey_).md>)
- [- keyEnumerator](<nsdictionary/keyenumerator().md>)

The other methods of `NSDictionary` operate by invoking one or more of these primitives. The non-primitive methods provide convenient ways of accessing multiple entries at once.

#### Alternatives to Subclassing

Before making a custom class of `NSDictionary`, investigate [NSMapTable](nsmaptable.md) and the corresponding Core Foundation type, [CFDictionary](../corefoundation/cfdictionary.md). Because `NSDictionary` and `CFDictionary` are “toll-free bridged,” you can substitute a `CFDictionary` object for a `NSDictionary` object in your code (with appropriate casting). Although they are corresponding types, `CFDictionary` and `NSDictionary` do not have identical interfaces or implementations, and you can sometimes do things with `CFDictionary` that you cannot easily do with `NSDictionary`.

If the behavior you want to add supplements that of the existing class, you could write a category on `NSDictionary`. Keep in mind, however, that this category will be in effect for all instances of `NSDictionary` that you use, and this might have unintended consequences. Alternatively, you could use composition to achieve the desired behavior.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSMutableDictionary](nsmutabledictionary.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [ExpressibleByDictionaryLiteral](../swift/expressiblebydictionaryliteral.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSFastEnumeration](nsfastenumeration.md), [NSFetchRequestResult](../coredata/nsfetchrequestresult.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sequence](../swift/sequence.md)

## Topics

### Creating an Empty Dictionary

- [- init](<nsdictionary/init().md>) — Initializes a newly allocated dictionary.

### Creating a Dictionary from Objects and Keys

- [- initWithObjects:forKeys:](<nsdictionary/init(objects_forkeys_).md>) — Initializes a newly allocated dictionary with key-value pairs constructed from the provided arrays of keys and objects.
- [- initWithObjects:forKeys:count:](<nsdictionary/init(objects_forkeys_count_).md>) — Initializes a newly allocated dictionary with the specified number of key-value pairs constructed from the provided C arrays of keys and objects.
- [+ dictionaryWithObject:forKey:](<nsdictionary/init(object_forkey_).md>) — Creates a dictionary containing a given key and value.

### Creating a Dictionary from Another Dictionary

- [- initWithDictionary:](<nsdictionary/init(dictionary_)-9fw1u.md>) — Initializes a newly allocated dictionary by placing in it the keys and values contained in another given dictionary.
- [- initWithDictionary:copyItems:](<nsdictionary/init(dictionary_copyitems_).md>) — Initializes a newly allocated dictionary using the objects contained in another given dictionary.
- [init(dictionaryLiteral:)](<nsdictionary/init(dictionaryliteral_).md>) — Initializes a newly allocated dictionary from the given key-value pairs.

### Creating a Dictionary from an External Source

- [init(contentsOfURL:error:)](<nsdictionary/init(contentsofurl_error_).md>) — Initializes a newly allocated dictionary using the keys and values found at a given URL.
- [- initWithContentsOfFile:](<nsdictionary/init(contentsoffile_).md>) — Initializes a newly allocated dictionary using the keys and values found in a file at a given path. _(deprecated)_

### Creating a Dictionary from an NSCoder

- [- initWithCoder:](<nsdictionary/init(coder_).md>) — Creates a dictionary initialized from data in the provided unarchiver.

### Creating Key Sets for Shared-Key Optimized Dictionaries

- [+ sharedKeySetForKeys:](<nsdictionary/sharedkeyset(forkeys_).md>) — Creates a shared key set object for the specified keys.

### Counting Entries

- [count](nsdictionary/count.md) — The number of entries in the dictionary.

### Comparing Dictionaries

- [- isEqualToDictionary:](<nsdictionary/isequal(to_).md>) — Returns a Boolean value that indicates whether the contents of the receiving dictionary are equal to the contents of another given dictionary.

### Accessing Keys and Values

- [allKeys](nsdictionary/allkeys.md) — A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [- allKeysForObject:](<nsdictionary/allkeys(for_).md>) — Returns a new array containing the keys corresponding to all occurrences of a given object in the dictionary.
- [allValues](nsdictionary/allvalues.md) — A new array containing the dictionary’s values, or an empty array if the dictionary has no entries.
- [- valueForKey:](<nsdictionary/value(forkey_).md>) — Returns the value associated with a given key.
- [- objectsForKeys:notFoundMarker:](<nsdictionary/objects(forkeys_notfoundmarker_).md>) — Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.
- [- objectForKey:](<nsdictionary/object(forkey_).md>) — Returns the value associated with a given key.
- [- objectForKeyedSubscript:](<nsdictionary/subscript(__)-52n56.md>) — Returns the value associated with a given key.
- [subscript(_:)](<nsdictionary/subscript(__)-1bt1b.md>) — Accesses the value associated with a given key.

### Enumerating Dictionaries

- [- keyEnumerator](<nsdictionary/keyenumerator().md>) — Provides an enumerator to access the keys in the dictionary.
- [- objectEnumerator](<nsdictionary/objectenumerator().md>) — Returns an enumerator object that lets you access each value in the dictionary.
- [- enumerateKeysAndObjectsUsingBlock:](<nsdictionary/enumeratekeysandobjects(__).md>) — Applies a given block object to the entries of the dictionary.
- [- enumerateKeysAndObjectsWithOptions:usingBlock:](<nsdictionary/enumeratekeysandobjects(options_using_).md>) — Applies a given block object to the entries of the dictionary, with options specifying how the enumeration is performed.
- [makeIterator()](<nsdictionary/makeiterator().md>) — Returns an iterator over the elements of this sequence.

### Sorting Dictionaries

- [- keysSortedByValueUsingSelector:](<nsdictionary/keyssortedbyvalue(using_).md>) — Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values.
- [- keysSortedByValueUsingComparator:](<nsdictionary/keyssortedbyvalue(comparator_).md>) — Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block.
- [- keysSortedByValueWithOptions:usingComparator:](<nsdictionary/keyssortedbyvalue(options_usingcomparator_).md>) — Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block and a specified set of options.

### Filtering Dictionaries

- [- keysOfEntriesPassingTest:](<nsdictionary/keysofentries(passingtest_).md>) — Returns the set of keys whose corresponding value satisfies a constraint described by a block object.
- [- keysOfEntriesWithOptions:passingTest:](<nsdictionary/keysofentries(options_passingtest_).md>) — Returns the set of keys whose corresponding value satisfies a constraint described by a block object.

### Storing Dictionaries

- [- writeToURL:error:](<nsdictionary/write(to_).md>) — Writes a property list representation of the contents of the dictionary to a given URL.
- [- writeToURL:atomically:](<nsdictionary/write(to_atomically_).md>) — Writes a property list representation of the contents of the dictionary to a given URL. _(deprecated)_
- [- writeToFile:atomically:](<nsdictionary/write(tofile_atomically_).md>) — Writes a property list representation of the contents of the dictionary to a given path. _(deprecated)_

### Accessing File Attributes

- [- fileSize](<nsdictionary/filesize().md>) — Returns the file’s size, in bytes.
- [- fileType](<nsdictionary/filetype().md>) — Returns the file type.
- [- fileCreationDate](<nsdictionary/filecreationdate().md>) — Returns the file’s creation date.
- [- fileModificationDate](<nsdictionary/filemodificationdate().md>) — Returns file’s modification date.
- [- filePosixPermissions](<nsdictionary/fileposixpermissions().md>) — Returns the file’s POSIX permissions.
- [- fileOwnerAccountID](<nsdictionary/fileowneraccountid().md>) — Returns the file’s owner account ID.
- [- fileOwnerAccountName](<nsdictionary/fileowneraccountname().md>) — Returns the file’s owner account name.
- [- fileGroupOwnerAccountID](<nsdictionary/filegroupowneraccountid().md>) — Returns file’s group owner account ID.
- [- fileGroupOwnerAccountName](<nsdictionary/filegroupowneraccountname().md>) — Returns the file’s group owner account name.
- [- fileExtensionHidden](<nsdictionary/fileextensionhidden().md>) — Returns a Boolean value indicating whether the file hides its extension.
- [- fileIsImmutable](<nsdictionary/fileisimmutable().md>) — Returns a Boolean value indicating whether the file is immutable.
- [- fileIsAppendOnly](<nsdictionary/fileisappendonly().md>) — Returns a Boolean value indicating whether the file is append only.
- [- fileSystemFileNumber](<nsdictionary/filesystemfilenumber().md>) — Returns the filesystem file number.
- [- fileSystemNumber](<nsdictionary/filesystemnumber().md>) — Returns the filesystem number.
- [- fileHFSTypeCode](<nsdictionary/filehfstypecode().md>) — Returns file’s HFS type code.
- [- fileHFSCreatorCode](<nsdictionary/filehfscreatorcode().md>) — Returns the file’s HFS creator code.

### Describing a Dictionary

- [description](nsdictionary/description.md) — A string that represents the contents of the dictionary, formatted as a property list.
- [descriptionInStringsFileFormat](nsdictionary/descriptioninstringsfileformat.md) — A string that represents the contents of the dictionary, formatted in `.strings` file format.
- [- descriptionWithLocale:](<nsdictionary/description(withlocale_).md>) — Returns a string object that represents the contents of the dictionary, formatted as a property list.
- [- descriptionWithLocale:indent:](<nsdictionary/description(withlocale_indent_).md>) — Returns a string object that represents the contents of the dictionary, formatted as a property list.

### Supporting Types

- [Iterator](nsdictionary/iterator.md) — A class that you use to provide members of a dictionary, one-by-one.

### Initializers

- [- initWithContentsOfURL:](<nsdictionary/init(contentsof_).md>) — Initializes a newly allocated dictionary using the keys and values found at a given URL. _(deprecated)_
- [- initWithContentsOfURL:error:](<nsdictionary/init(contentsof_error_).md>) — Initializes a newly allocated dictionary using the keys and values found at a given URL.
- [init(dictionary:)](<nsdictionary/init(dictionary_)-4gc13.md>) — Initializes a newly allocated dictionary and adds to it objects from another given dictionary.

### Default Implementations

- [ExpressibleByDictionaryLiteral Implementations](nsdictionary/expressiblebydictionaryliteral-implementations.md)
- [NSDictionary Implementations](nsdictionary/nsdictionary-implementations.md)
- [Sequence Implementations](nsdictionary/sequence-implementations.md)
