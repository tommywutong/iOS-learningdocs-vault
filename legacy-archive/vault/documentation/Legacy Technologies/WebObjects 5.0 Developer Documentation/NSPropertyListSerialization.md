---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSPropListSerial.html
archived_at: '2026-07-15T08:13:56.422664Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSPropertyListSerialization

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

This class provides static methods that convert between property lists and their string representations, which can be either strings or NSData objects. A property list is a structure that represents organized data. It can be built from a combination of NSArrays, NSDictionaries, Strings, and NSData objects.

The string representation can be in XML or the ASCII plist format. To distinguish between the two formats, the parser that converts strings to property lists checks if the string starts with `<?xml`. A discussion of the ASCII plist format, _A Primer on ASCII Property Lists_, is available in the Mac OS X section of the Apple Developer Connection website. A discussion of XML property lists, _Property List Services_, is also available in the same area of the Apple Developer Connection website.

Some methods do not support XML property list representations, specifically [booleanForString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3cn5xwyzlbnzdg64storzgs3th) and [intForString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3jnz2em33skn2he2lom4).

The NSPropertyListSerialization class cannot be instantiated.

## Method Types

---

> **Extracting typed data**
>
> : [arrayForString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3bojzgc6kgn5zfg5dsnfxgo): [booleanForString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3cn5xwyzlbnzdg64storzgs3th): [dictionaryForString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3enfrxi2lpnzqxe6kgn5zfg5dsnfxgo): [intForString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3jnz2em33skn2he2lom4)
>
> **Converting to property lists**
>
> : [propertyListFromData](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3qojxxazlsor4uy2ltordhe33nirqxiyi): [propertyListFromString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3qojxxazlsor4uy2ltordhe33nkn2he2lom4)
>
> **Converting from property lists**
>
> : [dataFromPropertyList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3emf2gcrtsn5wva4tpobsxe5dzjruxg5a): [stringFromPropertyList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3torzgs3thizzg63kqojxxazlsor4uy2ltoq)

## Static Methods

---

### arrayForString

`public static NSArray arrayForString(String string)`

Parses the property list representation _string_ and returns the resulting property list as an NSArray. If the root object is not an array, this method throws a ClassCastException.

__See Also:__ [dictionaryForString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3enfrxi2lpnzqxe6kgn5zfg5dsnfxgo).

---

### booleanForString

`public static boolean booleanForString(String string)`

Returns a boolean based on _string_ according to the following table:

|  |  |
| --- | --- |
| ___string_'s value__ | __Value returned__ |
| "`YES`" | `true` |
| "`true`" | `true` |
| Any other value | `false` |

The tests for "`YES`" and "`true`" are case insensitive.

---

### dataFromPropertyList

`public static NSData dataFromPropertyList( Object object, String encoding)`

`public static NSData dataFromPropertyList(Object object)`

Converts the property list _object_ into a string and returns it as a NSData object. The _encoding_ parameter specifies the encoding used to convert the characters in the result string to byte. The one-argument version of the method uses the platform's default character encoding.

__See Also:__ [stringFromPropertyList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3torzgs3thizzg63kqojxxazlsor4uy2ltoq)

---

### dictionaryForString

`public static NSDictionary dictionaryForString(String string)`

Parses the property list representation _string_ and returns the resulting property list as an NSDictionary. If the root object is not a dictionary, this method throws a ClassCastException.

__See Also:__ [arrayForString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3bojzgc6kgn5zfg5dsnfxgo).

---

### intForString

`public static int intForString(String string)`

Parses _string_ and returns the corresponding integer. If _string_ is `null`, returns zero.

---

### propertyListFromData

`public static Object propertyListFromData( NSData data, String encoding)`

`public static Object propertyListFromData(NSData data)`

Returns a property list converted from the byte array representation in _data_. The _encoding_ parameter specifies the encoding used to convert the bytes in the _data_ byte array to characters in a string representation. The one-argument version of the method uses the platform's default character encoding.

__See Also:__ [propertyListFromString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3qojxxazlsor4uy2ltordhe33nkn2he2lom4)

---

### propertyListFromString

`public static Object propertyListFromString(String string)`

Returns a property list converted from the string representation _string_.

---

### stringFromPropertyList

`public static String stringFromPropertyList(Object object)`

Converts the property list _object_ into a string and returns it.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
