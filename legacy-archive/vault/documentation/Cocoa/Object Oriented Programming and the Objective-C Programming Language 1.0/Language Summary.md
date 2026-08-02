---
title: Object Oriented Programming and the Objective-C Programming Language 1.0
apple_id: TP40005191
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OOPandObjC1/Articles/ocLanguageSummary.html
archived_at: '2026-07-15T07:17:25.015131Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Object Oriented Programming and the Objective-C Programming Language 1.0](Introduction%20to%20The%20Objective-C%20Programming%20Language%201.0.md)


[Next](Grammar.md)[Previous](The%20Runtime%20System.md)

# Language Summary

Objective-C adds a small number of constructs to the C language and defines a handful of conventions for effectively interacting with the runtime system. This appendix lists all the additions to the language but doesn’t go into great detail. For more information, see [The Language](The%20Language.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznijauuq2kifbei). For a more formal presentation of Objective-C syntax, see [Grammar](Grammar.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnbnijbusq2gi5eui).

Message expressions are enclosed in square brackets:

```
[receiver message]
```

The receiver can be:

- A variable or expression that evaluates to an object (including the variable `self`)
- A class name (indicating the class object)
- `super` (indicating an alternative search for the method implementation)

The _message_ is the name of a method plus any arguments passed to it.

The principal types used in Objective-C are defined in `objc/objc.h`. They are:

| Type | Definition |
| --- | --- |
| `id` | An object (a pointer to its data structure). |
| `Class` | A class object (a pointer to the class data structure). |
| `SEL` | A selector, a compiler-assigned code that identifies a method name. |
| `IMP` | A pointer to a method implementation that returns an `id`. |
| `BOOL` | A Boolean value, either `YES` or `NO`. |

`id` can be used to type any kind of object, class, or instance. In addition, class names can be used as type names to statically type instances of a class. A statically typed instance is declared to be a pointer to its class or to any class it inherits from.

The `objc.h` header file also defines these useful terms:

| Type | Definition |
| --- | --- |
| `nil` | A null object pointer, `(id)0`. |
| `Nil` | A null class pointer, `(Class)0`. |
| `NO` | A boolean false value, `(BOOL)0`. |
| `YES` | A boolean true value, `(BOOL)1`. |

The preprocessor understands these special notations:

| Notation | Definition |
| --- | --- |
| `#import` | Imports a header file. This directive is identical to `#include`, except that it doesn’t include the same file more than once. |
| `//` | Begins a comment that continues to the end of the line. |

Directives to the compiler begin with “@”. The following directives are used to declare and define classes, categories, and protocols:

| Directive | Definition |
| --- | --- |
| `@interface` | Begins the declaration of a class or category interface. |
| `@implementation` | Begins the definition of a class or category. |
| `@protocol` | Begins the declaration of a formal protocol. |
| `@end` | Ends the declaration/definition of a class, category, or protocol. |

The following mutually exclusive directives specify the visibility of instance variables:

| Directive | Definition |
| --- | --- |
| `@private` | Limits the scope of an instance variable to the class that declares it. |
| `@protected` | Limits instance variable scope to declaring and inheriting classes. |
| `@public` | Removes restrictions on the scope of instance variables. |

The default is `@protected`.

These directives support exception handling:

| Directive | Definition |
| --- | --- |
| `@try` | Defines a block within which exceptions can be thrown. |
| `@throw` | Throws an exception object. |
| `@catch()` | Catches an exception thrown within the preceding `@try` block. |
| `@finally` | Defines a block of code that is executed whether exceptions were thrown or not in a preceding `@try` block. |

In addition, there are directives for these particular purposes:

| Directive | Definition |
| --- | --- |
| `@class` | Declares the names of classes defined elsewhere. |
| `@selector``(method_name)` | Returns the compiled selector that identifies _method_name_. |
| `@protocol``(protocol_name)` | Returns the _protocol_name_ protocol (an instance of the Protocol class). (`@protocol` is also valid without (_protocol_name_) for forward declarations.) |
| `@encode``(type_spec)` | Yields a character string that encodes the type structure of _type_spec_. |
| `@defs``(class_name)` | Yields the internal data structure of _class_name_ instances |
| `@"string"` | Defines a constant `NSString` object in the current module and initializes the object with the specified 7-bit ASCII-encoded string. |
| `@"string1" @"string2" ... @"stringN"` | Defines a constant `NSString` object in the current module. The string created is the result of concatenating the strings specified in the two directives. |
| `@synchronized()` | Defines a block of code that must be executed only by one thread at a time. |

A new class is declared with the `@interface` directive. The interface file for its superclass must be imported:

```objc
#import "ItsSuperclass.h"

@interface ClassName : ItsSuperclass < protocol_list >
{
    instance variable declarations
}
method declarations
@end
```

Everything but the compiler directives and class name is optional. If the colon and superclass name are omitted, the class is declared to be a new root class. If any protocols are listed, the header files where they’re declared must also be imported.

A file containing a class definition imports its own interface:

```objc
#import “ClassName.h”

@implementation ClassName
method definitions
@end
```


A category is declared in much the same way as a class. The interface file that declares the class must be imported:

```objc
#import "ClassName.h"

@interface ClassName ( CategoryName ) < protocol list >
method declarations
@end
```

The protocol list and method declarations are optional. If any protocols are listed, the header files where they’re declared must also be imported.

Like a class definition, a file containing a category definition imports its own interface:

```objc
#import "CategoryName.h"

@implementation ClassName ( CategoryName )
method definitions
@end
```


Formal protocols are declared using the `@protocol` directive:

```objc
@protocol ProtocolName < protocol list >
method declarations
@end
```

The list of incorporated protocols and the method declarations are optional. The protocol must import the header files that declare any protocols it incorporates.

You can create a forward reference to a protocol using the `@protocol` directive in the following manner:

```objc
@protocol ProtocolName;
```

Within source code, protocols are referred to using the similar `@protocol()` directive, where the parentheses enclose the protocol name.

Protocol names listed within angle brackets (<...>) are used to do three different things:

- In a protocol declaration, to incorporate other protocols (as shown earlier)
- In a class or category declaration, to adopt the protocol (as shown in [Classes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqmznha3denbr) and [Categories](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqmznha3dgnjq))
- In a type specification, to limit the type to objects that conform to the protocol

Within protocol declarations, these type qualifiers support remote messaging:

| Type Qualifier | Definition |
| --- | --- |
| `oneway` | The method is for asynchronous messages and has no valid return type. |
| `in` | The argument passes information to the remote receiver. |
| `out` | The argument gets information returned by reference. |
| `inout` | The argument both passes information and gets information. |
| `bycopy` | A copy of the object, not a proxy, should be passed or returned. |
| `byref` | A reference to the object, not a copy, should be passed or returned. |

The following conventions are used in method declarations:

- A “+” precedes declarations of class methods.
- A “-” precedes declarations of instance methods.
- Argument and return types are declared using the C syntax for type casting.
- Arguments are declared after colons (:), for example:

```objc
- (void)setWidth:(int)newWidth height:(int)newHeight
```

  Typically, a label describing the argument precedes the colon—the following example is valid but is considered bad style:

```objc
- (void)setWidthAndHeight:(int)newWidth :(int)newHeight
```

  Both labels and colons are considered part of the method name.
- The default return and argument type for methods is `id`, not `int` as it is for functions. (However, the modifier `unsigned` when used without a following type always means `unsigned int`.)

Each method implementation is passed two hidden arguments:

- The receiving object (`self`).
- The selector for the method (`_cmd`).

Within the implementation, both `self` and `super` refer to the receiving object. `super` replaces `self` as the receiver of a message to indicate that only methods inherited by the implementation should be performed in response to the message.

Methods with no other valid return typically return `void`.

The names of files that contain Objective-C source code have the `.m` extension. Files that declare class and category interfaces or that declare protocols have the `.h` extension typical of header files.

Class, category, and protocol names generally begin with an uppercase letter; the names of methods and instance variables typically begin with a lowercase letter. The names of variables that hold instances usually also begin with lowercase letters.

In Objective-C, identical names that serve different purposes don’t clash. Within a class, names can be freely assigned:

- A class can declare methods with the same names as methods in other classes.
- A class can declare instance variables with the same names as variables in other classes.
- An instance method can have the same name as a class method.
- A method can have the same name as an instance variable.
- Method names beginning with “_”, a single underscore character, are reserved for use by Apple.

Likewise, protocols and categories of the same class have protected name spaces:

- A protocol can have the same name as a class, a category, or anything else.
- A category of one class can have the same name as a category of another class.

However, class names are in the same name space as global variables and defined types. A program can’t have a global variable with the same name as a class.

[Next](Grammar.md)[Previous](The%20Runtime%20System.md)

