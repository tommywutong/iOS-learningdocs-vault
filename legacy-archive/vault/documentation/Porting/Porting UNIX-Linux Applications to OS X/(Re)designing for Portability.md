---
title: Porting UNIX/Linux Applications to OS X
apple_id: TP30001003
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2012-06-11'
source_url: https://developer.apple.com/library/archive/documentation/Porting/Conceptual/PortingUnix/portability/portability.html
archived_at: '2026-07-18T01:50:47.770656Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Porting UNIX/Linux Applications to OS X](Introduction%20to%20Porting%20UNIX-Linux%20Applications%20to%20OS%20X.md)


[Next](Glossary.md)[Previous](Additional%20Features.md)

# (Re)designing for Portability

When porting applications to OS X, you might consider making architectural changes to make your port (and future ports) more maintainable.

If you are a new developer designing an application that you eventually hope to use on multiple platforms, many of the portability issues described in this chapter apply regardless of the platforms involved.

There are many different definitions for portability in the context of code design. One definition of portability is limiting yourself to functions specified in a commonly accepted standard such as the Single UNIX Specification (SUS) or the Portable Operating System Interface (POSIX). This is useful for non-GUI software, particularly when moving among UNIX-based and UNIX-like systems, but it does not address graphical user interfaces and does not allow you to take advantage of operating-system–specific capabilities.

The alternative to such limitations is to design your code in a modular fashion so that additional features specific to a given OS can be “plugged into” your application. Whether you do this with a plug-in interface, a class hierarchy, or simple abstraction, this is the most effective way to allow your software to be easily ported to multiple platforms without sacrificing functionality.

There are many different ways to achieve this degree of portability, all of which have valid uses. The goal of this chapter is to describe some of these and to explain when it is appropriate (or inappropriate) to use each one. This should help you avoid some of the common pitfalls when modifying software to support multiple platforms.

Of course, the proper time to make such decisions is before you begin writing the first line of code. Since this is not always possible, this chapter will also describe ways to retrofit these concepts into an existing application in the most maintainable manner possible.

Abstraction layers are the easiest, most general-purpose way of making code more portable. The basic concept is well discussed in computer science textbooks. However, most people still find themselves unclear on when it is appropriate to add an additional layer of abstraction.

The most straightforward rule of abstraction is that you should split functionality by use. If a block of code is likely to be reused, even if the code needs to be slightly modified or wrapped in different code, that block should be a separate function. If a block of code is only relevant to the function in which it is enclosed, it probably should not be, unless doing so represents a significant benefit to readability.

You’d be surprised how well this single rule fits most situations. Take file access, for example. Say you want to take advantage of the Carbon file API (to get alias support, for example). The code to open, read, and write a file is used in many places in most applications. Therefore, it should be abstracted into its own function and called from those places.

What you should generally avoid doing, though, is abstracting the open, read, and write calls individually, then using them inside large loops. This leads to needlessly unreadable code with lots of very small abstraction layer functions. You should instead present an interface that makes sense in the context of your application.

For example, if your application performs streaming, you might have the following overall structure:

- A function that opens a file
- A function that reads the next _n_ bytes that returns to a buffer containing the data
- A function that rewinds the stream by _n_ bytes
- A function that closes the file

Your open function might return an opaque handle that can be passed around within the core of the application but whose structure is unknown outside the file functions.

Similarly, you might have functions that read and write the preferences file using a large data structure, a function to read the header of a file, and so on.

Don’t fall into the trap of conditionalizing hundreds of bits of code with `#ifdef` directives. (An occasional `#ifdef` is OK.) This quickly leads to unmanageable code, particularly when you support OS X, multiple UNIX-based and UNIX-like systems, Classic Mac OS, and Windows.

If you study the spots in your code that you need to special-case, more often than not, you will find that their issues are closely related. For example, they might all be graphics routines. If so, you might pull all the functions that call graphics routines into their own file and conditionalize the inclusion of the entire file. For example, you might use using one file for X11 routines, one for Win32 routines, and one for Carbon or Cocoa routines. It is easier to conditionalize code in a few core functions than to conditionalize it in a hundred random places in the code. Similarly, it is easier to replace an entire file than to replace bits of a file.

Most _non-GUI_ abstraction layers should be as thin as possible, since a thick abstraction layer tends to lead to significant platform divergence. However, with a GUI, platform divergence is desirable and is thus an exception to this rule.

If you want your application to look identical on all platforms, then you should make the abstraction layer thin. However, this tends to result in OS X users throwing your application in a dumpster because it doesn’t feel like a Mac application. OS X has common GUI style rules that most X11 applications don’t follow.

For example, X11 applications often have per-window menus, while OS X has per-application menus (with the ability to add or remove menus when a different window is in the foreground). X11 applications tend to have very square features and small, space-efficient buttons, while Mac apps tend to have rounded, large, easier-to-read buttons.

Similarly, other operating systems, such as Windows and Classic Mac OS, have different design rules. You must understand the GUI design rules for each computing platform or your application will not be accepted easily on those platforms.

For this reason, it is easiest to split your entire user interface into a separate file or directory for X11, then clone that and rewrite it for Carbon or Cocoa when porting to OS X. That way, you can heavily redesign the OS X interface to match what Mac users expect without annoying your UNIX users.

A good way to implement this is to write your GUI to operate in a separate thread (or multiple threads, if desired). It can then communicate with the core of the application using pipes or other platform-specific solutions.

Another way to implement this is to simply have the GUI call functions in the core of the code. This design is effective when the core of the application is entirely GUI driven, but tends to result in the GUI appearing to wedge if the core of the application can take a long time to complete an operation, and is particularly hard to implement if the core code needs to do something continuously in the background during normal operation. You should consider these issues in your redesign to make your application more palatable to end users.

Don’t fall into the trap of overly abstracting your code. If a block of code will not be used in multiple places, don’t abstract it out unless it is platform-specific. Abstracting out code that appears in two or three places is, for readability reasons, usually not worth splitting into a separate function.

Do try to limit your functions to a reasonable length. Abstraction for readability alone is probably not a good idea, as splitting a function unnecessarily can end up making it harder to read. If the purpose of a function doesn’t divide in an obvious way into multiple subtasks, it is probably better not to split it. In many cases, though, you may find that an inner loop within that function can be considered a distinct operation unto itself. If so, that loop may be split into a separate function if doing so improves readability.

Don’t make abstraction layers more than five or six layers deep, as measured from the top level of a major functional unit. The deeper the nesting, the harder it is to follow the code when debugging.

Don’t make functions shorter than about ten lines of code. The readability improvement of such a small change in the outer function is rarely significant. There are, of course, exceptions, such as inline assembly (which should always be abstracted). These exceptions are good candidates for an inline function (or even a macro, if you are so inclined).

Remember that these are guidelines, not rules. You should generally follow your instincts. If you feel like something might be reusable, go ahead and abstract it even if it is only being used in one place. If you feel that splitting an inner loop into its own function is pointless, don’t split it. This applies to all guidelines, not just the ones in this chapter.

Plug-ins can be an effective way to minimize platform-specific code in the core of an application. This section describes places where plug-ins are appropriate. The specifics of writing plug-ins for OS X are described in depth in [Dynamic Libraries and Plug-ins](Compiling%20Your%20Code%20in%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjqfvkfawcsivddcmbt).

Effectively managing plug-ins can be tricky when dealing with multiple platforms. You may choose to have a plug-in for each platform, or for each service, or both. The choice of methodology depends largely on the amount of code that you need to put into an external module.

If you have only a few platform-specific bits, it is probably sufficient to have a single per-platform plug-in. A good place for such a design is in an application that needs, for example, to support a single feature in both Mac OS 9 and OS X. By isolating this block of code into an external module, the appropriate piece can be loaded according to the platform in which the application is launched.

Another approach is to have a separate plug-in for each distinct service from the operating system. This is particularly effective if the number of services is significant. Separating services into separate modules makes debugging each service easier from a version control point of view.

There are several right ways to design a plug-in architecture and many, many more wrong ways. The most important features of a plug-in architecture are extensibility, simplicity, extensibility, robustness, and extensibility, with emphasis on extensibility.

Ensuring that an architecture is robust is the responsibility of the implementors, and is beyond the scope of any design document. You should consider extensibility and simplicity early and often during the design process.

In general, the simpler the plug-in API, the more likely people will use it rather than grafting hacks into other parts of the code. Of course, this becomes a problem if you fail to expose features that are needed for a given plug-in. To solve this problem, design your API based around message passing concepts rather than function calls. That way, you can easily add additional types of messages to the API without modifying the API itself.

Of course, if your plug-in API only needs to handle one particular type of communication and you are relatively certain that this will not change, a plug-in architecture based on functions is somewhat easier to use. As with all designs, there are tradeoffs.

Extensibility in API design is a tricky issue. When you are creating a plug-in architecture in general, you can rarely envision the sorts of plug-ins that might eventually be useful. Someone might want plug-ins to add additional functionality that no one had even thought of, much less invented, when you created the architecture

You can also use plug-ins to abstract the interface presented by platform-specific services into a more generic form to simplify your application. These designs are more straightforward than architectures intended for adding new functionality; creating plug-in architectures for adding features are beyond the scope of this document.

The first step in designing a plug-in API for service abstraction is to choose the level of abstraction at which the application ends and the plug-in begins. If you choose a level that is too close to the application, the plug-ins will contain redundant code. If you choose a level that is too far removed, you will eventually need to interface your application with an environment that does not meet your initial expectations. As a result, the interface code for that module will become excessively complex. In either case, a rewrite is probably in order, which wastes time and resources that could have been saved had you chosen the right level of abstraction to begin with.

Choosing the level of abstraction for a plug-in interface can range from straightforward to downright impossible, depending on the application. In general, you should choose to split out the smallest amount of code possible such that the following conditions are met:

- No assumptions are made about the data structures of the underlying service.
- Return values are standardized in a way that meets the needs of your application.
- The calling convention can be implemented on any system that provides the support necessary for your application to function—that is, no special features of the underlying service should be implied at the plug-in API level or in your application.
- The data types passed to and from the plug-in API are one of two kinds: either base types in the programming language of choice, or composites of those base types that are structurally relevant to the application as a whole rather than to the underlying service.

Designing a plug-in API in this fashion may, however, result in substantial duplication of code. In such environments, a nested plug-in approach may be more practical.

The concept of nesting plug-ins is straightforward. You should consider using nested plug-ins when you find numerous opportunities for dividing an application from its plug-ins—that is, when dealing with a general class of underlying services divided into a number of subclasses that contain multiple specific variants with common characteristics.

Nested modules are convenient for:

- Authentication—a generic authentication layer with a generic plug-in for UNIX-based systems and specific plug-ins below to handle platform-specific variations
- Databases—at the top level, you might have ODBC, JDBC, STET, and SQL, with submodules for other, more specific SQL implementations
- Printing—for example, you might have a plug-in that handles PostScript printers with narrower plug-ins that override generic assumptions for a particular printer model

In short, whenever you have a group of underlying services that are substantially similar in behavior, but where you want to be able to also support services with dramatically different behavior, a nested plug-in approach is an effective design (unless the differences in behavior at the lowest level are very minimal).

A good example of plug-in API design is database access. As an example, consider a project that uses a database to obtain song playlist information.

Such a program requires various specific pieces of information from the database. For a given song, it might need the title, the artist, the total length, the intro (talk-over) time, the time at which the next song should begin playing (trigger time), and the time at which the song should be faded out, if applicable. In addition, a comments field could be included for composer or other genre-specific information. This is referred to as the internal data level.

To facilitate support for arbitrary databases, you add the first layer of abstraction at the internal data level. The core code calls functions with names like `getsongname` and `getsongtrigger`. Any arbitrary database, regardless of the query language used, can easily return a string or an integer (or at worst, be coerced into doing so). This is considered the minimum level of functionality needed to support this application, and thus forms the first plug-in split.

However, a surprising number of databases use a common syntax, SQL, for making requests. Although the syntax is the same, certain details (data types) are different, and the libraries used for accessing them are also different. For these reasons, supporting multiple SQL servers is a desirable goal, because you can use most common databases as storage.

Because the SQL instructions themselves are so similar between databases, the second split comes somewhat naturally. The code to actually execute a query can be placed in an implementation-specific module, and the code to generate the query—for a song’s name, for example—can be placed in a generic SQL language module. The API for the implementation-specific module could, for example, include:

- `getdbc`—Returns a pointer to a database connection object. The SQL core code treats this as an opaque type, but this is necessary to allow many database implementations to be used in a multithreaded environment. This information should not leave the SQL core unless the larger design requires connections to multiple databases simultaneously.
- `opendb`—Opens a database connection.
- `closedb`—Closes a database connection.
- `dbquerystring`—Executes an SQL query and returns the first result as a string.
- `dblistsongs`—Returns an array of song IDs that match an SQL query.

It might strike you as odd that this design doesn’t specify a generic SQL query call. This is largely a space–time tradeoff. Implementing a generic query would allow the GUI, for example, to request all of the information about a call in a single request. However, doing so would add a great deal of code for a relatively small time benefit. Since the GUI does not need to refresh frequently, and since the number of queries per second, therefore, tends to be relatively small, it makes sense to design the API to be as simple as possible. If low latency and high bandwidth are required for the specific application, a generic routine is desirable.

If you are familiar with SQL, though, you are probably aware that the similarities among SQL implementations end at inserting new tables into the database. Because this is such a small piece of the overall picture for this type of application (one or two lines of code total), it could easily be “special-cased” in the core code or (preferably) in the generic SQL code. This is one of those cases where you must decide whether the extra 1% of functional abstraction is worth the extra effort involved. In many cases, it is not.

If creating tables is more significant, you could create them in one of two ways: by adding a function in the implementation-specific plug-in, or by adding a function in the generic SQL plug-in, using a table for the data types (which could, if desired, reside in the implementation-specific plug-in).

To demonstrate the effectiveness of this design, MySQL database support was added to an application that used this exact design in about an hour. With the exception of table creation, no modifications to the generic SQL support routines were required.

In summary, proper plug-in design is much like proper abstraction. Code that can be reused should be reused, but the API to the plug-ins should not assume any knowledge of the underlying system.

If your software depends on command-line tools that ship as part of the operating system, you should be aware of differences in command-line flags and behavior. The behavior of some command-line tools varies not only across platforms but also across different versions of OS X.

For an extensive explanation of these differences, see [Designing Scripts for Cross-Platform Deployment](https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/PortingScriptstoMacOSX/PortingScriptstoMacOSX.html#//apple_ref/doc/uid/TP40004268-TP40003517).

As a good general rule, when writing abstraction layers, plug-in architectures, and so on, architectural portability should be considered. Most existing open source software is already fairly flexible in this regard. However, when dealing with OS-specific code, you may find that consistent support for things like endianness and alignment are not always considered.

When you encounter code specific to OS X with architectural dependencies on a particular processor architecture, there are a number of ways to handle the situation. Here are some tips that should help:

- Altivec or SSE code should be special-cased with equivalent scalar versions that can be compiled in. This will ensure that it is easy for developers familiar with other chip architectures to understand what is happening and write equivalents for other architectures.
- Testing of alignment should generally occur at compile time, not configuration time, to avoid unnecessary problems when cross-compiling.
- Testing of endianness should generally occur at either compile time or execution time, at your option.
- Executing intermediate build products is a bad idea and should be avoided where possible.

For more detailed information, see [Compiling for Multiple CPU Architectures](Compiling%20Your%20Code%20in%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjqfvbecssdizcueqi) and the document _[Universal Binary Programming Guidelines, Second Edition](../../Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_.

[Next](Glossary.md)[Previous](Additional%20Features.md)

