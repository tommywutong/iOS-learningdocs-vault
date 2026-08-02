---
title: Key-Value Coding Programming Guide
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/ValidatingProperties.html
archived_at: '2026-07-15T07:16:16.598036Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Key-Value Coding Programming Guide](index.md)



## Validating Properties

The key-value coding protocol defines methods to support property validation. Just as you use key-based accessors to read and write properties of a key-value coding compliant object, you can also validate properties by key (or key path). When you call the [validateValue:forKey:error:](https://developer.apple.com/documentation/objectivec/nsobject/1416754-validatevalue) (or the [validateValue:forKeyPath:error:](https://developer.apple.com/documentation/objectivec/nsobject/1416245-validatevalue)) method, the default implementation of the protocol searches the object receiving the validation message (or the one at the end of the key path) for a method whose name matches the pattern `validate<Key>:error:`. If the object has no such method, the validation succeeds by default, and the default implementation returns `YES``true`. When a property-specific validation method exists, the default implementation returns the result of calling that method instead.

> [!NOTE]
> 

Because property-specific validation methods receive the value and error parameters by reference, validation has three possible outcomes:

1. The validation method deems the value object valid and returns `YES``true` without altering the value or the error.
2. The validation method deems the value object invalid, but chooses not to alter it. In this case, the method returns `NO``false` and sets the error reference (if provided by the caller) to an `NSError` object that indicates the reason for failure.
3. The validation method deems the value object invalid, but creates a new, valid one as a replacement. In this case, the method returns `YES``true` while leaving the error object untouched. Before returning, the method modifies the value reference to point at the new value object. When it makes a modification, the method always creates a new object, rather than modifying the old one, even if the value object is mutable.

Listing 6-1 shows an example of how to call validation for a name string.

__Listing 6-1__Validation of the name property

1. `Person* person = [[Person alloc] init];`
2. `NSError* error;`
3. `NSString* name = @"John";`
4. `if (![person validateValue:&name forKey:@"name" error:&error]) {`
5. `NSLog(@"%@",error);`
6. `}`

### Automatic Validation

In general, neither the key-value coding protocol nor its default implementation define any mechanism to perform validation automatically. Instead, you make use of the validation methods when appropriate for your app.

Certain other Cocoa technologies do perform validation automatically in some circumstances. For example, Core Data automatically performs validation when the managed object context is saved (see _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_). Also, in macOS, Cocoa bindings allow you to specify that validation should occur automatically (see _[Cocoa Bindings Programming Topics](../Cocoa%20Bindings%20Programming%20Topics/Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3do2i)_ for more information).

[Representing Non-Object Values](DataTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tclkciffekqkjivcq)

[Accessor Search Patterns](SearchImplementation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2tklkdjjbeeqsgizaq)
