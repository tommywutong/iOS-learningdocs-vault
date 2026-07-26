---
title: 'CFStringCreateArrayBySeparatingStrings(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringcreatearraybyseparatingstrings(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringcreatearraybyseparatingstrings(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringcreatearraybyseparatingstrings%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:533e6abd982d10ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringCreateArrayBySeparatingStrings(_:_:_:)

<sub>Function</sub>

Creates an array of CFString objects from a single CFString object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringCreateArrayBySeparatingStrings(_ alloc: CFAllocator!, _ theString: CFString!, _ separatorString: CFString!) -> CFArray!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new CFArray object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `theString` — The string to be divided into substrings. The substrings should be separated by `separatorString`.

- `separatorString` — The string used to separate the substrings in `theString`.

## Return Value

A new array that contains CFString objects that represent substrings of `theString`, or `NULL` if there was a problem creating the object. The order of elements in the array is identical to the order of the substrings in `theString`. If `separatorString` does not occur in `theString`, the result is an array containing `theString`. If `separatorString` is equal to `theString`, then the result is an array containing two empty strings. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function provides a convenient way to convert units of data captured in a single string to a form (an array) suitable for iterative processing. One or more delimiter characters (or “separator string”) separates the substrings in the source string—these characters are frequently whitespace characters such as tabs and newlines (carriage returns). For example, you might have a file containing a localized list of place names with each name separated by a tab character. You could create a CFString object from this file and call this function on the string to obtain a CFArray object whose elements are these place names.

`separatorString` is treated as a complete unit. If you specify `XYZ` as the separator string, then if `theString` is `aXbYZcXYZe`, then the returned array contains `aXbYZc` and `e`.

See also [CFStringCreateByCombiningStrings](<cfstringcreatebycombiningstrings(______).md>).

## See Also

### Creating a CFString

- [CFStringCreateByCombiningStrings](<cfstringcreatebycombiningstrings(______).md>) — Creates a single string from the individual CFString objects that comprise the elements of an array.
- [CFStringCreateCopy](<cfstringcreatecopy(____).md>) — Creates an immutable copy of a string.
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
