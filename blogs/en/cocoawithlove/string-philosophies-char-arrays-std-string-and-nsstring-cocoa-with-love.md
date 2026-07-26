---
title: 'String philosophies: char arrays, std::string and NSString | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/08/string-philosophies-char-arrays.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:2eced68a242bfc73'
translated: false
---

> 原文：[String philosophies: char arrays, std::string and NSString | Cocoa with Love](https://www.cocoawithlove.com/2008/08/string-philosophies-char-arrays.html)　·　Cocoa with Love (Matt Gallagher)

Each of the major C variants on the Mac implement character strings in their own way. It is fairly easy to learn the syntax differences between them but a simple API Reference doesn't explain the reasons for implementations: the different philosophies behind the implementations. In this post, I'll go past the 'How' of string differences and instead explain the 'Why' of differences between the three string implementations.

## The differences

In C, char * is just a pointer and requires that you access each character in turn to make any sense of the string. The C Standard Library provides a few functions but very little beyond basic array manipulation.

In C++, std::string is more type-safe, offers bounds checking, plays nicely with input and output streams and provides traversal and extraction functions but otherwise expects that you'll access each character individually, in much the same way as you would for char *.

NSString lives apart from its C-derived bretheren. You may never need to access its characters individually — in fact, direct access to the enclosed storage is forbidden. It is loaded with various processing functions. It also understands its own encoding and can convert itself to others.

## Underlying binary representations

### Standard C's char arrays

A Standard C string (normally typed as a char *, or char[]) is a series of 8-bit bytes of binary data, starting at an arbitrary memory address and proceeding until a zero byte ('\\0') is encountered. You can set a char * to any address in memory and begin treating memory from that point as a string.

If the string is an ASCII string, the highest bit in every byte will be zero, for other representations, there's no guarantee. String length is always a byte-length calculation (that doesn't include the '\\0' valued terminating byte), so for any variable length character representations (UTF-8), the length and the number of characters are not guaranteed to be the same thing.

### C++'s std::string

The philosophy of C++ is to provide a "limited overhead" addition of object-orientation to Standard C. Following this philosophy, the content of std::string in C++ is binary identical to a char[]. There's normally a capacity, length and possibly vtable value in there but otherwise it's pretty much a Standard C string.

C++ also provides std::wstring which is 16-bits per character (instead of std::string's 8-bits) but is otherwise fairly similar. But despite handling wide characters, std::wstring is still unaware of its encoding, making any encoding conversion, including conversion to std::string entirely the programmer's responsibility.

### Objective-C's NSString

Objective-C's NSString (technically, Foundation's but the distinction is blurred in Cocoa) is nothing like the other two. Following the philosophy of a class-cluster, NSString offers no guarantees about how it is represented internally since it may transparently substitute a content-optimised subclass for NSString on construction, choosing to represent its internals in whatever way is most appropriate for the data. Internally, an NSString could be 8-bit, 16-bit or 32-bit values; it could be stored contiguously or in a heap structure for mutability; although most of the time, it's a contiguous block of 16-bit values.

Accessors to NSString's characters return unichar (16-bit values values), so generally you treat NSString as though it is a contiguous block of unichar values, even though it may not technically be true. Since a few UTF-16 characters actually span multiple unichar the number of fully decoded character sequences is not guaranteed to be the same as the string's length but in non-Latin scripts, the length will generally be closer than either char * or std::string would be.

NSString is encoding aware, meaning that it knows how to convert itself correctly to other encodings. This can be a little annoying for programmers not used to specifying their encodings but makes NSString easily adaptable for display and processing of any language.

## Aggregate versus iterative processing

Both C and C++, promote the philosophies of sequential access. If you need to transform or process the a string, you're expected to access each character yourself and perform the work needed.

For example, converting a string to uppercase takes one of the following forms:

```objc
int i, length = strlen(myString);
for (i = 0; i < length; i++)
{
    myString[i] = toupper(myString[i]);
}
```

or

```objc
std::transform(
    myString.begin(),
    myString.end(),
    myString.begin(),
    (int(*)(int))std::toupper);
```

Since NSString limits access to its internals, it must provide most function done character by character in C or C++ at the string level. This means that NSString must provide vastly more functions to cover your likely needs but it also makes common tasks really easy:

```objc
myString = [myString uppercase];
```

It also has the advantage that these operations can be multi-character sequence aware, unlike the character operators in C and C++ which only act on single characters.

Objective-C's philosophy of aggregate processing goes further than this. NSString methods such as pathComponents and componentsSeparatedByString: provide the means to extract multiple objects in one pass — something that C and C++ never do in their standard libraries. Methods like rangeOfCharacterFromSet: allow aggregate testing — testing multiple characters against the string in a single instruction.

A final aspect of NSString's design philosophy is that it is intended to be used as a class in a modern operating system. This is shown through the method stringByResolvingSymlinksInPath. This task, while common on Unix derived operating systems, would be pointless in many of the environments in which pure C runs. It also shows NSString's willingness to adapt itself towards one of its common uses, something which the C++ Standard Libraries avoid.

## Conclusions

C is often described as the programming language which most closely models a general abstract CPU. It is tiny and light, providing the programmer with little more than basic arithmetic, memory access and input/ouput primitives to do their work. C's small size has allowed it to be ported to practically every CPU and environment in existence. Its closeness to an abstracted CPU also means that, if used correctly, it is as fast and optimal as a compiled language can be.

C++ adds a whole host of object paradigms and an extended standard library to the underlying syntax of C. Where possible, C++ tries to be a "zero cost" addition to C. In reality, this amounts to "limited overhead" but with understanding, C++ still allows precise C-level control. The C++ libraries focus on templating, with the premise that the choice of template variable should determine the scope, not the available methods.

From a compiler perspective, Objective-C is more C-like than C++. Philosophically speaking though, it's truly the odd one out. It provides proper unicode string handling. It provides large amounts of processing options, outputs arrays and provides specialized methods for the most common tasks. It doesn't reveal details about how it is stored internally but uses this to provide significant optimizations solutions where possible.
