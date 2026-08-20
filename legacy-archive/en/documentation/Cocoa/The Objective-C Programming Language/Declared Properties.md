---
title: The Objective-C Programming Language
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocProperties.html
archived_at: '2026-07-15T07:17:31.884592Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [The Objective-C Programming Language](Introduction.md)


[Next](Categories%20and%20Extensions.md)[Previous](Protocols.md)

# Declared Properties

The Objective-C declared properties feature provides a simple way to declare and implement an object’s accessor methods.

You typically access an object’s properties (in the sense of its attributes and relationships) through a pair of accessor (getter/setter) methods. By using accessor methods, you adhere to the principle of _encapsulation_ (see [Mechanisms Of Abstraction](../Object-Oriented%20Programming%20with%20Objective-C/The%20Object%20Model.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnbzfvbuqnjnha3dgmjw) in _[Object-Oriented Programming with Objective-C](../Object-Oriented%20Programming%20with%20Objective-C/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnbz)_). You can exercise tight control of the behavior of the getter/setter pair and the underlying state management while clients of the API remain insulated from the implementation changes.

Although using accessor methods therefore has significant advantages, writing accessor methods is a tedious process. Moreover, aspects of the property that may be important to consumers of the API are left obscured—such as whether the accessor methods are thread-safe or whether new values are copied when set.

Declared properties address these issues by providing the following features:

- The property declaration provides a clear, explicit specification of how the accessor methods behave.
- The compiler can synthesize accessor methods for you, according to the specification you provide in the declaration.
- Properties are represented syntactically as identifiers and are scoped, so the compiler can detect use of undeclared properties.

There are two parts to a declared property, its declaration and its implementation.

A property declaration begins with the keyword `@property`. `@property` can appear anywhere in the method declaration list found in the `@interface` block of a class. `@property` can also appear in the declaration of a [protocol](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45) or [category](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Category.html#//apple_ref/doc/uid/TP40008195-CH5).

```objc
@property (attributes) type name;
```

The `@property` directive declares a property. An optional parenthesized set of attributes provides additional details about the storage semantics and other behaviors of the property—see [Property Declaration Attributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomq) for possible values. Like any other Objective-C type, each property has a type specification and a name.

Listing 4-1 illustrates the declaration of a simple property.

__Listing 4-1__  Declaring a simple property

```objc
@interface MyClass : NSObject
@property float value;
@end
```

You can think of a property declaration as being equivalent to declaring two accessor methods. Thus

```objc
@property float value;
```

is equivalent to:

```objc
- (float)value;
- (void)setValue:(float)newValue;
```

A property declaration, however, provides additional information about how the accessor methods are implemented (as described in [Property Declaration Attributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomq)).

You can also put property declarations in class extensions (see [Extensions](Categories%20and%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmrqfvjvomq)). For example, you could declare the `value` property shown previously as follows:

```objc
@interface MyClass : NSObject
@end

@interface MyClass ()
@property float value;
@end
```

This is useful if you want to hide the declaration of private properties.

You can decorate a property with attributes by using the form `@property(attribute [, attribute2, ...])`. Like methods, properties are scoped to their enclosing interface declaration. For property declarations that use a comma-delimited list of variable names, the property attributes apply to all of the named properties.

If you use the `@synthesize` directive to tell the compiler to create the accessor methods (see [Property Implementation Directives](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvooi)), the code it generates matches the specification given by the keywords. If you implement the accessor methods yourself, you should ensure that it matches the specification (for example, if you specify `copy` you must make sure that you do copy the input value in the setter method).

The default names for the getter and setter methods associated with a property are _propertyName_ and `set`_PropertyName_`:` respectively—for example, given a property “foo”, the accessors would be `foo` and `setFoo:`. The following attributes allow you to specify custom names instead. They are both optional and can appear with any other attribute (except for `readonly` in the case of `setter=`).

**`getter=getterName`**
: Specifies the name of the get accessor for the property. The getter must return a type matching the property’s type and take no parameters.

**`setter=setterName`**
: Specifies the name of the set accessor for the property. The setter method must take a single parameter of a type matching the property’s type and must return `void`.

If you specify that a property is `readonly` and also specify a setter with `setter=`, you get a compiler warning.

Typically you should specify accessor method names that are key-value coding compliant (see _[Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)_)—a common reason for using the `getter` decorator is to adhere to the `is`_PropertyName_ convention for Boolean values.

These attributes specify whether or not a property has an associated set accessor. They are mutually exclusive.

**`readwrite`**
: Indicates that the property should be treated as read/write. This attribute is the default.

Both a getter and setter method are required in the `@implementation` block. If you use the `@synthesize` directive in the implementation block, the getter and setter methods are synthesized.

**`readonly`**
: Indicates that the property is read-only.

If you specify `readonly`, only a getter method is required in the `@implementation` block. If you use the `@synthesize` directive in the implementation block, only the getter method is synthesized. Moreover, if you attempt to assign a value using the dot syntax, you get a compiler error.

These attributes specify the semantics of a set accessor. They are mutually exclusive.

**`strong`**
: Specifies that there is a strong (owning) relationship to the destination object.

**`weak`**
: Specifies that there is a weak (non-owning) relationship to the destination object.

If the destination object is deallocated, the property value is automatically set to `nil`.

(Weak properties are not supported on OS X v10.6 and iOS 4; use `assign` instead.)

**`copy`**
: Specifies that a copy of the object should be used for assignment.

The previous value is sent a [release](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/release) message.

The copy is made by invoking the [copy](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/copy) method. This attribute is valid only for object types, which must implement the `NSCopying`  [protocol](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45).

**`assign`**
: Specifies that the setter uses simple assignment. This attribute is the default.

You use this attribute for scalar types such as `NSInteger` and `CGRect`.

**`retain`**
: Specifies that [retain](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/retain) should be invoked on the object upon assignment.

The previous value is sent a [release](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/release) message.

In OS X v10.6 and later, you can use the `__attribute__` keyword to specify that a Core Foundation property should be treated like an Objective-C object for memory management:

```objc
@property(retain) __attribute__((NSObject)) CFDictionaryRef myDictionary;
```


You can use this attribute to specify that accessor methods are not atomic.

**`nonatomic`**
: Specifies that accessors are nonatomic. _By default, accessors are atomic._

Properties are `atomic` by default so that synthesized accessors provide robust access to properties in a multithreaded environment—that is, the value returned from the getter or set via the setter is always fully retrieved or set regardless of what other threads are executing concurrently.

If you specify `strong`, `copy`, or `retain` and do not specify `nonatomic`, then in a reference-counted environment, a synthesized get accessor for an object property uses a lock and retains and autoreleases the returned value—the implementation will be similar to the following:

```
[_internal lock]; // lock using an object-level lock
id result = [[value retain] autorelease];
[_internal unlock];
return result;
```

If you specify `nonatomic`, a synthesized accessor for an object property simply returns the value directly.

Properties support the full range of C-style decorators. Properties can be deprecated and support `__attribute__` style markup:

```objc
@property CGFloat x
AVAILABLE_MAC_OS_X_VERSION_10_1_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_4;
@property CGFloat y __attribute__((...));
```

If you want to specify that a property is an outlet (see [outlet](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Outlet.html#//apple_ref/doc/uid/TP40009071-CH4) in iOS, and [outlet](https://developer.apple.com/library/archive/documentation/General/Devpedia-CocoaApp-MOSX/Outlet.html#//apple_ref/doc/uid/TP40009448-CH4) in OS X), you use the `IBOutlet` identifier:

```objc
@property (nonatomic, weak) IBOutlet NSButton *myButton;
```

`IBOutlet` is not, though, a formal part of the list of attributes. For more about declaring outlet properties, see [Nib Files](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/CocoaNibs/CocoaNibs.html#//apple_ref/doc/uid/10000051i-CH4).

You can use the `@synthesize` and `@dynamic` directives in `@implementation` blocks to trigger specific compiler actions. Note that neither is _required_ for any given `@property` declaration.

**`@synthesize`**
: You use the `@synthesize` directive to tell the compiler that it should synthesize the setter and/or getter methods for a property if you do not supply them within the `@implementation` block. The `@synthesize` directive also synthesizes an appropriate instance variable if it is not otherwise declared.

__Listing 4-2__  Using @synthesize

```objc
@interface MyClass : NSObject
@property(copy, readwrite) NSString *value;
@end

@implementation MyClass
@synthesize value;
@end
```

You can use the form `property=ivar` to indicate that a particular instance variable should be used for the property, for example:

```objc
@synthesize firstName, lastName, age=yearsOld;
```

This specifies that the accessor methods for `firstName`, `lastName`, and `age` should be synthesized and that the property `age` is represented by the instance variable `yearsOld`. Other aspects of the synthesized methods are determined by the optional attributes (see [Property Declaration Attributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomq)).

Whether or not you specify the name of the instance variable, the `@synthesize` directive can use an instance variable only from the current class, not a superclass.

There are differences in the behavior of accessor synthesis that depend on the runtime (see also [Runtime Difference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomy)):

- For the legacy runtimes, instance variables must already be declared in the `@interface` block of the current class. If an instance variable of the same name as the property exists, and if its type is compatible with the property’s type, it is used—otherwise, you get a compiler error.
- For the modern runtimes (see [Runtime Versions and Platforms](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtVersionsPlatforms.html#//apple_ref/doc/uid/TP40008048-CH106) in _[Objective-C Runtime Programming Guide](../Objective-C%20Runtime%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danby)_), instance variables are synthesized as needed. If an instance variable of the same name already exists, it is used.

**`@dynamic`**
: You use the `@dynamic` keyword to tell the compiler that you will fulfill the API contract implied by a property either by providing method implementations directly or at runtime using other mechanisms such as dynamic loading of code or dynamic method resolution. It suppresses the warnings that the compiler would otherwise generate if it can’t find suitable implementations. You should use it only if you know that the methods will be available at runtime.

The example shown in Listing 4-3 illustrates using `@dynamic` with a subclass of [NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject).

__Listing 4-3__  Using @dynamic with NSManagedObject

```objc
@interface MyClass : NSManagedObject
@property(nonatomic, retain) NSString *value;
@end

@implementation MyClass
@dynamic value;
@end
```

`NSManagedObject` is provided by the Core Data framework. A managed object class has a corresponding schema that defines attributes and relationships for the class; at runtime, the Core Data framework generates accessor methods for these as necessary. You therefore typically declare properties for the attributes and relationships, but you don’t have to implement the accessor methods yourself and shouldn’t ask the compiler to do so. If you just declared the property without providing any implementation, however, the compiler would generate a warning. Using `@dynamic` suppresses the warning.

You can declare a property for any Objective-C class, Core Foundation data type, or “plain old data” (POD) type (see [C++ Language Note: POD Types](http://www.fnal.gov/docs/working-groups/fpcltf/Pkg/ISOcxx/doc/POD.html)). For constraints on using Core Foundation types, however, see [Core Foundation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomjq).

You can redeclare a property in a subclass, but (with the exception of `readonly` versus `readwrite`) you must repeat its attributes in whole in the subclasses. The same holds true for a property declared in a [category](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Category.html#//apple_ref/doc/uid/TP40008195-CH5) or [protocol](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45)—while the property may be redeclared in a category or protocol, the property’s attributes must be repeated in whole.

If you declare a property in one class as `readonly`, you can redeclare it as `readwrite` in a class extension (see [Extensions](Categories%20and%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmrqfvjvomq)), in a protocol, or in a subclass (see [Subclassing with Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvona)). In the case of a class extension redeclaration, the fact that the property was redeclared prior to any `@synthesize` statement causes the setter to be synthesized. The ability to redeclare a read-only property as read/write enables two common implementation patterns: a mutable subclass of an immutable class (`NSString`, `NSArray`, and `NSDictionary` are all examples) and a property that has a public API that is `readonly` but a private `readwrite` implementation internal to the class. The following example shows using a class extension to provide a property that is declared as read-only in the public header but is redeclared privately as read/write.

```objc
// public header file
@interface MyObject : NSObject
@property (readonly, copy) NSString *language;
@end

// private implementation file
@interface MyObject ()
@property (readwrite, copy) NSString *language;
@end

@implementation MyObject
@synthesize language;
@end
```


As noted in [Property Declaration Attributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomq), prior to OS X v10.6 you cannot specify the `retain` attribute for non-object types. If, therefore, you declare a property whose type is a CFType and synthesize the accessors as illustrated in the following example:

```objc
@interface MyClass : NSObject
@property(readwrite) CGImageRef myImage;
@end

@implementation MyClass
@synthesize myImage;
@end
```

then in a reference-counted environment, the synthesized set accessor simply assigns the new value to the instance variable (the new value is not retained and the old value is not released). Simple assignment is typically incorrect for Core Foundation objects; you should not synthesize the methods but rather implement them yourself.

You can override a `readonly` property to make it writable. For example, you could define a class `MyInteger` with a `readonly` property, `value`:

```objc
@interface MyInteger : NSObject
@property(readonly) NSInteger value;
@end

@implementation MyInteger
@synthesize value;
@end
```

You could then implement a subclass, `MyMutableInteger`, which redefines the property to make it writable:

```objc
@interface MyMutableInteger : MyInteger
@property(readwrite) NSInteger value;
@end

@implementation MyMutableInteger
@dynamic value;

- (void)setValue:(NSInteger)newX {
    value = newX;
}
@end
```


In general the behavior of properties is identical on both modern and legacy runtimes (see [Runtime Versions and Platforms](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtVersionsPlatforms.html#//apple_ref/doc/uid/TP40008048-CH106) in _[Objective-C Runtime Programming Guide](../Objective-C%20Runtime%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danby)_). There is one key difference: the modern runtime supports instance variable synthesis whereas the legacy runtime does not.

For `@synthesize` to work in the legacy runtime, you must either provide an instance variable with the same name and compatible type of the property or specify another existing instance variable in the `@synthesize` statement. With the modern runtime, if you do not provide an instance variable, the compiler adds one for you. For example, given the following class declaration and implementation:

```objc
@interface MyClass : NSObject
@property float noDeclaredIvar;
@end

@implementation MyClass
@synthesize noDeclaredIvar;
@end
```

the compiler for the legacy runtime would generate an error at `@synthesize noDeclaredIvar;` whereas the compiler for the modern runtime would add an instance variable to represent `noDeclaredIvar`.

[Next](Categories%20and%20Extensions.md)[Previous](Protocols.md)

