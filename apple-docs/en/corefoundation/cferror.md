---
title: CFError
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cferror
source_url: 'https://developer.apple.com/documentation/corefoundation/cferror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cferror.json'
content_hash: 'sha256:14645b842e1f54f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFError

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFError
```

## Overview

A CFError object encapsulates more rich and extensible error information than is possible using only an error code or error string. The core attributes of a CFError object are an error domain (represented by a string), a domain-specific error code, and a “user info” dictionary containing application-specific information. Errors are required to have a domain and an error code within that domain. Several well-known domains are defined corresponding to Mach, POSIX, and OSStatus errors.

The optional “user info” dictionary may provide additional information that might be useful for the interpretation and reporting of the error, including a human-readable description for the error. The “user info” dictionary sometimes includes another CFError object that represents an error in a subsystem underlying the error represented by the containing CFError object. This underlying error object may provide more specific information about the cause of the error.

In general, a method should signal an error condition by returning, for example, `false` or `NULL` rather than by the simple presence of an error object. The method can then optionally return an CFError object by reference, in order to further describe the error.

CFError is toll-free bridged to [NSError](../foundation/nserror.md) in the Foundation framework—for more details on toll-free bridging, see [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677). `NSError` has some additional guidelines that make it easy to report errors automatically to users and attempt to recover from them. See [Error Handling Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ErrorHandlingCocoa/ErrorHandling/ErrorHandling.html#//apple_ref/doc/uid/TP40001806) for more information on `NSError` programming guidelines.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a CFError

- [CFErrorCreate](<cferrorcreate(________).md>) — Creates a new CFError object.
- [CFErrorCreateWithUserInfoKeysAndValues](<cferrorcreatewithuserinfokeysandvalues(____________).md>) — Creates a new CFError object using given keys and values to create the user info dictionary.

### Getting Information About an Error

- [CFErrorGetDomain](<cferrorgetdomain(__).md>) — Returns the error domain for a given CFError.
- [CFErrorGetCode](<cferrorgetcode(__).md>) — Returns the error code for a given CFError.
- [CFErrorCopyUserInfo](<cferrorcopyuserinfo(__).md>) — Returns the user info dictionary for a given CFError.
- [CFErrorCopyDescription](<cferrorcopydescription(__).md>) — Returns a human-presentable description for a given error.
- [CFErrorCopyFailureReason](<cferrorcopyfailurereason(__).md>) — Returns a human-presentable failure reason for a given error.
- [CFErrorCopyRecoverySuggestion](<cferrorcopyrecoverysuggestion(__).md>) — Returns a human presentable recovery suggestion for a given error.

### Getting the CFError Type ID

- [CFErrorGetTypeID](<cferrorgettypeid().md>) — Returns the type identifier for the CFError opaque type.

### Constants

- [Error domains](error-domains.md) — These constants define domains for CFError objects.
- [Keys for the user info dictionary](keys-for-the-user-info-dictionary.md) — Keys in the `userInfo` dictionary.

## See Also

### Related Documentation

- [Error Handling Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ErrorHandlingCocoa/ErrorHandling/ErrorHandling.html#//apple_ref/doc/uid/TP40001806)

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFFileDescriptor](cffiledescriptor.md)
