---
title: Core Foundation Design Concepts
apple_id: 10000122i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: CoreFoundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/Comparing.html
archived_at: '2026-07-15T07:22:22.169491Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Foundation Design Concepts](Introduction%20to%20Core%20Foundation%20Design%20Concepts.md)


[Next](Inspecting%20Objects.md)[Previous](Other%20Types.md)

# Comparing Objects

You compare two Core Foundation objects with the `CFEqual` function. If the two objects are essentially equal, the function returns a boolean true value. “Essential” equality depends on the type of objects compared. For example, when you compare two CFString objects, Core Foundation considers them essentially equal when they match character by character, regardless of their encodings or mutability attribute. Two CFArray objects are considered equal when they have the same count of elements _and_ each element object in one array is essentially equal with its counterpart in the other array. Obviously, compared objects must be of the same type (or a mutable or immutable variant of the same type) to be considered equal.

The following code fragment shows how you might use the `CFEqual` function to compare a constant with a passed-in parameter:

__Listing 1__  Comparing Core Foundation objects

```
void stringTest(CFStringRef myString) {
    Boolean equal = CFEqual(myString, CFSTR(“Kalamazoo”));
    if (!equal) {
        printf(“They’re not equal!");
    }
    else {
        printf(“They’re equal!”):
    }
}
```

[Next](Inspecting%20Objects.md)[Previous](Other%20Types.md)

