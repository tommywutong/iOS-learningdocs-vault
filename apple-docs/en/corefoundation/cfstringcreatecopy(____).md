---
title: 'CFStringCreateCopy(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringcreatecopy(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringcreatecopy(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringcreatecopy%28_%3A_%3A%29.json'
content_hash: 'sha256:a9ce777d0347702e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringCreateCopy(_:_:)

<sub>Function</sub>

Creates an immutable copy of a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringCreateCopy(_ alloc: CFAllocator!, _ theString: CFString!) -> CFString!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new string. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `theString` — The string to copy.

## Return Value

An immutable string whose contents are identical to `theString`. Returns `NULL` if there was a problem copying the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The resulting object has the same Unicode contents as the original object, but it is always immutable. It might also have different storage characteristics, and hence might reply differently to functions such as [CFStringGetCStringPtr](<cfstringgetcstringptr(____).md>). Also, if the specified allocator and the allocator of the original object are the same, and the string is already immutable, this function may simply increment the retention count without making a true copy. However, the resulting object is a true immutable copy, except the operation was a lot more efficient.

You should use this function in situations where a string is or could be mutable, and you need to take a snapshot of its current value. For example, you might decide to pass a copy of a string to a function that stores its current value in a list for later use.

## See Also

### Creating a CFString

- [CFStringCreateArrayBySeparatingStrings](<cfstringcreatearraybyseparatingstrings(______).md>) — Creates an array of CFString objects from a single CFString object.
- [CFStringCreateByCombiningStrings](<cfstringcreatebycombiningstrings(______).md>) — Creates a single string from the individual CFString objects that comprise the elements of an array.
- [CFStringCreateFromExternalRepresentation](<cfstringcreatefromexternalrepresentation(______).md>) — Creates a string from its “external representation.”
- [CFStringCreateWithBytes](<cfstringcreatewithbytes(__________).md>) — Creates a string from a buffer containing characters in a specified encoding.
- [CFStringCreateWithBytesNoCopy](<cfstringcreatewithbytesnocopy(____________).md>) — Creates a string from a buffer, containing characters in a specified encoding, that might serve as the backing store for the new string.
- [CFStringCreateWithCharacters](<cfstringcreatewithcharacters(______).md>) — Creates a string from a buffer of Unicode characters.
- [CFStringCreateWithCharactersNoCopy](<cfstringcreatewithcharactersnocopy(________).md>) — Creates a string from a buffer of Unicode characters that might serve as the backing store for the object.
- [CFStringCreateWithCString](<cfstringcreatewithcstring(______).md>) — Creates an immutable string from a C string.
- [CFStringCreateWithCStringNoCopy](<cfstringcreatewithcstringnocopy(________).md>) — Creates a CFString object from an external C string buffer that might serve as the backing store for the object.
- [CFStringCreateWithFormatAndArguments](<cfstringcreatewithformatandarguments(________).md>) — Creates an immutable string from a formatted string and a variable number of arguments (specified in a parameter of type `va_list`).
- [CFStringCreateWithPascalString](<cfstringcreatewithpascalstring(______).md>) — Creates an immutable CFString object from a Pascal string.
- [CFStringCreateWithPascalStringNoCopy](<cfstringcreatewithpascalstringnocopy(________).md>) — Creates a CFString object from an external Pascal string buffer that might serve as the backing store for the object.
- [CFStringCreateWithSubstring](<cfstringcreatewithsubstring(______).md>) — Creates an immutable string from a segment (substring) of an existing string.
