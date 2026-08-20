---
title: String Programming Guide for Core Foundation
apple_id: 10000131i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/Articles/ComparingAndSearching.html
archived_at: '2026-07-15T07:22:53.101600Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [String Programming Guide for Core Foundation](Introduction%20to%20Strings%20Programming%20Guide%20for%20Core%20Foundation.md)


[Next](Manipulating%20Mutable%20String%20Objects.md)[Previous](Accessing%20the%20Contents%20of%20String%20Objects.md)

# Comparing, Sorting, and Searching String Objects

Core Foundation string objects include a number of functions for searching the contents of strings and for comparing two strings. Because these operations are semantically related, it is not surprising that the main functions for each operation—`CFStringFindWithOptions` and `CFStringCompareWithOptions`—have some things in common. Their first four parameters are almost identical: two references to CFString objects (the strings to be compared or the substring to find in the main string), a range of characters to include in the operation, and a bitmask for specifying options. If you are sorting strings to present to the user, you should perform a localized comparison with the user’s local using [CFStringCompareWithOptionsAndLocale](https://developer.apple.com/documentation/corefoundation/1543315-cfstringcomparewithoptionsandloc).

Although `CFStringFindWithOptions` and `CFStringCompareWithOptions` have features in common, they have important differences too. The `CFStringCompareWithOptions` function returns a result of type [Comparison Results](https://developer.apple.com/documentation/corefoundation/cfcomparisonresult); this `enum` constant indicates whether the comparison found the strings equal or whether the first specified string was greater than or less than the second string. The `CFStringFindWithOptions` function, on the other hand, returns a `Boolean` result that indicates the success of the operation. The more useful result, returned indirectly by this function, is a range (a structure of type `CFRange`) pointed to by its final parameter; this range contains the location of the found string in the main string.

[Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dkljrgaytamrrfvbuqrccireeurq) illustrates the use of both `CFStringCompareWithOptions` and `CFStringFindWithOptions` (it also makes use of the `show` function given in [Listing 2](Creating%20and%20Copying%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dgljrgaytgnbxfvbuqrccinaukrq) of [Creating and Copying Strings](Creating%20and%20Copying%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dglkdjjbekscbifdq)).

In this example, both the find and compare functions specify the `kCFCompareCaseInsensitive` flag as an option for the operation, causing it to ignore differences in case. Other option flags are available, including `kCFCompareBackwards` (start the operation from the end of the string), `kCFCompareNumerically` (compare similar strings containing numeric substrings numerically), and `kCFCompareLocalized` (use the user’s default locale for the operation).

__Listing 1__  Comparing and searching CFString contents

```
void compareAndSearchStringsExample() {
    CFStringRef str1 = CFSTR("ABCDEFG");
    CFStringRef str2 = CFSTR("abcdefg");
    CFStringRef str3 = CFSTR("Kindergarten is the time to start teaching the ABCDEFG's");
    CFRange foundRange;
    CFComparisonResult result;

    result = CFStringCompareWithOptions(str1, str2, CFRangeMake(0,CFStringGetLength(str1)), kCFCompareCaseInsensitive);
    if (result == kCFCompareEqualTo) {
        show(CFSTR("%@ is the same as %@"), str1, str2);
    } else {
        show(CFSTR("%@ is not the same as %@"), str1, str2);
    }
    if ( CFStringFindWithOptions(str3, str1, CFRangeMake(0,CFStringGetLength(str3)), kCFCompareCaseInsensitive, &foundRange) == true ) {
        show(CFSTR("The string \"%@\" was found at index %d in string \"%@\"."), str1, foundRange.location, str3);
    } else {
        show(CFSTR("The string \"%@\" was not found in string \"%@\"."), str1,  str3);
    }
}
```

This code generates the following output:

```
ABCDEFG is the same as abcdefg
The string "ABCDEFG" was found at index 47 in string "Kindergarten is the time to start teaching the ABCDEFG's".
```

By default, the basis for comparison of CFString objects is a character-by-character literal comparison. In some circumstances this may not give you results you expect, since some characters can be represented in several different ways (for example, “ö” can be represented as two distinct characters (“o” and “umlaut”) or by a single character (“o-umlaut”). If you want to allow loose equivalence, use a search or compare function with the `kCFCompareNonliteral` flag as an option. Note that if you do specify a non-literal comparison, the length of the range returned from a find function might not be the same as the length of the search string.

In addition to the main compare and find functions, string objects provide some convenience functions. `CFStringFind` and `CFStringCompare` are similar to the “main” functions described above but they do not require the specification of a range (the entire string is assumed). Note that you can use `CFStringCompare` elsewhere in Core Foundation when a function pointer conforming to the `CFComparatorFunction` type is required.

Other search and comparison functions of string objects are [CFStringHasPrefix](https://developer.apple.com/documentation/corefoundation/1542014-cfstringhasprefix), [CFStringHasSuffix](https://developer.apple.com/documentation/corefoundation/1542768-cfstringhassuffix), and [CFStringCreateArrayWithFindResults](https://developer.apple.com/documentation/corefoundation/1542263-cfstringcreatearraywithfindresul). The last of these functions is useful when you expect multiple hits with a search operation; it returns an array of `CFRange` structures, each of which specifies the location of a matching substring in the main string.

If you sort strings and present the results to the user, you should make sure that you perform a localized comparison using the user’s locale. You may also want to arrange strings as they would appear in Finder—for example, these strings { "String 12", "String 1", "string 22", "string 02" } should be sorted as { "String 1", "string 02", "String 12", "string 22" }.

To achieve this, you can use [CFStringCompareWithOptionsAndLocale](https://developer.apple.com/documentation/corefoundation/1543315-cfstringcomparewithoptionsandloc) with the options `kCFCompareCaseInsensitive`, `kCFCompareNonliteral`, `kCFCompareLocalized`, `kCFCompareNumerically`, `kCFCompareWidthInsensitive`, and `kCFCompareForcedOrdering`. First, implement a function to perform the appropriate comparison:

```
CFComparisonResult CompareStringsLikeFinderWithLocale (
    const void *string1, const void *string2, void *locale)
{
    static CFOptionFlags compareOptions = kCFCompareCaseInsensitive |
                                          kCFCompareNonliteral |
                                          kCFCompareLocalized |
                                          kCFCompareNumerically |
                                          kCFCompareWidthInsensitive |
                                          kCFCompareForcedOrdering;

    CFRange string1Range = CFRangeMake(0, CFStringGetLength(string1));

    return CFStringCompareWithOptionsAndLocale
               (string1, string2, string1Range, compareOptions, (CFLocaleRef)locale);
}
```

Then perform the comparison using that function:

```
// ignore memory management for the sake of clarity and brevity
CFMutableArrayRef theArray = CFArrayCreateMutable(kCFAllocatorDefault, 4, NULL);
CFArrayAppendValue(theArray, CFSTR("String 12"));
CFArrayAppendValue(theArray, CFSTR("String 1"));
CFArrayAppendValue(theArray, CFSTR("string 22"));
CFArrayAppendValue(theArray, CFSTR("string 02"));

CFRange arrayRange = CFRangeMake(0, CFArrayGetCount(theArray));
CFLocaleRef locale = CFLocaleCopyCurrent();

CFArraySortValues (theArray, arrayRange,
                   CompareStringsLikeFinderWithLocale, (void *)locale);

// theArray now contains { "String 1", "string 02", "String 12", "string 22" }
```

[Next](Manipulating%20Mutable%20String%20Objects.md)[Previous](Accessing%20the%20Contents%20of%20String%20Objects.md)

