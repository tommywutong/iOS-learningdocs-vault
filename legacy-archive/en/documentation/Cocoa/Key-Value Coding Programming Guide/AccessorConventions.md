---
title: Key-Value Coding Programming Guide
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/AccessorConventions.html
archived_at: '2026-07-15T07:16:10.549450Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Key-Value Coding Programming Guide](index.md)



## Achieving Basic Key-Value Coding Compliance

When adopting key-value coding for an object, you rely on the default implementation of the `NSKeyValueCoding` protocol by having your object inherit from `NSObject` or one of its many subclasses. The default implementation, in turn, relies on you to define your object’s instance variables (or _ivars_) and accessor methods following certain well-defined patterns, so that it can associate key strings with properties when it receives key-value coded messages, such as `valueForKey:` and `setValue:forKey:`.

You often adhere to the standard patterns in Objective-C by simply declaring a property using a `@property` statement, and allowing the compiler to automatically synthesize the ivar and accessors. The compiler follows the expected patterns by default.

> [!NOTE]
> 

If you do need to implement accessors or ivars manually in Objective-C, follow the guidelines in this section to maintain basic compliance. To provide additional functionality that enhances interaction with your object’s collection properties in any language, implement the methods described in [Defining Collection Methods](DefiningCollectionMethods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedcnznknltc). To further enhance your object with key-value validation, implement the methods described in [Adding Validation](Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tglkdjjbeiqsiinba).

> [!NOTE]
> 

### Basic Getters

To implement a getter that returns the value of a property, while perhaps doing additional custom work, use a method named like the property, such as for the `title` string property:

1. `- (NSString*)title`
2. `{`
3. `// Extra getter logic…`
5. `return _title;`
6. `}`

For a property holding a Boolean value, you can alternatively use a method prefixed with `is`, such as for the `hidden` Boolean property:

1. `- (BOOL)isHidden`
2. `{`
3. `// Extra getter logic…`
5. `return _hidden;`
6. `}`

When the property is a scalar or a structure, the default implementation of key-value coding wraps the value in an object for use on the protocol method’s interface, as described in [Representing Non-Object Values](DataTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tclkciffekqkjivcq). You do not need to do anything special to support this behavior.

### Basic Setters

To implement a setter that stores the value of a property, use a method with the capitalized name of the property prefixed by the word `set`. For the `hidden` property:

1. `- (void)setHidden:(BOOL)hidden`
2. `{`
3. `// Extra setter logic…`
5. `_hidden = hidden;`
6. `}`

> [!WARNING]
> 

When a property is a non-object type, such as the Boolean `hidden`, the protocol’s default implementation detects the underlying data type, and unwraps the object value (an `NSNumber` instance in this case) that comes from `setValue:forKey:` before applying it to your setter, as described in [Representing Non-Object Values](DataTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tclkciffekqkjivcq). You do not need to handle this in the setter itself. However, if there is a possibility that a `nil` value might be written to your non-object property, you override [setNilValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415174-setnilvalueforkey) to handle this situation, as described in [Handling Non-Object Values](HandlingNon-ObjectValues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedklktk4yq). An appropriate behavior for the `hidden` property might simply be to interpret `nil` as `NO``false`:

1. `- (void)setNilValueForKey:(NSString *)key`
2. `{`
3. `if ([key isEqualToString:@"hidden"]) {`
4. `[self setValue:@(NO) forKey:@”hidden”];`
5. `} else {`
6. `[super setNilValueForKey:key];`
7. `}`
8. `}`

You provide the above method override, if appropriate, even when you allow the compiler to synthesize the setter.

### Instance Variables

When the default implementation of one of the key-value coding accessor methods can’t find a property’s accessor, it queries its class’s [accessInstanceVariablesDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/clm/NSObject/accessInstanceVariablesDirectly) method to see if the class allows direct use of instance variables. By default, this class method returns `YES``true`, although you can override this method to return `NO``false`.

If you do allow use of ivars, ensure that they are named in the usual way, using the property name prefixed by an underscore (`_`). Normally, the compiler does this for you when automatically synthesizing properties, but if you use an explicit `@synthesize` directive, you can enforce this naming yourself:

1. `@synthesize title = _title;`

In some cases, instead of using a `@synthesize` directive or allowing the compiler to automatically synthesize a property, you use a `@dynamic` directive to inform the compiler that you will provide getters and setters at runtime. You might do this to avoid automatically synthesizing a getter, so that you can provide collection accessors instead, as described in [Defining Collection Methods](DefiningCollectionMethods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedcnznknltc). In this, case you declare the ivar yourself as part of the interface declaration:

1. `@interface MyObject : NSObject {`
2. `NSString* _title;`
3. `}`
5. `@property (nonatomic) NSString* title;`
7. `@end`

[Accessor Search Patterns](SearchImplementation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2tklkdjjbeeqsgizaq)

[Defining Collection Methods](DefiningCollectionMethods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedcnznknltc)
