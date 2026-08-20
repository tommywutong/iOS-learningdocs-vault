---
title: Key-Value Coding Programming Guide
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/HandlingNon-ObjectValues.html
archived_at: '2026-07-15T07:16:14.063018Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Key-Value Coding Programming Guide](index.md)



## Handling Non-Object Values

Typically, your key-value coding compliant object relies on the default implementation of key-value coding to automatically wrap and unwrap non-object properties, as described in [Representing Non-Object Values](DataTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tclkciffekqkjivcq). However, you can override the default behavior. The most common reason to do so is to handle attempts to store a `nil` value on non-object properties.

> [!NOTE]
> 

If your key-value coding compliant object receives a `setValue:forKey:` message with `nil` passed as the value for a non-object property, the default implementation has no appropriate, generalized course of action. It therefore sends itself a `setNilValueForKey:` message, which you can override. The default implementation of `setNilValueForKey:` raises an [NSInvalidArgumentException](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSInvalidArgumentException) exception, but you can provide an appropriate, implementation-specific behavior.

For example, the code in Listing 10-1 responds to an attempt to set a person’s age to a `nil` value by instead setting the age to 0, which is more appropriate for a floating point value. Notice that the override method calls upon its object’s superclass for any keys that it does not explicitly handle.

__Listing 10-1__Example implementation of setNilValueForKey:

1. `- (void)setNilValueForKey:(NSString *)key`
2. `{`
3. `if ([key isEqualToString:@"age"]) {`
4. `[self setValue:@(0) forKey:@”age”];`
5. `} else {`
6. `[super setNilValueForKey:key];`
7. `}`
8. `}`

> [!NOTE]
> 

[Defining Collection Methods](DefiningCollectionMethods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedcnznknltc)

[Adding Validation](Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tglkdjjbeiqsiinba)
