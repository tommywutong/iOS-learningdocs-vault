---
title: Object-Oriented Programming with Objective-C
apple_id: TP40005149
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2010-11-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OOP_ObjC/Articles/ooStructuringPrograms.html
archived_at: '2026-07-15T07:17:21.344398Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Object-Oriented Programming with Objective-C](Introduction.md)


[Next](Structuring%20the%20Programming%20Task.md)[Previous](The%20Object%20Model.md)

# Structuring Programs

Object-oriented programs have two kinds of structure. One can be seen in the inheritance hierarchy of class definitions. The other is evident in the pattern of message passing as the program runs. These messages reveal a network of object connections.

- The inheritance hierarchy explains how objects are related by type. For example, in the program that models water use, it might turn out that faucets and pipes are the same kind of object, except that faucets can be turned on and off and pipes can have multiple connections to other pipes. This similarity would be captured in the program design if the `Faucet` and `Pipe` classes inherit from a common superclass.
- The network of object connections explains how the program works. For example, `Appliance` objects might send messages requesting water to valves, and valves to pipes. Pipes might communicate with the `Building` object, and the `Building` object with all the valves, faucets, and pipes, but not directly with appliances. To communicate with each other in this way, objects must know about each other. An `Appliance` object would need a connection to a `Valve` object, and a `Valve` object to a `Pipe` object, and so on. These connections define a program structure.

Object-oriented programs are designed by laying out the network of objects with their behaviors and patterns of interaction and by arranging the hierarchy of classes. There’s structure both in the program’s activity and in its definition.

Part of the task of designing an object-oriented program is to arrange the object network. The network doesn’t have to be static; it can change dynamically as the program runs. Relationships between objects can be improvised as needed, and the cast of objects that play assigned roles can change from time to time. But there has to be a script.

Some connections can be entirely transitory. A message might contain a parameter identifying an object, perhaps the sender of the message, that the receiver can communicate with. As it responds to the message, the receiver can send messages to that object, perhaps identifying itself or still another object that the object can in turn communicate with. Such connections are fleeting; they last only as long as the chain of messages.

But not all connections between objects can be handled on the fly. Some need to be recorded in program data structures. There are various ways to do this. A table might be kept of object connections, or there might be a service that identifies objects by name. However, the simplest way is for each object to have  instance variables that keep track of the other objects it must communicate with. These instance variables—termed _outlets_
 because they record the outlets for messages—define the principal connections between objects in the program network.

Although the names of outlet instance variables are arbitrary, they generally reflect the roles that outlet objects play. Figure 4-1 illustrates an object with four outlets—an agent, a friend, a neighbor, and a boss. The objects that play these parts may change every now and then, but the roles remain the same.

__Figure 4-1__  Outlets

!

Some outlets are set when the object is first initialized and may never change. Others might be set automatically as the consequence of other actions. Still others can be set freely, using methods provided just for that purpose.

However they’re set, outlet instance variables reveal the structure of the application. They link objects into a communicating network, much as the components of a water system are linked by their physical connections or as individuals are linked by their patterns of social relations.

Outlet connections can capture many different kinds of relationships between objects. Sometimes the connection is between objects that communicate more or less as equal partners in an application, each with its own role to play and neither dominating the other. For example, an `Appliance` object might have an outlet instance variable to keep track of the valve it’s connected to.

Sometimes one object should be seen as being part of another. For example, a `Faucet` object might use a `Meter` object to measure the amount of water being released. The `Meter` object would serve no other object and would act only under orders from the `Faucet` object. It would be an intrinsic part of the `Faucet` object, in contrast to an `Appliance` object’s extrinsic connection to a `Valve` object.

Similarly, an object that oversees other objects might keep a list of its charges. A `Building` object, for example, might have a list of all the `Pipe` objects in the program. The `Pipe` objects would be considered an intrinsic part of the `Building` object and belong to it. `Pipe` objects, on the other hand, would maintain extrinsic connections to each other.

Intrinsic outlets behave differently from extrinsic ones. When an object is freed or archived in a file on disk, the objects that its intrinsic outlets point to must be freed or archived with it. For example, when a faucet is freed, its meter is rendered useless and therefore should be freed as well. A faucet archived without its meter would be of little use when it’s unarchived (unless it could create a new `Meter` object for itself).

Extrinsic outlets, on the other hand, capture the organization of the program at a higher level. They record connections between relatively independent program subcomponents. When an `Appliance` object is freed, the `Valve` object it was connected to still is of use and remains in place. When an `Appliance` object is unarchived, it can be connected to another valve and resume playing the same sort of role it played before.

The object network is set into motion by an external stimulus. If you’re writing an interactive application with a user interface, it will respond to user actions on the keyboard and mouse. A program that tries to factor very large numbers might start when you pass it a target number on the command line. Other programs might respond to data received over a phone line, information obtained from a database, or information about the state of a mechanical process the program monitors.

Programs often are activated by a flow of _events_, which are reports of external activity of some sort. Applications that display a user interface are driven by events from the keyboard and mouse. Every press of a key or click of the mouse generates events that the application receives and responds to. An object-oriented program structure (a network of objects that’s prepared to respond to an external stimulus) is ideally suited for this kind of user-driven application.

Another part of the design task is deciding the arrangement of classes—when to add functionality to an existing class by defining a subclass and when to define an independent class. The problem can be clarified by imagining what would happen in the extreme case:

- It’s possible to conceive of a program consisting of just one object. Because it’s the only object, it can send messages only to itself. It therefore can’t take advantage of polymorphism, or the modularity of a variety of classes, or a program design conceived as a network of interconnected objects. The true structure of the program would be hidden inside the class definition. Despite being written in an object-oriented language, there would be very little that was object-oriented about it.
- On the other hand, it’s also possible to imagine a program that consists of hundreds of different kinds of objects, each with very few methods and limited functionality. Here, too, the structure of the program would be lost, this time in a maze of object connections.

Obviously, it’s best to avoid either of these extremes, to keep objects large enough to take on a substantial role in the program but small enough to keep that role well-defined. The structure of the program should be easy to grasp in the pattern of object connections.

Nevertheless, the question often arises of whether to add more functionality to a class or to factor out the additional functionality and put it in a separate class definition. For example, a `Faucet` object needs to keep track of how much water is being used over time. To do that, you could either implement the necessary methods in the `Faucet` class, or you could devise a generic `Meter` object to do the job, as suggested earlier. Each `Faucet` object would have an outlet connecting it to a `Meter` object, and the meter would not interact with any object but the faucet.

The choice often depends on your design goals. If the `Meter` object could be used in more than one situation, perhaps in another project entirely, it would increase the reusability of your code to factor the metering task into a separate class. If you have reason to make `Faucet` objects as self-contained as possible, the metering functionality could be added to the `Faucet` class.

It’s generally better to try for reusable code and avoid having large classes that do so many things that they can’t be adapted to other situations. When objects are designed as components, they become that much more reusable. What works in one system or configuration might well work in another.

Dividing functionality between different classes doesn’t necessarily complicate the programming interface. If the `Faucet` class keeps the `Meter` object private, the `Meter` interface wouldn’t have to be published for users of the `Faucet` class; the object would be as hidden as any other `Faucet` instance variable.

Objects combine state and behavior, and so resemble things in the real world. Because they resemble real things, designing an object-oriented program is very much like thinking about real things—what they do, how they work, and how one thing is connected to another.

When you design an object-oriented program, you are, in effect, putting together a computer simulation of how something works. Object networks look and behave like models of real systems. An object-oriented program can be thought of as a model, even if there’s no actual counterpart to it in the real world.

Each component of the model—each kind of object—is described in terms of its behavior, responsibilities, and interactions with other components. Because an object’s interface lies in its methods, not its data, you can begin the design process by thinking about what a system component must do, not how it’s represented in data. Once the behavior of an object is decided, the appropriate data structure can be chosen, but this is a matter of implementation, not the initial design.

For example, in the water-use program, you wouldn’t begin by deciding what the `Faucet` data structure looked like, but what you wanted a `Faucet` object to do—make a connection to a pipe, be turned on and off, adjust the rate of flow, and so on. The design is therefore not bound from the outset by data choices. You can decide on the behavior first and implement the data afterwards. Your choice of data structures can change over time without affecting the design.

Designing an object-oriented program doesn’t necessarily entail writing great amounts of code. The reusability of class definitions means that the opportunity is great for building a program largely out of classes devised by others. It might even be possible to construct interesting programs entirely out of classes someone else defined. As the suite of class definitions grows, you have more and more reusable parts to choose from.

Reusable classes come from many sources. Development projects often yield reusable class definitions, and some enterprising developers market them. Object-oriented programming environments typically come with class libraries. There are well over a thousand classes in the Cocoa libraries. Some of these classes offer basic services (hashing, data storage, remote messaging). Others are more specific (user interface devices, video displays, sound).

Typically, a group of library classes work together to define a partial program structure. These classes constitute a software framework (or kit) that can be used to build a variety of different kinds of applications. When you use a framework, you accept the program model it provides and adapt your design to it. You use the framework by:

- Initializing and arranging instances of framework classes
- Defining subclasses of framework classes
- Defining new classes of your own to work with classes defined in the framework

In each of these ways, you not only adapt your program to the framework, but you also adapt the generic framework structure to the specialized purposes of your application.

The framework, in essence, sets up part of an object network for your program and provides part of its class hierarchy. Your own code completes the program model started by the framework.

[Next](Structuring%20the%20Programming%20Task.md)[Previous](The%20Object%20Model.md)

