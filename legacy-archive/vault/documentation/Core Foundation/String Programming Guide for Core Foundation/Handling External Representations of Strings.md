---
title: String Programming Guide for Core Foundation
apple_id: 10000131i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/Articles/ExternalReps.html
archived_at: '2026-07-15T07:22:54.466260Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [String Programming Guide for Core Foundation](Introduction%20to%20Strings%20Programming%20Guide%20for%20Core%20Foundation.md)


[Next](Creating%20and%20Using%20Ranges.md)[Previous](Converting%20Between%20String%20Encodings.md)

# Handling External Representations of Strings

An _external representation_ of a CFString object in Core Foundation is the string data in a form that can be written to disk and read back in on the same platform or on a different platform. The format of an externally represented CFString object is a CFData object. If the encoding of the characters is Unicode, the data usually includes a special character called a BOM (for “byte order mark”) that designates the endianness of the data. When the external representation of a string is read, Core Foundation evaluates the BOM and does any necessary byte swapping. If the encoding is Unicode and there is no BOM, the data is assumed to be big-endian. When you use string objects to write out an external representation of Unicode characters, the BOM is inserted, except for representations created with encoding constants kCFStringEncodingUTF16BE, kCFStringEncodingUTF16LE, kCFStringEncodingUTF32BE, and kCFStringEncodingUTF32LE. These encodings do not require a BOM because the byte order is explicitly indicated by the letters "BE" (big-endian) and "LE" (little-endian).

When you want the character data represented by a CFString object to persist, either as a file on disk or as data sent over a network, you should first convert the CFString object to a CFData object using the function `CFStringCreateExternalRepresentation`. The CFData object is called an “external representation” of the CFString object; if the encoding is Unicode, the function automatically inserts a BOM (byte order marker) in the data to specify endianness. You can convert an external-representation CFData object back to a CFString object with the `CFStringCreateFromExternalRepresentation` function.

[Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dqljrgaytambqfvbuqrcfinaueqq) shows how the external-representation functions might be used. The last parameter of the `CFStringCreateExternalRepresentation` function specifies a loss byte, the value to be assigned to characters that cannot be converted to the specified encoding. If the loss byte is 0 (as in the example below) and conversion errors occur, the result of the function is `NULL`. This feature is similar to that provided by the `CFStringGetBytes` function; however the `CFStringCreateExternalRepresentation` function is more convenient since it gives you a CFData object.

__Listing 1__  Using the external-representation functions

```
CFDataRef appendTimeToLog(CFDataRef log) {
    CFMutableStringRef mstr;
    CFStringRef str;
    CFDataRef newLog;
    CFGregorianDate date =
        CFAbsoluteTimeGetGregorianDate(CFAbsoluteTimeGetCurrent(),
            CFTimeZoneCopySystem());

    str = CFStringCreateFromExternalRepresentation(NULL, log,
            kCFStringEncodingUTF8);
    CFShow(str);
    mstr = CFStringCreateMutableCopy(NULL, 0, str);
    CFStringAppendFormat(mstr, NULL,
        CFSTR("Received at %d/%d/%d %.2d:%.2d:%2.0f\n"),
        date.month, date.day, date.year, date.hour, date.minute,
        date.second);
    CFShow(mstr);
    newLog = CFStringCreateExternalRepresentation(NULL, mstr,
        kCFStringEncodingUTF8, '?');
    CFRelease(str);
    CFRelease(mstr);
    CFShow(newLog);
    return newLog;
}
```

This code generates output similar to the following snippet:

```
Master Log

Master Log

Received at 7/20/1999 19:23:16

<CFData 0x103c0 [0x69bce158]>{length = 43, capacity = 43, bytes = 0x4d6173746572204c6f670a0a52656365 ... 393a32333a31360a}
```

As the example shows, the CFString object in its external representation is immutable, regardless of its mutability status before being stored as a CFData object. If you want to modify the CFString object returned from `CFStringCreateFromExternalRepresentation`, you need to make a mutable copy of it.

Instead of using the `CFStringCreateFromExternalRepresentation` function to create a CFString object and _then_ access the characters in the object, you can use CFData functions to get at the characters directly. [Listing 3](Creating%20and%20Copying%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dgljrgaytinzvfvbuqrccijdemsi) shows how this is done using the CFData functions `CFDataGetLength` and `CFDataGetBytePtr`.

[Next](Creating%20and%20Using%20Ranges.md)[Previous](Converting%20Between%20String%20Encodings.md)

