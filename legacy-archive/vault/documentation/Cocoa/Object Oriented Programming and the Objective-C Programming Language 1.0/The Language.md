---
title: Object Oriented Programming and the Objective-C Programming Language 1.0
apple_id: TP40005191
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OOPandObjC1/Articles/ocLanguage.html
archived_at: '2026-07-15T07:17:21.897362Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Object Oriented Programming and the Objective-C Programming Language 1.0](Introduction%20to%20The%20Objective-C%20Programming%20Language%201.0.md)


[Next](The%20Runtime%20System.md)[Previous](Introduction%20to%20The%20Objective-C%20Programming%20Language%201.0.md)

# The Language

This chapter describes the Objective-C language and discusses the principles of object-oriented programming as they’re implemented in Objective-C. It covers all the features that the language adds to standard C and C++.

Because object-oriented programs postpone many decisions from compile time to runtime, object-oriented languages depend on a runtime system for executing the compiled code. The runtime system for the Objective-C language is discussed in [The Runtime System](The%20Runtime%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqojninfeeqscineeo). This chapter presents the language, but touches on important elements of the runtime system.

The Apple compilers are based on the compilers of the GNU Compiler Collection. Objective-C syntax is a superset of GNU C/C++ syntax, and the Objective-C compiler works for C, C++ and Objective-C source code. The compiler recognizes Objective-C source files by the filename extension `.m`, just as it recognizes files containing only standard C syntax by filename extension `.c`. Similarly, the compiler recognizes C++ files that use Objective-C by the extension `.mm`. Other issues when using Objective-C with C++ are covered in the section [Using C++ With Objective-C](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnzngeytombrgu).

As the name implies, object-oriented programs are built around _objects_. An object associates data with the particular operations that can use or affect that data. In Objective-C, these operations are known as the object’s _methods_; the data they affect are its _instance variables_. In essence, an object bundles a data structure (instance variables) and a group of procedures (methods) into a self-contained programming unit.

For example, if you are writing a drawing program that allows a user to create images composed of lines, circles, rectangles, text, bit-mapped images, and so forth, you might create classes for many of the basic shapes that a user can manipulate. A Rectangle object, for instance, might have instance variables that identify the position of the rectangle within the drawing along with its width and its height. Other instance variables could define the rectangle’s color, whether or not it is to be filled, and a line pattern that should be used to display the rectangle. A Rectangle class would have methods to set an instance’s position, size, color, fill status, and line pattern, along with a method that causes the instance to display itself.

In Objective-C, an object’s instance variables are internal to the object; generally, you get access to an object’s state only through the object’s methods (you can specify whether subclasses or other objects can access instance variables directly by using scope directives, see [The Scope of Instance Variables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznha4dinry)). For others to find out something about an object, there has to be a method to supply the information. For example, a Rectangle would have methods that reveal its size and its position.

Moreover, an object sees only the methods that were designed for it; it can’t mistakenly perform methods intended for other types of objects. Just as a C function protects its local variables, hiding them from the rest of the program, an object hides both its instance variables and its method implementations.

In Objective-C, object identifiers are a distinct data type: `id`. This type is defined as a pointer to an object—in reality, a pointer to the instance variables of the object, the object’s unique data. Like a C function or an array, an object is identified by its address. All objects, regardless of their instance variables or methods, are of type `id`.

```
id anObject;
```

For the object-oriented constructs of Objective-C, such as method return values, `id` replaces `int` as the default data type. (For strictly C constructs, such as function return values, `int` remains the default type.)

The keyword `nil` is defined as a null object, an `id` with a value of `0`. `id`, `nil`, and the other basic types of Objective-C are defined in the header file `objc/objc.h`.

The `id` type is completely nonrestrictive. By itself, it yields no information about an object, except that it is an object.

But objects aren’t all the same. A Rectangle won’t have the same methods or instance variables as an object that represents a bit-mapped image. At some point, a program needs to find more specific information about the objects it contains—what the object’s instance variables are, what methods it can perform, and so on. Since the `id` type designator can’t supply this information to the compiler, each object has to be able to supply it at runtime.

This is possible because every object carries with it an `isa` instance variable that identifies the object’s _class_—what kind of object it is. Every Rectangle object would be able to tell the runtime system that it is a Rectangle. Every Circle can say that it is a Circle. Objects with the same behavior (methods) and the same kinds of data (instance variables) are members of the same class.

Objects are thus _dynamically typed_ at runtime. Whenever it needs to, the runtime system can find the exact class that an object belongs to, just by asking the object. Dynamic typing in Objective-C serves as the foundation for dynamic binding, discussed later.

The `isa` pointer also enables objects to perform _introspection_—to find out about themselves (or other objects). The compiler records information about class definitions in data structures for the runtime system to use. The functions of the runtime system use `isa`, to find this information at runtime. Using the runtime system, you can, for example, determine whether an object implements a particular method, or discover the name of its superclass.

Object classes are discussed in more detail under [Classes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznha3dgmrz).

It’s also possible to give the compiler information about the class of an object by statically typing it in source code using the class name. Classes are particular kinds of objects, and the class name can serve as a type name. See [Class Types](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznha3dmmzs) and [Enabling Static Behaviors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznheztgojy).

This section explains the syntax of sending messages, including how you can nest message expressions. It also discusses the “visibility” of an object’s instance variables, and the concepts of polymorphism and dynamic binding.

To get an object to do something, you send it a _message_ telling it to apply a method. In Objective-C, _message expressions_ are enclosed in brackets:

```
[receiver message]
```

The receiver is an object, and the message tells it what to do. In source code, the message is simply the name of a method and any arguments that are passed to it. When a message is sent, the runtime system selects the appropriate method from the receiver’s repertoire and invokes it.

For example, this message tells the `myRect` object to perform its `display` method, which causes the rectangle to display itself:

```
[myRect display];
```

Methods can also take arguments. The imaginary message below tells `myRect` to set its location within the window to coordinates (30.0, 50.0):

```
[myRect setOrigin:30.0 :50.0];
```

Here the method name, `setOrigin::`, has two colons, one for each of its arguments. The arguments are inserted after the colons. This method name uses unlabeled arguments. Unlabeled arguments make it difficult to determine the kind and purpose of a method’s arguments. Instead, method names should include labels describing each of their arguments. Argument labels precede each colon in the method name. The `setWidth:height:` method, for example, makes the purpose of its two arguments clear:

```
[myRect setWidth:10.0 height:15.0];
```

Methods that take a variable number of arguments are also possible, though they’re somewhat rare. Extra arguments are separated by commas after the end of the method name. (Unlike colons, the commas aren’t considered part of the name.) In the following example, the imaginary `makeGroup:` method is passed one required argument (_group_) and three that are optional:

```
[receiver makeGroup:group, memberOne, memberTwo, memberThree];
```

Like standard C functions, methods can return values. The following example sets the variable `isFilled` to `YES` if `myRect` is drawn as a solid rectangle, or `NO` if it’s drawn in outline form only.

```
BOOL isFilled;
isFilled = [myRect isFilled];
```

Note that a variable and a method can have the same name.

One message expression can be nested inside another. Here, the color of one rectangle is set to the color of another:

```
[myRect setPrimaryColor:[otherRect primaryColor]];
```

A message to `nil` also is valid, as long as the message returns an object, any pointer type, `void`, or any integer scalar of size less than or equal to `sizeof(void*)`; if it does, a message sent to `nil` returns `nil`. If the message sent to `nil` returns anything other than the aforementioned value types (for example, if it returns any struct type, any floating-point type, or any vector type) the return value is undefined. You should therefore not rely on the return value of messages sent to `nil` unless the method’s return type is an object, any pointer type, or any integer scalar of size less than or equal to `sizeof(void*)`:

```
id anObject = nil;

// this is valid
if ([anObject methodThatReturnsAnInt] == nil) {
    // implementation continues...
}

// this is not valid
if ([anObject methodThatReturnsAFloat] == nil) {
    // implementation continues...
}
```


A method has automatic access to the receiving object’s instance variables. You don’t need to pass them to the method as arguments. For example, the `primaryColor` method illustrated above takes no arguments, yet it can find the primary color for `otherRect` and return it. Every method assumes the receiver and its instance variables, without having to declare them as arguments.

This convention simplifies Objective-C source code. It also supports the way object-oriented programmers think about objects and messages. Messages are sent to receivers much as letters are delivered to your home. Message arguments bring information from the outside to the receiver; they don’t need to bring the receiver to itself.

A method has automatic access only to the receiver’s instance variables. If it requires information about a variable stored in another object, it must send a message to the object asking it to reveal the contents of the variable. The `primaryColor` and `isFilled` methods shown above are used for just this purpose.

See [Defining a Class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnzngeztsmjzgi) for more information on referring to instance variables.

As the examples above illustrate, messages in Objective-C appear in the same syntactic positions as function calls in standard C. But, because methods “belong to” an object, messages behave differently than function calls.

In particular, an object can be operated on by only those methods that were defined for it. It can’t confuse them with methods defined for other kinds of objects, even if another object has a method with the same name. This means that two objects can respond differently to the same message. For example, each kind of object sent a `display` message could display itself in a unique way. A Circle and a Rectangle would respond differently to identical instructions to track the cursor.

This feature, referred to as _polymorphism_, plays a significant role in the design of object-oriented programs. Together with dynamic binding, it permits you to write code that might apply to any number of different kinds of objects, without you having to choose at the time you write the code what kinds of objects they might be. They might even be objects that will be developed later, by other programmers working on other projects. If you write code that sends a `display` message to an `id` variable, any object that has a `display` method is a potential receiver.

A crucial difference between function calls and messages is that a function and its arguments are joined together in the compiled code, but a message and a receiving object aren’t united until the program is running and the message is sent. Therefore, the exact method that’s invoked to respond to a message can only be determined at runtime, not when the code is compiled.

The precise method that a message invokes depends on the receiver. Different receivers may have different method implementations for the same method name (polymorphism). For the compiler to find the right method implementation for a message, it would have to know what kind of object the receiver is—what class it belongs to. This is information the receiver is able to reveal at runtime when it receives a message (dynamic typing), but it’s not available from the type declarations found in source code.

The selection of a method implementation happens at runtime. When a message is sent, a runtime messaging routine looks at the receiver and at the method named in the message. It locates the receiver’s implementation of a method matching the name, “calls” the method, and passes it a pointer to the receiver’s instance variables. (For more on this routine, see [How Messaging Works](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznha4dqnbw).)

The method name in a message thus serves to “select” a method implementation. For this reason, method names in messages are often referred to as _selectors_.

This _dynamic binding_ of methods to messages works hand-in-hand with polymorphism to give object-oriented programming much of its flexibility and power. Since each object can have its own version of a method, a program can achieve a variety of results, not by varying the message itself, but by varying just the object that receives the message. This can be done as the program runs; receivers can be decided “on the fly” and can be made dependent on external factors such as user actions.

When executing code based upon the Application Kit, for example, users determine which objects receive messages from menu commands like Cut, Copy, and Paste. The message goes to whatever object controls the current selection. An object that displays text would react to a `copy` message differently from an object that displays scanned images. An object that represents a set of shapes would respond differently from a Rectangle. Since messages don’t select methods (methods aren’t bound to messages) until runtime, these differences are isolated in the methods that respond to the message. The code that sends the message doesn’t have to be concerned with them; it doesn’t even have to enumerate the possibilities. Each application can invent its own objects that respond in their own way to `copy` messages.

Objective-C takes dynamic binding one step further and allows even the message that’s sent (the method selector) to be a variable that’s determined at runtime. This is discussed in the section [How Messaging Works](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznha4dqnbw).

An object-oriented program is typically built from a variety of objects. A program based on the Cocoa frameworks might use `NSMatrix` objects, `NSWindow` objects, `NSDictionary` objects, `NSFont` objects, `NSText` objects, and many others. Programs often use more than one object of the same kind or class—several `NSArray` objects or `NSWindow` objects, for example.

In Objective-C, you define objects by defining their class. The class definition is a prototype for a kind of object; it declares the instance variables that become part of every member of the class, and it defines a set of methods that all objects in the class can use.

The compiler creates just one accessible object for each class, a _class object_ that knows how to build new objects belonging to the class. (For this reason it’s traditionally called a “factory object.”) The class object is the compiled version of the class; the objects it builds are _instances_ of the class. The objects that do the main work of your program are instances created by the class object at runtime.

All instances of a class have the same set of methods, and they all have a set of instance variables cut from the same mold. Each object gets its own instance variables, but the methods are shared.

By convention, class names begin with an uppercase letter (such as “Rectangle”); the names of instances typically begin with a lowercase letter (such as “myRect”).

Class definitions are additive; each new class that you define is based on another class from which it _inherits_ methods and instance variables. The new class simply adds to or modifies what it inherits. It doesn’t need to duplicate inherited code.

Inheritance links all classes together in a hierarchical tree with a single class at its root. When writing code that is based upon the Foundation framework, that root class is typically `NSObject`. Every class (except a root class) has a _superclass_ one step nearer the root, and any class (including a root class) can be the superclass for any number of _subclasses_ one step farther from the root. Figure 1-1 illustrates the hierarchy for a few of the classes used in the drawing program.

__Figure 1-1__  Some Drawing Program Classes

!

This figure shows that the Square class is a subclass of the Rectangle class, the Rectangle class is a subclass of Shape, Shape is a subclass of Graphic, and Graphic is a subclass of `NSObject`. Inheritance is cumulative. So a Square object has the methods and instance variables defined for Rectangle, Shape, Graphic, and `NSObject`, as well as those defined specifically for Square. This is simply to say that a Square object isn’t only a Square, it’s also a Rectangle, a Shape, a Graphic, and an `NSObject`.

Every class but `NSObject` can thus be seen as a specialization or an adaptation of another class. Each successive subclass further modifies the cumulative total of what’s inherited. The Square class defines only the minimum needed to turn a Rectangle into a Square.

When you define a class, you link it to the hierarchy by declaring its superclass; every class you create must be the subclass of another class (unless you define a new root class). Plenty of potential superclasses are available. Cocoa includes the `NSObject` class and several frameworks containing definitions for more than 250 additional classes. Some are classes that you can use “off the shelf”—incorporate into your program as is. Others you might want to adapt to your own needs by defining a subclass.

Some framework classes define almost everything you need, but leave some specifics to be implemented in a subclass. You can thus create very sophisticated objects by writing only a small amount of code, and reusing work done by the programmers of the framework.

`NSObject` is a root class, and so doesn’t have a superclass. It defines the basic framework for Objective-C objects and object interactions. It imparts to the classes and instances of classes that inherit from it the ability to behave as objects and cooperate with the runtime system.

A class that doesn’t need to inherit any special behavior from another class should nevertheless be made a subclass of the `NSObject` class. Instances of the class must at least have the ability to behave like Objective-C objects at runtime. Inheriting this ability from the `NSObject` class is much simpler and much more reliable than reinventing it in a new class definition.

When a class object creates a new instance, the new object contains not only the instance variables that were defined for its class but also the instance variables defined for its superclass and for its superclass’s superclass, all the way back to the root class. Thus, the `isa` instance variable defined in the `NSObject` class becomes part of every object. `isa` connects each object to its class.

Figure 1-2 shows some of the instance variables that could be defined for a particular implementation of Rectangle, and where they may come from. Note that the variables that make the object a Rectangle are added to the ones that make it a Shape, and the ones that make it a Shape are added to the ones that make it a Graphic, and so on.

__Figure 1-2__  Rectangle Instance Variables

!

A class doesn’t have to declare instance variables. It can simply define new methods and rely on the instance variables it inherits, if it needs any instance variables at all. For example, Square might not declare any new instance variables of its own.

An object has access not only to the methods defined for its class, but also to methods defined for its superclass, and for its superclass’s superclass, all the way back to the root of the hierarchy. For instance, a Square object can use methods defined in the Rectangle, Shape, Graphic, and `NSObject` classes as well as methods defined in its own class.

Any new class you define in your program can therefore make use of the code written for all the classes above it in the hierarchy. This type of inheritance is a major benefit of object-oriented programming. When you use one of the object-oriented frameworks provided by Cocoa, your programs can take advantage of the basic functionality coded into the framework classes. You have to add only the code that customizes the standard functionality to your application.

Class objects also inherit from the classes above them in the hierarchy. But because they don’t have instance variables (only instances do), they inherit only methods.

There’s one useful exception to inheritance: When you define a new class, you can implement a new method with the same name as one defined in a class farther up the hierarchy. The new method overrides the original; instances of the new class perform it rather than the original, and subclasses of the new class inherit it rather than the original.

For example, Graphic defines a `display` method that Rectangle overrides by defining its own version of `display`. The Graphic method is available to all kinds of objects that inherit from the Graphic class—but not to Rectangle objects, which instead perform the Rectangle version of `display`.

Although overriding a method blocks the original version from being inherited, other methods defined in the new class can skip over the redefined method and find the original (see [Messages to self and super](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznha4tmnrq) to learn how).

A redefined method can also incorporate the very method it overrides. When it does, the new method serves only to refine or modify the method it overrides, rather than replace it outright. When several classes in the hierarchy define the same method, but each new version incorporates the version it overrides, the implementation of the method is effectively spread over all the classes.

Although a subclass can override inherited methods, it can’t override inherited instance variables. Since an object has memory allocated for every instance variable it inherits, you can’t override an inherited variable by declaring a new one with the same name. If you try, the compiler will complain.

Some classes are designed only so that other classes can inherit from them. These _abstract classes_ group methods and instance variables that can be used by a number of different subclasses into a common definition. The abstract class is incomplete by itself, but contains useful code that reduces the implementation burden of its subclasses.

The `NSObject` class is the prime example of an abstract class. Although programs often define `NSObject` subclasses and use instances belonging to the subclasses, they never use instances belonging directly to the `NSObject` class. An `NSObject` instance wouldn’t be good for anything; it would be a generic object with the ability to do nothing in particular.

Abstract classes often contain code that helps define the structure of an application. When you create subclasses of these classes, instances of your new classes fit effortlessly into the application structure and work automatically with other objects.

(Because abstract classes must have subclasses to be useful, they’re sometimes also called _abstract superclasses_.)

A class definition is a specification for a kind of object. The class, in effect, defines a data type. The type is based not just on the data structure the class defines (instance variables), but also on the behavior included in the definition (methods).

A class name can appear in source code wherever a type specifier is permitted in C—for example, as an argument to the `sizeof` operator:

```
int i = sizeof(Rectangle);
```


You can use a class name in place of `id` to designate an object’s type:

```
Rectangle *myRect;
```

Because this way of declaring an object type gives the compiler information about the kind of object it is, it’s known as _static typing_. Just as `id` is defined as a pointer to an object, objects are statically typed as pointers to a class. Objects are always typed by a pointer. Static typing makes the pointer explicit; `id` hides it.

Static typing permits the compiler to do some type checking—for example, to warn if an object could receive a message that it appears not to be able to respond to—and to loosen some restrictions that apply to objects generically typed `id`. In addition, it can make your intentions clearer to others who read your source code. However, it doesn’t defeat dynamic binding or alter the dynamic determination of a receiver’s class at runtime.

An object can be statically typed to its own class or to any class that it inherits from. For example, since inheritance makes a Rectangle a kind of Graphic, a Rectangle instance could be statically typed to the Graphic class:

```
Graphic *myRect;
```

This is possible because a Rectangle is a Graphic. It’s more than a Graphic since it also has the instance variables and method capabilities of a Shape and a Rectangle, but it’s a Graphic nonetheless. For purposes of type checking, the compiler considers `myRect` to be a Graphic, but at runtime it’s treated as a Rectangle.

See [Enabling Static Behaviors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznheztgojy) in the next chapter for more on static typing and its benefits.

Instances can reveal their types at runtime. The `isMemberOfClass:` method, defined in the `NSObject` class, checks whether the receiver is an instance of a particular class:

```
if ( [anObject isMemberOfClass:someClass] )
    ...
```

The `isKindOfClass:` method, also defined in the `NSObject` class, checks more generally whether the receiver inherits from or is a member of a particular class (whether it has the class in its inheritance path):

```
if ( [anObject isKindOfClass:someClass] )
    ...
```

The set of classes for which `isKindOfClass:` returns `YES` is the same set to which the receiver can be statically typed.

Introspection isn’t limited to type information. Later sections of this chapter discuss methods that return the class object, report whether an object can respond to a message, and reveal other information.

See the `NSObject` class specification in the Foundation framework reference for more on `isKindOfClass:`, `isMemberOfClass:`, and related methods.

A class definition contains various kinds of information, much of it about instances of the class:

- The name of the class and its superclass
- A template describing a set of instance variables
- The declarations of method names and their return and argument types
- The method implementations

This information is compiled and recorded in data structures made available to the runtime system. The compiler creates just one object, a _class object_, to represent the class. The class object has access to all the information about the class, which means mainly information about what instances of the class are like. It’s able to produce new instances according to the plan put forward in the class definition.

Although a class object keeps the prototype of a class instance, it’s not an instance itself. It has no instance variables of its own and it can’t perform methods intended for instances of the class. However, a class definition can include methods intended specifically for the class object—_class methods_ as opposed to _instance methods_. A class object inherits class methods from the classes above it in the hierarchy, just as instances inherit instance methods.

In source code, the class object is represented by the class name. In the following example, the Rectangle class returns the class version number using a method inherited from the `NSObject` class:

```
int versionNumber = [Rectangle version];
```

However, the class name stands for the class object only as the receiver in a message expression. Elsewhere, you need to ask an instance or the class to return the class `id`. Both respond to a `class` message:

```
id aClass = [anObject class];
id rectClass = [Rectangle class];
```

As these examples show, class objects can, like all other objects, be typed `id`. But class objects can also be more specifically typed to the Class data type:

```
Class aClass = [anObject class];
Class rectClass = [Rectangle class];
```

All class objects are of type Class. Using this type name for a class is equivalent to using the class name to statically type an instance.

Class objects are thus full-fledged objects that can be dynamically typed, receive messages, and inherit methods from other classes. They’re special only in that they’re created by the compiler, lack data structures (instance variables) of their own other than those built from the class definition, and are the agents for producing instances at runtime.

A principal function of a class object is to create new instances. This code tells the Rectangle class to create a new Rectangle instance and assign it to the `myRect` variable:

```
id  myRect;
myRect = [Rectangle alloc];
```

The `alloc` method dynamically allocates memory for the new object’s instance variables and initializes them all to `0`—all, that is, except the `isa` variable that connects the new instance to its class. For an object to be useful, it generally needs to be more completely initialized. That’s the function of an `init` method. Initialization typically follows immediately after allocation:

```
myRect = [[Rectangle alloc] init];
```

This line of code, or one like it, would be necessary before `myRect` could receive any of the messages that were illustrated in previous examples in this chapter. The `alloc` method returns a new instance and that instance performs an `init` method to set its initial state. Every class object has at least one method (like `alloc`) that enables it to produce new objects, and every instance has at least one method (like `init`) that prepares it for use. Initialization methods often take arguments to allow particular values to be passed and have keywords to label the arguments (`initWithPosition:size:`, for example, is a method that might initialize a new Rectangle instance), but they all begin with “init”.

It’s not just a whim of the Objective-C language that classes are treated as objects. It’s a choice that has intended, and sometimes surprising, benefits for design. It’s possible, for example, to customize an object with a class, where the class belongs to an open-ended set. In the Application Kit, for example, an `NSMatrix` object can be customized with a particular kind of `NSCell` object.

An `NSMatrix` object can take responsibility for creating the individual objects that represent its cells. It can do this when the matrix is first initialized and later when new cells are needed. The visible matrix that an `NSMatrix` object draws on the screen can grow and shrink at runtime, perhaps in response to user actions. When it grows, the matrix needs to be able to produce new objects to fill the new slots that are added.

But what kind of objects should they be? Each matrix displays just one kind of `NSCell`, but there are many different kinds. The inheritance hierarchy in Figure 1-3 shows some of those provided by the Application Kit. All inherit from the generic `NSCell` class:

__Figure 1-3__  Inheritance hierarchy for NSCell

!

When an matrix creates `NSCell` objects, should they be `NSButtonCell` objects to display a bank of buttons or switches, `NSTextFieldCell` objects to display fields where the user can enter and edit text, or some other kind of `NSCell`? The `NSMatrix` object must allow for any kind of cell, even types that haven’t been invented yet.

One solution to this problem is to define the `NSMatrix` class as an abstract class and require everyone who uses it to declare a subclass and implement the methods that produce new cells. Because they would be implementing the methods, users of the class could be sure that the objects they created were of the right type.

But this requires others to do work that ought to be done in the `NSMatrix` class, and it unnecessarily proliferates the number of classes. Since an application might need more than one kind of `NSMatrix`, each with a different kind of `NSCell`, it could become cluttered with `NSMatrix` subclasses. Every time you invented a new kind of `NSCell`, you’d also have to define a new kind of `NSMatrix`. Moreover, programmers on different projects would be writing virtually identical code to do the same job, all to make up for `NSMatrix`'s failure to do it.

A better solution, the solution the `NSMatrix` class actually adopts, is to allow `NSMatrix` instances to be initialized with a kind of `NSCell`—with a class object. It defines a `setCellClass:` method that passes the class object for the kind of `NSCell` object an `NSMatrix` should use to fill empty slots:

```
[myMatrix setCellClass:[NSButtonCell class]];
```

The `NSMatrix` object uses the class object to produce new cells when it’s first initialized and whenever it’s resized to contain more cells. This kind of customization would be difficult if classes weren’t objects that could be passed in messages and assigned to variables.

When you define a new class, you can specify instance variables. Every instance of the class can maintain its own copy of the variables you declare—each object controls its own data. There is, however, no “class variable” counterpart to an instance variable. Only internal data structures, initialized from the class definition, are provided for the class. Moreover, a class object has no access to the instance variables of any instances; it can’t initialize, read, or alter them.

For all the instances of a class to share data, you must define an external variable of some sort. The simplest way to do this is to declare a variable in the class implementation file as illustrated in the following code fragment.

```objc
int MCLSGlobalVariable;

@implementation MyClass
// implementation continues
```

In a more sophisticated implementation, you can declare a variable to be `static`, and provide class methods to manage it. Declaring a variable `static` limits its scope to just the class—and to just the part of the class that’s implemented in the file. (Thus unlike instance variables, static variables cannot be inherited by, or directly manipulated by, subclasses.) This pattern is commonly used to define shared instances of a class (such as singletons, see Creating a Singleton Instance).

```objc
static MyClass *MCLSSharedInstance;

@implementation MyClass

+ (MyClass *)sharedInstance
{
    // check for existence of shared instance
    // create if necessary
    return MCLSSharedInstance;
}
// implementation continues
```

Static variables help give the class object more functionality than just that of a “factory” producing instances; it can approach being a complete and versatile object in its own right. A class object can be used to coordinate the instances it creates, dispense instances from lists of objects already created, or manage other processes essential to the application. In the case when you need only one object of a particular class, you can put all the object’s state into static variables and use only class methods. This saves the step of allocating and initializing an instance.

If a class object is to be used for anything besides allocating instances, it may need to be initialized just as an instance is. Although programs don’t allocate class objects, Objective-C does provide a way for programs to initialize them.

If a class makes use of static or global variables, the `initialize` method is a good place to set their initial values. For example, if a class maintains an array of instances, the `initialize` method could set up the array and even allocate one or two default instances to have them ready.

The runtime system sends an `initialize` message to every class object before the class receives any other messages and after its superclass has received the `initialize` message. This gives the class a chance to set up its runtime environment before it’s used. If no initialization is required, you don’t need to write an `initialize` method to respond to the message.

Because of inheritance, an `initialize` message sent to a class that doesn’t implement the `initialize` method is forwarded to the superclass, even though the superclass has already received the `initialize` message. For example, assume class A implements the `initialize` method, and class B inherits from class A but does not implement the `initialize` method. Just before class B is to receive its first message, the runtime system sends `initialize` to it. But, because class B doesn’t implement `initialize`, class A’s `initialize` is executed instead. Therefore, class A should ensure that its initialization logic is performed only once.

To avoid performing initialization logic more than once, use the template in Listing 1-1 when implementing the `initialize` method.

__Listing 1-1__  Implementation of the initialize method

```objc
+ (void)initialize
{
    static BOOL initialized = NO;
    if (!initialized) {
        // Perform initialization here.
        ...
        initialized = YES;
    }
}
```


All objects, classes and instances alike, need an interface to the runtime system. Both class objects and instances should be able to introspect about their abilities and to report their place in the inheritance hierarchy. It’s the province of the `NSObject` class to provide this interface.

So that `NSObject`'s methods don’t have to be implemented twice—once to provide a runtime interface for instances and again to duplicate that interface for class objects—class objects are given special dispensation to perform instance methods defined in the root class. When a class object receives a message that it can’t respond to with a class method, the runtime system determines whether there’s a root instance method that can respond. The only instance methods that a class object can perform are those defined in the root class, and only if there’s no class method that can do the job.

For more on this peculiar ability of class objects to perform root instance methods, see the `NSObject` class specification in the Foundation framework reference.

In source code, class names can be used in only two very different contexts. These contexts reflect the dual role of a class as a data type and as an object:

- The class name can be used as a type name for a kind of object. For example:

```
Rectangle * anObject;
```

  Here `anObject` is statically typed to be a pointer to a Rectangle. The compiler expects it to have the data structure of a Rectangle instance and the instance methods defined and inherited by the Rectangle class. Static typing enables the compiler to do better type checking and makes source code more self-documenting. See [Enabling Static Behaviors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznheztgojy) for details.

  Only instances can be statically typed; class objects can’t be, since they aren’t members of a class, but rather belong to the Class data type.
- As the receiver in a message expression, the class name refers to the class object. This usage was illustrated in several of the earlier examples. The class name can stand for the class object only as a message receiver. In any other context, you must ask the class object to reveal its `id` (by sending it a class message). The example below passes the Rectangle class as an argument in an `isKindOfClass:` message.

```
if ( [anObject isKindOfClass:[Rectangle class]] )
    ...
```

  It would have been illegal to simply use the name “Rectangle” as the argument. The class name can only be a receiver.

  If you don’t know the class name at compile time but have it as a string at runtime, `NSClassFromString` will return the class object:

```
NSString *className;
    ...
if ( [anObject isKindOfClass:NSClassFromString(className)] )
    ...
```

  This function returns `nil` if the string it’s passed is not a valid class name.

Classnames exist in the same namespace as global variables and function names. A class and a global variable can’t have the same name. Classnames are about the only names with global visibility in Objective-C.

Much of object-oriented programming consists of writing the code for new objects—defining new classes. In Objective-C, classes are defined in two parts:

- An _interface_ that declares the methods and instance variables of the class and names its superclass
- An _implementation_ that actually defines the class (contains the code that implements its methods)

Although the compiler doesn’t require it, the interface and implementation are usually separated into two different files. The interface file must be made available to anyone who uses the class.

A single file can declare or implement more than one class. Nevertheless, it’s customary to have a separate interface file for each class, if not also a separate implementation file. Keeping class interfaces separate better reflects their status as independent entities.

Interface and implementation files typically are named after the class. The name of the implementation file has the `.m` extension, indicating that it contains Objective-C source code. The interface file can be assigned any other extension. Because it’s included in other source files, the name of the interface file usually has the `.h` extension typical of header files. For example, the Rectangle class would be declared in `Rectangle.h` and defined in `Rectangle.m`.

Separating an object’s interface from its implementation fits well with the design of object-oriented programs. An object is a self-contained entity that can be viewed from the outside almost as a “black box.” Once you’ve determined how an object interacts with other elements in your program—that is, once you’ve declared its interface—you can freely alter its implementation without affecting any other part of the application.

The declaration of a class interface begins with the compiler directive `@interface` and ends with the directive `@end`. (All Objective-C directives to the compiler begin with “@”.)

```objc
@interface ClassName : ItsSuperclass
{
    instance variable declarations
}
method declarations
@end
```

The first line of the declaration presents the new class name and links it to its superclass. The superclass defines the position of the new class in the inheritance hierarchy, as discussed under [Inheritance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznha3dgnzq). If the colon and superclass name are omitted, the new class is declared as a root class, a rival to the `NSObject` class.

Following the first part of the class declaration, braces enclose declarations of _instance variables_, the data structures that are part of each instance of the class. Here’s a partial list of instance variables that might be declared in the Rectangle class:

```
float width;
float height;
BOOL filled;
NSColor *fillColor;
```

Methods for the class are declared next, after the braces enclosing instance variables and before the end of the class declaration. The names of methods that can be used by class objects, _class methods_, are preceded by a plus sign:

```
+ alloc;
```

The methods that instances of a class can use, _instance methods_, are marked with a minus sign:

```objc
- (void)display;
```

Although it’s not a common practice, you can define a class method and an instance method with the same name. A method can also have the same name as an instance variable. This is more common, especially if the method returns the value in the variable. For example, Circle has a `radius` method that could match a `radius` instance variable.

Method return types are declared using the standard C syntax for casting one type to another:

```objc
- (float)radius;
```

Argument types are declared in the same way:

```objc
- (void)setRadius:(float)aRadius;
```

If a return or argument type isn’t explicitly declared, it’s assumed to be the default type for methods and messages—an `id`. The `alloc` method illustrated earlier returns `id`.

When there’s more than one argument, the arguments are declared within the method name after the colons. Arguments break the name apart in the declaration, just as in a message. For example:

```objc
- (void)setWidth:(float)width height:(float)height;
```

Methods that take a variable number of arguments declare them using a comma and ellipsis points, just as a function would:

```
- makeGroup:group, ...;
```


The interface file must be included in any source module that depends on the class interface—that includes any module that creates an instance of the class, sends a message to invoke a method declared for the class, or mentions an instance variable declared in the class. The interface is usually included with the `#import` directive:

```objc
#import "Rectangle.h"
```

This directive is identical to `#include`, except that it makes sure that the same file is never included more than once. It’s therefore preferred and is used in place of `#include` in code examples throughout Objective-C–based documentation.

To reflect the fact that a class definition builds on the definitions of inherited classes, an interface file begins by importing the interface for its superclass:

```objc
#import "ItsSuperclass.h"

@interface ClassName : ItsSuperclass
{
    instance variable declarations
}
method declarations
@end
```

This convention means that every interface file includes, indirectly, the interface files for all inherited classes. When a source module imports a class interface, it gets interfaces for the entire inheritance hierarchy that the class is built upon.

Note that if there is a _precomp_—a precompiled header—that supports the superclass, you may prefer to import the precomp instead.

An interface file declares a class and, by importing its superclass, implicitly contains declarations for all inherited classes, from `NSObject` on down through its superclass. If the interface mentions classes not in this hierarchy, it must import them explicitly or declare them with the `@class` directive:

```
@class Rectangle, Circle;
```

This directive simply informs the compiler that “Rectangle” and “Circle” are class names. It doesn’t import their interface files.

An interface file mentions class names when it statically types instance variables, return values, and arguments. For example, this declaration

```objc
- (void)setPrimaryColor:(NSColor *)aColor;
```

mentions the `NSColor` class.

Since declarations like this simply use the class name as a type and don’t depend on any details of the class interface (its methods and instance variables), the `@class` directive gives the compiler sufficient forewarning of what to expect. However, where the interface to a class is actually used (instances created, messages sent), the class interface must be imported. Typically, an interface file uses `@class` to declare classes, and the corresponding implementation file imports their interfaces (since it will need to create instances of those classes or send them messages).

The `@class` directive minimizes the amount of code seen by the compiler and linker, and is therefore the simplest way to give a forward declaration of a class name. Being simple, it avoids potential problems that may come with importing files that import still other files. For example, if one class declares a statically typed instance variable of another class, and their two interface files import each other, neither class may compile correctly.

The purpose of the interface file is to declare the new class to other source modules (and to other programmers). It contains all the information they need to work with the class (programmers might also appreciate a little documentation).

- The interface file tells users how the class is connected into the inheritance hierarchy and what other classes—inherited or simply referred to somewhere in the class—are needed.
- The interface file also lets the compiler know what instance variables an object contains, and tells programmers what variables subclasses inherit. Although instance variables are most naturally viewed as a matter of the implementation of a class rather than its interface, they must nevertheless be declared in the interface file. This is because the compiler must be aware of the structure of an object where it’s used, not just where it’s defined. As a programmer, however, you can generally ignore the instance variables of the classes you use, except when defining a subclass.
- Finally, through its list of method declarations, the interface file lets other modules know what messages can be sent to the class object and instances of the class. Every method that can be used outside the class definition is declared in the interface file; methods that are internal to the class implementation can be omitted.

The definition of a class is structured very much like its declaration. It begins with the `@implementation` directive and ends with the `@end` directive:

```objc
@implementation ClassName : ItsSuperclass
{
    instance variable declarations
}
method definitions
@end
```

However, every implementation file must import its own interface. For example, `Rectangle.m` imports `Rectangle.h`. Because the implementation doesn’t need to repeat any of the declarations it imports, it can safely omit:

- The name of the superclass
- The declarations of instance variables

This simplifies the implementation and makes it mainly devoted to method definitions:

```objc
#import "ClassName.h"

@implementation ClassName
method definitions
@end
```

Methods for a class are defined, like C functions, within a pair of braces. Before the braces, they’re declared in the same manner as in the interface file, but without the semicolon. For example:

```objc
+ alloc
{
    ...
}

- (BOOL)isfilled
{
    ...
}

- (void)setFilled:(BOOL)flag
{
    ...
}
```

Methods that take a variable number of arguments handle them just as a function would:

```objc
#import <stdarg.h>

 ...

- getGroup:group, ...
{
    va_list ap;
    va_start(ap, group);
    ...
}
```


By default, the definition of an instance method has all the instance variables of the object within its scope. It can refer to them simply by name. Although the compiler creates the equivalent of C structures to store instance variables, the exact nature of the structure is hidden. You don’t need either of the structure operators (`.` or `->`) to refer to an object’s data. For example, the following method definition refers to the receiver’s `filled` instance variable:

```objc
- (void)setFilled:(BOOL)flag
{
    filled = flag;
    ...
}
```

Neither the receiving object nor its `filled` instance variable is declared as an argument to this method, yet the instance variable falls within its scope. This simplification of method syntax is a significant shorthand in the writing of Objective-C code.

When the instance variable belongs to an object that’s not the receiver, the object’s type must be made explicit to the compiler through static typing. In referring to the instance variable of a statically typed object, the structure pointer operator (`->`) is used.

Suppose, for example, that the Sibling class declares a statically typed object, `twin`, as an instance variable:

```objc
@interface Sibling : NSObject
{
    Sibling *twin;
    int gender;
    struct features *appearance;
}
```

As long as the instance variables of the statically typed object are within the scope of the class (as they are here because `twin` is typed to the same class), a Sibling method can set them directly:

```swift
- makeIdenticalTwin
{
    if ( !twin ) {
        twin = [[Sibling alloc] init];
        twin->gender = gender;
        twin->appearance = appearance;
    }
    return twin;
}
```


Although they’re declared in the class interface, instance variables are more a matter of the way a class is implemented than of the way it’s used. An object’s interface lies in its methods, not in its internal data structures.

Often there’s a one-to-one correspondence between a method and an instance variable, as in the following example:

```objc
- (BOOL)isFilled
{
    return filled;
}
```

But this need not be the case. Some methods might return information not stored in instance variables, and some instance variables might store information that an object is unwilling to reveal.

As a class is revised from time to time, the choice of instance variables may change, even though the methods it declares remain the same. As long as messages are the vehicle for interacting with instances of the class, these changes won’t really affect its interface.

To enforce the ability of an object to hide its data, the compiler limits the scope of instance variables—that is, limits their visibility within the program. But to provide flexibility, it also lets you explicitly set the scope at three different levels. Each level is marked by a compiler directive:

| Directive | Meaning |
| --- | --- |
| `@private` | The instance variable is accessible only within the class that declares it. |
| `@protected` | The instance variable is accessible within the class that declares it and within classes that inherit it. |
| `@public` | The instance variable is accessible everywhere. |

This is illustrated in Figure 1-4.

__Figure 1-4__  The scope of instance variables

!

A directive applies to all the instance variables listed after it, up to the next directive or the end of the list. In the following example, the `age` and `evaluation` instance variables are private, `name`, `job`, and `wage` are protected, and `boss` is public.

```objc
@interface Worker : NSObject
{
    char *name;
@private
    int age;
    char *evaluation;
@protected
    id job;
    float wage;
@public
    id boss;
}
```

By default, all unmarked instance variables (like `name` above) are `@protected`.

All instance variables that a class declares, no matter how they’re marked, are within the scope of the class definition. For example, a class that declares a `job` instance variable, such as the Worker class shown above, can refer to it in a method definition:

```
- promoteTo:newPosition
{
    id old = job;
    job = newPosition;
    return old;
}
```

Obviously, if a class couldn’t access its own instance variables, the instance variables would be of no use whatsoever.

Normally, a class also has access to the instance variables it inherits. The ability to refer to an instance variable is usually inherited along with the variable. It makes sense for classes to have their entire data structures within their scope, especially if you think of a class definition as merely an elaboration of the classes it inherits from. The `promoteTo:` method illustrated earlier could just as well have been defined in any class that inherits the `job` instance variable from the Worker class.

However, there are reasons why you might want to restrict inheriting classes from directly accessing an instance variable:

- Once a subclass accesses an inherited instance variable, the class that declares the variable is tied to that part of its implementation. In later versions, it can’t eliminate the variable or alter the role it plays without inadvertently breaking the subclass.
- Moreover, if a subclass accesses an inherited instance variable and alters its value, it may inadvertently introduce bugs in the class that declares the variable, especially if the variable is involved in class-internal dependencies.

To limit an instance variable’s scope to just the class that declares it, you must mark it `@private`. Instance variables marked `@private` are only available to subclasses by calling public accessor methods, if they exist.

At the other extreme, marking a variable `@public` makes it generally available, even outside of class definitions that inherit or declare the variable. Normally, to get information stored in an instance variable, other objects must send a message requesting it. However, a public instance variable can be accessed anywhere as if it were a field in a C structure. For example:

```swift
Worker *ceo = [[Worker alloc] init];
ceo->boss = nil;
```

Note that the object must be statically typed.

Marking instance variables `@public` defeats the ability of an object to hide its data. It runs counter to a fundamental principle of object-oriented programming—the encapsulation of data within objects where it’s protected from view and inadvertent error. Public instance variables should therefore be avoided except in extraordinary cases.

In Objective-C, messages aren’t bound to method implementations until runtime. The compiler converts a message expression,

```
[receiver message]
```

into a call on a messaging function, `objc_msgSend`. This function takes the receiver and the name of the method mentioned in the message—that is, the method selector—as its two principal parameters:

```
objc_msgSend(receiver, selector)
```

Any arguments passed in the message are also handed to `objc_msgSend`:

```
objc_msgSend(receiver, selector, arg1, arg2, ...)
```

The messaging function does everything necessary for dynamic binding:

- It first finds the procedure (method implementation) that the selector refers to. Since the same method can be implemented differently by separate classes, the precise procedure that it finds depends on the class of the receiver.
- It then calls the procedure, passing it the receiving object (a pointer to its data), along with any arguments that were specified for the method.
- Finally, it passes on the return value of the procedure as its own return value.

The key to messaging lies in the structures that the compiler builds for each class and object. Every class structure includes these two essential elements:

- A pointer to the superclass.
- A class _dispatch table_. This table has entries that associate method selectors with the class-specific addresses of the methods they identify. The selector for the `setOrigin::` method is associated with the address of (the procedure that implements) `setOrigin::`, the selector for the `display` method is associated with `display`’s address, and so on.

When a new object is created, memory for it is allocated, and its instance variables are initialized. First among the object’s variables is a pointer to its class structure. This pointer, called `isa`, gives the object access to its class and, through the class, to all the classes it inherits from.

These elements of class and object structure are illustrated in Figure 1-5.

__Figure 1-5__  Messaging Framework

!

When a message is sent to an object, the messaging function follows the object’s `isa` pointer to the class structure where it looks up the method selector in the dispatch table. If it can’t find the selector there, `objc_msgSend` follows the pointer to the superclass and tries to find the selector in its dispatch table. Successive failures cause `objc_msgSend` to climb the class hierarchy until it reaches the `NSObject` class. Once it locates the selector, the function calls the method entered in the table and passes it the receiving object’s data structure.

This is the way that method implementations are chosen at runtime—or, in the jargon of object-oriented programming, that methods are dynamically bound to messages.

To speed the messaging process, the runtime system caches the selectors and addresses of methods as they are used. There’s a separate cache for each class, and it can contain selectors for inherited methods as well as for methods defined in the class. Before searching the dispatch tables, the messaging routine first checks the cache of the receiving object’s class (on the theory that a method that was used once may likely be used again). If the method selector is in the cache, messaging is only slightly slower than a function call. Once a program has been running long enough to “warm up” its caches, almost all the messages it sends find a cached method. Caches grow dynamically to accommodate new messages as the program runs.

For efficiency, full ASCII names are not used as method selectors in compiled code. Instead, the compiler writes each method name into a table, then pairs the name with a unique identifier that represents the method at runtime. The runtime system makes sure each identifier is unique: No two selectors are the same, and all methods with the same name have the same selector. Compiled selectors are assigned to a special type, `SEL`, to distinguish them from other data. Valid selectors are never 0. You must let the system assign `SEL` identifiers to methods; it’s futile to assign them arbitrarily.

The `@selector()` directive lets Objective-C source code refer to the compiled selector, rather than to the full method name. Here, the selector for `setWidth:height:` is assigned to the `setWidthHeight` variable:

```
SEL  setWidthHeight;
setWidthHeight = @selector(setWidth:height:);
```

It’s most efficient to assign values to `SEL` variables at compile time with the `@selector()` directive. However, in some cases, a program may need to convert a character string to a selector at runtime. This can be done with the [NSSelectorFromString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSSelectorFromString) function:

```
setWidthHeight = NSSelectorFromString(aBuffer);
```

Conversion in the opposite direction is also possible. The [NSStringFromSelector](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSStringFromSelector) function returns a method name for a selector:

```
NSString *method;
method = NSStringFromSelector(setWidthHeight);
```

These and other runtime functions are described in the Cocoa framework reference documentation.

Compiled selectors identify method names, not method implementations. Rectangle’s `display` method, for example, has the same selector as `display` methods defined in other classes. This is essential for polymorphism and dynamic binding; it lets you send the same message to receivers belonging to different classes. If there were one selector per method implementation, a message would be no different than a function call.

A class method and an instance method with the same name are assigned the same selector. However, because of their separate domains, there’s no confusion between the two. A class could define a `display` class method in addition to a `display` instance method.

The messaging routine has access to method implementations only through selectors, so it treats all methods with the same selector alike. It discovers the return type of a method, and the data types of its arguments, from the selector. Therefore, except for messages sent to statically typed receivers, dynamic binding requires all implementations of identically named methods to have the same return type and the same argument types. (Statically typed receivers are an exception to this rule, since the compiler can learn about the method implementation from the class type.)

Although identically named class methods and instance methods are represented by the same selector, they can have different argument and return types.

The `performSelector:`, `performSelector:withObject:`, and `performSelector:withObject:withObject:` methods, defined in the `NSObject` protocol, take `SEL` identifiers as their initial arguments. All three methods map directly into the messaging function. For example,

```
[friend performSelector:@selector(gossipAbout:)
    withObject:aNeighbor];
```

is equivalent to:

```
[friend gossipAbout:aNeighbor];
```

These methods make it possible to vary a message at runtime, just as it’s possible to vary the object that receives the message. Variable names can be used in both halves of a message expression:

```
id   helper = getTheReceiver();
SEL  request = getTheSelector();
[helper performSelector:request];
```

In this example, the receiver (`helper`) is chosen at runtime (by the fictitious `getTheReceiver` function), and the method the receiver is asked to perform (`request`) is also determined at runtime (by the equally fictitious `getTheSelector` function).

In its treatment of user-interface controls, the Application Kit makes good use of the ability to vary both the receiver and the message.

`NSControl` objects are graphical devices that can be used to give instructions to an application. Most resemble real-world control devices such as buttons, switches, knobs, text fields, dials, menu items, and the like. In software, these devices stand between the application and the user. They interpret events coming from hardware devices like the keyboard and mouse and translate them into application-specific instructions. For example, a button labeled “Find” would translate a mouse click into an instruction for the application to start searching for something.

The Application Kit defines a template for creating control devices and defines a few “off-the-shelf” devices of its own. For example, the `NSButtonCell` class defines an object that you can assign to an `NSMatrix` instance and initialize with a size, a label, a picture, a font, and a keyboard alternative. When the user clicks the button (or uses the keyboard alternative), the `NSButtonCell` object sends a message instructing the application to do something. To do this, an `NSButtonCell` object must be initialized not just with an image, a size, and a label, but with directions on what message to send and who to send it to. Accordingly, an `NSButtonCell` instance can be initialized for an action message, the method selector it should use in the message it sends, and a target, the object that should receive the message.

```
[myButtonCell setAction:@selector(reapTheWind:)];
[myButtonCell setTarget:anObject];
```

The button cell sends the message using `NSObject`’s `performSelector:withObject:` method. All action messages take a single argument, the `id` of the control device sending the message.

If Objective-C didn’t allow the message to be varied, all `NSButtonCell` objects would have to send the same message; the name of the method would be frozen in the `NSButtonCell` source code. Instead of simply implementing a mechanism for translating user actions into action messages, button cells and other controls would have to constrain the content of the message. This would make it difficult for any object to respond to more than one button cell. There would either have to be one target for each button, or the target object would have to discover which button the message came from and act accordingly. Each time you rearranged the user interface, you would also have to re-implement the method that responds to the action message. This would be an unnecessary complication that Objective-C happily avoids.

If an object receives a message to perform a method that isn’t in its repertoire, an error results. It’s the same sort of error as calling a nonexistent function. But because messaging occurs at runtime, the error often isn’t evident until the program executes.

It’s relatively easy to avoid this error when the message selector is constant and the class of the receiving object is known. As you write your programs, you can make sure that the receiver is able to respond. If the receiver is statically typed, the compiler performs this test for you.

However, if the message selector or the class of the receiver varies, it may be necessary to postpone this test until runtime. The `respondsToSelector:` method, defined in the `NSObject` class, determines whether a receiver can respond to a message. It takes the method selector as an argument and returns whether the receiver has access to a method matching the selector:

```
if ( [anObject respondsToSelector:@selector(setOrigin::)] )
    [anObject setOrigin:0.0 :0.0];
else
    fprintf(stderr, "%s can’t be placed\n",
        [NSStringFromClass([anObject class]) UTF8String]);
```

The `respondsToSelector:` test is especially important when sending messages to objects that you don’t have control over at compile time. For example, if you write code that sends a message to an object represented by a variable that others can set, you should make sure the receiver implements a method that can respond to the message.

When the messaging function finds the procedure that implements a method, it calls the procedure and passes it all the arguments in the message. It also passes the procedure two hidden arguments:

- The receiving object
- The selector for the method

These arguments give every method implementation explicit information about the two halves of the message expression that invoked it. They’re said to be “hidden” because they aren’t declared in the source code that defines the method. They’re inserted into the implementation when the code is compiled.

Although these arguments aren’t explicitly declared, source code can still refer to them (just as it can refer to the receiving object’s instance variables). A method refers to the receiving object as `self`, and to its own selector as `_cmd`. In the example below, `_cmd` refers to the selector for the `strange` method and `self` to the object that receives a `strange` message.

```
- strange
{
    id  target = getTheReceiver();
    SEL method = getTheMethod();

    if ( target == self || method == _cmd )
        return nil;
    return [target performSelector:method];
}
```

`self` is the more useful of the two arguments. It is, in fact, the way the receiving object’s instance variables are made available to the method definition.

Objective-C provides two terms that can be used within a method definition to refer to the object that performs the method—`self` and `super`.

Suppose, for example, that you define a `reposition` method that needs to change the coordinates of whatever object it acts on. It can invoke the `setOrigin::` method to make the change. All it needs to do is send a `setOrigin::` message to the same object that the `reposition` message itself was sent to. When you’re writing the reposition code, you can refer to that object as either `self` or `super`. The `reposition` method could read either:

```
- reposition
{
    ...
    [self setOrigin:someX :someY];
    ...
}
```

or:

```
- reposition
{
    ...
    [super setOrigin:someX :someY];
    ...
}
```

Here, `self` and `super` both refer to the object receiving a `reposition` message, whatever object that may happen to be. The two terms are quite different, however. `self` is one of the hidden arguments that the messaging routine passes to every method; it’s a local variable that can be used freely within a method implementation, just as the names of instance variables can be. `super` is a term that substitutes for `self` only as the receiver in a message expression. As receivers, the two terms differ principally in how they affect the messaging process:

- `self` searches for the method implementation in the usual manner, starting in the dispatch table of the receiving object’s class. In the example above, it would begin with the class of the object receiving the reposition message.
- `super` starts the search for the method implementation in a very different place. It begins in the superclass of the class that defines the method where `super` appears. In the example above, it would begin with the superclass of the class where reposition is defined.

Wherever `super` receives a message, the compiler substitutes another messaging routine for the `objc_msgSend` function. The substitute routine looks directly to the superclass of the defining class—that is, to the superclass of the class sending the message to `super`—rather than to the class of the object receiving the message.

The difference between `self` and `super` becomes clear in a hierarchy of three classes. Suppose, for example, that we create an object belonging to a class called Low. Low’s superclass is Mid; Mid’s superclass is High. All three classes define a method called `negotiate`, which they use for a variety of purposes. In addition, Mid defines an ambitious method called `makeLastingPeace`, which also has need of the `negotiate` method. This is illustrated in Figure 1-6:

__Figure 1-6__  High, Mid, Low

!

We now send a message to our Low object to perform the `makeLastingPeace` method, and `makeLastingPeace`, in turn, sends a `negotiate` message to the same Low object. If source code calls this object `self`,

```
- makeLastingPeace
{
    [self negotiate];
    ...
}
```

the messaging routine finds the version of `negotiate` defined in Low, `self`’s class. However, if Mid’s source code calls this object `super`,

```
- makeLastingPeace
{
    [super negotiate];
    ...
}
```

the messaging routine will find the version of `negotiate` defined in High. It ignores the receiving object’s class (Low) and skips to the superclass of Mid, since Mid is where `makeLastingPeace` is defined. Neither message finds Mid’s version of `negotiate`.

As this example illustrates, `super` provides a way to bypass a method that overrides another method. Here it enabled `makeLastingPeace` to avoid the Mid version of `negotiate` that redefined the original High version.

Not being able to reach Mid’s version of `negotiate` may seem like a flaw, but, under the circumstances, it’s right to avoid it:

- The author of the Low class intentionally overrode Mid’s version of `negotiate` so that instances of the Low class (and its subclasses) would invoke the redefined version of the method instead. The designer of Low didn’t want Low objects to perform the inherited method.
- In sending the message to `super`, the author of Mid’s `makeLastingPeace` method intentionally skipped over Mid’s version of `negotiate` (and over any versions that might be defined in classes like Low that inherit from Mid) to perform the version defined in the High class. Mid’s designer wanted to use the High version of `negotiate` and no other.

Mid’s version of `negotiate` could still be used, but it would take a direct message to a Mid instance to do it.

Messages to `super` allow method implementations to be distributed over more than one class. You can override an existing method to modify or add to it, and still incorporate the original method in the modification:

```
- negotiate
{
    ...
    return [super negotiate];
}
```

For some tasks, each class in the inheritance hierarchy can implement a method that does part of the job and passes the message on to `super` for the rest. The `init` method, which initializes a newly allocated instance, is designed to work like this. Each `init` method has responsibility for initializing the instance variables defined in its class. But before doing so, it sends an `init` message to `super` to have the classes it inherits from initialize their instance variables. Each version of `init` follows this procedure, so classes initialize their instance variables in the order of inheritance:

```objc
- (id)init
{
    [super init];
    ...
}
```

It’s also possible to concentrate core functionality in one method defined in a superclass, and have subclasses incorporate the method through messages to `super`. For example, every class method that creates an instance must allocate storage for the new object and initialize its `isa` pointer to the class structure. This is typically left to the `alloc` and `allocWithZone:` methods defined in the `NSObject` class. If another class overrides these methods (a rare case), it can still get the basic functionality by sending a message to `super`.

`super` is simply a flag to the compiler telling it where to begin searching for the method to perform; it’s used only as the receiver of a message. But `self` is a variable name that can be used in any number of ways, even assigned a new value.

There’s a tendency to do just that in definitions of class methods. Class methods are often concerned not with the class object, but with instances of the class. For example, many class methods combine allocation and initialization of an instance, often setting up instance variable values at the same time. In such a method, it might be tempting to send messages to the newly allocated instance and to call the instance `self`, just as in an instance method. But that would be an error. `self` and `super` both refer to the receiving object—the object that gets a message telling it to perform the method. Inside an instance method, `self` refers to the instance; but inside a class method, `self` refers to the class object. This is an example of what not to do:

```objc
+ (Rectangle *)rectangleOfColor:(NSColor *) color
{
    self = [[Rectangle alloc] init]; // BAD
    [self setColor:color];
    return [self autorelease];
}
```

To avoid confusion, it’s usually better to use a variable other than `self` to refer to an instance inside a class method:

```objc
+ (id)rectangleOfColor:(NSColor *)color
{
    id newInstance = [[Rectangle alloc] init]; // GOOD
    [newInstance setColor:color];
    return [newInstance autorelease];
}
```

In fact, rather than sending the `alloc` message to the class in a class method, it’s often better to send `alloc` to `self`. This way, if the class is subclassed, and the `rectangleOfColor:` message is received by a subclass, the instance returned will be the same type as the subclass (for example, the `array` method of `NSArray` is inherited by `NSMutableArray`).

```objc
+ (id)rectangleOfColor:(NSColor *)color
{
    id newInstance = [[self alloc] init]; // EXCELLENT
    [newInstance setColor:color];
    return [newInstance autorelease];
}
```

See [Allocating, Initializing, and Deallocating Objects](The%20Runtime%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqojngeydkmzxg4) for more information about object allocation.

Class definitions are at the heart of Objective-C programming, but they’re not the only mechanism for structuring object definitions in Objective-C. This section discusses two other ways of declaring methods and associating them with a class:

- Categories can compartmentalize a class definition or extend an existing one.
- Protocols declare methods that can be implemented by any class.

You can add methods to a class by declaring them in an interface file under a category name and defining them in an implementation file under the same name. The category name indicates that the methods are additions to a class declared elsewhere, not a new class. You cannot, however, use a category to add additional instance variables to a class.

A category can be an alternative to a subclass. Rather than define a subclass to extend an existing class, through a category you can add methods to the class directly. For example, you could add categories to `NSArray` and other Cocoa classes. As in the case of a subclass, you don’t need source code for the class you’re extending.

The methods the category adds become part of the class type. For example, methods added to the `NSArray` class in a category are among the methods the compiler expects an `NSArray` instance to have in its repertoire. Methods added to the `NSArray` class in a subclass are not included in the `NSArray` type. (This matters only for statically typed objects, since static typing is the only way the compiler can know an object’s class.)

Category methods can do anything that methods defined in the class proper can do. At runtime, there’s no difference. The methods the category adds to the class are inherited by all the class’s subclasses, just like other methods.

The declaration of a category interface looks very much like a class interface declaration—except the category name is listed within parentheses after the class name and the superclass isn’t mentioned. Unless its methods don’t access any instance variables of the class, the category must import the interface file for the class it extends:

```objc
#import "ClassName.h"

@interface ClassName ( CategoryName )
// method declarations
@end
```

The implementation, as usual, imports its own interface. Assuming that the interface file is named after the category, a category implementation looks like this:

```objc
#import "CategoryName.h"

@implementation ClassName ( CategoryName )
// method definitions
@end
```

Note that a category can’t declare additional instance variables for the class; it includes only methods. However, all instance variables within the scope of the class are also within the scope of the category. That includes all instance variables declared by the class, even ones declared `@private`.

There’s no limit to the number of categories that you can add to a class, but each category name must be different, and each should declare and define a different set of methods.

The methods added in a category can be used to extend the functionality of the class or override methods the class inherits. A category can also override methods declared in the class interface. However, it cannot reliably override methods declared in another category of the same class. A category is not a substitute for a subclass. It’s best if categories don’t attempt to redefine methods that are explicitly declared in the class’s `@interface` section. Also note that a class can’t define the same method more than once.

When a category overrides an inherited method, the new version can, as usual, incorporate the inherited version through a message to `super`. But there’s no way for a category method to incorporate a method with the same name defined for the same class.

Categories can be used to extend classes defined by other implementors—for example, you can add methods to the classes defined in the Cocoa frameworks. The added methods are inherited by subclasses and are indistinguishable at runtime from the original methods of the class.

Categories can also be used to distribute the implementation of a new class into separate source files—for example, you could group the methods of a large class into several categories and put each category in a different file. When used like this, categories can benefit the development process in a number of ways:

- They provide a simple way of grouping related methods. Similar methods defined in different classes can be kept together in the same source file.
- They simplify the management of a large class when several developers contribute to the class definition.
- They let you achieve some of the benefits of incremental compilation for a very large class.
- They can help improve locality of reference for commonly used methods.
- They enable you to configure a class differently for separate applications, without having to maintain different versions of the same source code.

Categories are also used to declare informal protocols, as discussed under [Protocols—Declaring Interfaces for Others to Implement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnzngeytgojsgi).

A category can add methods to any class, including the root class. Methods added to `NSObject` become available to all classes that are linked to your code. While this can be useful at times, it can also be quite dangerous. Although it may seem that the modifications the category makes are well understood and of limited impact, inheritance gives them a wide scope. You may be making unintended changes to unseen classes; you may not know all the consequences of what you’re doing. Moreover, others who are unaware of your changes won’t understand what they’re doing.

In addition, there are two other considerations to keep in mind when implementing methods for the root class:

- Messages to `super` are invalid (there is no superclass).
- Class objects can perform instance methods defined in the root class.

Normally, class objects can perform only class methods. But instance methods defined in the root class are a special case. They define an interface to the runtime system that all objects inherit. Class objects are full-fledged objects and need to share the same interface.

This feature means that you need to take into account the possibility that an instance method you define in a category of the `NSObject` class might be performed not only by instances but by class objects as well. For example, within the body of the method, `self` might mean a class object as well as an instance. See the [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject) class specification in the Foundation framework reference for more information on class access to root instance methods.

Class and category interfaces declare methods that are associated with a particular class—mainly methods that the class implements. Informal and formal _protocols_, on the other hand, declare methods not associated with a class, but which any class, and perhaps many classes, might implement.

A protocol is simply a list of method declarations, unattached to a class definition. For example, these methods that report user actions on the mouse could be gathered into a protocol:

```objc
- (void)mouseDown:(NSEvent *)theEvent;
- (void)mouseDragged:(NSEvent *)theEvent;
- (void)mouseUp:(NSEvent *)theEvent;
```

Any class that wanted to respond to mouse events could adopt the protocol and implement its methods.

Protocols free method declarations from dependency on the class hierarchy, so they can be used in ways that classes and categories cannot. Protocols list methods that are (or may be) implemented somewhere, but the identity of the class that implements them is not of interest. What is of interest is whether or not a particular class _conforms_ to the protocol—whether it has implementations of the methods the protocol declares. Thus objects can be grouped into types not just on the basis of similarities due to the fact that they inherit from the same class, but also on the basis of their similarity in conforming to the same protocol. Classes in unrelated branches of the inheritance hierarchy might be typed alike because they conform to the same protocol.

Protocols can play a significant role in object-oriented design, especially where a project is divided among many implementors or it incorporates objects developed in other projects. Cocoa software uses them heavily to support interprocess communication through Objective-C messages.

However, an Objective-C program doesn’t need to use protocols. Unlike class definitions and message expressions, they’re optional. Some Cocoa frameworks use them; some don’t. It all depends on the task at hand.

Protocols are useful in at least three situations:

- To declare methods that others are expected to implement
- To declare the interface to an object while concealing its class
- To capture similarities among classes that are not hierarchically related

The following sections discuss these situations and the roles protocols can play.

If you know the class of an object, you can look at its interface declaration (and the interface declarations of the classes it inherits from) to find what messages it responds to. These declarations advertise the messages it can receive. Protocols provide a way for it to also advertise the messages it sends.

Communication works both ways; objects send messages as well as receive them. For example, an object might delegate responsibility for a certain operation to another object, or it may on occasion simply need to ask another object for information. In some cases, an object might be willing to notify other objects of its actions so that they can take whatever collateral measures might be required.

If you develop the class of the sender and the class of the receiver as part of the same project (or if someone else has supplied you with the receiver and its interface file), this communication is easily coordinated. The sender simply imports the interface file of the receiver. The imported file declares the method selectors the sender uses in the messages it sends.

However, if you develop an object that sends messages to objects that aren’t yet defined—objects that you’re leaving for others to implement—you won’t have the receiver’s interface file. You need another way to declare the methods you use in messages but don’t implement. A protocol serves this purpose. It informs the compiler about methods the class uses and also informs other implementors of the methods they need to define to have their objects work with yours.

Suppose, for example, that you develop an object that asks for the assistance of another object by sending it `helpOut:` and other messages. You provide an `assistant` instance variable to record the outlet for these messages and define a companion method to set the instance variable. This method lets other objects register themselves as potential recipients of your object’s messages:

```
- setAssistant:anObject
{
    assistant = anObject;
}
```

Then, whenever a message is to be sent to the `assistant`, a check is made to be sure that the receiver implements a method that can respond:

```objc
- (BOOL)doWork
{
    ...
    if ( [assistant respondsTo:@selector(helpOut:)] ) {
        [assistant helpOut:self];
        return YES;
    }
    return NO;
}
```

Since, at the time you write this code, you can’t know what kind of object might register itself as the `assistant`, you can only declare a protocol for the `helpOut:` method; you can’t import the interface file of the class that implements it.

A protocol can be used to declare the methods of an _anonymous object_, an object of unknown class. An anonymous object may represent a service or handle a limited set of functions, especially where only one object of its kind is needed. (Objects that play a fundamental role in defining an application’s architecture and objects that you must initialize before using are not good candidates for anonymity.)

Objects are not anonymous to their developers, of course, but they are anonymous when the developer supplies them to someone else. For example, consider the following situations:

- Someone who supplies a framework or a suite of objects for others to use can include objects that are not identified by a class name or an interface file. Lacking the name and class interface, users have no way of creating instances of the class. Instead, the supplier must provide a ready-made instance. Typically, a method in another class returns a usable object:

```
id formatter = [receiver formattingService];
```

  The object returned by the method is an object without a class identity, at least not one the supplier is willing to reveal. For it to be of any use at all, the supplier must be willing to identify at least some of the messages that it can respond to. This is done by associating the object with a list of methods declared in a protocol.
- You can send Objective-C messages to _remote objects_—objects in other applications. ([Remote Messaging](The%20Runtime%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqojngeydgnrug4), discusses this possibility in more detail.)

  Each application has its own structure, classes, and internal logic. But you don’t need to know how another application works or what its components are to communicate with it. As an outsider, all you need to know is what messages you can send (the protocol) and where to send them (the receiver).

  An application that publishes one of its objects as a potential receiver of remote messages must also publish a protocol declaring the methods the object will use to respond to those messages. It doesn’t have to disclose anything else about the object. The sending application doesn’t need to know the class of the object or use the class in its own design. All it needs is the protocol.

Protocols make anonymous objects possible. Without a protocol, there would be no way to declare an interface to an object without identifying its class.

If more than one class implements a set of methods, those classes are often grouped under an abstract class that declares the methods they have in common. Each subclass may re-implement the methods in its own way, but the inheritance hierarchy and the common declaration in the abstract class captures the essential similarity between the subclasses.

However, sometimes it’s not possible to group common methods in an abstract class. Classes that are unrelated in most respects might nevertheless need to implement some similar methods. This limited similarity may not justify a hierarchical relationship. For example, many different kinds of classes might implement methods to facilitate reference counting (this is just an example, since the Foundation Framework already implements reference counting for you):

```objc
- setRefCount:(int)count;
- (int)refCount;
- incrementCount;
- decrementCount;
```

These methods could be grouped into a protocol and the similarity between implementing classes accounted for by noting that they all conform to the same protocol.

Objects can be typed by this similarity (the protocols they conform to), rather than by their class. For example, an `NSMatrix` instance must communicate with the objects that represent its cells. The matrix could require each of these objects to be a kind of `NSCell` (a type based on class) and rely on the fact that all objects that inherit from the `NSCell` class have the methods needed to respond to `NSMatrix` messages. Alternatively, the `NSMatrix` object could require objects representing cells to have methods that can respond to a particular set of messages (a type based on protocol). In this case, the `NSMatrix` object wouldn’t care what class a cell object belonged to, just that it implemented the methods.

The simplest way of declaring a protocol is to group the methods in a category declaration:

```objc
@interface NSObject ( RefCounting )
- (int)refCount;
- incrementCount;
- decrementCount;
@end
```

Informal protocols are typically declared as categories of the `NSObject` class, since that broadly associates the method names with any class that inherits from `NSObject`. Because all classes inherit from the root class, the methods aren’t restricted to any part of the inheritance hierarchy. (It would also be possible to declare an informal protocol as a category of another class to limit it to a certain branch of the inheritance hierarchy, but there is little reason to do so.)

When used to declare a protocol, a category interface doesn’t have a corresponding implementation. Instead, classes that implement the protocol declare the methods again in their own interface files and define them along with other methods in their implementation files.

An informal protocol bends the rules of category declarations to list a group of methods but not associate them with any particular class or implementation.

Being informal, protocols declared in categories don’t receive much language support. There’s no type checking at compile time nor a check at runtime to see whether an object conforms to the protocol. To get these benefits, you must use a formal protocol. An informal protocol is good for times when implementing all the methods is optional, such as for a delegate.

The Objective-C language provides a way to formally declare a list of methods as a protocol. Formal protocols are supported by the language and the runtime system. For example, the compiler can check for types based on protocols, and objects can introspect at runtime to report whether or not they conform to a protocol.

Formal protocols are declared with the `@protocol` directive:

```objc
@protocol ProtocolName
method declarations
@end
```

For example, the reference-counting protocol could be declared like this:

```objc
@protocol ReferenceCounting
- (int)refCount;
- incrementCount;
- decrementCount;
@end
```

Unlike class names, protocol names don’t have global visibility. They live in their own namespace.

A class is said to _adopt_ a formal protocol if it agrees to implement the methods the protocol declares. Class declarations list the names of adopted protocols within angle brackets after the superclass name:

```objc
@interface ClassName : ItsSuperclass < protocol list >
```

Categories adopt protocols in much the same way:

```objc
@interface ClassName ( CategoryName ) < protocol list >
```

Names in the protocol list are separated by commas.

A class or category that adopts a protocol must import the header file where the protocol is declared. The methods declared in the adopted protocol are not declared elsewhere in the class or category interface.

It’s possible for a class to simply adopt protocols and declare no other methods. For example, the following class declaration adopts the Formatting and Prettifying protocols, but declares no instance variables or methods of its own:

```objc
@interface Formatter : NSObject < Formatting, Prettifying >
@end
```

A class or category that adopts a protocol is obligated to implement all the methods the protocol declares. Otherwise, the compiler issues a warning. The Formatter class above would define all the methods declared in the two protocols it adopts, in addition to any it might have declared itself.

Adopting a protocol is similar in some ways to declaring a superclass. Both assign methods to the class. The superclass declaration assigns it inherited methods; the protocol assigns it methods declared in the protocol list.

Just as classes are represented at runtime by class objects and methods by selector codes, formal protocols are represented by a special data type—instances of the Protocol class. Source code that deals with a protocol (other than to use it in a type specification) must refer to the Protocol object.

In many ways, protocols are similar to class definitions. They both declare methods, and at runtime they’re both represented by objects—classes by class objects and protocols by Protocol objects. Like class objects, Protocol objects are created automatically from the definitions and declarations found in source code and are used by the runtime system. They’re not allocated and initialized in program source code.

Source code can refer to a Protocol object using the `@protocol()` directive—the same directive that declares a protocol, except that here it has a set of trailing parentheses. The parentheses enclose the protocol name:

```
Protocol *counter = @protocol(ReferenceCounting);
```

This is the only way that source code can conjure up a Protocol object. Unlike a class name, a protocol name doesn’t designate the object—except inside `@protocol()`.

The compiler creates a Protocol object for each protocol declaration it encounters, but only if the protocol is also:

- Adopted by a class, or
- Referred to somewhere in source code (using `@protocol()`)

Protocols that are declared but not used (except for type checking as described below) aren’t represented by Protocol objects at runtime.

A class is said to _conform_ to a formal protocol if it (or a superclass) implements the methods declared in the protocol. An instance of a class is said to conform to the same set of protocols its class conforms to.

Since a class must implement all the methods declared in the protocols it adopts, and those methods are inherited by its subclasses, saying that a class or an instance conforms to a protocol is tantamount to saying that it has in its repertoire all the methods the protocol declares.

It’s possible to check whether an object conforms to a protocol by sending it a `conformsToProtocol:` message.

```
if ( [receiver conformsToProtocol:@protocol(ReferenceCounting)]  )
    [receiver incrementCount];
```

The `conformsToProtocol:` test is very much like the `respondsTo:` test for a single method, except that it tests whether a protocol has been adopted (and presumably all the methods it declares implemented) rather than just whether one particular method has been implemented. Because it checks for a whole list of methods, `conformsToProtocol:` can be more efficient than `respondsTo:`.

The `conformsToProtocol:` test is also very much like the `isKindOfClass:` test, except that it tests for a type based on a protocol rather than a type based on the inheritance hierarchy.

Type declarations for objects can be extended to include formal protocols. Protocols thus offer the possibility of another level of type checking by the compiler, one that’s more abstract since it’s not tied to particular implementations.

In a type declaration, protocol names are listed between angle brackets after the type name:

```objc
- (id <Formatting>)formattingService;
id <ReferenceCounting, AutoFreeing> anObject;
```

Just as static typing permits the compiler to test for a type based on the class hierarchy, this syntax permits the compiler to test for a type based on conformance to a protocol.

For example, if Formatter is an abstract class, this declaration

```
Formatter *anObject;
```

groups all objects that inherit from Formatter into a type and permits the compiler to check assignments against that type.

Similarly, this declaration,

```
id <Formatting> anObject;
```

groups all objects that conform to the Formatting protocol into a type, regardless of their positions in the class hierarchy. The compiler can make sure only objects that conform to the protocol are assigned to the type.

In each case, the type groups similar objects—either because they share a common inheritance, or because they converge on a common set of methods.

The two types can be combined in a single declaration:

```
Formatter <Formatting> *anObject;
```

Protocols can’t be used to type class objects. Only instances can be statically typed to a protocol, just as only instances can be statically typed to a class. (However, at runtime, both classes and instances will respond to a `conformsToProtocol:` message.)

One protocol can incorporate other protocols using the same syntax that classes use to adopt a protocol:

```objc
@protocol ProtocolName < protocol list >
```

All the protocols listed between angle brackets are considered part of the _ProtocolName_ protocol. For example, if the Paging protocol incorporates the Formatting protocol,

```objc
@protocol Paging < Formatting >
```

any object that conforms to the Paging protocol also conforms to Formatting. Type declarations

```
id <Paging> someObject;
```

and `conformsToProtocol:` messages

```
if ( [anotherObject conformsToProtocol:@protocol(Paging)] )
    ...
```

need to mention only the Paging protocol to test for conformance to Formatting as well.

When a class adopts a protocol, it must implement the methods the protocol declares, as mentioned earlier. In addition, it must conform to any protocols the adopted protocol incorporates. If an incorporated protocol incorporates still other protocols, the class must also conform to them. A class can conform to an incorporated protocol by either:

- Implementing the methods the protocol declares, or
- Inheriting from a class that adopts the protocol and implements the methods.

Suppose, for example, that the Pager class adopts the Paging protocol. If Pager is a subclass of `NSObject`,

```objc
@interface Pager : NSObject < Paging >
```

it must implement all the Paging methods, including those declared in the incorporated Formatting protocol. It adopts the Formatting protocol along with Paging.

On the other hand, if Pager is a subclass of Formatter (a class that independently adopts the Formatting protocol),

```objc
@interface Pager : Formatter < Paging >
```

it must implement all the methods declared in the Paging protocol proper, but not those declared in Formatting. Pager inherits conformance to the Formatting protocol from Formatter.

Note that a class can conform to a protocol without formally adopting it simply by implementing the methods declared in the protocol.

When working on complex applications, you occasionally find yourself writing code that looks like this:

```objc
#import "B.h"

@protocol A
- foo:(id <B>)anObject;
@end
```

where protocol B is declared like this:

```objc
#import "A.h"

@protocol B
- bar:(id <A>)anObject;
@end
```

In such a situation, circularity results and neither file will compile correctly. To break this recursive cycle, you must use the `@protocol` directive to make a forward reference to the needed protocol instead of importing the interface file where the protocol is defined. The following code excerpt illustrates how you would do this:

```objc
@protocol B;

@protocol A
- foo:(id <B>)anObject;
@end
```

Note that using the `@protocol` directive in this manner simply informs the compiler that “B” is a protocol to be defined later. It doesn’t import the interface file where protocol B is defined.

This section explains how static typing works and discusses some other features of Objective-C, including ways to temporarily overcome its inherent dynamism.

Objective-C objects are dynamic entities. As many decisions about them as possible are pushed from compile time to runtime:

- The memory for objects is _dynamically allocated_ at runtime by class methods that create new instances.
- Objects are _dynamically typed_. In source code (at compile time), any object pointer can be of type `id` no matter what the object’s class is. The exact class of an `id` variable (and therefore its particular methods and data structure) isn’t determined until the program runs.
- Messages and methods are _dynamically bound_, as described under [How Messaging Works](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznha4dqnbw). A runtime procedure matches the method selector in the message to a method implementation that “belongs to” the receiver.

These features give object-oriented programs a great deal of flexibility and power, but there’s a price to pay. Messages are somewhat slower than function calls, for example, (though not much slower due to the efficiency of the runtime system) and the compiler can’t check the exact types (classes) of `id` variables.

To permit better compile-time type checking, and to make code more self-documenting, Objective-C allows objects to be statically typed with a class name rather than generically typed as `id`. It also lets you turn some of its object-oriented features off in order to shift operations from runtime back to compile time.

If a pointer to a class name is used in place of `id` in an object declaration,

```
Rectangle *thisObject;
```

the compiler restricts the value of the declared variable to be either an instance of the class named in the declaration or an instance of a class that inherits from the named class. In the example above, `thisObject` can only be a Rectangle of some kind.

Statically typed objects have the same internal data structures as objects declared to be `id`s. The type doesn’t affect the object; it affects only the amount of information given to the compiler about the object and the amount of information available to those reading the source code.

Static typing also doesn’t affect how the object is treated at runtime. Statically typed objects are dynamically allocated by the same class methods that create instances of type `id`. If Square is a subclass of Rectangle, the following code would still produce an object with all the instance variables of a Square, not just those of a Rectangle:

```
Rectangle *thisObject = [[Square alloc] init];
```

Messages sent to statically typed objects are dynamically bound, just as objects typed `id` are. The exact type of a statically typed receiver is still determined at runtime as part of the messaging process. A `display` message sent to `thisObject`

```
[thisObject display];
```

performs the version of the method defined in the Square class, not the one in its Rectangle superclass.

By giving the compiler more information about an object, static typing opens up possibilities that are absent for objects typed `id`:

- In certain situations, it allows for compile-time type checking.
- It can free objects from the restriction that identically named methods must have identical return and argument types.
- It permits you to use the structure pointer operator to directly access an object’s instance variables.

The first two topics are discussed in the sections that follow. The third is covered in [Defining a Class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnzngeztsmjzgi).

With the additional information provided by static typing, the compiler can deliver better type-checking services in two situations:

- When a message is sent to a statically typed receiver, the compiler can make sure the receiver can respond. A warning is issued if the receiver doesn’t have access to the method named in the message.
- When a statically typed object is assigned to a statically typed variable, the compiler makes sure the types are compatible. A warning is issued if they’re not.

An assignment can be made without warning, provided the class of the object being assigned is identical to, or inherits from, the class of the variable receiving the assignment. The following example illustrates this:

```
Shape     *aShape;
Rectangle *aRect;

aRect = [[Rectangle alloc] init];
aShape = aRect;
```

Here `aRect` can be assigned to `aShape` because a Rectangle is a kind of Shape—the Rectangle class inherits from Shape. However, if the roles of the two variables are reversed and `aShape` is assigned to `aRect`, the compiler generates a warning; not every Shape is a Rectangle. (For reference, see [Figure 1-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznha3dkmbr), which shows the class hierarchy including Shape and Rectangle.)

There’s no check when the expression on either side of the assignment operator is an `id`. A statically typed object can be freely assigned to an `id`, or an `id` to a statically typed object. Because methods like `alloc` and `init` return `id`s, the compiler doesn’t ensure that a compatible object is returned to a statically typed variable. The following code is error-prone, but is allowed nonetheless:

```
Rectangle *aRect;
aRect = [[Shape alloc] init];
```


In general, methods in different classes that have the same selector (the same name) must also share the same return and argument types. This constraint is imposed by the compiler to allow dynamic binding. Because the class of a message receiver (and therefore class-specific details about the method it’s asked to perform), can’t be known at compile time, the compiler must treat all methods with the same name alike. When it prepares information on method return and argument types for the runtime system, it creates just one method description for each method selector.

However, when a message is sent to a statically typed object, the class of the receiver is known by the compiler. The compiler has access to class-specific information about the methods. Therefore, the message is freed from the restrictions on its return and argument types.

An instance can be statically typed to its own class or to any class that it inherits from. All instances, for example, can be statically typed as `NSObject`.

However, the compiler understands the class of a statically typed object only from the class name in the type designation, and it does its type checking accordingly. Typing an instance to an inherited class can therefore result in discrepancies between what the compiler thinks would happen at runtime and what actually happens.

For example, if you statically type a Rectangle instance as a Shape,

```
Shape *myRect = [[Rectangle alloc] init];
```

the compiler will treat it as a Shape. If you send the object a message to perform a Rectangle method,

```
BOOL solid = [myRect isFilled];
```

the compiler will complain. The `isFilled` method is defined in the Rectangle class, not in Shape.

However, if you send it a message to perform a method that the Shape class knows about,

```
[myRect display];
```

the compiler won’t complain, even though Rectangle overrides the method. At runtime, Rectangle’s version of the method is performed.

Similarly, suppose that the Upper class declares a `worry` method that returns a `double`,

```objc
- (double)worry;
```

and the Middle subclass of Upper overrides the method and declares a new return type:

```objc
- (int)worry;
```

If an instance is statically typed to the Upper class, the compiler will think that its `worry` method returns a `double`, and if an instance is typed to the Middle class, it will think that `worry` returns an `int`. Errors will obviously result if a Middle instance is typed to the Upper class. The compiler will inform the runtime system that a `worry` message sent to the object returns a `double`, but at runtime it actually returns an `int` and generates an error.

Static typing can free identically named methods from the restriction that they must have identical return and argument types, but it can do so reliably only if the methods are declared in different branches of the class hierarchy.

The only way to circumvent dynamic binding is to get the address of a method and call it directly as if it were a function. This might be appropriate on the rare occasions when a particular method will be performed many times in succession and you want to avoid the overhead of messaging each time the method is performed.

With a method defined in the `NSObject` class, `methodForSelector:`, you can ask for a pointer to the procedure that implements a method, then use the pointer to call the procedure. The pointer that `methodForSelector:` returns must be carefully cast to the proper function type. Both return and argument types should be included in the cast.

The example below shows how the procedure that implements the `setFilled:` method might be called:

```
void (*setter)(id, SEL, BOOL);
int i;

setter = (void (*)(id, SEL, BOOL))[target
    methodForSelector:@selector(setFilled:)];
for ( i = 0; i < 1000, i++ )
    setter(targetList[i], @selector(setFilled:), YES);
```

The first two arguments passed to the procedure are the receiving object (`self`) and the method selector (`_cmd`). These arguments are hidden in method syntax but must be made explicit when the method is called as a function.

Using `methodForSelector:` to circumvent dynamic binding saves most of the time required by messaging. However, the savings will be significant only where a particular message is repeated many times, as in the `for` loop shown above.

Note that `methodForSelector:` is provided by the Cocoa runtime system; it’s not a feature of the Objective-C language itself.

A fundamental tenet of object-oriented programming is that the data structure of an object is private to the object. Information stored there can be accessed only through messages sent to the object. Although it is generally considered a poor programming practice, there is a way to strip an object data structure of its “objectness” and treat it like any other C structure. This makes all the object’s instance variables publicly available.

When given a class name as an argument, the `@defs()` directive produces the declaration list for an instance of the class. This list is useful only in declaring structures, so `@defs()` can appear only in the body of a structure declaration. This code, for example, declares a structure that’s identical to the template for an instance of the Worker class:

```
struct workerDef {
    @defs(Worker)
} *public;
```

Here `public` is declared as a pointer to a structure that’s essentially indistinguishable from a Worker instance. With a little help from a type cast, a Worker `id` can be assigned to the pointer. The object’s instance variables can then be accessed publicly through the pointer:

```swift
id aWorker;
aWorker = [[Worker alloc] init];

public = (struct workerDef *)aWorker;
public->boss = nil;
```

This technique of turning an object into a structure makes all its instance variables public, whether they are declared `@private`, `@protected`, or `@public`.

Objects generally aren’t designed with the expectation that they be turned into C structures. You may want to use `@defs()` for classes you define entirely yourself, but it should not be applied to classes found in a framework or to classes you define that inherit from framework classes.

Objective-C provides support for exception handling and thread synchronization, which are explained in [Handling Exceptions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznge3tcnrsga) and [Synchronizing Thread Execution](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznge3tcmztgq). To turn on support for these features, use the `-fobjc-exceptions` switch of the GNU Compiler Collection (GCC) version 3.3 and later.

The Objective-C language has an exception-handling syntax similar to that of Java and C++. Coupled with the use of the `NSException`, `NSError`, or custom classes, you can add robust error-handling to your programs.

The exception support revolves around four compiler directives: `@try`, `@catch`, `@throw`, and `@finally`. Code that can potentially throw an exception is enclosed in a `@try` block. `@catch()`blocks contain the exception-handling logic for exceptions thrown in a `@try`block. A `@finally`block contains code that must be executed whether an exception is thrown or not. You use the `@throw`directive to throw an exception, which is essentially a pointer to an Objective-C object. You can use `NSException` objects but are not limited to them.

The example below depicts a simple exception-handling algorithm:

```
Cup *cup = [[Cup alloc] init];

@try {
    [cup fill];
}
@catch (NSException *exception) {
    NSLog(@"main: Caught %@: %@", [exception name], [exception  reason]);
}
@finally {
    [cup release];
}
```


To throw an exception you must instantiate an object with the appropriate information, such as the exception name and the reason it was thrown.

```
NSException *exception = [NSException exceptionWithName:@"HotTeaException"
                            reason:@"The tea is too hot"  userInfo:nil];
@throw exception;
```

Inside a `@catch()` block, you can re-throw the caught exception using the `@throw` directive without an argument. This can help make your code more readable.

You can subclass `NSException` to implement specialized types of exceptions, such as file-system exceptions or communications exceptions.

To catch an exception thrown in a `@try` block, use one or more `@catch()`blocks following the `@try` block. The `@catch()` blocks should be ordered from most-specific to the least-specific. That way you can tailor the processing of exceptions as groups, as shown in Listing 1-2.

__Listing 1-2__  An exception handler


```
@try {
    ...
}
@catch (CustomException *ce) {  // 1
    ...
}
@catch (NSException *ne) {  // 2
    // Perform processing necessary at this level.
    ...

    // Rethrow the exception so that it's handled at a higher level.
    @throw;  // 3
}
@catch (id ue) {
    ...
}
@finally {  // 4
    // Perform processing necessary whether an exception occurred  or not.
    ...
}
```

The following list describes the numbered code-lines:

1. Catches the most specific exception type.
2. Catches a more general exception type.
3. Re-throws the exception caught.

   To compartmentalize exception processing, you can nest exception handlers in a program. That way if a method or function catches an exception that it cannot process, it can rethrow it to the next exception handler.
4. Performs any clean-up processing that must always be performed, whether exceptions were thrown or not.

Objective-C supports multithreading in applications. This means that two threads can try to modify the same object at the same time, a situation that can cause serious problems in a program. To protect sections of code from being executed by more than one thread at a time, Objective-C provides the `@synchronized()` directive.

The `@synchronized()`directive locks a section of code for use by a single thread. Other threads are blocked until the thread exits the protected code; that is, when execution continues past the last statement in the `@synchronized()` block.

The `@synchronized()` directive takes as its only argument any Objective-C object, including `self`. This object is known as a _mutual exclusion_ semaphore or _mutex_. It allows a thread to lock a section of code to prevent its use by other threads. You should use separate semaphores to protect different critical sections of a program. It’s safest to create all the mutual exclusion objects before the application becomes multithreaded to avoid race conditions.

Listing 1-3 shows an example of code that uses `self` as the mutex to synchronize access to the instance methods of the current object. You can take a similar approach to synchronize the class methods of the associated class, using the Class object instead of `self`. In the latter case, of course, only one thread at a time is allowed to execute a class method because there is only one class object that is shared by all callers.

__Listing 1-3__  Locking a method using `self`

```objc
- (void)criticalMethod
{
    @synchronized(self) {
        // Critical code.
        ...
    }
}
```

Listing 1-4 uses the current selector, `_cmd`, as the mutex. This kind of synchronization is beneficial only when the method being synchronized has a unique name. This is because no other object or class would be allowed to execute a different method with the same name until the current method ends.

__Listing 1-4__  Locking a method using _cmd

```objc
- (void)criticalMethod
{
    @synchronized(NSStringFromSelector(_cmd)) {
        // Critical code.
        ...
    }
}
```

Listing 1-5 shows a general approach. Before executing a critical process, the code obtains a semaphore from the Account class and uses it to lock the critical section. The Account class could create the semaphore in its `initialize` method.

__Listing 1-5__  Locking a method using a custom semaphore

```
Account *account = [Account accountFromString:[accountField stringValue]];

// Get the semaphore.
id accountSemaphore = [Account semaphore];

@synchronized(accountSemaphore) {
    // Critical code.
    ...
}
```

The Objective-C synchronization feature supports recursive and reentrant code. A thread can use a single semaphore several times in a recursive manner; other threads are blocked from using it until the thread releases all the locks obtained with it; that is, every `@synchronized()` block is exited normally or through an exception.

When code in an `@synchronized()` block throws an exception, the Objective-C runtime catches the exception, releases the semaphore (so that the protected code can be executed by other threads), and re-throws the exception to the next exception handler.

Apple’s Objective-C compiler allows you to freely mix C++ and Objective-C code in the same source file. This Objective-C/C++ language hybrid is called Objective-C++. With it you can make use of existing C++ libraries from your Objective-C applications. Note that XCode requires that file names have a “.mm” extension for the Objective-C++ extensions to be enabled by the compiler.

Objective-C++ does not add C++ features to Objective-C classes, nor does it add Objective-C features to C++ classes. For example, you cannot use Objective-C syntax to call a C++ object, you cannot add constructors or destructors to an Objective-C object, and you cannot use the keywords `this` and `self` interchangeably. The class hierarchies are separate; a C++ class cannot inherit from an Objective-C class, and an Objective-C class cannot inherit from a C++ class. In addition, multi-language exception handling is not supported. That is, an exception thrown in Objective-C code cannot be caught in C++ code and, conversely, an exception thrown in C++ code cannot be caught in Objective-C code. For more information on exceptions in Objective-C, see [Exception Handling and Thread Synchronization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznge3dsobsgu).

The next section discusses what you _can_ do with Objective-C++.

In Objective-C++, you can call methods from either language in C++ code and in Objective-C methods. Pointers to objects in either language are just pointers, and as such can be used anywhere. For example, you can include pointers to Objective-C objects as data members of C++ classes, and you can include pointers to C++ objects as instance variables of Objective-C classes. [Listing 1-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnzngeytombvha) illustrates this.

__Listing 1-6__  Using C++ and Objective-C instances as instance variables

```objc
/* Hello.mm
 * Compile with: g++ -x objective-c++ -framework Foundation Hello.mm  -o hello
 */

#import <Foundation/Foundation.h>
class Hello {
    private:
        id _greeting_text;  // holds an NSString
    public:
        Hello() {
            _greeting_text = @"Hello, world!";
        }
        Hello(const char* greeting_text) {
            _greeting_text = [NSString stringWithUTF8String:greeting_text];
        }
        void say_hello() {
            printf("%s\n", [_greeting_text UTF8String]);
        }
};

@interface Greeting : NSObject {
    @private
        Hello *_hello;
}
- (id)init;
- (void)dealloc;
- (void)sayGreeting;
- (void)sayGreeting:(Hello*)greeting;
@end

@implementation Greeting
- (id)init {
    if (self = [super init]) {
        _hello = new Hello();
    }
    return self;
}
- (void)dealloc {
    delete _hello;
    [super dealloc];
}
- (void)sayGreeting {
    _hello->say_hello();
}
- (void)sayGreeting:(Hello*)greeting {
    greeting->say_hello();
}
@end

int main() {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];

    Greeting *greeting = [[Greeting alloc] init];
    [greeting sayGreeting];                         // > Hello,  world!

    Hello *hello = new Hello("Bonjour, monde!");
    [greeting sayGreeting:hello];                   // > Bonjour,  monde!

    delete hello;
    [greeting release];
    [pool release];
    return 0;
}
```

As you can declare C structs in Objective-C interfaces, you can also declare C++ classes in Objective-C interfaces. As with C structs, C++ classes defined within an Objective-C interface are globally-scoped, not nested within the Objective-C class. (This is consistent with the way in which standard C—though not C++—promotes nested struct definitions to file scope.)

To allow you to conditionalize your code based on the language variant, the Objective-C++ compiler defines both the `__cplusplus` and the `__OBJC__` preprocessor constants, as specified by (respectively) the C++ and Objective-C language standards.

As previously noted, Objective-C++ does not allow you to inherit C++ classes from Objective-C objects, nor does it allow you to inherit Objective-C classes from C++ objects.

```objc
class Base { /* ... */ };
@interface ObjCClass: Base ... @end // ERROR!
class Derived: public ObjCClass ... // ERROR!
```

Unlike Objective-C, objects in C++ are statically typed, with runtime polymorphism available as an exceptional case. The object models of the two languages are thus not directly compatible. More fundamentally, the layout of Objective-C and C++ objects in memory is mutually incompatible, meaning that it is generally impossible to create an object instance that would be valid from the perspective of both languages. Hence, the two type hierarchies cannot be intermixed.

You can declare a C++ class within an Objective-C class declaration. The compiler treats such classes as having been declared in the global namespace, as follows:

```objc
@interface Foo {
 class Bar { ... } // OK
}
@end

Bar *barPtr; // OK
```

Objective-C allows C structures (whether declared inside of an Objective-C declaration or not) to be used as instance variables.

```objc
@interface Foo {
   struct CStruct { ... };
   struct CStruct bigIvar; // OK
} ... @end
```

Objective-C++ similarly strives to allow C++ class instances to serve as instance variables. This is possible as long as the C++ class in question (along with all of its superclasses) does not have any virtual member functions defined. If any virtual member functions are present, the C++ class may not serve as an Objective-C instance variable.

```objc
#import <Cocoa/Cocoa.h>

struct Class0 { void foo(); };
struct Class1 { virtual void foo(); };
struct Class2 { Class2(int i, int j); };

@interface Foo : NSObject {
    Class0 class0;      // OK
    Class1 class1;      // ERROR!
    Class1 *ptr;        // OK—call 'ptr = new Class1()' from Foo'  init,
                        // 'delete ptr' from Foo's dealloc
    Class2 class2;      // WARNING - constructor not called!
...
@end
```

C++ requires each instance of a class containing virtual functions to contain a suitable virtual function table pointer. However, the Objective-C runtime cannot initialize the virtual function table pointer, because it is not familiar with the C++ object model. Similarly, the Objective-C runtime cannot dispatch calls to C++ constructors or destructors for those objects. If a C++ class has any user-defined constructors or destructors, they are not called. The compiler emits a warning in such cases.

Objective-C does not have a notion of nested namespaces. You cannot declare Objective-C classes within C++ namespaces, nor can you declare namespaces within Objective-C classes.

Objective-C classes, protocols, and categories cannot be declared inside a C++ template, nor can a C++ template be declared inside the scope of an Objective-C interface, protocol, or category.

However, Objective-C classes may serve as C++ template parameters. C++ template parameters can also be used as receivers or parameters (though not as selectors) in Objective-C message expressions.

There are a few identifiers that are defined in the Objective-C header files that every Objective-C program must include. These identifiers are `id`, `Class`, `SEL`, `IMP`, and `BOOL`.

Inside an Objective-C method, the compiler predeclares the identifiers `self` and `super`, similarly to the keyword `this` in C++. However, unlike the C++ `this` keyword, `self` and `super` are context-sensitive; they may be used as ordinary identifiers outside of Objective-C methods.

In the parameter list of methods within a protocol, there are five more context-sensitive keywords (`oneway`, `in`, `out`, `inout`, and `bycopy`). These are not keywords in any other contexts.

From an Objective-C programmer's point of view, C++ adds quite a few new keywords. You can still use C++ keywords as a part of an Objective-C selector, so the impact isn’t too severe, but you cannot use them for naming Objective-C classes or instance variables. For example, even though `class` is a C++ keyword, you can still use the `NSObject` method `class`:

```
[foo class]; // OK
```

However, because it is a keyword, you cannot use `class` as the name of a variable:

```
NSObject *class; // Error
```

In Objective-C, the names for classes and categories live in separate namespaces. That is, both `@interface foo` and `@interface(foo)` can exist in the same source code. In Objective-C++, you can also have a category whose name matches that of a C++ class or structure.

Protocol and template specifiers use the same syntax for different purposes:

```
id<someProtocolName> foo;
TemplateType<SomeTypeName> bar;
```

To avoid this ambiguity, the compiler doesn’t permit `id` to be used as a template name.

Finally, there is a lexical ambiguity in C++ when a label is followed by an expression that mentions a global name, as in:

```
label: ::global_name = 3;
```

The space after the first colon is required. Objective-C++ adds a similar case, which also requires a space:

```
receiver selector: ::global_c++_name;
```

[Next](The%20Runtime%20System.md)[Previous](Introduction%20to%20The%20Objective-C%20Programming%20Language%201.0.md)

