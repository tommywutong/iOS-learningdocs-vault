---
title: The Objective-C Programming Language
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocGlossary.html
archived_at: '2026-07-15T07:17:30.401070Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [The Objective-C Programming Language](Introduction.md)


[Previous](Document%20Revision%20History.md)

# Glossary

- __abstract class__

  A class that’s defined solely so that other classes can inherit from it. Programs don’t use instances of an abstract class; they use only instances of its subclasses.

- __abstract superclass__

  Same as [abstract class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqnjnijauur2iivcee).

- __adopt__

  In the Objective-C language, a class is said to adopt a protocol if it declares that it implements all the methods in the protocol. Protocols are adopted by listing their names between angle brackets in a class or category declaration.

- __anonymous object__

  An object of unknown class. The interface to an anonymous object is published through a protocol declaration.

- __AppKit__

  Sometimes called _Application Kit_. A Cocoa framework that implements an application's user interface. AppKit provides a basic program structure for applications that draw on the screen and respond to events.

- __asynchronous message__

  A remote message that returns immediately, without waiting for the application that receives the message to respond. The sending application and the receiving application act independently, and are therefore not in sync. Compare [synchronous message](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqnjnijauurcki5feo).

- __category__

  In the Objective-C language, a set of method definitions that is segregated from the rest of the class definition. Categories can be used to split a class definition into parts or to add methods to an existing class.

- __class__

  In the Objective-C language, a prototype for a particular kind of object. A class definition declares instance variables and defines methods for all members of the class. Objects that have the same types of instance variables and have access to the same methods belong to the same class. See also [class object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqnjnijauurceinbeo).

- __class method__

  In the Objective-C language, a method that can operate on class objects rather than instances of the class.

- __class object__

  In the Objective-C language, an object that represents a class and knows how to create new instances of the class. Class objects are created by the compiler, lack instance variables, and can’t be statically typed, but otherwise behave like all other objects. As the receiver in a message expression, a class object is represented by the class name.

- __Cocoa__

  An advanced object-oriented development platform in OS X. Cocoa is a set of frameworks whose primary programming interfaces are in Objective-C.

- __compile time__

  The time when source code is compiled. Decisions made at compile time are constrained by the amount and kind of information encoded in source files.

- __conform__

  In the Objective-C language, a class is said to conform to a protocol if it (or a superclass) implements the methods declared in the protocol. An instance conforms to a protocol if its class does. Thus, an instance that conforms to a protocol can perform any of the instance methods declared in the protocol.

- __delegate__

  An object that acts on behalf of another object.

- __designated initializer__

  The `init...` method that has primary responsibility for initializing new instances of a class. Each class defines or inherits its own designated initializer. Through messages to `self`, other `init...` methods in the same class directly or indirectly invoke the designated initializer, and the designated initializer, through a message to `super`, invokes the designated initializer of its superclass.

- __dispatch table__

  The Objective-C runtime table that contains entries that associate method selectors with the class-specific addresses of the methods they identify.

- __distributed objects__

  An architecture that facilitates communication between objects in different address spaces.

- __dynamic allocation__

  A technique used in C-based languages where the operating system provides memory to a running application as it needs it, instead of when it launches.

- __dynamic binding__

  Binding a method to a message—that is, finding the method implementation to invoke in response to the message—at runtime, rather than at compile time.

- __dynamic typing__

  Discovering the class of an object at runtime rather than at compile time.

- __encapsulation__

  A programming technique that hides the implementation of an operation from its users behind an abstract interface. It allows the implementation to be updated or changed without impacting the users of the interface.

- __event__

  The direct or indirect report of external activity, especially user activity on the keyboard and mouse.

- __factory__

  Same as [class object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqnjnijauurceinbeo).

- __factory object__

  Same as [class object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqnjnijauurceinbeo).

- __formal protocol__

  In the Objective-C language, a protocol that’s declared with the `@protocol` directive. Classes can adopt formal protocols, objects can respond at runtime when asked if they conform to a formal protocol, and instances can be typed by the formal protocols they conform to.

- __framework__

  A way to package a logically related set of classes, protocols, and functions together with localized strings, online documentation, and other pertinent files. Cocoa provides the Foundation framework and the AppKit framework, among others.

- __id__

  In the Objective-C language, the general type for any kind of object regardless of class. `id` is defined as a pointer to an object data structure. It can be used for both class objects and instances of a class.

- __implementation__

  The part of an Objective-C class specification that defines public methods (those declared in the class’s interface) as well as private methods (those not declared in the class’s interface).

- __informal protocol__

  In the Objective-C language, a protocol declared as a category, usually as a category of the `NSObject` class. The language gives explicit support to formal protocols, but not to informal ones.

- __inheritance__

  In object-oriented programming, the ability of a superclass to pass its characteristics (methods and instance variables) on to its subclasses.

- __inheritance hierarchy__

  In object-oriented programming, the hierarchy of classes that’s defined by the arrangement of superclasses and subclasses. Every class (except root classes such as `NSObject`) has a superclass, and any class may have an unlimited number of subclasses. Through its superclass, each class inherits from those above it in the hierarchy.

- __instance__

  In the Objective-C language, an object that belongs to (is a member of) a particular class. Instances are created at runtime according to the specification in the class definition.

- __instance method__

  In the Objective-C language, any method that can be used by an instance of a class rather than by the class object.

- __instance variable__

  In the Objective-C language, any variable that’s part of the internal data structure of an instance. Instance variables are declared in a class definition and become part of all objects that are members of or inherit from the class.

- __interface__

  The part of an Objective-C class specification that declares its public interface, which includes its superclass name, instances variables, and public-method prototypes.

- __Interface Builder__

  A tool that lets you graphically specify your application’s user interface. It sets up the corresponding objects for you and makes it easy for you to establish connections between these objects and your own code where needed.

- __link time__

  The time when files compiled from different source modules are linked into a single program. Decisions made by the linker are constrained by the compiled code and ultimately by the information contained in source code.

- __message__

  In object-oriented programming, the method selector (name) and accompanying parameters that tell the receiving object in a message expression what to do.

- __message expression__

  In object-oriented programming, an expression that sends a message to an object. In the Objective-C language, message expressions are enclosed within square brackets and consist of a receiver followed by a message (method selector and parameters).

- __method__

  In object-oriented programming, a procedure that can be executed by an object.

- __mutex__

  Short for _mutual exclusion semaphore_. An object used to synchronize thread execution.

- __namespace__

  A logical subdivision of a program within which all names must be unique. Symbols in one namespace do not conflict with identically named symbols in another namespace. For example, in Objective-C, the instance methods of a class are in a unique namespace for the class. Similarly, the class methods of a class are in their own namespace, and the instance variables of a class are in their own namespace.

- __nil__

  In the Objective-C language, an object `id` with a value of 0.

- __object__

  A programming unit that groups together a data structure (instance variables) and the operations (methods) that can use or affect that data. Objects are the principal building blocks of object-oriented programs.

- __outlet__

  An instance variable that points to another object. Outlet instance variables are a way for an object to keep track of the other objects to which it may need to send messages.

- __polymorphism__

  In object-oriented programming, the ability of different objects to respond, each in its own way, to the same message.

- __procedural programming language__

  A language, such as C, that organizes a program as a set of procedures that have definite beginnings and ends.

- __protocol__

  In the Objective-C language, the declaration of a group of methods not associated with any particular class. See also [formal protocol](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqnjnijauurshinduq), [informal protocol](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqnjnijauuqsjizeuq).

- __receiver__

  In object-oriented programming, the object that is sent a message.

- __reference counting__

  A memory-management technique in which each entity that claims ownership of an object increments the object’s reference count and later decrements it. When the object’s reference count reaches zero, the object is deallocated. This technique allows one instance of an object to be safely shared among several other objects.

- __remote message__

  A message sent from one application to an object in another application.

- __remote object__

  An object in another application, one that’s a potential receiver for a remote message.

- __runtime__

  The time after a program is launched and while it’s running. Decisions made at runtime can be influenced by choices the user makes.

- __selector__

  In the Objective-C language, the name of a method when it’s used in a source-code message to an object, or the unique identifier that replaces the name when the source code is compiled. Compiled selectors are of type `SEL`.

- __static typing__

  In the Objective-C language, giving the compiler information about what kind of object an instance is, by typing it as a pointer to a class.

- __subclass__

  In the Objective-C language, any class that’s one step below another class in the inheritance hierarchy. Occasionally used more generally to mean any class that inherits from another class. Also used as a verb to mean the process of defining a subclass of another class.

- __superclass__

  In the Objective-C language, a class that’s one step above another class in the inheritance hierarchy; the class through which a subclass inherits methods and instance variables.

- __synchronous message__

  A remote message that doesn’t return until the receiving application finishes responding to the message. Because the application that sends the message waits for an acknowledgment or return information from the receiving application, the two applications are kept in sync. Compare [asynchronous message](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqnjnijauursjirceo).

[Previous](Document%20Revision%20History.md)

