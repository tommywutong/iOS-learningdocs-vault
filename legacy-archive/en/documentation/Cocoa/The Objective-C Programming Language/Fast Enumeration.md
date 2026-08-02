---
title: The Objective-C Programming Language
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocFastEnumeration.html
archived_at: '2026-07-15T07:17:30.392078Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [The Objective-C Programming Language](Introduction.md)


[Next](Enabling%20Static%20Behavior.md)[Previous](Associative%20References.md)

# Fast Enumeration

Fast enumeration is a language feature that allows you to efficiently and safely enumerate over the contents of a collection using a concise syntax.

The syntax for fast enumeration is defined as follows:

```
for ( Type newVariable in expression ) { statements }
```

or

```
Type existingItem;
for ( existingItem in expression ) { statements }
```

In both cases, _expression_ yields an object that conforms to the [NSFastEnumeration](https://developer.apple.com/documentation/foundation/nsfastenumeration) protocol (see [Adopting Fast Enumeration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjyfvjvomq)). The iterating variable is set to each item in the returned object in turn, and the code defined by `statements` is executed. The iterating variable is set to `nil` when the loop ends by exhausting the source pool of objects. If the loop is terminated early, the iterating variable is left pointing to the last iteration item.

There are several advantages to using fast enumeration:

- The enumeration is considerably more efficient than, for example, using `NSEnumerator` directly.
- The syntax is concise.
- Enumeration is “safe”—the enumerator has a mutation guard so that if you attempt to modify the collection during enumeration, an exception is raised.

Because mutation of the object during iteration is forbidden, you can perform multiple enumerations concurrently.

In other respects, the feature behaves like a standard `for` loop. You can use `break` to interrupt the iteration and `continue` to advance to the next element.

Any class whose instances provide access to a collection of other objects can adopt the [NSFastEnumeration](https://developer.apple.com/documentation/foundation/nsfastenumeration) protocol. The collection classes in the Foundation framework—[NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray), [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary), and [NSSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSSet)—adopt this protocol, as does `NSEnumerator`. It should be obvious that in the cases of `NSArray` and `NSSet` the enumeration is over their contents. For other classes, the corresponding documentation should make clear what property is iterated over—for example, [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) and the Core Data class [NSManagedObjectModel](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel) provide support for fast enumeration; `NSDictionary` enumerates its keys, and `NSManagedObjectModel` enumerates its entities.

The following code example illustrates using fast enumeration with `NSArray` and `NSDictionary` objects.

```
NSArray *array = [NSArray arrayWithObjects:
        @"one", @"two", @"three", @"four", nil];

for (NSString *element in array) {
    NSLog(@"element: %@", element);
}

NSDictionary *dictionary = [NSDictionary dictionaryWithObjectsAndKeys:
    @"quattuor", @"four", @"quinque", @"five", @"sex", @"six", nil];

NSString *key;
for (key in dictionary) {
    NSLog(@"English: %@, Latin: %@", key, [dictionary objectForKey:key]);
}
```

You can also use `NSEnumerator` objects with fast enumeration, as illustrated in this example:

```
NSArray *array = [NSArray arrayWithObjects:
        @"one", @"two", @"three", @"four", nil];

NSEnumerator *enumerator = [array reverseObjectEnumerator];
for (NSString *element in enumerator) {
    if ([element isEqualToString:@"three"]) {
        break;
    }
}

NSString *next = [enumerator nextObject];
// next = "two"
```

For collections or enumerators that have a well-defined order—such as an `NSArray` or an `NSEnumerator` instance derived from an array—the enumeration proceeds in that order, so simply counting iterations gives you the proper index into the collection if you need it.

```
NSArray *array = <#Get an array#>;
NSUInteger index = 0;

for (id element in array) {
    NSLog(@"Element at index %u is: %@", index, element);
    index++;
}
```

[Next](Enabling%20Static%20Behavior.md)[Previous](Associative%20References.md)

