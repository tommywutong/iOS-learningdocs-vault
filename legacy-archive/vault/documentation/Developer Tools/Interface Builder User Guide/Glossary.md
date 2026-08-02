---
title: Interface Builder User Guide
apple_id: TP40005344
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/IB_UserGuide/Glossary/Glossary.html
archived_at: '2026-07-15T07:25:01.094904Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Interface Builder User Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Interface%20Builder%20Gesture%20Guide.md)

# Glossary

- __action__

  A connection that involves the sending of a message from one object to another when a certain user action occurs. For example, when a user presses a button, the button object calls the action method of its target object to notify that object that the action occurred.

- __autosizing behavior__

  A mechanism that automatically adjusts the size and position of views during resize operations based on a set of options. See also [spring](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmjxfvjvomq) and [strut](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmjxfvjvomy).

- __automatic guide__

  An alignment tool that shows the spacing required to meet the appropriate interface guidelines for the target platform. This type of guide appears and disappears automatically.

- __binding__

  A two-way connection between the objects of your data model and the views of your interface. Cocoa bindings provide automatic synchronization between your data objects and the views displaying information about those objects.

- __connections panel__

  A panel that appears as needed to display the connection status of outlets and actions.

- __content view__

  In iOS applications, the portion of an iOS window that displays the application’s custom content. Each content view may be represented by one or more actual views and typically presents a single screen’s worth of application content. In Mac OS X applications, it is the view object that acts as the root for all other views in the window.

- __controller object__

  An object that manages the interactions between an application’s data objects and the objects that display that data.

- __Core Data__

  A technology for managing structured data in your application. The data model of a Core Data application is built on a schema that defines one or more entities and their properties and the relationships between those entities. At runtime, Core Data manages the data for those entities using a database or other structured form of data store.

- __custom guide__

  An alignment tool that is placed by the user in order to align objects to an arbitrary location on the design surface.

- __design surface__

  The content area of a window object. This area is where you drop views and other visual objects and is also where you manipulate those objects directly.

- __dynamic guide__

  An alignment tool that provides information about the position of a view relative to other objects on the design surface. Dynamic guides appear only when the Option key is held down.

- __event__

  A type of connection that is specific to iOS applications. Events represent different phases of user interaction for a control. Each event connection can also have multiple assigned target objects, each with its own distinct action message.

- __File’s Owner__

  The runtime object that manages the contents of a nib file. The File’s Owner is typically a controller object that maintains pointers to key objects in a nib file and responds to user interactions with those objects.

- __First Responder__

  The object given the first opportunity to respond to events. The First Responder object is determined dynamically at runtime based on the several conditions, including which view is selected or has focus and which view is willing to accept certain types of events. If the First Responder does not handle an event, it passes the event to other objects in the responder chain.

- __interface object__

  An object in a nib file that is created for your application at load time. Interface objects can consist of both visual objects (such as windows, views, and menus) and non-visual objects (such as controllers).

- __nib document__

  The runtime representation of a nib file. Nib documents are the primary document type of the Interface Builder application. The on-disk representation of a nib document is a nib file.

- __nib file__

  An on-disk collection of resource data. Nib files contain binary data representing one or more resources that you want to load into your application at runtime.

- __outlet__

  A pointer to another object that can be set in Interface Builder. Applications use outlets to store references to objects in nib files.

- __placeholder object__

  A placeholder for an object that is specified at runtime. Placeholder objects act as stand-ins for objects that are not available at design time. Instead, such objects are created by a running application and connected to the objects in a nib file when that nib file is loaded. Cocoa nib files use placeholder objects to represent the owner of a nib file’s contents, the application object itself, and the first object to respond to events.

- __resource__

  A generic term for structured data that is used at runtime to simplify the creation of some complex feature. Nib files store window resources, view resources, menu resources, and all the relationships between those objects and other objects in your application. When a nib file is loaded, its resources are turned into actual objects that can be used exactly as if they’d been created programmatically.

- __Responder chain__

  The set of objects responsible for handling events in a window.

- __spring__

  An element in the Size pane of the inspector window that controls the autosizing behavior of a view or control. When a spring is present, the width or height of your view grows and shrinks proportionally to its parent view. When no spring is present, the width or height of your view remains fixed.

- __strut__

  An element in the Size pane of the inspector window that controls the autosizing behavior of a view or control. When a strut is present, the distance between the edge of a view to its parent view remains fixed. When absent, the distance grows and shrinks as the size of the views change.

- __xib file__

  An XML–based version of a nib file. Xib files are the preferred format to use during development of your application. At build-time, they are compiled into nib files so that they can be deployed in your application bundle.

[Next](Document%20Revision%20History.md)[Previous](Interface%20Builder%20Gesture%20Guide.md)

