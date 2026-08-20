---
title: Property List Programming Topics for Core Foundation
apple_id: 10000130i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/Articles/Numbers.html
archived_at: '2026-07-15T07:22:46.070193Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Property List Programming Topics for Core Foundation](Introduction%20to%20Property%20List%20Programming%20Topics%20for%20Core%20Foundation.md)


[Next](Property%20List%20XML%20Tags.md)[Previous](Saving%20and%20Restoring%20Property%20Lists.md)

# Using Numbers in Property Lists

You cannot use C numeric data values directly in Core Foundation property lists. Core Foundation provides the function `CFNumberCreate` to convert C numerical values into CFNumber objects, the form that is required to use numbers in property lists.

A CFNumber object serves simply as a wrapper for C numeric values. Core Foundation includes functions to create a CFNumber, obtain its value, and compare two CFNumber objects. Note that CFNumber objects are immutable with respect to value, but type information may not be maintained. You can get information about a CFNumber object’s type, but this is the type the CFNumber object used to store your value and _may not_ be the same type as the original C data.

When comparing CFNumber objects, conversion and comparison follow human expectations and not C promotion and comparison rules. Negative zero compares less than positive zero. Positive infinity compares greater than everything except itself, to which it compares equal. Negative infinity compares less than everything except itself, to which it compares equal. Unlike standard practice, if both numbers are NaNs, then they compare equal; if only one of the numbers is a NaN, then the NaN compares greater than the other number if it is negative, and smaller than the other number if it is positive.

[Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3tglktk4yq) shows how to create a CFNumber object from a 16-bit integer and then get information about the CFNumber object.

__Listing 1__  Creating a CFNumber object from an integer

```
Int16               sint16val = 276;
CFNumberRef         aCFNumber;
CFNumberType        type;
Int32               size;
Boolean             status;

// Make a CFNumber from a 16-bit integer.
aCFNumber = CFNumberCreate(kCFAllocatorDefault,
                           kCFNumberSInt16Type,
                           &sint16val);

// Find out what type is being used by this CFNumber.
type = CFNumberGetType(aCFNumber);

// Now find out the size in bytes.
size = CFNumberGetByteSize(aCFNumber);

// Get the value back from the CFNumber.
status = CFNumberGetValue(aCFNumber,
                          kCFNumberSInt16Type,
                          &sint16val);
```

[Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3tglktk4za) creates another CFNumber object and compares it with the one created in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3tglktk4yq).

__Listing 2__  Comparing two CFNumber objects

```
CFNumberRef         anotherCFNumber;
CFComparisonResult  result;

// Make a new CFNumber.
sint16val = 382;
anotherCFNumber = CFNumberCreate(kCFAllocatorDefault,
                        kCFNumberSInt16Type,
                        &sint16val);

// Compare two CFNumber objects.
result = CFNumberCompare(aCFNumber, anotherCFNumber, NULL);

switch (result) {
    case kCFCompareLessThan:
        printf("aCFNumber is less than anotherCFNumber.\n");
        break;
    case kCFCompareEqualTo:
        printf("aCFNumber is equal to anotherCFNumber.\n");
        break;
    case kCFCompareGreaterThan:
        printf("aCFNumber is greater than anotherCFNumber.\n");
        break;
}
```

[Next](Property%20List%20XML%20Tags.md)[Previous](Saving%20and%20Restoring%20Property%20Lists.md)

