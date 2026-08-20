---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/Foundation/DictionaryMethods.html
archived_at: '2026-07-15T07:51:39.217518Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](FoundationTOC.md) [!Previous Section](DictionaryIntro.md)

# Commonly Used Dictionary Methods

The following sections list some of the most commonly used methods of NSDictionary and NSMutableDictionary, grouped according to function.

## Creating Dictionaries

The methods in this section are class methods, as denoted by the plus sign (+). You use class methods to send messages to a class-in this case, NSDictionary and NSMutableDictionary. For more information on class methods, see ["Sending a Message to a Class"](../WebScript/MessageToClass.md#apple-gi2ts).

**__+ dictionary__**
: Returns an empty dictionary. Usually used to create NSMutableDictionaries. NSDictionaries created with this method are permanently empty.

```
        // Most common use
        id mutableDictionary = [NSMutableDictionary dictionary];

        // May not be what you want
        id dictionary = [NSDictionary dictionary];
```


**__+ dictionaryWithObjects:forKeys:__**
: Returns a dictionary containing entries constructed from the contents of a specified array of objects and a specified array of keys. The two arrays must have the same number of elements.

```
        id preferences = [NSMutableDictionary
            dictionaryWithObjects:@("window", "non-smoking", "747")
            forKeys:@("seatAssignment", "smoking", "aircraft")];
```


**__+ dictionaryWithObjectsAndKeys:__**
: Returns a dictionary containing entries constructed from a specified set of objects and keys. This method takes a variable number of arguments: a list of alternating objects and keys ending with __nil__.

```
        id customerPreferences = [NSDictionary dictionaryWithObjectsAndKeys:
            seatingPreference, @"seatAssignment",
            smokingPreference, @"smoking",
            aircraftPreference, @"aircraft", nil];
```


**__+ dictionaryWithDictionary:__**
: Returns a dictionary containing the contents of a specified dictionary. Usually used to create an NSMutableDictionary from an immutable NSDictionary.

**__+ dictionaryWithContentsOfFile:__**
: Returns a dictionary initialized from the contents of a specified file. The specified file can be a full or relative pathname; the file that it names must contain a string representation of a dictionary, such as that produced by the [__writeToFile:atomically:__](#apple-gezdeoa) method.
: See also [__description__](#apple-gezdema) .

## Querying Dictionaries

**__- allKeys__**
: Returns an array containing the dictionary's keys or an empty array if the dictionary has no entries. This method is useful for accessing all the entries in a dictionary. For example, the following code excerpt creates the NSArray __keys__ and uses it to access the value of each entry in the dictionary:

```
        id index;
        id keys = [dictionary allKeys];
        for (index = 0; index < [keys count]; index++) {
            value = [dictionary objectForKey:[keys
            objectAtIndex:index]];
            // Use the value
        }
```


**__- allKeysForObject:__**
: Returns an array containing all the keys corresponding to values equivalent to a specified object. Equivalency is determined using the __isEqual:__ method. If the specified object isn't equivalent to any of the values in the receiver, this method returns __nil__.

**__- allValues:__**
: Returns an array containing the dictionary's values, or an empty array if the dictionary has no entries.
: Note that the array returned from __allValues__ may have a different count than the array returned from __allKeys__. An object can be in a dictionary more than once if it corresponds to multiple keys.

**__- keysSortedByValueUsingSelector:__**
: Returns an NSArray containing the dictionary's keys such that their corresponding values are sorted in ascending order, as determined by a specified method. For example, the following code excerpt creates the NSArray __keys__ containing the string "Pasta" at index 0, "Seafood" at index 1, and "Steak" at index 2:

```
        id choices = @{"Steak" = 3; "Seafood" = 2; "Pasta" = 1};
        id keys = [choices sortedByValueUsingSelector:@"compare:"];
```


**__- count__**
: Returns the number of entries currently in the dictionary.

**__- isEqual:__**
: Returns YES if the specified object is a dictionary and has contents equivalent to the receiver; NO, otherwise. Two dictionaries have equivalent contents if they each hold the same number of entries and, for a given key, the corresponding value objects in each dictionary satisfy the __isEqual:__ test.

**__- objectForKey:__**
: Returns the object that corresponds to a specified key. For example, the following code excerpt produces the NSString __sectionPreference__ with the contents "non-smoking":

```
        id preferences = [NSMutableDictionary
            dictionaryWithObjects:@("window", "non-smoking", "747")
            forKeys:@("seatAssignment", "section", "aircraft")];
        id sectionPreference = [dictionary objectForKey:@"section"];
```


## Adding, Removing, and Modifying Entries

__Warning:__  The following methods are not supported by NSDictionary. They are available only to NSMutableDictionary objects.

**__- setObject:forKey:__**
: Adds an entry to the receiver, consisting of a specified key and its corresponding value object. If the receiver already has an entry for the specified key, the previous value for that key is replaced with the argument for __setObject:__. For example, the following code excerpt produces the NSMutableDictionary __dictionary__ with the value "non-smoking" for the key "section" and the value "aisle" for the key "seatAssignment." Notice that the original value for "seatAssignment" is replaced:

```
        id dictionary = [NSMutableDictionary dictionaryWithDictionary:
            @{"seatAssignment" = "window"}];
        [dictionary setObject:@"non-smoking" forKey:@"section"];
        [dictionary setObject:@"aisle" forKey:@"seatAssignment"];

It is an error to specify nil as an argument for setObject: or forKey:. You can't put nil in a dictionary as a key or as a value.
```


**__- addEntriesFromDictionary:__**
: Adds the entries from a specified dictionary to the receiver. If both dictionaries contain the same key, the receiver's previous value for that key is replaced with the new value.

**__- removeAllObjects__**
: Empties the dictionary of its entries.

**__- removeObjectForKey:__**
: Removes the entry for a specified key.

**__- removeObjectsForKeys:__**
: Removes the entries for each key in a specified array.

**__- setDictionary:__**
: Removes all the entries in the receiver, then adds the entries from a specified dictionary.

## Representing Dictionaries as Strings

**__- description__**
: Returns a string that represents the contents of the receiver. For example, the following code excerpt produces the string "{"seatAssignment" = "Window"; "section" = "Non-smoking"; "aircraft" = "747"}":

```
        id preferences = [NSMutableDictionary
            dictionaryWithObjects:@("window", "non-smoking", "747")
            forKeys:@("seatAssignment", "section", "aircraft")];
        id description = [preferences description];
```


## Storing Dictionaries

**__- writeToFile:atomically:__**
: Writes the dictionary's string representation to a specified file using the __description__ method. Returns YES on success and NO on failure. If YES is specified for __atomically:__, this method attempts to write the file safely so that an existing file with the specified path is not overwritten. It does not create a new file at the specified path unless the write is successful. The resulting file is suitable for use with [__dictionaryWithContentsOfFile:__](#apple-geytmni). For example, the following excerpt creates an NSMutableDictionary from the contents of the file specified by __path__, updates the object for the key @"Language", and saves the updated dictionary back to the same file:

```
        id defaults = [NSMutableDictionary
            dictionaryWithContentsOfFile:path];
        [defaults setObject:newLanguagePreference forKey:@"Language"];
        [defaults writeToFile:path atomically:YES];

See also description.
```

[!Table of Contents](FoundationTOC.md) [!Next Section](DateIntro.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
