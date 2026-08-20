---
title: Object-Oriented Programming with Objective-C
apple_id: TP40005149
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2010-11-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OOP_ObjC/Articles/ooStructuringTask.html
archived_at: '2026-07-15T07:17:21.845954Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Object-Oriented Programming with Objective-C](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Structuring%20Programs.md)

# Structuring the Programming Task

Object-oriented programming not only structures programs in a better way, it also helps structure the programming task.

As software tries to do more and more, and programs become bigger and more complicated, the problem of managing the task also grows. There are more pieces to fit together and more people working together to build them. The object-oriented approach offers ways of dealing with this complexity, not just in design, but also in the organization of the work.

Complex software requires an extraordinary collaborative effort among people who must be individually creative, yet still make what they do fit exactly with what others are doing.

The sheer size of the effort and the number of people working on the same project at the same time in the same place can get in the way of the group’s ability to work cooperatively towards a common goal. In addition, collaboration is often impeded by barriers of time, space, and organization:

- Code must be maintained, improved, and used long after it’s written. Programmers who collaborate on a project may not be working on it at the same time, so they may not be in a position to talk things over and keep each other informed about details of the implementation.
- Even if programmers work on the same project at the same time, they may not be located in the same place. This also inhibits how closely they can work together.
- Programmers working in different groups with different priorities and different schedules often must collaborate on projects. Communication across organizational barriers isn’t always easy to achieve.

The answer to these difficulties must grow out of the way programs are designed and written. It can’t be imposed from the outside in the form of hierarchical management structures and strict levels of authority. These often get in the way of people’s creativity, and become burdens in and of themselves. Rather, collaboration must be built into the work itself.

That’s where object-oriented programming techniques can help. For example, the reusability of object-oriented code means that programmers can collaborate effectively, even when they work on different projects at different times or are in different organizations, just by sharing their code in libraries. This kind of collaboration holds a great deal of promise, for it can conceivably lighten difficult tasks and make seemingly impossible projects achievable.

Object-oriented programming helps restructure the programming task in ways that benefit collaboration. It helps eliminate the need to collaborate on low-level implementation details, while providing structures that facilitate collaboration at a higher level. Almost every feature of the object model, from the possibility of large-scale design to the increased reusability of code, has consequences for the way people work together.

When programs are designed at a high level of abstraction, the division of labor is more easily conceived. It can match the division of the program on logical lines; the way a project is organized can grow out of its design.

With an object-oriented design, it’s easier to keep common goals in sight, instead of losing them in the implementation, and easier for everyone to see how the piece they’re working on fits into the whole. Their collaborative efforts are therefore more likely to be on target.

The connections between the various components of an object-oriented program are worked out early in the design process. They can be well-defined, at least for the initial phase of development, before implementation begins.

During implementation, only this interface needs to be coordinated, and most of that falls naturally out of the design. Because each class encapsulates its implementation and has its own namespace, there’s no need to coordinate implementation details. Collaboration is simpler when there are fewer coordination requirements.

The modularity of object-oriented programming means that the logical components of a large program can each be implemented separately. Different people can work on different classes. Each implementation task is isolated from the others.

Modularity has benefits, not just for organizing the implementation, but for fixing problems later. Because implementations are contained within class boundaries, problems that come up are also likely to be isolated. It’s easier to track down bugs when they’re located in a well-defined part of the program.

Separating responsibilities by class also means that each part can be worked on by specialists. Classes can be updated periodically to optimize their performance and make the best use of new technologies. These updates don’t have to be coordinated with other parts of the program. As long as the interface to an object doesn’t change, improvements to its implementation can be scheduled at any time.

The polymorphism of object-oriented programs yields simpler programming interfaces, since the same names and conventions can be reused in any number of classes. The result is less to learn, a greater shared understanding of how the whole system works, and a simpler path to cooperation and collaboration.

Because object-oriented programs make decisions dynamically at runtime, less information needs to be supplied at compile time (in source code) to make two pieces of code work together. Consequently, there’s less to coordinate and less to go wrong.

Inheritance is a way of reusing code. If you can define your classes as specializations of more generic classes, your programming task is simplified. The design is simplified as well, since the inheritance hierarchy lays out the relationships between the different levels of implementation and makes them easier to understand.

Inheritance also increases the reusability and reliability of code. The code placed in a superclass is tested by its subclasses. The generic class you find in a library will have been tested by other subclasses written by other developers for other applications.

The more software you can borrow from others and incorporate in your own programs, the less you have to do yourself. There’s more software to borrow in an object-oriented programming environment because the code is more reusable. Collaboration between programmers working in different places for different organizations is enhanced, while the burden of each project is eased.

Classes and frameworks from an object-oriented library can make substantial contributions to your program. When you program with the software frameworks provided by Apple, for example, you’re effectively collaborating with the programmers at Apple; you’re contracting a part of your program, often a substantial part, to them. You can concentrate on what you do best and leave other tasks to the library developer. Your projects can be prototyped faster, completed faster, with less of a collaborative challenge at your own site.

The increased reusability of object-oriented code also increases its reliability. A class taken from a library is likely to have found its way into a variety of applications and situations. The more the code has been used, the more likely it is that problems will have been encountered and fixed. Bugs that would have seemed strange and hard to find in your program might already have been tracked down and eliminated.

[Next](Document%20Revision%20History.md)[Previous](Structuring%20Programs.md)

