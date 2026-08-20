---
title: Core Foundation Design Concepts
apple_id: 10000122i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: CoreFoundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/Inspecting.html
archived_at: '2026-07-15T07:22:22.675859Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Foundation Design Concepts](Introduction%20to%20Core%20Foundation%20Design%20Concepts.md)


[Next](Toll-Free%20Bridged%20Types.md)[Previous](Comparing%20Objects.md)

# Inspecting Objects

A primary characteristic of Core Foundation objects is that they’re based on an opaque (or private) type; it is thus difficult to inspect the internal data of an object directly. Base Services, however, provide two functions with which you can inspect Core Foundation objects. These functions return descriptions of an object and of the object’s type.

To find out the contents of a Core Foundation object, call the `CFCopyDescription` function on that object and then print the character sequence “contained” in the referred-to string object:

__Listing 1__  Using CFCopyDescription

```
void describe255(CFTypeRef tested) {
    char buffer[256];
    CFIndex got;
    CFStringRef description = CFCopyDescription(tested);
    CFStringGetBytes(description,
        CFRangeMake(0, CFStringGetLength(description)),
        CFStringGetSystemEncoding(), '?', TRUE, buffer, 255, &got);
    buffer[got] = (char)0;
    fprintf(stdout, "%s", buffer);
    CFRelease(description);
}
```

This example shows just one approach for printing a description. You could use CFString functions other than `CFStringGetBytes` to get the actual string.

To determine the type of an “unknown” object, obtain its type ID with the `CFGetTypeID` function and compare that value with known type IDs until you find a match. You obtain an object’s type ID with the `CFGetTypeID` function. Each opaque type also defines a function of the form `CF`_Type_`GetTypeID` (for example, `CFArrayGetTypeID`); this function returns the type ID for that type. Therefore, you can test whether a CFType object is a member of a specific opaque type as in:

```
CFTypeID type = CFGetTypeID(anObject);
if (CFArrayGetTypeID() == type)
    printf(“anObject is an array.”);
else
    printf(“anObject is NOT an array.”);
```

To display information about the type of a Core Foundation object in the debugger, use the `CFGetTypeID` function to get its type ID, then pass that value to the `CFCopyTypeIDDescription` function:

```
/* aCFObject is any Core Foundation object */
CFStringRef descrip = CFCopyTypeIDDescription(CFGetTypeID(aCFObject));
```

[Next](Toll-Free%20Bridged%20Types.md)[Previous](Comparing%20Objects.md)

