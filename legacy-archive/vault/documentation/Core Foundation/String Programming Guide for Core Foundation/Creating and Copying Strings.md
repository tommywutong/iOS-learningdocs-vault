---
title: String Programming Guide for Core Foundation
apple_id: 10000131i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/Articles/CreatingAndCopying.html
archived_at: '2026-07-15T07:22:54.000580Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [String Programming Guide for Core Foundation](Introduction%20to%20Strings%20Programming%20Guide%20for%20Core%20Foundation.md)


[Next](Accessing%20the%20Contents%20of%20String%20Objects.md)[Previous](String%20Storage.md)

# Creating and Copying Strings

String objects give you a variety of ways to create CFString objects—from constant strings, from buffers, from formatted strings, and by using existing CFString objects. The following sections describe each of these techniques.

Some functions that return references to CFString objects are described elsewhere. The `CFStringCreateWithBytes` function is described in [Converting Between String Encodings](Converting%20Between%20String%20Encodings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dolkdjjbekscbifdq). The section [Handling External Representations of Strings](Handling%20External%20Representations%20of%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dqlkdjjbekscbifdq) describes the `CFStringCreateFromExternalRepresentation` function.

The easiest way to create immutable CFString objects is to use the `CFSTR` macro. The argument of the macro must be a constant compile-time string—text enclosed in quotation marks. `CFSTR` returns a reference to a CFString object.

Here’s an example:

```
CFStringRef hello = CFSTR("Hello, world.");
```

The returned CFString has the following semantics:

- Because `CFSTR` is not a Create or Copy function, you are not responsible for releasing the string when you no longer need it.
- The string is not released by CFString. In other words, CFString guarantees its validity until the program terminates.
- The string can be retained and released in a balanced fashion, like any other CFString.

If there are two or more exact instances of a constant string in an executable, in some cases only one might be stored. A common use of the `CFSTR` macro is in the creation of formatted strings (see [Creating String Objects From Formatted Strings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dgljrgaytgmbz) for more information).

A common technique for creating a CFString object is to call functions that take C character buffers (or string pointers) as “source” for the object. These functions are the counterparts of functions that convert CFString objects to C strings; see [Accessing the Contents of String Objects](Accessing%20the%20Contents%20of%20String%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dilkdjjbekscbifdq) for more on these functions.

These functions come in two varieties. One set of functions copies the buffer into the internal storage of the created CFString object. Once you create the object you are free to dispose of the buffer. Related functions create CFString objects from C string buffers (`CFStringCreateWithCString`) and from Unicode string buffers (`CFStringCreateWithCharacters`). The latter function takes an extra parameter for character count but does not include the encoding parameter.

A parallel set of functions have corresponding names that end with `NoCopy`. These functions also create CFString objects from a user-supplied string buffer but they do not always copy the buffer to the object’s internal storage. They try to but are not guaranteed to take the provided pointer as-is, using the buffer as the backing store without copying the data. Obviously you must ensure that you do not free the buffer while the CFString exists. The character data should never be on the stack or be data with a lifetime you cannot guarantee.

In practice, these `NoCopy` functions are useful in a limited number of circumstances:

- You have compile-time constant data such as a C string (“Hello”). The `NoCopy` functions offer an efficient way to make CFString objects from this data and, if you specify `kCFAllocatorNull` as the last parameter (see below), when the CFString ceases to exist the buffer is not automatically deallocated. (Often you can use the `CFSTR` macro for the same purpose.)
- You allocate some memory for some string data and you want to put a CFString object in it but otherwise you don’t need the original memory. Of course, you can create a CFString object with one of the non-`NoCopy` functions (which copies the data) and then free the buffer. But the `NoCopy` functions allow you to transfer ownership of the memory to a CFString object, saving you the need to free it yourself.

The `NoCopy` functions include an extra parameter (_contentsDeallocator_) for passing a reference to a CFAllocator object that is used for deallocating the buffer when it is no longer needed. If the default CFAllocator object is sufficient for this purpose, you can pass `NULL`. If you do not want the CFString object to deallocate the buffer, pass `kCFAllocatorNull`.

[Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dgljrgaytemztfvbuqrcdjjcuqqi) shows the creation of a CFString object with the `CFStringCreateWithCStringNoCopy` function:

__Listing 1__  Creating a CFString object with a NoCopy function

```
const char *bytes;
CFStringRef str;
bytes = CFAllocatorAllocate(CFAllocatorGetDefault(), 6, 0);
strcpy(bytes, "Hello");
str = CFStringCreateWithCStringNoCopy(NULL, bytes,
    kCFStringEncodingMacRoman, NULL);
/* do something with str here...*/
CFRelease(str); /* default allocator also frees bytes */
```

You can also create mutable CFString objects with source buffers that you control entirely; see [Mutable Strings With Client-Owned Buffers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dgljrgaytmobu) for more on this matter.

String objects includes functions that create CFString objects from formatted strings—strings incorporating `printf`-style specifiers for substituting variable values into the string, after converting them (if necessary) to character data. String format specifiers are defined in [String Format Specifiers](String%20Format%20Specifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denrvfvjvomi). Formatted strings are useful when it is necessary to display information that may have changeable elements. For example, you might need to use these functions when you put up a dialog box to show the progress of an operation, such as “Copying file _x_ of _y_.”

The `CFStringCreateWithFormat` function creates a CFString object from a simple formatted string, as shown in [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dgljrgaytgnbxfvbuqrccinaukrq).

__Listing 2__  Creating a CFString object from a formatted string

```
CFStringRef PrintGross(CFStringRef employeeName, UInt8 hours, float wage) {
    return CFStringCreateWithFormat(NULL, NULL, CFSTR(“Employee %@
    earned $%.2f this week.”), employeeName, hours * wage);
}
```

The first parameter, as usual, specifies the allocator object to use (`NULL` means use the default CFAllocator object). The second parameter is for locale-dependent format options, such as thousand and decimal separators; it is currently not used. The remaining parameters are for the format string and the variable values.

As mentioned earlier, the format string has `printf`-style specifiers embedded in it (for example, `“%d %s %2.2f”`). Core Foundation introduces a couple of extensions to this convention. One is the `%@` specifier (shown in [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dgljrgaytgnbxfvbuqrccinaukrq)) which indicates any Core Foundation object. Another new specifier indicates argument order. This specifier takes the form _n_`$` where _n_ is the order-number of the argument following the string. This argument-order feature is useful when you want to localize whole sentences or even paragraphs to other languages without worrying about the order of arguments, which might vary from one language to another.

For example, the function above would result in a string such as “John Doe earned $1012.32 this week.” But in another language the grammatically proper way of expressing the same sentence might be (roughly translated) “$1012.32 was earned by John Doe this week.” You wouldn’t have to call `CFStringCreateWithFormat` again with the arguments in a different order. Instead, you would have a function call that looked like this:

```
return CFStringCreateWithFormat(NULL, NULL, CFSTR(“$%2$.2f was earned by
    employee %1$@.”), employeeName, hours * wage);
```

Of course, the string itself would not be hard-coded, but would be loaded from a file (for instance, an XML property list or an OpenStep ASCII property list) that contains localized strings and their translations.

Another CFString function, `CFStringCreateWithFormatAndArguments`, takes a variable argument list (`vararg`) as well as a format string. This function allows the formatting of `vararg`s passed into your function. [Listing 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dgljrgaytinzvfvbuqrccijdemsi) shows how it might be used:

__Listing 3__  Creating a CFString from a variable argument list

```
void show(CFStringRef formatString, ...) {
    CFStringRef resultString;
    CFDataRef data;
    va_list argList;

    va_start(argList, formatString);
    resultString = CFStringCreateWithFormatAndArguments(NULL, NULL,
        formatString, argList);
    va_end(argList);

    data = CFStringCreateExternalRepresentation(NULL, resultString,
        kCFStringEncodingMacRoman, '?');

    if (data != NULL) {
        printf ("%.*s\n\n", (int)CFDataGetLength(data),
            CFDataGetBytePtr(data));
        CFRelease(data);
    }

    CFRelease(resultString);
}
```


String objects includes only a handful of functions for creating mutable CFString objects. The reason for this much smaller set is obvious. Because these are mutable objects, you can modify them after you create them with the functions described in [Manipulating Mutable String Objects](Manipulating%20Mutable%20String%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dmlkdjjbekscbifdq).

There are two basic functions for creating mutable CFString objects. The `CFStringCreateMutable` function creates an “empty” object; the `CFStringCreateMutableCopy` makes a mutable copy of an immutable CFString object. [Listing 4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dgljrgaytmmryfvbuqrcdindeeqq) illustrates the latter function and shows a character being appended to the created object:

__Listing 4__  Creating a mutable copy of a CFString object

```
const UniChar u[] = {'5', '+', '*', ‘d’, 'x', '4', 'Q', '?'};
CFMutableStringRef str;

str = CFStringCreateMutableCopy(alloc, 0, CFSTR("abc"));
CFStringAppendCharacters(str, &u[3], 1);
CFRelease(str);
```

The second parameter of both functions is a `CFIndex` value named _maxLength_. This value specifies the maximum numbers of characters in the string and allows the created object to optimize its storage and catch errors if too many characters are inserted. If 0 is specified for this parameter (as above), the string can grow to any size.

When you create most Core Foundation objects, the object takes the initializing data you provide and stores that data internally. String objects allow some exceptions to this behavior, and for mutable CFString objects that exception is the `CFStringCreateMutableWithExternalCharactersNoCopy` function. This function creates a mutable CFString object whose backing store is some Unicode buffer that you create and own. You can test and manipulate this buffer independently of the object.

[Listing 5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dgljrgaytomjqfvbuqrceivcemry) shows how to create such a cheap mutable CFString “wrapper” for your character buffer.

__Listing 5__  Creating a mutable CFString object with independent backing store

```
void stringWithExternalContentsExample(void) {
#define BufferSize 1000
    CFMutableStringRef mutStr;
    UniChar *myBuffer;

    myBuffer = malloc(BufferSize * sizeof(UniChar));

    mutStr = CFStringCreateMutableWithExternalCharactersNoCopy(NULL, myBuffer, 0, BufferSize, kCFAllocatorNull);
    CFStringAppend(mutStr, CFSTR("Appended string... "));
    CFStringAppend(mutStr, CFSTR("More stuff... "));
    CFStringAppendFormat(mutStr, NULL, CFSTR("%d %4.2f %@..."), 42, -3.14, CFSTR("Hello"));

    CFRelease(mutStr);
    free(myBuffer);
}
```

The third and fourth parameters in the creation function specify the number of characters in the buffer and the buffer capacity. The final parameter, _externalCharsAllocator_, specifies the CFAllocator object to use for reallocating the buffer when editing takes place and for deallocating the buffer when the CFString object is deallocated. In the above example, `kCFAllocatorNull` is specified, which tells the object that the client assumes responsibility for these actions. If you specified an allocator object to use, such as `NULL` for the default allocator, there is usually no need to worry about reallocation or deallocation of the buffer.

The example illustrates how you can modify the contents of the buffer with CFString functions. You can also modify the contents of the buffer directly, but if you do so, you must notify the mutable CFString “wrapper” object with the `CFStringSetExternalCharactersNoCopy` function. You can also substitute an entirely different buffer with this function because it makes the mutable CFString object point directly at the specified `UniChar` array as its backing store. (However, the CFString object must have been created with the `CFStringCreateMutableWithExternalCharactersNoCopy` function.) The `CFStringSetExternalCharactersNoCopy` function does not free the previous buffer.

Using these functions comes at a cost because some CFString optimizations are invalidated. For example, mutable CFString objects can no longer use a gap for editing, and they cannot optimize storage by using 8-bit characters.

[Next](Accessing%20the%20Contents%20of%20String%20Objects.md)[Previous](String%20Storage.md)

