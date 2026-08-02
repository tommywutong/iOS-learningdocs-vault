---
title: The Objective-C Programming Language
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocCategories.html
archived_at: '2026-07-15T07:17:29.435424Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [The Objective-C Programming Language](Introduction.md)


[Next](Associative%20References.md)[Previous](Declared%20Properties.md)

# Categories and Extensions

A _category_ allows you to add methods to an existing class—even to one for which you do not have the source. Categories are a powerful feature that allows you to extend the functionality of existing classes without subclassing. Using categories, you can also distribute the implementation of your own classes among several files. _Class extensions_ are similar, but allow additional _required_ APIs to be declared for a class in locations other than within the primary class `@interface` block.

You can add methods to a class by declaring them in an interface file under a category name and defining them in an implementation file under the same name. The category name indicates that the methods are additions to a class declared elsewhere, not a new class. You cannot, however, use a category to add additional instance variables to a class.

The methods the category adds become part of the class type. For example, methods added to the `NSArray` class in a category are included as methods the compiler expects an `NSArray` instance to have in its repertoire. Methods added to the `NSArray` class in a subclass, however, are not included in the `NSArray` type. (This matters only for statically typed objects because static typing is the only way the compiler can know an object’s class.)

Category methods can do anything that methods defined in the class proper can do. At runtime, there’s no difference. The methods the category adds to the class are inherited by all the class’s subclasses, just like other methods.

The declaration of a category interface looks very much like a class interface declaration—except the category name is listed within parentheses after the class name and the superclass isn’t mentioned. Unless its methods don’t access any instance variables of the class, the category must import the interface file for the class it extends:

```objc
#import "ClassName.h"

@interface ClassName ( CategoryName )
// method declarations
@end
```

Note that a category can’t declare additional instance variables for the class; it includes only methods. However, all instance variables within the scope of the class are also within the scope of the category. That includes all instance variables declared by the class, even ones declared `@private`.

There’s no limit to the number of categories that you can add to a class, but each category name must be different, and each should declare and define a different set of methods.

Class extensions are like anonymous categories, except that the methods they declare must be implemented in the main `@implementation` block for the corresponding class. Using the Clang/LLVM 2.0 compiler, you can also declare properties and instance variables in a class extension.

A common use for class extensions is to redeclare property that is publicly declared as read-only privately as readwrite:

```objc
@interface MyClass : NSObject
@property (retain, readonly) float value;
@end

// Private extension, typically hidden in the main implementation file.
@interface MyClass ()
@property (retain, readwrite) float value;
@end
```

Notice that (in contrast to a category) no name is given in the parentheses in the second `@interface` block.

It is also generally common for a class to have a publicly declared API and to then have additional methods declared privately for use solely by the class or the framework within which the class resides. Class extensions allow you to declare additional _required_ methods for a class in locations other than within the primary class `@interface` block, as illustrated in the following example:

```objc
@interface MyClass : NSObject
- (float)value;
@end


@interface MyClass () {
    float value;
}
- (void)setValue:(float)newValue;
@end

@implementation MyClass

- (float)value {
    return value;
}

- (void)setValue:(float)newValue {
    value = newValue;
}

@end
```

The implementation of the `setValue:` method _must_ appear within the main `@implementation` block for the class (you cannot implement it in a category). If this is not the case, the compiler emits a warning that it cannot find a method definition for `setValue:`.

[Next](Associative%20References.md)[Previous](Declared%20Properties.md)

