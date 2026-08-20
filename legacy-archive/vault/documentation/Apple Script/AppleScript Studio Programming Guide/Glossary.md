---
title: AppleScript Studio Programming Guide
apple_id: TP30000889
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2011-01-07'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/StudioBuildingApps/glossary/studio_glossary.html
archived_at: '2026-07-15T05:20:44.668285Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AppleScript Studio Programming Guide](Introduction%20to%20AppleScript%20Studio%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Mail%20Search%20Tutorial%2C%20Full%20Script%20Listing.md)

# Glossary

- __'aete' resource__

  An Apple event terminology resource; supplies scripting terminology for a Carbon application. Compare script suite.

- __AppKit framework__

  Defines classes to support a graphical, event-driven user interface for applications. See also Cocoa framework.

- __Apple Event Manager__

  Provides an API for sending and receiving Apple events and working with the information they contain.

- __AppleScript__

  A scripting system that allows users to directly control Macintosh applications, including the Mac OS itself, by creating sets of English-like instructions, or scripts.

- __AppleScript component__

  The scripting component in Mac OS X that implements the AppleScript scripting language. A scripting component provides services for compiling and executing scripts (and relies on the _Open Scripting Architecture_).

- __AppleScriptKit framework__

  Supplies advanced Cocoa scripting support and other features required by AppleScript Studio.

- __AppleScript object__

  A distinct object in an application or its documents that can be specified in a script.

- __AppleScript object class__

  A category for AppleScript objects that share characteristics, such as properties and elements.

- __AppleScript script file__

  A file with the extension “.applescript” that contains statements in the AppleScript scripting language.

- __AppleScript source code editor__

  an Xcode pane for editing and compiling AppleScript script files (files with the extension “.applescript”). The source editor relies on the `osacompile` shell tool to compile scripts.

- __AppleScript Studio__

  A development environment and application framework that combines features from AppleScript, Xcode, Interface Builder, and the Cocoa application framework to provide a sophisticated environment for creating AppleScript Studio applications.

- __AppleScript Studio application__

  A Mac OS X application that combines AppleScript scripts and Cocoa user-interface objects.

- __backtrace__

  A list of the handlers that have been invoked at any point in a script execution. Each handler is listed as a call frame.

- __build directory__

  The file system directory in which built products are stored. This is usually the “build” folder in the project folder.

- __build phase__

  A step of the process of building a target. Each build phase deals with one category of source or resource files (e.g. Objective-C, AppleScript, Bundle resources, shell scripts). The Jam system automatically performs all necessary build phases in reverse order of their dependency on each other.

- __build style__

  A methodology of creating a product from a target in Xcode. Development and Deployment build styles use different methodologies.

- __call frame__

  The information about a handler call, including its calling parameters and local variables.

- __Cocoa framework__

  An object-oriented application framework, consisting of a collection of advanced object-oriented APIs. The Cocoa framework is made up of the AppKit and Foundation frameworks. Also referred to simply as _Cocoa_.

- __Cocoa user interface class__

  A class that supports a user interface item. The Application Kit provides many of these classes; for example, NSButton and NSBrowser are Cocoa user interface classes provided by the Application Kit.

- __Cocoa user interface object__

  An instance of a Cocoa user interface class.

- __command__

  A word or phrase in a script that requests an action. For example, a script can send a `stop` command to a progress indicator object. Compare _event_.

- __CVS__

  The Concurrent Version System, a source-code control system that Xcode can use to manage changes in source code over time and across multiple developers.

- __data source object__

  An object supplied by AppleScript Studio that supplies data to a table view or other view with rows and columns.

- __deployment build style__

  A methodology of creating a product from a target that makes the product more appropriate for distribution to users.

- __development build style__

  A methodology of creating a product from a target that makes the product more appropriate for debugging and testing.

- __dictionary browser__

  See _terminology browser._

- __droplet__

  A script application that launches when you drag a file or folder icon in the Finder and “drop” it on the droplet’s icon. A droplet receives a list of descriptors for the folders or files dropped on it and typically performs operations on each item in the list.

- __event__

  An action an object can respond to. For example, a button click is an event that may result in execution of a `clicked` handler for the button that was clicked. Compare _command_.

- __event handler__

  A handler that responds to an action in an AppleScript Studio application. Compare _handler_.

- __executable__

  An application that uses a project’s product and can be launched in order to debug that product. For AppleScript Studio, the executable is the product.

- __Foundation framework__

  Defines a layer of useful primitive object classes, including support for Unicode strings, allocation and deallocation of objects, arrays and collections, dates, ports, and more. See also _Cocoa framework_.

- __framework__

  A type of bundle (or directory in the file system) that packages software with the resources that software requires, including its interface.

- __GDB or gdb__

  The GNU debugger—an open-source debugger, available with Mac OS X, for debugging programs written in C, C++, and Objective-C.

- __handler__

  A named series of one or more script statements that are executed by calling its name. Compare _event handler_.

- __information property list__

  A special property list that contains predefined keys for application information that may be used by the Finder, by other applications, and by the application itself. See also _property list_.

- __Info window__

  An Interface Builder window for setting both attributes and connections for the associated user interface object.

- __Interface Builder__

  A graphical user interface editor for creating interfaces for Cocoa, Carbon, and AppleScript Studio applications.

- __model-view-controller (MVC)__

  A programming paradigm in which the view is responsible for part of the application visible on screen, the model represents the application’s data and algorithms, and the controller interprets user input and specifies changes to the model and the view.

- __nib__

  A resource that stores a collection of Cocoa user interface objects, such as buttons, text fields, and pop-up menus, as well as information about the relationships between those objects and project code.

- __nib file__

  A file that stores one or more nibs.

- __Open Scripting Architecture (OSA)__

  An API for compiling and executing scripts, and for creating scripting components.

- __osacompile__

  A shell tool for compiling script files.

- __Palette window__

  An Interface Builder window that provides a number of palettes (or panes), each of which contains object instances you can add to an application.

- __product__

  An application or framework produced by Xcode. AppleScript Studio projects create an application as a product.

- __product directory__

  The file system directory that contains a project file, the project's source code and resources, and the build directory.

- __Xcode__

  An integrated development environment for Mac OS X that supports building Cocoa, Carbon, and AppleScript Studio applications (as well as bundles, frameworks, plug-ins, and tools) with C, C++, Objective-C, and Java.

- __project file__

  A file created by Xcode that organizes source code, resources, and settings used to build a product.

- __property list__

  A structured, textual representation of data, commonly stored in Extensible Markup Language (XML) format. Elements of a property list represent data of certain types, such as arrays, dictionaries, and strings.

- __Script Editor application__

  An application distributed with the Mac OS that provides a basic environment for editing, compiling, and executing scripts.

- __scripting addition__

  Code, stored in `/System/Library/SystemAdditions`, that makes additional commands or coercions available to scripts on the same computer.

- __script object__

  A user-defined object, combining data (in the form of properties) and handlers, that can be used in a script.

- __script object definition__

  A compound statement that can contain collections of properties, handlers, and other AppleScript script statements.

- __script suite__

  The combination of at least one suite definition and one suite terminology that together define the scripting capabilities and terminology for Cocoa and AppleScript Studio applications.

- __SOAP (simple object access protocol)__

  A remote procedure call protocol designed for a distributed environment, where a server may consist of a hierarchy of objects whose methods can be called over the Internet.

- __suite definition__

  A property list that describes scriptable objects in terms of their attributes, relationships, and supported commands

- __suite terminology__

  A property list that maps AppleScript terminology—the English-like words and phrases you can use in a script—to the class and command descriptions in a suite definition.

- __target__

  A subdivision of an Xcode project that is responsible for building one product. AppleScript Studio projects usually have only one target.

- __terminology browser__

  A graphical tool for displaying the scripting terminology for a scriptable application. Also known as a _dictionary browser_.

- __XML-RPC__

  A simple protocol for making remote procedure requests to Internet-based servers.

[Next](Document%20Revision%20History.md)[Previous](Mail%20Search%20Tutorial%2C%20Full%20Script%20Listing.md)

