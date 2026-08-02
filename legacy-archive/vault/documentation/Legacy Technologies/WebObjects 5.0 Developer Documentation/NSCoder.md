---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSCoder.html
archived_at: '2026-07-15T08:13:55.813961Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSCoder

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

NSCoder is an abstract class that declares the API used by concrete subclasses to transfer objects and other data items between memory and some other format. This capability provides the basis for archiving (where objects and data items are stored on disk) and distribution (where objects and data items are copied between different processes or threads).

You should never need to subclass NSCoder. Rather, WebObjects provides private concrete subclasses that it uses by default. However, you might interact with a coder object if you create a class that implements the [NSCoding](NSCoding.md#apple-ineucskcizbeq) interface.

NSCoder operates on scalars (booleans, bytes, and integers, for example), and any other types of object. A coder object stores object type information along with an object's data, so an object decoded from a stream of bytes is normally of the same class as the object that was originally encoded into the stream.

## Encoding and Decoding Objects and Data Items

To encode or decode an object or data item, you must first create a coder object, then send it a message defined by NSCoder or by a concrete subclass to actually encode or decode the item. NSCoder itself defines no particular method for creating a coder; this typically varies with the subclass.

To encode an object or data item, use any of the __encode...__ methods. To decode an object or data item, simply use the __decode...__ method corresponding to the original __encode...__ method. Matching these is important, as the method originally used determines the format of the encoded data.

NSCoder's interface is quite general. Concrete subclasses aren't required to properly implement all of NSCoder's methods, and may explicitly restrict themselves to certain types of operations.

## Managing Object Graphs

Objects frequently contain references to other objects, which may in turn contain references to other objects. When analyzed, a group of objects may contain circular references or one object may be referred to by several other objects. In these cases, the objects form an object graph and require special handling to preserve the graph structure. NSCoder's [encodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsu6ytkmvrxi) method preserves the graph structure.

## Method Types

---

> **Encoding data**
>
> : [encodeBoolean](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsue33pnrswc3q): [encodeByte](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsue6lumu): [encodeBytes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsue6lumvzq): [encodeChar](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsug2dboi): [encodeClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsug3dbonzq): [encodeDouble](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsui33vmjwgk): [encodeFloat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsum3dpmf2a): [encodeInt](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsus3tu): [encodeLong](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsuy33om4): [encodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsu6ytkmvrxi): [encodeObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsu6ytkmvrxi4y): [encodeShort](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsvg2dpoj2a)
>
> **Decoding data**
>
> : [decodeBoolean](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsue33pnrswc3q): [decodeByte](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsue6lumu): [decodeBytes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsue6lumvzq): [decodeChar](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsug2dboi): [decodeClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsug3dbonzq): [decodeDouble](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsui33vmjwgk): [decodeFloat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsum3dpmf2a): [decodeInt](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsus3tu): [decodeLong](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsuy33om4): [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsu6ytkmvrxi): [decodeObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsu6ytkmvrxi4y): [decodeShort](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsvg2dpoj2a)
>
> **All methods**
>
> : [finishCoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5tgs3tjonueg33enfxgo): [prepareForReading](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5yhezlqmfzgkrtpojjgkylenfxgo): [prepareForWriting](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5yhezlqmfzgkrtpojlxe2lunfxgo)

## Constructors

---

### NSCoder

`public NSCoder()`

The no-arg constructor. Don't use this method; because NSCoder is an abstract class, you can never create an instance of it.

---

## Instance Methods

---

### decodeBoolean

`public abstract boolean decodeBoolean()`

Decodes and returns a boolean value that was previously encoded with [encodeBoolean](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsue33pnrswc3q).

---

### decodeByte

`public abstract byte decodeByte()`

Decodes and returns a byte value that was previously encoded with [encodeByte](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsue6lumu).

---

### decodeBytes

`public abstract byte[] decodeBytes()`

Decodes and returns an array of byte values that were previously encoded with [encodeBytes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsue6lumvzq).

---

### decodeChar

`public abstract char decodeChar()`

Decodes and returns a char value that was previously encoded with [encodeChar](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsug2dboi).

---

### decodeClass

`public abstract Class decodeClass()`

Decodes and returns a class that was previously encoded with [encodeClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsug3dbonzq).

---

### decodeDouble

`public abstract double decodeDouble()`

Decodes and returns a double value that was previously encoded with [encodeDouble](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsui33vmjwgk).

---

### decodeFloat

`public abstract float decodeFloat()`

Decodes and returns a float value that was previously encoded with [encodeFloat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsum3dpmf2a).

---

### decodeInt

`public abstract int decodeInt()`

Decodes and returns an int value that was previously encoded with [encodeInt](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsus3tu).

---

### decodeLong

`public abstract long decodeLong()`

Decodes and returns a long value that was previously encoded with [encodeLong](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsuy33om4).

---

### decodeObject

`public abstract Object decodeObject()`

Decodes and returns an object that was previously encoded with [encodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsu6ytkmvrxi).

---

### decodeObjects

`public abstract Object[] decodeObjects()`

Decodes and returns an array of objects that were previously encoded with [encodeObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsu6ytkmvrxi4y).

---

### decodeShort

`public abstract short decodeShort()`

Decodes and returns a short value that was previously encoded with [encodeShort](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sw4y3pmrsvg2dpoj2a).

---

### encodeBoolean

`public abstract void encodeBoolean(boolean aBoolean)`

Encodes _aBoolean_. To decode a value encoded with this method, use [decodeBoolean](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsue33pnrswc3q).

---

### encodeByte

`public abstract void encodeByte(byte aByte)`

Encodes _aByte_. To decode a value encoded with this method, use [decodeByte](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsue6lumu).

---

### encodeBytes

`public abstract void encodeBytes(byte[] bytes[])`

Encodes the _bytes_ array. To decode a value encoded with this method, use [decodeBytes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsue6lumvzq).

---

### encodeChar

`public abstract void encodeChar(char aChar)`

Encodes _aChar_. To decode a value encoded with this method, use [decodeChar](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsug2dboi).

---

### encodeClass

`public abstract void encodeClass(Class aClass)`

Encodes _aClass_. To decode a value encoded with this method, use [decodeClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsug3dbonzq).

---

### encodeDouble

`public abstract void encodeDouble(double aDouble)`

Encodes _aDouble_. To decode a value encoded with this method, use [decodeDouble](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsui33vmjwgk).

---

### encodeFloat

`public abstract void encodeFloat(float aFloat)`

Encodes _aFloat_. To decode a value encoded with this method, use [decodeFloat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsum3dpmf2a).

---

### encodeInt

`public abstract void encodeInt(int anInt)`

Encodes _anInt_. To decode a value encoded with this method, use [decodeInt](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsus3tu).

---

### encodeLong

`public abstract void encodeLong(long aLong)`

Encodes _aLong_. To decode a value encoded with this method, use [decodeLong](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsuy33om4).

---

### encodeObject

`public abstract void encodeObject(Object anObject)`

Encodes _anObject_. To decode a value encoded with this method, use [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsu6ytkmvrxi).

---

### encodeObjects

`public abstract void encodeObjects(Object[] anObject[])`

Encodes the _objects_ array. To decode a value encoded with this method, use [decodeObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsu6ytkmvrxi4y).

---

### encodeShort

`public abstract void encodeShort(short aShort)`

Encodes _aShort_. To decode a value encoded with this method, use [decodeShort](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwizlsf5sgky3pmrsvg2dpoj2a).

---

### finishCoding

`public void finishCoding()`

Cleans up the receiver's state after the receiver has finished encoding data. NSCoder's implementation does nothing.

---

### prepareForReading

`public void prepareForReading(java.io.InputStream inputStream)`

Prepares the receiver for reading data from _inputStream_. NSCoder's implementation does nothing.

---

### prepareForWriting

`public void prepareForWriting(java.io.OutputStream outputStream)`

Prepares the receiver for writing to _outputStream_. NSCoder's implementation does nothing.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
