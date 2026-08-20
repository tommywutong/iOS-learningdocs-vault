---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSMutableData.html
archived_at: '2026-07-15T08:13:56.238563Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

# NSMutableData

> **__Inherits from:__**
> : [NSData](NSData.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpjzjuiylume): Object

> **__Implements:__**
> : Cloneable: java.io.Serializable: NSCoding

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

The NSMutableData class declares the programmatic interface to an object that contains modifiable data in the form of bytes. The data grows automatically if necessary.

[Table 0-8](#apple-ijbuqskkincec) describes the NSMutableData methods that provide the basis for all NSMutableData's other methods; that is, all other methods are implemented in terms of these nine. If you create a subclass of NSMutableData, you need only ensure that these base methods work properly. Having done so, you can be sure that all your subclass's inherited methods operate properly.

__Table 0-8 NSMutableData's Base API__

| __Method__ | __Description__ |
| [appendByte](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexwc4dqmvxgiqtzorsq) | Appends a byte to the receiver. |
| [appendBytes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexwc4dqmvxgiqtzorsxg) | Appends the contents of a byte array to the receiver. The two-argument version is part of the base API. |
| [bytesNoCopy](NSData.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpmj4xizltjzxug33qpe) | Returns the internal byte array that contains the receiver's data. Inherited from [NSData](NSData.md#apple-incuqrsjizdui). |
| [immutableBytes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexws3lnov2gcytmmvbhs5dfom) | Returns an immutable byte array that contains a copy of the receiver's data. |
| [immutableRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexws3lnov2gcytmmvjgc3thmu) | Returns an immutable copy of the NSRange object that specifies the receiver's length. |
| [rangeNoCopy](NSData.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstirqxiyjpojqw4z3fjzxug33qpe) | Returns the internal NSRange object that specifies the receiver's length. Inherited from [NSData](NSData.md#apple-incuqrsjizdui). |
| [resetBytesInRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexxezltmv2ee6lumvzus3ssmfxgozi) | Resets to zero the receiver's bytes that fall within the specified range. |
| [setData](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexxgzluirqxiyi) | Replaces the receiver's contents with the specified NSData object. |
| [setLength](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexxgzlujrsw4z3una) | Extends or truncates a mutable data object to the specified length. |

To modify the data, use the [setData](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexxgzluirqxiyi), [appendByte](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexwc4dqmvxgiqtzorsq), [appendBytes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexwc4dqmvxgiqtzorsxg), and [appendData](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexwc4dqmvxgirdborqq) methods. If you want to set a range of bytes to zero, use the [resetBytesInRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexxezltmv2ee6lumvzus3ssmfxgozi) method. To change the length of the data, use the [setLength](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexxgzlujrsw4z3una) and [increaseLengthBy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexws3tdojswc43fjrsw4z3unbbhs) methods.

## Interfaces Implemented

---

> : Cloneable
>
> : [clone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexwg3dpnzsq)
>
> :
>
> : java.io.Serializable:
>
> : NSCoding
>
> : classForCoder: decodeObject: encodeWithCoder
>
> :

## Method Types

---

> **Constructors**
>
> : [NSMutableData](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexu4u2nov2gcytmmvcgc5db)
>
> **Modifying the data**
>
> : [appendByte](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexwc4dqmvxgiqtzorsq): [appendBytes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexwc4dqmvxgiqtzorsxg): [appendData](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexwc4dqmvxgirdborqq): [resetBytesInRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexxezltmv2ee6lumvzus3ssmfxgozi): [setData](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexxgzluirqxiyi)
>
> **Modifying the range**
>
> : [increaseLengthBy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexws3tdojswc43fjrsw4z3unbbhs): [setLength](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexxgzlujrsw4z3una)
>
> **Accessing internal data directly**
>
> : [immutableBytes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexws3lnov2gcytmmvbhs5dfom): [immutableRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexws3lnov2gcytmmvjgc3thmu)

## Constructors

---

### NSMutableData

`public NSMutableData()`

Creates an empty NSMutableData object.

`public NSMutableData(NSData data)`

Creates an NSMutableData object containing the contents of another data object _data_.

`public NSMutableData(String string)`

This constructor is deprecated. Use `NSMutableData(string.getBytes())` instead.

`public NSMutableData(byte[] bytes)`

Creates a NSMutableData object with all the data in the byte array _bytes_.

`public NSMutableData( byte[] bytes, NSRange range)`

Creates an NSMutableData object with the bytes from the language array _bytes_ that fall in the range specified by _range_.

`public NSMutableData( byte[] bytes, NSRange range, boolean nocopy)`

Creates an NSMutableData object with the bytes from the language array _bytes_ that fall in the range specified by _range_. The _noCopy_ parameter specifies whether or not a copy of _bytes_ is made.

`public NSMutableData(int capacity)`

Creates an NSMutableData object prepared to store at least _capacity_ bytes. If you know the upper bound on the size of your data, you can use this constructor to improve performance. As long as the data size does not exceed _capacity_ bytes, the internal byte array will not be reallocated.

`public NSMutableData(java.io.File file) throws java.io.IOException`

This constructor is deprecated. Use `NSMutableData(new FileInputStream(file),myChunkSize)` instead.

`public NSMutableData( java.io.InputStream inputStream, int chunkSize) throws java.io.IOException`

Creates a data object with the data from the stream specified by _inputStream_. The _chunkSize_ parameter specifies the size, in bytes, of the block that the input stream returns when it reads. For maximum performance, you should set the chunk size to the approximate size of the data. This constructor does not close the stream.

`public NSMutableData(java.net.URL url) throws java.io.IOException`

This constructor is deprecated. Use the following code instead:
> ```
>     URLConnection connection = url.openConnection();
>     connection.connect();
>     NSMutableData myData = new NSMutableData(connection.getInputStream(),myChunkSize);
> ```

---

## Instance Methods

---

### appendByte

`public void appendByte(byte byte)`

Appends the specified byte to the receiver.

__See Also:__ [appendBytes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexwc4dqmvxgiqtzorsxg), [appendData](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexwc4dqmvxgirdborqq)

---

### appendBytes

`public void appendBytes(byte[] bytes[])`

`public void appendBytes( byte[] bytes, NSRange range)`

Appends the contents of byte array _bytes_ to the receiver. The two-argument method appends the bytes in _bytes_ that fall within the range specified by _range_.

__See Also:__ [appendByte](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexwc4dqmvxgiqtzorsq), [appendData](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexwc4dqmvxgirdborqq)

---

### appendData

`public void appendData(NSData otherData)`

Appends the contents of a data object _otherData_ to the receiver.

__See Also:__ [appendByte](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexwc4dqmvxgiqtzorsq), [appendBytes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexwc4dqmvxgiqtzorsxg)

---

### clone

`public Object clone()`

Returns a copy (an NSMutableData object) of the receiver.

---

### immutableBytes

`protected byte[] immutableBytes()`

Returns an immutable copy of the byte array that contains the receiver's data.

---

### immutableRange

`protected NSRange immutableRange()`

Returns an immutable copy of the NSRange object that contains the receiver's length.

---

### increaseLengthBy

`public void increaseLengthBy(int additionalLength)`

Increases the length of the receiver by _additionalLength_. The additional bytes are all set to zero.

__See Also:__ [setLength](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexxgzlujrsw4z3una)

---

### resetBytesInRange

`public void resetBytesInRange(NSRange range)`

Resets to zero the receiver's bytes that fall within the specified range. If the location of _range_ isn't within the receiver's range of bytes, an IllegalArgumentException is thrown. The receiver is resized to accommodate the new bytes, if necessary.

---

### setData

`public void setData(NSData data)`

Replaces the entire contents of the receiver with the contents of _data_.

__See Also:__ [setLength](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexxgzlujrsw4z3una)

---

### setLength

`public void setLength(int length)`

Extends or truncates a mutable data object to the specified length. If the mutable data object is extended, the additional bytes are filled with zero.

__See Also:__ [increaseLengthBy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexws3tdojswc43fjrsw4z3unbbhs), [setData](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuiylumexxgzluirqxiyi)

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
