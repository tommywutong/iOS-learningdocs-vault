---
title: The Objective-C Programming Language
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocAssociativeReferences.html
archived_at: '2026-07-15T07:17:29.426764Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [The Objective-C Programming Language](Introduction.md)


[Next](Fast%20Enumeration.md)[Previous](Categories%20and%20Extensions.md)

# Associative References

Associative references, available starting in OS X v10.6, simulate the addition of object instance variables to an existing class. Using associative references, you can add storage to an object without modifying the class declaration. This may be useful if you do not have access to the source code for the class, or if for binary-compatibility reasons you cannot alter the layout of the object.

Associations are based on a key. For any object you can add as many associations as you want, each using a different key. An association can also ensure that the associated object remains valid for at least the lifetime of the source object.

You use the Objective-C runtime function [objc_setAssociatedObject](https://developer.apple.com/documentation/objectivec/1418509-objc_setassociatedobject) to make an association between one object and another. The function takes four parameters: the source object, a key, the value, and an association policy constant. Of these, the key and the association policy merit further discussion.

- The key is a `void` pointer. The key for each association must be unique. A typical pattern is to use a `static` variable.
- The policy specifies whether the associated object is assigned, retained, or copied, and whether the association is be made atomically or non-atomically. This pattern is similar to that of the attributes of a declared property (see [Property Declaration Attributes](Declared%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomq)). You specify the policy for the relationship using a constant (see [objc_AssociationPolicy](https://developer.apple.com/documentation/objectivec/objc_associationpolicy) and `Associative Object Behaviors`).

Listing 6-1 shows how you can establish an association between an array and a string.

__Listing 6-1__  Establishing an association between an array and a string

```
static char overviewKey;

NSArray *array =
    [[NSArray alloc] initWithObjects:@"One", @"Two", @"Three", nil];
// For the purposes of illustration, use initWithFormat: to ensure
// the string can be deallocated
NSString *overview =
    [[NSString alloc] initWithFormat:@"%@", @"First three numbers"];

objc_setAssociatedObject (
    array,
    &overviewKey,
    overview,
    OBJC_ASSOCIATION_RETAIN
);

[overview release];
// (1) overview valid
[array release];
// (2) overview invalid
```

At point 1, the string `overview` is still valid because the [OBJC_ASSOCIATION_RETAIN](https://developer.apple.com/documentation/objectivec/objc_associationpolicy/objc_association_retain) policy specifies that the array retains the associated object. When the array is deallocated, however (at point 2), `overview` is released and so in this case also deallocated. If you try to, for example, log the value of `overview`, you generate a runtime exception.

You retrieve an associated object using the Objective-C runtime function [objc_getAssociatedObject](https://developer.apple.com/documentation/objectivec/1418865-objc_getassociatedobject). Continuing the example shown in [Listing 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmrufvjvona), you could retrieve the overview from the array using the following line of code:

```
NSString *associatedObject =
    (NSString *)objc_getAssociatedObject(array, &overviewKey);
```


To break an association, you typically call `objc_setAssociatedObject`, passing `nil` as the value.

Continuing the example shown in [Listing 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmrufvjvona), you could break the association between the array and the string `overview` using the following line of code:

```
objc_setAssociatedObject(array, &overviewKey, nil, OBJC_ASSOCIATION_ASSIGN);
```

Given that the associated object is being set to `nil`, the policy isn’t actually important.

To break _all_ associations for an object, you can call [objc_removeAssociatedObjects](https://developer.apple.com/documentation/objectivec/1418683-objc_removeassociatedobjects). In general, however, you are discouraged from using this function because it breaks all associations for all clients. Use this function only if you need to restore an object to “pristine condition.”

The following program combines code from the preceding sections.

```objc
#import <Foundation/Foundation.h>
#import <objc/runtime.h>

int main (int argc, const char * argv[]) {

    @autoreleasepool {
        static char overviewKey;

        NSArray *array = [[NSArray alloc]
            initWithObjects:@ "One", @"Two", @"Three", nil];
        // For the purposes of illustration, use initWithFormat: to ensure
        // we get a deallocatable string
        NSString *overview = [[NSString alloc]
            initWithFormat:@"%@", @"First three numbers"];

        objc_setAssociatedObject (
            array,
            &overviewKey,
            overview,
            OBJC_ASSOCIATION_RETAIN
        );
        [overview release];

        NSString *associatedObject =
            (NSString *) objc_getAssociatedObject (array, &overviewKey);
        NSLog(@"associatedObject: %@", associatedObject);

        objc_setAssociatedObject (
            array,
            &overviewKey,
            nil,
            OBJC_ASSOCIATION_ASSIGN
        );
        [array release];

    }
    return 0;
}
```

[Next](Fast%20Enumeration.md)[Previous](Categories%20and%20Extensions.md)

