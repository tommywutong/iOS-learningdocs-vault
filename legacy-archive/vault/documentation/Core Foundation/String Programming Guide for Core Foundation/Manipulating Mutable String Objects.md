---
title: String Programming Guide for Core Foundation
apple_id: 10000131i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/Articles/MutableStrings.html
archived_at: '2026-07-15T07:22:54.911014Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [String Programming Guide for Core Foundation](Introduction%20to%20Strings%20Programming%20Guide%20for%20Core%20Foundation.md)


[Next](Converting%20Between%20String%20Encodings.md)[Previous](Comparing%2C%20Sorting%2C%20and%20Searching%20String%20Objects.md)

# Manipulating Mutable String Objects

You can choose from a variety of string object functions to add to and modify the contents of mutable `CFString` objects. These functions, as one might expect, do not work on immutable `CFString` objects. If you want to change the contents of a `CFString` object, you must either start with a content-less mutable `CFString` object or make a mutable copy of an immutable `CFString` object. See [Creating Mutable String Objects](Creating%20and%20Copying%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dgljrgaytkoju) for information on creating objects of this kind.

The functions that manipulate mutable `CFString` objects fall into several categories, described in the following sections.

You can append strings in a variety of formats to a mutable `CFString` object: other `CFString` objects (`CFStringAppend`), C strings (`CFStringAppendCString`), Unicode characters (`CFStringAppendCharacters`), and formatted strings (`CFStringAppendFormat` and `CFStringAppendFormatAndArguments`).

The functions `CFStringInsert`, `CFStringDelete`, and `CFStringReplace` perform the corresponding operations. These functions require you to specify a zero-based index into, or range of, the string to be modified.

The `CFStringPad` function extends or truncates a mutable `CFString` to a given length; if it extends the string, it pads with a specified character or characters. The `CFStringTrim` function trims a specific character from both sides of the string. For example, the call:

```
CFStringTrim(CFStringCreateMutableCopy(NULL, NULL, CFSTR("xxxabcx")), CFSTR("x"));
```

would result in the string “abc”. A related function, `CFStringTrimWhitespace`, does the same thing with whitespace characters, which include such characters as tabs and carriage returns.

Three functions modify the case of a mutable string, making it all uppercase (`CFStringUppercase`), all lowercase (`CFStringLowercase`), or just the first character of each word in a string uppercase (`CFStringCapitalize`).

[Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dmljrgaytaojrfvbuqrcejbeucri) exemplifies several of the functions that manipulate mutable `CFString` objects:

__Listing 1__  Various operations on a mutable string

```
void mutableStringOperations() {

    CFMutableStringRef mstr;
    CFRange range;
    StringPtr pbuf;
    CFIndex length;

    mstr = CFStringCreateMutable(NULL, 0);
    CFStringAppend(mstr, CFSTR("Now is the time for all good men to come to the aid of their "));
    CFStringAppend(mstr, CFSTR("party."));
    CFShow(CFSTR("Mutable String 1 - Appended CFStrings"));
    CFShow(mstr);

    range = CFStringFind(mstr, CFSTR("good"), 0);
    if (range.length > 0) {
        CFStringReplace(mstr, range, CFSTR("bad"));
        CFShow(CFSTR("Mutable String 2 - Replaced substring"));
        CFShow(mstr);
    }

    CFStringUppercase(mstr, NULL);
    CFShow(CFSTR("Mutable String 3 - Convert to uppercase:"));
    CFShow(mstr);
}
```

When compiled and run, this code generates the following output:

```
Mutable String 1 - Appended CFStrings
Now is the time for all good men to come to the aid of their party.
Mutable String 2 - Replaced substring
Now is the time for all bad men to come to the aid of their party.
Mutable String 3 - Convert to uppercase:
NOW IS THE TIME FOR ALL BAD MEN TO COME TO THE AID OF THEIR PARTY.
```

[Next](Converting%20Between%20String%20Encodings.md)[Previous](Comparing%2C%20Sorting%2C%20and%20Searching%20String%20Objects.md)

