---
title: NSData
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdata
source_url: 'https://developer.apple.com/documentation/foundation/nsdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata.json'
content_hash: 'sha256:21a5707625c02666'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSData

<sub>Class</sub>

A static byte buffer in memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSData
```

## Overview

In Swift, the buffer bridges to [Data](data.md); use [NSData](nsdata.md) when you need reference semantics or other Foundation-specific behavior.

[NSData](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) and its mutable subclass [NSMutableData](nsmutabledata.md) provide data objects, or object-oriented wrappers for byte buffers. Data objects let simple allocated buffers (that is, data with no embedded pointers) take on the behavior of Foundation objects.

The size of the data is subject to a theoretical limit of about 8 exabytes (1 EB = 10¹⁸ bytes; in practice, the limit should not be a factor).

[NSData](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) is _toll-free bridged_ with its Core Foundation counterpart, [CFData](../corefoundation/cfdata.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

> [!important] Important
> The Swift overlay to the Foundation framework provides the [Data](data.md) structure, which bridges to the [NSData](nsdata.md) class and its mutable subclass [NSMutableData](nsmutabledata.md). For more information about value types, see [Working with Foundation Types](../swift/working-with-foundation-types.md).

### Writing Data Atomically

[NSData](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) provides methods for atomically saving their contents to a file, which guarantee that the data is either saved in its entirety, or it fails completely. An atomic write first writes the data to a temporary file and then, only if this write succeeds, moves the temporary file to its final location.

Although atomic write operations minimize the risk of data loss due to corrupt or partially written files, they may not be appropriate when writing to a temporary directory, the user’s home directory or other publicly accessible directories. When you work with a publicly accessible file, treat that file as an untrusted and potentially dangerous resource. An attacker may compromise or corrupt these files. The attacker can also replace the files with hard or symbolic links, causing your write operations to overwrite or corrupt other system resources.

Avoid using the [- writeToURL:atomically:](<nsdata/write(to_atomically_).md>) method (and the related methods) when working inside a publicly accessible directory. Instead, use [FileHandle](filehandle.md) with an existing file descriptor to securely write the file.

For more information, see [Securing File Operations](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/RaceConditions.html#//apple_ref/doc/uid/TP40002585-SW9) in [Secure Coding Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSMutableData](nsmutabledata.md)

- **Conforms To**: [BidirectionalCollection](../swift/bidirectionalcollection.md), [CKRecordValue](../cloudkit/ckrecordvalue-c.protocol.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVarArg](../swift/cvararg.md), [Collection](../swift/collection.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [DataProtocol](dataprotocol.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [RandomAccessCollection](../swift/randomaccesscollection.md), [Sequence](../swift/sequence.md)

## Topics

### Creating Data

- [- initWithBytes:length:](<nsdata/init(bytes_length_).md>) — Initializes a data object filled with a given number of bytes copied from a given buffer.
- [- initWithBytesNoCopy:length:](<nsdata/init(bytesnocopy_length_).md>) — Initializes a data object filled with a given number of bytes of data from a given buffer.
- [- initWithBytesNoCopy:length:deallocator:](<nsdata/init(bytesnocopy_length_deallocator_).md>) — Initializes a data object filled with a given number of bytes of data from a given buffer, with a custom deallocator block.
- [- initWithBytesNoCopy:length:freeWhenDone:](<nsdata/init(bytesnocopy_length_freewhendone_).md>) — Initializes a newly allocated data object by adding the given number of bytes from the given buffer.
- [- initWithData:](<nsdata/init(data_).md>) — Initializes a data object with the contents of another data object.

### Reading Data from a File

- [- initWithContentsOfFile:](<nsdata/init(contentsoffile_).md>) — Initializes a data object with the content of the file at a given path.
- [- initWithContentsOfFile:options:error:](<nsdata/init(contentsoffile_options_).md>) — Initializes a data object with the content of the file at a given path.
- [ReadingOptions](nsdata/readingoptions.md) — Options for methods used to read data objects.
- [- initWithContentsOfMappedFile:](<nsdata/init(contentsofmappedfile_).md>) — Initializes a data object with the contents of the mapped file specified by a given path. _(deprecated)_
- [+ dataWithContentsOfMappedFile:](<nsdata/datawithcontentsofmappedfile(__).md>) — Creates a data object from the mapped file at a given path. _(deprecated)_

### Writing Data to a File

- [- writeToFile:atomically:](<nsdata/write(tofile_atomically_).md>) — Writes the data object’s bytes to the file specified by a given path.
- [- writeToFile:options:error:](<nsdata/write(tofile_options_).md>) — Writes the data object’s bytes to the file specified by a given path.
- [- writeToURL:atomically:](<nsdata/write(to_atomically_).md>) — Writes the data object’s bytes to the location specified by a given URL.
- [- writeToURL:options:error:](<nsdata/write(to_options_).md>) — Writes the data object’s bytes to the location specified by a given URL.
- [WritingOptions](nsdata/writingoptions.md) — Options for methods used to write data objects.

### Encoding and Decoding Base64 Representations

- [init(base64EncodedData:options:)](<nsdata/init(base64encodeddata_options_).md>) — Initializes a data object with the given Base64 encoded data.
- [- initWithBase64Encoding:](<nsdata/init(base64encoding_).md>) — Initializes a data object initialized with the given Base64 encoded string. _(deprecated)_
- [init(base64EncodedString:options:)](<nsdata/init(base64encodedstring_options_).md>) — Initializes a data object with the given Base64 encoded string.
- [- base64EncodedDataWithOptions:](<nsdata/base64encodeddata(options_).md>) — Creates a Base64, UTF-8 encoded data object from the string using the given options.
- [- base64EncodedStringWithOptions:](<nsdata/base64encodedstring(options_).md>) — Creates a Base64 encoded string from the string using the given options.
- [- base64Encoding](<nsdata/base64encoding().md>) — Initializes a Base64 encoded string from the string. _(deprecated)_
- [Base64EncodingOptions](nsdata/base64encodingoptions.md) — Options for methods used to Base64 encode data.
- [Base64DecodingOptions](nsdata/base64decodingoptions.md) — Options to modify the decoding algorithm used to decode Base64 encoded data.

### Accessing Underlying Bytes

- [bytes](nsdata/bytes.md) — A pointer to the data object’s contents.
- [- enumerateByteRangesUsingBlock:](<nsdata/enumeratebytes(__).md>) — Enumerates each range of bytes in the data object using a block.
- [- getBytes:](<nsdata/getbytes(__).md>) — Copies a data object’s contents into a given buffer. _(deprecated)_
- [- getBytes:length:](<nsdata/getbytes(__length_).md>) — Copies a number of bytes from the start of the data object into a given buffer.
- [- getBytes:range:](<nsdata/getbytes(__range_).md>) — Copies a range of bytes from the data object into a given buffer.

### Finding Data

- [- subdataWithRange:](<nsdata/subdata(with_).md>) — Returns a new data object containing the data object’s bytes that fall within the limits specified by a given range.
- [- rangeOfData:options:range:](<nsdata/range(of_options_in_).md>) — Finds and returns the range of the first occurrence of the given data, within the given range, subject to given options.
- [SearchOptions](nsdata/searchoptions.md) — Options for method used to search data objects.

### Testing Data

- [- isEqualToData:](<nsdata/isequal(to_).md>) — Returns a Boolean value indicating whether this data object is the same as another.
- [length](nsdata/length.md) — The number of bytes contained by the data object.

### Describing Data

- [description](nsdata/description.md) — A string that contains a hexadecimal representation of the data object’s contents in a property list format.

### Compressing and Decompressing Data

- [- compressedDataUsingAlgorithm:error:](<nsdata/compressed(using_).md>) — Returns a new data object by compressing the data object’s bytes.
- [- decompressedDataUsingAlgorithm:error:](<nsdata/decompressed(using_).md>) — Returns a new data object by decompressing data object’s bytes.
- [CompressionAlgorithm](nsdata/compressionalgorithm.md) — An algorithm that indicates how to compress or decompress data.
- [NSCompressionErrorMaximum](nscompressionerrormaximum-swift.var.md) — The end of the range of error codes reserved for compression errors.
- [NSCompressionErrorMinimum](nscompressionerrorminimum-swift.var.md) — The start of the range of error codes reserved for compression errors.
- [NSCompressionFailedError](nscompressionfailederror-swift.var.md) — An error code value that indicates a failure to compress data using the provided algorithm.
- [NSDecompressionFailedError](nsdecompressionfailederror-swift.var.md) — An error code value that indicates a failure to decompress data using the provided algorithm.

### Initializers

- [- initWithBase64EncodedString:options:](<nsdata/init(base64encoded_options_)-3ksry.md>) — Initializes a data object with the given Base64 encoded string.
- [- initWithBase64EncodedData:options:](<nsdata/init(base64encoded_options_)-4t5yq.md>) — Initializes a data object with the given Base64 encoded data.
- [init(coder:)](<nsdata/init(coder_).md>)
- [- initWithContentsOfURL:](<nsdata/init(contentsof_).md>) — Creates a data object from the data at the specified file URL, or returns `nil` if the system can’t create one.
- [- initWithContentsOfURL:options:error:](<nsdata/init(contentsof_options_).md>) — Creates a data object from the data at the provided file URL using specific reading options.

### Default Implementations

- [NSData Implementations](nsdata/nsdata-implementations.md)
