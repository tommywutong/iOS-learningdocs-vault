---
title: Key-Value Coding Programming Guide
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/DataTypes.html
archived_at: '2026-07-15T07:16:13.068342Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Key-Value Coding Programming Guide](index.md)



## Representing Non-Object Values

The default implementation of the key-value coding protocol methods provided by `NSObject` work with both object and non-object properties. The default implementation automatically translates between object parameters or return values, and non-object properties. This allows the signatures of the key-based getters and setters to remain consistent even when the stored property is a scalar or a structure.

> [!NOTE]
> 

When you invoke one of the protocol’s getters, such as `valueForKey:`, the default implementation determines the particular accessor method or instance variable that supplies the value for the specified key according to the rules described in [Accessor Search Patterns](SearchImplementation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2tklkdjjbeeqsgizaq). If the return value is not an object, the getter uses this value to initialize an `NSNumber` object (for scalars) or `NSValue` object (for structures) and returns that instead.

Similarly, by default, setters like `setValue:forKey:` determine the data type required by a property’s accessor or instance variable, given a particular key. If the data type is not an object, the setter first sends an appropriate `<type>Value` message to the incoming value object to extract the underlying data, and stores that instead.

> [!NOTE]
> 

### Wrapping and Unwrapping Scalar Types

Table 5-1 lists the scalar types that the default key-value coding implementation wraps using an `NSNumber` instance. For each data type, the table shows the creation method used to initialize an `NSNumber` from the underlying property value to supply a getter return value. It then shows the accessor method used to extract the value from the setter input parameter during a set operation.

__Table 5-1__Scalar types as wrapped in `NSNumber` objects

| Data type | Creation method | Accessor method |
| --- | --- | --- |
| `BOOL` | `numberWithBool:` | `boolValue` (in iOS)  `charValue` (in macOS)\* |
| `char` | `numberWithChar:` | `charValue` |
| `double` | `numberWithDouble:` | `doubleValue` |
| `float` | `numberWithFloat:` | `floatValue` |
| `int` | `numberWithInt:` | `intValue` |
| `long` | `numberWithLong:` | `longValue` |
| `long long` | `numberWithLongLong:` | `longLongValue` |
| `short` | `numberWithShort:` | `shortValue` |
| `unsigned char` | `numberWithUnsignedChar:` | `unsignedChar` |
| `unsigned int` | `numberWithUnsignedInt:` | `unsignedInt` |
| `unsigned long` | `numberWithUnsignedLong:` | `unsignedLong` |
| `unsigned long long` | `numberWithUnsignedLongLong:` | `unsignedLongLong` |
| `unsigned short` | `numberWithUnsignedShort:` | `unsignedShort` |

> [!NOTE]
> 

### Wrapping and Unwrapping Structures

[Table 5-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tcljrha2dkobqfvbegskfircugrq) shows the creation and accessor methods that the default accessors use for wrapping and unwrapping the common `NSPoint`, `NSRange`, `NSRect`, and `NSSize` structures.

__Table 5-2__Common struct types as wrapped using `NSValue`.

| Data type | Creation method | Accessor method |
| --- | --- | --- |
| `NSPoint` | [valueWithPoint:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/clm/NSValue/valueWithPoint:) | `pointValue` |
| `NSRange` | [valueWithRange:](https://developer.apple.com/documentation/foundation/nsvalue/1410315-valuewithrange) | `rangeValue` |
| `NSRect` | [valueWithRect:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/clm/NSValue/valueWithRect:) (macOS only). | `rectValue` |
| `NSSize` | [valueWithSize:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/clm/NSValue/valueWithSize:) | `sizeValue` |

Automatic wrapping and unwrapping is not confined to `NSPoint`, `NSRange`, `NSRect`, and `NSSize`. Structure types (that is, types whose Objective-C type encoding strings start with `{`) can be wrapped in an `NSValue` object. For example, consider the structure and class interface declared in Listing 5-1.

__Listing 5-1__A sample class using a custom structure

1. `typedef struct {`
2. `float x, y, z;`
3. `} ThreeFloats;`
5. `@interface MyClass`
6. `@property (nonatomic) ThreeFloats threeFloats;`
7. `@end`

Using an instance of this class called `myClass`, you obtain the `threeFloats` value with key-value coding:

1. `NSValue* result = [myClass valueForKey:@"threeFloats"];`

The default implementation of `valueForKey:` invokes the `threeFloats` getter, and then returns the result wrapped in an `NSValue` object.

Similarly, you can set the `threeFloats` value using key-value coding:

1. `ThreeFloats floats = {1., 2., 3.};`
2. `NSValue* value = [NSValue valueWithBytes:&floats objCType:@encode(ThreeFloats)];`
3. `[myClass setValue:value forKey:@"threeFloats"];`

The default implementation unwraps the value with a [getValue:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/instm/NSValue/getValue:) message, and then invokes `setThreeFloats:` with the resulting structure.

[Using Collection Operators](CollectionOperators.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tmlkciffekqkjivcq)

[Validating Properties](ValidatingProperties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedcobnknltc)
