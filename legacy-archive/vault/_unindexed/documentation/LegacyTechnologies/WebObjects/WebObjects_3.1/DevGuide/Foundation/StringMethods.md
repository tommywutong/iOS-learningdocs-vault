---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Foundation/StringMethods.html
archived_at: '2026-07-15T07:46:48.194503Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Foundation.book.md) [!Previous Section](StringIntro.md)

# Commonly Used String Methods

The following sections list the most commonly used NSString and NSMutableString methods. The methods covered are grouped in the following categories:

- [Creating Strings](#apple-hezta)
- [Combining and Dividing Strings](#apple-he3di)
- [Comparing Strings](#apple-he4de)
- [Converting String Contents](#apple-he4ts)
- [Modifying Strings](#apple-geydana)
- [Storing Strings](#apple-geydcoi)

## Creating Strings

The methods in this section are class methods, as denoted by the plus sign (+). You use class methods to send messages to a class-in this case, NSString and NSMutableString. For more information on class methods, see "[Messaging in WebScript](../WebScript/Messaging.md)" in the "Using WebScript" chapter.

**__+ string__**
: Returns an empty string. Usually used to create NSMutableStrings. NSStrings created with this method are permanently empty.

```
/* Most common use */
id mutableString = [NSMutableString string];

/* May not be what you want */
id string = [NSString string];
```


**__+ stringWithFormat:__**
: Returns a string created by substituting arguments into a specified format string in the manner that __printf()__ does in the C programming language. In WebScript, only the "at sign" (@) conversion character is supported, and it expects a corresponding __id__ argument.

```
// These are fine
id party = [NSString stringWithFormat:@"Party date: %@", partyDate];
id mailto = [NSString stringWithFormat:@"mailto: %@", [person email]];
id footer = [NSString stringWithFormat:
@"Interaction %@ in session %@.",
    numberOfInteractions, sessionNumber];

// C users, NO! This won't work. Only %@ is supported.
id string = [NSString stringWithFormat:@"%d of %d %s", x, y,
    cString];
```


**__+ stringWithString:__**
: Returns a string containing the same contents as a specified string. This method is usually used to create an NSMutableString from an NSString. For example, the following statement:

```
id mutableString = [NSMutableString stringWithString:@"Change me."];
```


creates an NSMutableString from a constant NSString object.

**__+ stringWithContentsOfFile:__**
: Returns a string created by reading characters from a specified file. For example, the following statement creates an NSString containing the contents of the file specified in __path__.

```
id fileContents = [NSString stringWithContentsOfFile:path];
```


See also [__writeToFile:atomically:__](DictionaryMethods.md#apple-gezdeoa).

## Combining and Dividing Strings

**__- stringByAppendingFormat:__**
: Returns a string made by appending to the receiver a string constructed from a specified format string and following arguments in the manner of [__stringWithFormat:__](#apple-he2dm). For example, assume the variable __guestName__ contains the string "Rena". Then the following code excerpt:

```
id string = @"Hi";
id message = [string stringByAppendingFormat:@", %@!", guestName];
```


produces the string __message__ with contents "Hi, Rena!".

**__- stringByAppendingString:__**
: Returns a string object made by appending a specified string to the receiver. This code excerpt, for example:

```
id errorTag = @"Error: ";
id errorString = @"premature end of file.";
id errorMessage = [errorTag stringByAppendingString:errorString];
```


produces the string "Error: premature end of file.".

**__- componentsSeparatedByString:__**
: Returns an NSArray containing substrings from the receiver that have been divided by a specified separator string. For example, the following statements:

```
id toolString = @"wrenches, hammers, saws";
id toolArray = [toolString componentsSeparatedByString:@", "];
```


produce an NSArray containing the strings "wrenches", "hammers", and "saws."

See also [__componentsJoinedByString:__](ArrayMethods.md#apple-geytcoi) (NSArray and NSMutableArray).

**__- substringToIndex:__**
: Returns a string object containing the characters of the receiver up to, but not including, the one at the specified index.

**__- substringFromIndex:__**
: Returns a string object containing the characters of the receiver from the one at the specified index to the end.

## Comparing Strings

**__- compare:__**
: Returns -1 if the receiver precedes a specified string in lexical ordering, 0 if it is equal, and 1 if it follows. For example, the following statements:

```
if ([@"hello" compare:@"Hello"] == -1) {
    result = [NSString stringWithFormat:
            @"'%@' precedes '%@' lexicographically.",
            @"hello", @"Hello"];
}
```


result in an NSString __result__ with the contents "`hello' precedes `Hello' lexicographically."

**__- caseInsensitiveCompare:__**
: Same as __compare:__, but case distinctions among characters are ignored.

**__- isEqual:__**
: Returns YES if a specified object is equivalent to the receiver, NO otherwise. An object is equivalent to a string if the object is an NSString or an NSMutableString and __compare:__ returns 0. For example, the following statements:

```
if ([string isEqual:newString) {
    result = @"Found a match";
}
```


assign the contents "Found a match" to __result__ if __string__ and __newString__ are lexicographically equal.

## Converting String Contents

**__- doubleValue__**
: Returns the the floating-point value of the receiver's text as a double, skipping white space at the beginning of the string

**__- floatValue__**
: Returns the floating-point value of the receiver's text as a float, skipping white space at the beginning of the string.

**__- intValue__**
: Returns the integer value of the string's text, assuming a decimal representation and skipping white space at the beginning of the string.

## Modifying Strings

__Warning:__  The following methods are not supported by NSString. They are only available to NSMutableString objects.

**__- appendFormat:__**
: Appends a constructed string to the receiver. Creates the new string by using [__stringWithFormat:__](#apple-he2dm) method with the arguments listed. For example, in the following code excerpt, assume the variable __guestName__ contains the string "Rena":

```
id message = [NSMutableString stringWithString:@"Hi"];
[message appendFormat:@", %@!", guestName];
```


__message__ has the resulting contents "Hi, Rena!".

**__- appendString:__**
: Adds the characters of a specified string to the end of the receiver. For example, the following statements create an NSMutableString and append another string to its initial value:

```
id mutableString = [NSMutableString stringWithFormat:@"Hello "];
[mutableString appendString:@"world!"];
```


__mutableString__ has the resulting contents "Hello world!".

**__- setString:__**
: Replaces the characters of the receiver with those in a specified string. For example, the following statement replaces the contents of an NSMutableString with the empty string:

```
[mutableString setString:@""];
```


## Storing Strings

**__- writeToFile:atomically:__**
: Writes the string to a specified file, returning YES on success and NO on failure. If YES is specified for __atomically:__, this method writes the string to an auxiliary file and then renames the auxiliary file to the specified path. In this way, it ensures that the contents of the specified path do not become corrupted if the system crashes during writing. The resulting file is suitable for use with __stringWithContentsOfFile:__. For example, the following code excerpt:

```
id errorLog = [NSString stringWithContentsOfFile:errorPath];
id newErrorLog = [errorLog stringByAppendingFormat:@"%@: %@.\n",
        timeStamp, @"premature end of file."];
[newErrorLog writeToFile:errorPath atomically:YES];
```


reads the contents of an error log stored in a file, appends a new error to the log, and saves the updated log to the same file.

[!Table of Contents](Foundation.book.md) [!Next Section](ArrayIntro.md)
