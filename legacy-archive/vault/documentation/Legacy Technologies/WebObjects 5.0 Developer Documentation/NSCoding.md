---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Interfaces/NSCoding.html
archived_at: '2026-07-15T08:13:56.777068Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSCoding

> **__Package:__**
> : com.webobjects.foundation

---

## Interface Description

---

The [NSCoding](#apple-ineucskcizbeq) interface declares the methods that a class must implement so that instances of that class can be encoded and decoded. This capability provides the basis for archiving (where objects and other structures are stored on disk) and distribution (where objects are copied to different address spaces). See the [NSCoder](NSCoder.md#apple-ijeugr2jivduo) class specification for an introduction to coding.

In keeping with object-oriented design principles, an object being encoded or decoded is responsible for encoding and decoding its instance variables. A coder instructs the object to do so by invoking [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwk3tdn5sgkv3jorueg33emvza) or __decodeObject__, respectively. __encodeWithCoder__ instructs the object to encode its instance variables to the coder provided. Conversely, __decodeObject__ is the method that creates an object from the data in the coder provided.

The method __decodeObject__ isn't strictly part of the [NSCoding](#apple-ineucskcizbeq) interface, but it is required of any class that implements the interface. __decodeObject__ is a static method, and therefore can't be formally declared in the [NSCoding](#apple-ineucskcizbeq) interface. Any class that should be codable must adopt the NSCoding interface, implement its methods, and implement the static method __decodeObject__.

## Encoding

When an object receives an __encodeWithCoder__ message, it should encode all of its vital instance variables, after sending a message to __super__ if its superclass also conforms to the [NSCoding](#apple-ineucskcizbeq) interface. An object doesn't have to encode all of its instance variables. Some values may not be important to reestablish and others may be derivable from related state upon decoding. Other instance variables should be encoded only under certain conditions.

For example, suppose you were creating a fictitious MapView class that displays a legend and a map at various magnifications. The MapView class defines several instance variables, including the name of the map and the current magnification. The __encodeWithCoder__ method of MapView might look like the following:

> ```
> public void encodeWithCoder(NSCoder coder) {
>     super.encodeWithCoder(coder);
>     coder.encodeObject(mapName);
>     coder.encodeInt(magnification);
> }
> ```

This example assumes that the superclass of MapView also implements the [NSCoding](#apple-ineucskcizbeq) interface. If the superclass of your class does not implement [NSCoding](#apple-ineucskcizbeq), you should omit the line that invokes `super`'s __encodeWithCoder__ method.

[encodeObject](NSCoder.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsu6ytkmvrxi) and [encodeInt](NSCoder.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsus3tu) are coder methods that you can use to encode instance variables of your class. There are other coder methods for other types. The coder also defines corresponding methods for decoding values. See the [NSCoder](NSCoder.md#apple-ijeugr2jivduo) class specification for a list of methods.

## Decoding

In __decodeObject__ the class should first send a message to `super`'s implementation of __decodeObject__ (if appropriate) to initialize inherited instance variables. It should then decode and initialize its own. MapView's implementation of __decodeObject__ might look like this:

> ```
> public static Object decodeObject(NSCoder coder) {
>     MapView result = (MapView)(MapView.class.decodeObject(coder));
>     result.mapName = (String)coder.decodeObject();
>     result.magnification = coder.decodeInt();
>     return result;
> }
> ```

If the superclass of your class does not implement [NSCoding](#apple-ineucskcizbeq), you should simply create a new instance of your class instead of invoking the superclass's __decodeObject__ method.

## Making Substitutions During Coding

During encoding a coder allows an object being coded to substitute a different class for itself than the object's actual class. For example, this allows a private class to be represented in a coder by a public class. To allow the substitution, a coder invokes the method [classForCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwg3dbonzum33sinxwizls) on the object before its encoded. The coder uses the class returned by this method instead of the object's actual class.

## Static Methods

---

### decodeObject

`public static Object decodeObject(NSCoder coder)`

Creates an object from the data in _coder_. Classes that implement the NSCoding interface must also implement this method.

This method isn't strictly part of this interface because static methods can't be formally declared in an interface. However, this method is so closely related to the interface as to be considered part of it.

---

## Instance Methods

---

### classForCoder

`public Class classForCoder()`

Allows the receiver, before being encoded, to substitute a class other than its own in a coder. For example, private subclasses can substitute the name of a public superclass when being encoded.

---

### encodeWithCoder

`public void encodeWithCoder(NSCoder coder)`

Encodes the receiver using _coder_.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
