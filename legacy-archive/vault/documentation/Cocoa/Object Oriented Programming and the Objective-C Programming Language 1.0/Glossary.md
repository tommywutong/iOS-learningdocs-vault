---
title: Object Oriented Programming and the Objective-C Programming Language 1.0
apple_id: TP40005191
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OOPandObjC1/Articles/ocGlossary.html
archived_at: '2026-07-15T07:17:21.871807Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Object Oriented Programming and the Objective-C Programming Language 1.0](Introduction%20to%20The%20Objective-C%20Programming%20Language%201.0.md)


[Next](Document%20Revision%20History.md)[Previous](Grammar.md)

# Glossary

- __abstract class__

  A class that’s defined solely so that other classes can inherit from it. Programs don’t use instances of an abstract class, only of its subclasses.

- __abstract superclass__

  Same as [abstract class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnjnijauur2iivcee).

- __adopt__

  In the Objective-C language, a class is said to adopt a protocol if it declares that it implements all the methods in the protocol. Protocols are adopted by listing their names between angle brackets in a class or category declaration.

- __anonymous object__

  An object of unknown class. The interface to an anonymous object is published through a protocol declaration.

- __Application Kit__

  A Cocoa framework that implements an application's user interface. The Application Kit provides a basic program structure for applications that draw on the screen and respond to events.

- __archiving__

  The process of preserving a data structure, especially an object, for later use. An archived data structure is usually stored in a file, but it can also be written to memory, copied to the pasteboard, or sent to another application. In Cocoa, archiving involves writing data to an `NSData` object.

- __asynchronous message__

  A remote message that returns immediately, without waiting for the application that receives the message to respond. The sending application and the receiving application act independently, and are therefore not “in sync.” See also [synchronous message](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnjnijauurcki5feo).

- __category__

  In the Objective-C language, a set of method definitions that is segregated from the rest of the class definition. Categories can be used to split a class definition into parts or to add methods to an existing class.

- __class__

  In the Objective-C language, a prototype for a particular kind of object. A class definition declares instance variables and defines methods for all members of the class. Objects that have the same types of instance variables and have access to the same methods belong to the same class. See also [class object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnjnijauurceinbeo).

- __class method__

  In the Objective-C language, a method that can operate on class objects rather than instances of the class.

- __class object__

  In the Objective-C language, an object that represents a class and knows how to create new instances of the class. Class objects are created by the compiler, lack instance variables, and can’t be statically typed, but otherwise behave like all other objects. As the receiver in a message expression, a class object is represented by the class name.

- __Cocoa__

  An advanced object-oriented development platform on Mac OS X. Cocoa is a set of frameworks with programming interfaces in both Java and Objective-C.

- __compile time__

  The time when source code is compiled. Decisions made at compile time are constrained by the amount and kind of information encoded in source files.

- __conform__

  In the Objective-C language, a class is said to conform to a protocol if it (or a superclass) implements the methods declared in the protocol. An instance conforms to a protocol if its class does. Thus, an instance that conforms to a protocol can perform any of the instance methods declared in the protocol.

- __content view__

  In the Application Kit, the `NSView` object that’s associated with the content area of a window—all the area in the window excluding the title bar and border. All other views in the window are arranged in a hierarchy beneath the content view.

- __delegate__

  An object that acts on behalf of another object.

- __designated initializer__

  The `init...` method that has primary responsibility for initializing new instances of a class. Each class defines or inherits its own designated initializer. Through messages to `self`, other `init...` methods in the same class directly or indirectly invoke the designated initializer, and the designated initializer, through a message to `super`, invokes the designated initializer of its superclass.

- __dispatch table__

  Objective-C runtime table that contains entries that associate method selectors with the class-specific addresses of the methods they identify.

- __distributed objects__

  Architecture that facilitates communication between objects in different address spaces.

- __dynamic allocation__

  Technique used in C-based languages where the operating system provides memory to a running application as it needs it, instead of when it launches.

- __dynamic binding__

  Binding a method to a message—that is, finding the method implementation to invoke in response to the message—at runtime, rather than at compile time.

- __dynamic typing__

  Discovering the class of an object at runtime rather than at compile time.

- __encapsulation__

  Programming technique that hides the implementation of an operation from its users behind an abstract interface. This allows the implementation to be updated or changed without impacting the users of the interface.

- __event__

  The direct or indirect report of external activity, especially user activity on the keyboard and mouse.

- __factory__

  Same as [class object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnjnijauurceinbeo).

- __factory method__

  Same as [class method](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnjnijauurcbjbcuk).

- __factory object__

  Same as [class object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnjnijauurceinbeo).

- __formal protocol__

  In the Objective-C language, a protocol that’s declared with the `@protocol` directive. Classes can adopt formal protocols, objects can respond at runtime when asked if they conform to a formal protocol, and instances can be typed by the formal protocols they conform to.

- __framework__

  A way to package a logically-related set of classes, protocols and functions together with localized strings, on-line documentation, and other pertinent files. Cocoa provides the Foundation framework and the Application Kit framework, among others. Frameworks are sometimes referred to as “kits.”

- __gdb__

  The standard Mac OS X debugging tool.

- __id__

  In the Objective-C language, the general type for any kind of object regardless of class. `id` is defined as a pointer to an object data structure. It can be used for both class objects and instances of a class.

- __implementation__

  Part of an Objective-C class specification that defines its implementation. This section defines both public methods as well as private methods—methods that are not declared in the class’s interface.

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

  Part of an Objective-C class specification that declares its public interface, which include its superclass name, instances variables, and public-method prototypes.

- __Interface Builder__

  A tool that lets you graphically specify your application’s user interface. It sets up the corresponding objects for you and makes it easy for you to establish connections between these objects and your own code where needed.

- __introspection__

  The ability of an object to reveal information about itself as an object—such as its class and superclass, the messages it can respond to, and the protocols it conforms to.

- __key window__

  The window in the active application that receives keyboard events and is the focus of user activity.

- __link time__

  The time when files compiled from different source modules are linked into a single program. Decisions made by the linker are constrained by the compiled code and ultimately by the information contained in source code.

- __localize__

  To adapt an application to work under various local conditions—especially to have it use a language selected by the user. Localization entails freeing application code from language-specific and culture-specific references and making it able to import localized resources (such as character strings, images, and sounds). For example, an application localized in Spanish would display “Salir” in the application menu. In Italian, it would be “Esci,” in German “Verlassen,” and in English “Quit.”

- __main event loop__

  The principal control loop for applications that are driven by events. From the time it’s launched until the moment it’s terminated, an application gets one keyboard or mouse event after another from the Window Manager and responds to them, waiting between events if the next event isn’t ready. In the Application Kit, the `NSApplication` object runs the main event loop.

- __menu__

  A small window that displays a list of commands. Only menus for the active application are visible on-screen.

- __message__

  In object-oriented programming, the method selector (name) and accompanying arguments that tell the receiving object in a message expression what to do.

- __message expression__

  In object-oriented programming, an expression that sends a message to an object. In the Objective-C language, message expressions are enclosed within square brackets and consist of a receiver followed by a message (method selector and arguments).

- __method__

  In object-oriented programming, a procedure that can be executed by an object.

- __multiple inheritance__

  In object-oriented programming, the ability of a class to have more than one superclass—to inherit from different sources and thus combine separately-defined behaviors in a single class. Objective-C doesn’t support multiple inheritance.

- __mutex__

  Also known as mutual exclusion semaphore. Used to synchronize thread execution.

- __name space__

  A logical subdivision of a program within which all names must be unique. Symbols in one name space won’t conflict with identically named symbols in another name space. For example, in Objective-C, the instance methods of each class are in a separate name space, as are the class methods and instance variables.

- __nil__

  In the Objective-C language, an object `id` with a value of 0.

- __object__

  A programming unit that groups together a data structure (instance variables) and the operations (methods) that can use or affect that data. Objects are the principal building blocks of object-oriented programs.

- __outlet__

  An instance variable that points to another object. Outlet instance variables are a way for an object to keep track of the other objects to which it may need to send messages.

- __polymorphism__

  In object-oriented programming, the ability of different objects to respond, each in its own way, to the same message.

- __procedural programming language__

  A language, like C, that organizes a program as a set of procedures that have definite beginnings and ends.

- __protocol__

  In the Objective-C language, the declaration of a group of methods not associated with any particular class. See also [formal protocol](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnjnijauurshinduq) and [informal protocol](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnjnijauuqsjizeuq).

- __receiver__

  In object-oriented programming, the object that is sent a message.

- __reference counting__

  Memory-management technique in which each entity that claims ownership of an object increments the object’s reference count and later decrements it. When the object’s reference count reaches zero, the object is deallocated. This technique allows one instance of an object to be safely shared among several other objects.

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

  In the Objective-C language, any class that’s one step below another class in the inheritance hierarchy. Occasionally used more generally to mean any class that inherits from another class, and sometimes also used as a verb to mean the process of defining a subclass of another class.

- __superclass__

  In the Objective-C language, a class that’s one step above another class in the inheritance hierarchy; the class through which a subclass inherits methods and instance variables.

- __surrogate__

  An object that stands in for and forwards messages to another object.

- __synchronous message__

  A remote message that doesn’t return until the receiving application finishes responding to the message. Because the application that sends the message waits for an acknowledgment or return information from the receiving application, the two applications are kept “in sync.” See also [asynchronous message](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnjnijauursjirceo).

[Next](Document%20Revision%20History.md)[Previous](Grammar.md)

