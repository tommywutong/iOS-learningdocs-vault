---
title: String Programming Guide for Core Foundation
apple_id: 10000131i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/Articles/AccessingContents.html
archived_at: '2026-07-15T07:22:51.091917Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [String Programming Guide for Core Foundation](Introduction%20to%20Strings%20Programming%20Guide%20for%20Core%20Foundation.md)


[Next](Comparing%2C%20Sorting%2C%20and%20Searching%20String%20Objects.md)[Previous](Creating%20and%20Copying%20Strings.md)

# Accessing the Contents of String Objects

The two essential properties of CFString objects are an array of Unicode characters and a count of those characters. Several CFString functions not only obtain those properties, particularly the characters, but perform conversions to almost any desired format.

The `CFStringGetBytes` function, which copies the contents of a CFString object into a client-supplied byte buffer, is described in [The Basic Conversion Routines](Converting%20Between%20String%20Encodings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4doljrgaytcmrr). It is described there instead of in this section because it has features that make it particularly suitable for encoding conversions.

You may need to use programming interfaces that require C strings for some of their parameters. For performance reasons, a common strategy for accessing the contents of CFStrings as a C string is to first try to get a pointer of the appropriate type to these strings and, if that fails, to copy the contents into a local buffer. [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4diljrgaytamjqfvbuqrceincueqq) illustrates this strategy for C strings using the `CFStringGetCStringPtr` and `CFStringGetCString` functions.

__Listing 1__  Accessing CFString contents as a C string

```
CFStringRef str;
CFRange rangeToProcess;
const char *bytes;

str = CFStringCreateWithCString(NULL, "Hello World!", kCFStringEncodingMacRoman);

bytes = CFStringGetCStringPtr(str, kCFStringEncodingMacRoman);

if (bytes == NULL) {
    char localBuffer[10];
    Boolean success;
    success = CFStringGetCString(str, localBuffer, 10, kCFStringEncodingMacRoman);
}
```

These functions allow you to specify the encoding that the Unicode characters should be converted to. The functions that end with “Ptr” either return the desired pointer quickly, in constant time, or they return `NULL`. If the latter is the case, you should use `CFStringGetCString`.

The buffer for the `CFStringGetCString` functions can either be on the stack or a piece of allocated memory. These functions might still fail to get the characters, but that only happens in two circumstances: the conversion from the `UniChar` contents of CFString to the specified encoding fails or the buffer is too small. If you need a copy of the character buffer or if the code in question is not that performance-sensitive, you could simply call the `CFStringGetCString` function without even attempting to get the pointer first.

String objects offer a pair of functions similar to those for C strings for accessing the contents of a CFString as a 16-bit Unicode buffer: `CFStringGetCharactersPtr` and `CFStringGetCharacters`. The typical usage of these functions is also identical: you first optionally try to get a pointer to the characters and, if that fails, you try to copy the characters to a buffer you provide. These functions are different, however, in that they require a parameter specifying the length of the string.

[Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4diljrgaytcnzufvbuqrcejjcesqy) illustrates the common strategy for using these functions.

__Listing 2__  Accessing CFString contents as Unicode characters

```
CFStringRef str;
const UniChar *chars;

str = CFStringCreateWithCString(NULL, "Hello World", kCFStringEncodingMacRoman);
chars = CFStringGetCharactersPtr(str);
if (chars == NULL) {
    CFIndex length = CFStringGetLength(str);
    UniChar *buffer = malloc(length * sizeof(UniChar));
    CFStringGetCharacters(str, CFRangeMake(0, length), buffer);
    // Process the characters...
    free(buffer);
}
```

This example shows an allocated buffer (`malloc`) rather than a stack buffer. You can use one or the other. Because you need to know the size of the buffer for the `CFStringGetCharacters` function, allocating memory is easier to do but is less efficient. If you allocate memory for the characters you must, of course, free the buffer when you no longer need it.

Sometimes you might want to receive the contents of a CFString not as an entire block of characters but one Unicode character at a time. Perhaps you might be looking for a particular character or sequence of characters, such as special control characters indicating the start and end of a “record.” String objects give you three ways to process Unicode characters.

The first way is to use the `CFStringGetCharacters` function described in [Getting the Contents as Unicode Strings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4diljrgaytcnbu) to copy the characters to a local buffer and then cycle through the characters in the buffer. But this technique can be expensive memory-wise, especially if a large number of characters is involved.

The second way to access characters one at a time is to use the `CFStringGetCharacterAtIndex` function, as [Listing 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4diljrgaytgmbqfvbuqrcci5busrq) illustrates.

__Listing 3__  Getting a character at a time

```
CFIndex length, i;
UniChar uchar;
CFStringRef str;

str = CFStringCreateWithCString(NULL, "Hello World", kCFStringEncodingMacRoman);
length = CFStringGetLength(str);
for (i=0; i < length; i++) {
    uchar = CFStringGetCharacterAtIndex(str, i);
    // Process character....
}
```

Although this function does not require a large chunk of memory to hold a block of characters, using it in a loop can be inefficient. For such cases, use the `CFStringGetCharacters` function instead.

The third technique for character processing, exemplified in [Listing 4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4diljrgaytgojxfvbuqrccifceoqy), combines the convenience of one-at-a-time character access with the efficiency of bulk access. The in-line functions `CFStringInitInlineBuffer` and `CFStringGetCharacterFromInlineBuffer` give fast access to the contents of a string when you are doing sequential character processing. To use this programming interface, call the `CFStringInitInlineBuffer` function with a `CFStringInlineBuffer` structure (on the stack, typically) and a range of the CFString’s characters. Then call `CFStringGetCharacterFromInlineBuffer` as many times as you want using an index into that range relative to the start of the range. Because these are in-line functions they access the CFString object only periodically to fill the in-line buffer.

__Listing 4__  Processing characters in an in-line buffer

```
CFStringRef str;
CFStringInlineBuffer inlineBuffer;CFIndex length;CFIndex cnt;

str = CFStringCreateWithCString(NULL, "Hello World", kCFStringEncodingMacRoman);
length = CFStringGetLength(str)
CFStringInitInlineBuffer(str, &inlineBuffer, CFRangeMake(0, length));

for (cnt = 0; cnt < length; cnt++) {
     UniChar ch = CFStringGetCharacterFromInlineBuffer(&inlineBuffer, cnt);
     // Process character...
}
```

[Next](Comparing%2C%20Sorting%2C%20and%20Searching%20String%20Objects.md)[Previous](Creating%20and%20Copying%20Strings.md)

