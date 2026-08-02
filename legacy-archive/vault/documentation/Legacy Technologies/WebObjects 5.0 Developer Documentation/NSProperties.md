---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSProperties.html
archived_at: '2026-07-15T08:13:56.440427Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSProperties

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

The NSProperties class enhances Java's properties mechanism to merge application properties with the standard system properties available using the __java.lang.System.getProperties()__ method. The application properties can come from three sources: the command line, the application's `Properties` file, and the `Properties` files of any frameworks your application includes.

This class has only static methods and cannot be instantiated.

## Accessing the Properties

To access the application properties you first need to merge the application and command line properties with the system properties. A WebObjects application automatically performs this step for you. You can then access the property as a string, and convert the string to the property's actual data type.

To obtain the application properties and merge them with the system properties you invoke [setPropertiesFromArgv](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tunfsxgl3tmv2fa4tpobsxe5djmvzum4tpnvaxez3w). Application properties can come from the application's `Properties` file, the `Properties` files for the frameworks the application includes, and the command line. For more information about `Properties` files, see ["The Properties File" (page 238)](#apple-ijbuiscgindui). For more information about specifying properties on the command line, see ["Command Line Properties" (page 238)](#apple-ijbuisccjbbeg).

Every property is a key-value pair. For example, on Unix machines, the property value for the key "file.separator" is "/". To access a property corresponding to a particular key, use the __java.lang.System.getProperty__ method. This method returns the property as a string.

If the property string represents a boolean value, NSArray, or NSDictionary you need to convert it to the appropriate data type using the [NSPropertyListSerialization](NSPropertyListSerialization.md#apple-inbusscdivcec) [booleanForString](NSPropertyListSerialization.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3cn5xwyzlbnzdg64storzgs3th), [arrayForString](NSPropertyListSerialization.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3bojzgc6kgn5zfg5dsnfxgo), or [dictionaryForString](NSPropertyListSerialization.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3enfrxi2lpnzqxe6kgn5zfg5dsnfxgo) method, respectively. NSPropertyListSerialization also provides an [intForString](NSPropertyListSerialization.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3jnz2em33skn2he2lom4) method to simplify converting a property string to an integer.

## The Properties File

The properties must be stored in a file named `Properties` in the application or framework's `Resources` directory. You can add a `Properties` file to your application or framework by adding it to the Resources suitcase in Project Builder.

The Properties file must be in the format specified by java.io.Properties. See Sun's documentation for the __load__ method in that class for the format specification.

Boolean values, NSArrays, and NSDictionaries must be specified using the property list representation. See the [NSPropertyListSerialization](NSPropertyListSerialization.md#apple-inbusscdivcec) class description for more information on property lists.

## Command Line Properties

The [setPropertiesFromArgv](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tunfsxgl3tmv2fa4tpobsxe5djmvzum4tpnvaxez3w) method parses the command line arguments are recognizes the property formats listed in the table below.

|  |  |
| --- | --- |
| __Format__ | __Example__ |
| `-D`key`=`value | `-DWOPort=4321` |
| `-`key value | `-WOAutoOpenInBrowser NO` |

Properties specified in these formats will be available as system properties after you invoke __setPropertiesFromArgv__.

## Static Methods

---

### __arrayForKey__

`public static NSArray arrayForKey(String key)`

Deprecated in the Java Foundation framework. Don't use this method. Instead, get the system property using `System.getProperty(key)` and convert it to an NSArray using [NSPropertyListSerialization](NSPropertyListSerialization.md#apple-inbusscdivcec)'s [arrayForString](NSPropertyListSerialization.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3bojzgc6kgn5zfg5dsnfxgo) method.

Returns the system property with the specified name as an NSArray or `null` if no system property with that name exists. Throws a NullPointerException if _key_ is `null`.

---

### __booleanForKey__

`public static boolean booleanForKey(String key)`

Deprecated in the Java Foundation framework. Don't use this method. Instead, get the system property using `System.getProperty(key)` and convert it to a `boolean` using [NSPropertyListSerialization](NSPropertyListSerialization.md#apple-inbusscdivcec)'s [booleanForString](NSPropertyListSerialization.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3cn5xwyzlbnzdg64storzgs3th) method.

Returns the system property with the specified name as a `boolean`. Returns `false` if no system property with that name exists. Throws a NullPointerException if _key_ is `null`.

---

### __dataForKey__

`public static NSData dataForKey(String key)`

Deprecated in the Java Foundation framework. Don't use this method. Instead, get the system property using `System.getProperty(key)`, convert it to a property list using [NSPropertyListSerialization](NSPropertyListSerialization.md#apple-inbusscdivcec)'s [propertyListFromString](NSPropertyListSerialization.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3qojxxazlsor4uy2ltordhe33nkn2he2lom4) method, and convert the property list to an NSData object using NSPropertyListSerialization's [dataFromPropertyList](NSPropertyListSerialization.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3emf2gcrtsn5wva4tpobsxe5dzjruxg5a) method.

Interprets the system property with the specified name as a string representation of a property list, converts it to bytes using the current encoding, and stores the result in an NSData object. Returns `null` if no system property with that name exists. Throws a NullPointerException if _key_ is `null`.

---

### __dictionaryForKey__

`public static NSDictionary dictionaryForKey(String key)`

Deprecated in the Java Foundation framework. Don't use this method. Instead, get the system property using `System.getProperty(key)` and convert it to an NSDictionary using [NSPropertyListSerialization](NSPropertyListSerialization.md#apple-inbusscdivcec)'s [dictionaryForString](NSPropertyListSerialization.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3enfrxi2lpnzqxe6kgn5zfg5dsnfxgo) method.

Returns the system property with the specified name as an NSDictionary. Returns `null` if no system property with that name exists. Throws a NullPointerException if _key_ is `null`.

---

### __doubleForKey__

`public static double doubleForKey(String key)`

Deprecated in the Java Foundation framework. Don't use this method. Instead, get the system property using `System.getProperty(key)` and convert it to a `double`.

Returns the system property with the specified name as a `double`. Returns 0 if no system property with that name exists. Throws a NullPointerException if _key_ is `null`.

---

### __floatForKey__

`public static float floatForKey(String key)`

Deprecated in the Java Foundation framework. Don't use this method. Instead, get the system property using `System.getProperty(key)` and convert it to a `float`.

Returns the system property with the specified name as a `float`. Returns 0 if no system property with that name exists. Throws a NullPointerException if _key_ is `null`.

---

### __integerForKey__

`public static int integerForKey(String key)`

Deprecated in the Java Foundation framework. Don't use this method. Instead, get the system property using `System.getProperty(key)` and convert it to an `int` using [NSPropertyListSerialization](NSPropertyListSerialization.md#apple-inbusscdivcec)'s [intForString](NSPropertyListSerialization.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudsn5ygk4tupfggs43uknsxe2lbnruxuylunfxw4l3jnz2em33skn2he2lom4) method.

Returns the system property with the specified name as an `int`. Returns 0 if no system property with that name exists. Throws a NullPointerException if _key_ is `null`.

---

### __longForKey__

`public static long longForKey(String key)`

Deprecated in the Java Foundation framework. Don't use this method. Instead, get the system property using `System.getProperty(key)` and convert it to a `long`.

Returns the system property with the specified name as a `long`. Returns 0 if no system property with that name exists. Throws a NullPointerException if _key_ is `null`.

---

### setPropertiesFromArgv

`public static void setPropertiesFromArgv(String[] argv)`

Loads all of the application's properties and merges them with the Java System properties. This method obtains the properties (by invoking [NSProperties](NSBundle.md#apple-infeiq2diveuq)'s [properties](NSBundle.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxa4tpobsxe5djmvzq) method) for every bundle in the application including the application and all of the frameworks it includes. It also merges any properties specified by the string array into the system properties.

---

### __stringForKey__

`public static String stringForKey(String key)`

Deprecated in the Java Foundation framework. Don't use this method. Instead, get the system property using `System.getProperty(key)`.

Equivalent to `System.getProperty(key)`.

---

### __valuesFromArgv__

`public static NSDictionary valuesFromArgv(String[])`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
