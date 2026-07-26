---
title: 'CFStringCreateWithCStringNoCopy(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringcreatewithcstringnocopy(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringcreatewithcstringnocopy(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringcreatewithcstringnocopy%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:4ed077cf22d93ce8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringCreateWithCStringNoCopy(_:_:_:_:)

<sub>Function</sub>

Creates a CFString object from an external C string buffer that might serve as the backing store for the object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringCreateWithCStringNoCopy(_ alloc: CFAllocator!, _ cStr: UnsafePointer<CChar>!, _ encoding: CFStringEncoding, _ contentsDeallocator: CFAllocator!) -> CFString!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new string. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `cStr` — The `NULL`-terminated C string to be used to create the CFString object.  The string must use an 8-bit encoding.

- `encoding` — The encoding of the characters in the C string. The encoding must specify an 8-bit encoding.

- `contentsDeallocator` — The CFAllocator object to use to deallocate the external string buffer when it is no longer needed. You can pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to request the default allocator for this purpose. If the buffer does not need to be deallocated, or if you want to assume responsibility for deallocating the buffer (and not have the CFString object deallocate it), pass [kCFAllocatorNull](kcfallocatornull.md).

## Return Value

An immutable string containing `cStr` (after stripping off the `NULL` terminating character), or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

A C string is a string of 8-bit characters terminated with an 8-bit `NULL`. Unichar and Unichar32 are not considered C strings.

Unless the situation warrants otherwise, the created object does not copy the external buffer to internal storage but instead uses the buffer as its backing store. However, you should never assume that the object is using the external buffer since the object might copy the buffer to internal storage or even dump the buffer altogether and store the characters in another way.

The function includes a `contentsDeallocator` parameter with which to specify an allocator to use for deallocating the external buffer when the CFString object is deallocated. If you want to assume responsibility for deallocating this memory, specify [kCFAllocatorNull](kcfallocatornull.md) for this parameter.

If at creation time the CFString object decides it can’t use the buffer, and the function specifies a `contentsDeallocator` allocator, it will use this allocator to free the buffer at that time.

### Special Considerations

If an error occurs during the creation of the string, then `cStr` is not deallocated. In this case, the caller is responsible for freeing the buffer. This allows the caller to continue trying to create a string with the buffer, without having the buffer deallocated.

## See Also

### Creating a CFString

- [CFStringCreateArrayBySeparatingStrings](<cfstringcreatearraybyseparatingstrings(______).md>) — Creates an array of CFString objects from a single CFString object.
- [CFStringCreateByCombiningStrings](<cfstringcreatebycombiningstrings(______).md>) — Creates a single string from the individual CFString objects that comprise the elements of an array.
- [CFStringCreateCopy](<cfstringcreatecopy(____).md>) — Creates an immutable copy of a string.
- [CFStringCreateFromExternalRepresentation](<cfstringcreatefromexternalrepresentation(______).md>) — Creates a string from its “external representation.”
- [CFStringCreateWithBytes](<cfstringcreatewithbytes(__________).md>) — Creates a string from a buffer containing characters in a specified encoding.
- [CFStringCreateWithBytesNoCopy](<cfstringcreatewithbytesnocopy(____________).md>) — Creates a string from a buffer, containing characters in a specified encoding, that might serve as the backing store for the new string.
- [CFStringCreateWithCharacters](<cfstringcreatewithcharacters(______).md>) — Creates a string from a buffer of Unicode characters.
- [CFStringCreateWithCharactersNoCopy](<cfstringcreatewithcharactersnocopy(________).md>) — Creates a string from a buffer of Unicode characters that might serve as the backing store for the object.
- [CFStringCreateWithCString](<cfstringcreatewithcstring(______).md>) — Creates an immutable string from a C string.
- [CFStringCreateWithFormatAndArguments](<cfstringcreatewithformatandarguments(________).md>) — Creates an immutable string from a formatted string and a variable number of arguments (specified in a parameter of type `va_list`).
- [CFStringCreateWithPascalString](<cfstringcreatewithpascalstring(______).md>) — Creates an immutable CFString object from a Pascal string.
- [CFStringCreateWithPascalStringNoCopy](<cfstringcreatewithpascalstringnocopy(________).md>) — Creates a CFString object from an external Pascal string buffer that might serve as the backing store for the object.
- [CFStringCreateWithSubstring](<cfstringcreatewithsubstring(______).md>) — Creates an immutable string from a segment (substring) of an existing string.
