---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSData.html
archived_at: '2026-07-15T08:13:55.884087Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSData

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : Cloneable: java.io.Serializable: NSCoding

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

NSData and its subclass NSMutableData provide data objects, object-oriented wrappers for byte buffers. Data objects let byte arrays take on the behavior of Foundation objects. NSData creates static data objects, and NSMutableData creates dynamic data objects.

Data objects can wrap data of any size. The object contains no information about the data itself (such as its type); the responsibility for deciding how to use the data lies with the client. In particular, it will not handle byte-order swapping when distributed between big-endian and little-endian machines.

[Table 0-5](#apple-ijbuqskkincec) describes the NSData methods that provide the basis for all NSData's other methods; that is, all other methods are implemented in terms of these four. If you create a subclass of NSData, you need only ensure that these base methods work properly. Having done so, you can be sure that all your subclass's inherited methods operate properly.

__Table 0-5 NSData's Base API__

| __Method__ | __Description__ |
| [bytesNoCopy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpmj4xizltjzxug33qpe) | Returns the internal byte array that contains the receiver's data. Used by mutable subclasses of NSData. |
| [immutableBytes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpnfww25lumfrgyzkcpf2gk4y) | Returns an immutable byte array that contains the receiver's data. |
| [immutableRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpnfww25lumfrgyzksmfxgozi) | Returns an immutable NSRange object that specifies the receiver's length. |
| [rangeNoCopy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpojqw4z3fjzxug33qpe) | Returns the internal NSRange object that specifies the receiver's length. Used by mutable subclasses of NSData. |

To extract a data object that contains a subset of the bytes in another data object, use the [subdataWithRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpon2wezdborqvo2lunbjgc3thmu) method. To determine if two data objects are equal, use the [isEqualToData](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpnfzuk4lvmfwfi32emf2gc) method, which does a byte-for-byte comparison.

The [writeToStream](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpo5zgs5dfkrxvg5dsmvqw2) method lets you write the contents of a data object to a stream (a java.io.OutputStream object).

## Constants

---

NSData defines the following constant:

|  |  |  |
| --- | --- | --- |
| __Constant__ | __Type__ | __Description__ |
| EmptyData | NSData | An empty data object, which can be shared to save memory. |

## Interfaces Implemented

---

> : Cloneable
>
> : [clone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpmnwg63tf)
>
> :
>
> : java.io.Serializable:
>
> : NSCoding
>
> : [classForCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpmnwgc43tizxxeq3pmrsxe): [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgrdborqs6zdfmnxwizkpmjvgky3u): [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpmvxgg33emvlws5diinxwizls)
>
> :

## Method Types

---

> **Constructors**
>
> : [NSData](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpjzjuiylume)
>
> **Accessing data**
>
> : [bytes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpmj4xizlt): [bytesNoCopy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpmj4xizltjzxug33qpe): [immutableBytes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpnfww25lumfrgyzkcpf2gk4y): [subdataWithRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpon2wezdborqvo2lunbjgc3thmu)
>
> **Testing data**
>
> : [immutableRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpnfww25lumfrgyzksmfxgozi): [length](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpnrsw4z3una): [rangeNoCopy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpojqw4z3fjzxug33qpe): [isEqualToData](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpnfzuk4lvmfwfi32emf2gc)
>
> **Storing data**
>
> : [stream](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpon2hezlbnu): [writeToStream](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpo5zgs5dfkrxvg5dsmvqw2)
>
> **Methods inherited from Object**
>
> : [equals](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpmvyxkylmom): [hashCode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpnbqxg2cdn5sgk): [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjporxvg5dsnfxgo)
>
> **Deprecated methods**
>
> : [dataWithContentsOfFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgrdborqs6zdborqvo2lunbbw63tumvxhi42pmzdgs3df): [dataWithContentsOfMappedFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgrdborqs6zdborqvo2lunbbw63tumvxhi42pmzgwc4dqmvsem2lmmu): [writeToFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpo5zgs5dfkrxum2lmmu): [writeToURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpo5zgs5dfkrxvkusm)

## Constructors

---

### NSData

`public NSData()`

Creates an empty data object.

`public NSData(NSData data)`

Creates a data object containing the contents of another data object, _data_.

`public NSData(String string)`

Deprecated in the Java Foundation Framework. Don't use this constructor. Use `NSData(string.getBytes())` instead.

`public NSData(byte[] bytes)`

Creates a data object with all the data in the byte array _bytes_.

`public NSData( byte[] bytes, int offset, int count)`

Creates a data object with the bytes from the language array _bytes_ that fall in the range specified by _offset_ and _count_.

`public NSData( byte[] bytes, NSRange range)`

Creates a data object with the bytes from the language array _bytes_ that fall in the range specified by _range_.

`public NSData( byte[] bytes, NSRange range, boolean noCopy)`

Creates a data object with the bytes from the language array _bytes_ that are fall in the range specified by _range_. The _noCopy_ parameter specifies whether or not a copy of _bytes_ is made.

`public NSData(java.io.File file) throws java.io.IOException`

Deprecated in the Java Foundation Framework. Don't use this constructor. Use `NSData(new FileInputStream(file),chunkSize)` instead.

`public NSData( java.io.InputStream inputStream, int chunkSize) throws java.io.IOException`

Creates a data object with the data from the stream specified by _inputStream_. The _chunkSize_ parameter specifies the size, in bytes, of the block that the input stream returns when it reads. For maximum performance, you should set the chunk size to the approximate size of the data. This constructor reads the stream until it detects an end of file or encounters an exception, but it does not close the stream.

`public NSData(java.net.URL url) throws java.io.IOException`

Deprecated in the Java Foundation Framework. Don't use this constructor. Use the following code instead:
> ```
>     URLConnection connection = url.openConnection();
>     connection.connect();
>     NSData myData = new NSData(connection.getInputStream(),chunkSize);
> ```

---

## Static Methods

---

### dataWithContentsOfFile

`public static NSData dataWithContentsOfFile(java.io.File file) throws java.io.IOException`

Deprecated in the Java Foundation Framework. Don't use this method. Use the following code instead:
> ```
>     myData = new NSData(new FileInputStream(file), chunkSize);
> ```

`public static NSData dataWithContentsOfFile(String path) throws java.io.IOException`

Deprecated in the Java Foundation Framework. Don't use this method. Use the following code instead:
> ```
>     myData = new NSData(new FileInputStream(path), chunkSize);
> ```

---

### dataWithContentsOfMappedFile

`public static NSData dataWithContentsOfMappedFile(java.io.File file) throws java.io.IOException`

Deprecated in the Java Foundation Framework. Don't use this method. Use the following code instead:
> ```
>     myData = new NSData(new FileInputStream(file), chunkSize);
> ```

---

### decodeObject

`public static Object decodeObject(NSCoder coder)`

Creates an NSData from the data in _coder_.

__See Also:__ [NSCoding](NSCoding.md#apple-ineucskcizbeq)

---

## Instance Methods

---

### bytes

`public byte[] bytes( int offset, int count)`

Returns a byte array containing the receiver's contents that fall within the range specified by _offset_ and _count_.

`public byte[] bytes(NSRange range)`

Returns a byte array containing the receiver's contents that fall within the range specified by _range_.

`public byte[] bytes()`

Returns a byte array containing all of the receiver's contents.

---

### bytesNoCopy

`protected byte[] bytesNoCopy()`

Returns the internal byte array that contains the receiver's data. Due to the internal implementation of NSData, this array may contain bytes that are not actually a part of the receiver's data. The receiver's actual data is composed of the returned array's bytes that lie in the range returned by [rangeNoCopy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpojqw4z3fjzxug33qpe). Used by mutable subclasses of NSData.

`public byte[] bytesNoCopy(NSMutableRange dataRange)`

Returns the internal byte array that contains the receiver's data and sets _dataRange_'s offset and length to those of the receiver's internal NSRange object. The receiver's actual data is composed of the returned array's bytes that lie within _dataRange_. __WARNING__ NSData assumes the internal byte array is immutable. You should not change the contents of this array.

---

### classForCoder

`public Class classForCoder()`

Conformance to [NSCoding](NSCoding.md#apple-ineucskcizbeq). See the method description of [classForCoder](NSCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwg3dbonzum33sinxwizls) in the interface specification for NSCoding.

---

### clone

`public Object clone()`

Simply returns the receiver. Since NSData objects are immutable, there's no need to make an actual clone.

---

### encodeWithCoder

`public void encodeWithCoder(NSCoder coder)`

Conformance to [NSCoding](NSCoding.md#apple-ineucskcizbeq). See the method description of [encodeWithCoder](NSCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwk3tdn5sgkv3jorueg33emvza) in the interface specification for NSCoding.

---

### equals

`public boolean equals(Object anObject)`

Compares the receiving data object to _anObject_. If _anObject_ is an NSData and the contents of _anObject_ are equal to the contents of the receiver, this method returns `true`. If not, it returns `false`. Two data objects are equal if they hold the same number of bytes, and if the bytes at the same position in the objects are the same.

---

### hashCode

`public int hashCode()`

Provide an appropriate hash code useful for storing the receiver in a hash-based data structure.

---

### immutableBytes

`protected byte[] immutableBytes()`

Returns an immutable byte array that contains the receiver's data.

---

### immutableRange

`protected NSRange immutableRange()`

Returns an immutable NSRange object that specifies the receiver's length.

---

### isEqualToData

`public boolean isEqualToData(NSData otherData)`

Compares the receiving data object to _otherData_. If the contents of _otherData_ are equal to the contents of the receiver, this method returns `true`. If not, it returns `false`. Two data objects are equal if they hold the same number of bytes, and if the bytes at the same position in the objects are the same.

---

### length

`public int length()`

Returns the number of bytes contained by the receiver.

---

### rangeNoCopy

`protected NSRange rangeNoCopy()`

Returns the internal NSRange object that specifies the offset and length of the receiver's data relative to the internal byte array (as returned by [bytesNoCopy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpmj4xizltjzxug33qpe)). Used by mutable subclasses of NSData.

---

### stream

`public java.io.ByteArrayInputStream stream()`

Creates and returns a java.io.ByteArrayInputStream containing the receiver's data.

---

### subdataWithRange

`public NSData subdataWithRange(NSRange range)`

Returns a data object containing a copy of the receiver's bytes that are fall within the range specified by _range_. If _range_ isn't within the receiver's range of bytes, a RangeException is thrown.

---

### toString

`public String toString()`

Returns a string representation of the receiver that contains its length, its location, and some of its data.

---

### writeToFile

`public boolean writeToFile(String path)`

Deprecated in the Java Foundation Framework. Don't use this method. Use the following code instead:
> ```
> try {
>         FileOutputStream fileOutputStream = new FileOutputStream(path);
>         myData.writeToStream(fileOutputStream);
>         fileOutputStream.close();
>     } catch (IOException exception) {
>         /* Do something with the exception */
>     }
> ```

---

### writeToStream

`public void writeToStream(java.io.OutputStream outputStream) throws java.io.IOException`

Writes the bytes in the receiver contents to the _outputStream_. If the write fails for any reason, throws a java.io.IOException.

__See Also:__ [writeToStream](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpo5zgs5dfkrxvg5dsmvqw2)

---

### writeToURL

`public boolean writeToURL( java.net.URL url, boolean atomically)`

Deprecated in the Java Foundation Framework. Don't use this method. Use the following code instead:
> ```
> try {
>         FileOutputStream fileOutputStream = new FileOutputStream(url.getFile());
>         myData.writeToStream(fileOutputStream);
>         fileOutputStream.close();
>     } catch (IOException exception) {
>         /* Do something with the exception */
>     }
> ```

__See Also:__ [writeToStream](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpo5zgs5dfkrxvg5dsmvqw2)

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
