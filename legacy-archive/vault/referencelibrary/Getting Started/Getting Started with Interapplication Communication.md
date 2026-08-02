---
title: Getting Started with Interapplication Communication
apple_id: TP40008823
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: null
published: '2009-05-27'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_InterapplicationCommunication/_index.html
archived_at: '2026-07-18T02:39:24.171225Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)



## Introduction

An application running on OS X sometimes needs to communicate with another application. That other application could be on the same computer or a different one. For various reasons, it might want to tell another application to open a document or it might want to run a program as a subprocess. A user might want the application to transfer data to another application. Or the application might want to make its services available to users regardless of the application they’re currently using.

OS X provides a range of programmatic interfaces and services that enable these and others types of communication. The core Cocoa frameworks, Foundation and AppKit, have classes that support the following features:

- __Copy, cut and paste__. Users copy an object in one application and paste it in another application.
- __Drag and drop__. Users drag an object in one application to another application, which accepts it.
- __Application services__. Services let you share the resources and capabilities of your application with other applications in the system. Users select an object in one application and choose a service offered by another application to operate on it; for example, a user selects a word in a document and then chooses a service that looks that word up in a dictionary application.
- __Workspace services__. The [NSWorkspace](https://developer.apple.com/documentation/appkit/nsworkspace) class functions as an intermediary between Cocoa applications and the OS X “workspace,” which consists primarily of the services provided by the Finder. The services of this class enable an application to launch another application, open a file in another application, manipulate files and devices, and track changes in the workspace.
- __Running subprocesses__. Using certain Foundation classes, your application can launch subprocesses and communicate with them.
- __Remote messaging__. Using the distributed objects technology, you application can send messages to another application (on the same or a different computer) and receive messages from it.

In addition, the XML-RPC and SOAP technologies enable remote procedure calls from applications or AppleScript scripts.

### Start Here

#### Want to get familiar with the fundamentals?

To take advantage of the technologies and programming interfaces for interapplication communication, you should become familiar with basic Cocoa concepts, such as protocols, delegation, property lists, and notifications. Read [Cocoa Fundamentals Guide](../../documentation/Cocoa/Cocoa%20Fundamentals%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzu) to acquire this essential knowledge.

#### Prefer to learn by example?

- [CocoaDragAndDrop](../../samplecode/CocoaDragAndDrop/CocoaDragAndDrop.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydamzygq) demonstrates a Cocoa application that enables you to drag and drop images.
- [Moriarity](../../samplecode/Moriarity/Moriarity.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydamzzgy) builds an application that launches a subprocess to run a command-line tool.
- _SimpleService_ creates two application services, one that capitalizes words and the other that open files textually specified as paths.

### Go In Depth

__Transferring Data Between Applications__

- [Pasteboard Programming Guide](../../documentation/Cocoa/Pasteboard%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojz) describes how to use pasteboards, a standardized mechanism for exchanging data within applications or between applications. With pasteboards, you can copy, cut, and paste data within and between applications. But you may also use them in other operations, such as drag-and-drop and application services.
- [Drag and Drop Programming Topics](../../documentation/Cocoa/Drag%20and%20Drop%20Programming%20Topics/Introduction%20to%20Drag%20and%20Drop.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3ds2i) explains how to implement the feature enabling users to drag data-representing objects between your application and another application (or within your application).

__Implementing Application Services__

- [Services Implementation Guide](../../documentation/Cocoa/Services%20Implementation%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydc2i) describes how OS X services work, shows some typical Services menus, and provides instructions on how you can use services in your application.

__Accessing Workspace Services__

- [Workspace Services Programming Topics](../../documentation/Cocoa/Workspace%20Services%20Programming%20Topics/Introduction%20to%20Workspace%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyda2i) explains how to use the `NSWorkspace` class to open files and URLs, to perform file operations (such as moving files), to launch applications and open documents, and to retrieve information about mounted volumes.

__Running Subprocesses and Piping Data Between Processes__

- [Interacting with the Operating System](../../documentation/Cocoa/Interacting%20with%20the%20Operating%20System/Introduction%20to%20Interacting%20with%20the%20Operating%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tq2i) explains how you can use various Foundation classes to can launch subprocesses, pipe data between processes, obtain your process’s environment variables, get the current host’s name and address, look up domain names, obtain the user’s home directory and full name, and more.

__Remote Messaging and Procedure Calls__

- [Distributed Objects Programming Topics](../../documentation/Cocoa/Distributed%20Objects%20Programming%20Topics/Introduction%20to%20Distributed%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyde2i) describes the mechanism that enables a Cocoa application to call an object in another Cocoa application (or in a different thread in the same application). The applications can even be running on other computers on a network.
- [XML-RPC and SOAP Programming Guide](../../documentation/Apple%20Script/XML-RPC%20and%20SOAP%20Programming%20Guide/Introduction%20to%20XML-RPC%20and%20SOAP%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrw) describes how to use Apple Script and the Apple Event Manager in OS X to make remote procedure calls using the XML-RPC and SOAP (Simple Object Access Protocol) protocols.

__Uniform Type Identifiers__

- [Uniform Type Identifiers Overview](../../documentation/File%20Management/Uniform%20Type%20Identifiers%20Overview/Introduction%20to%20Uniform%20Type%20Identifiers%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmjz) gives an overview of the purpose, syntax, and usage of Uniform Type Identifiers (UTIs), provides guidelines for adopting UTIs, and includes a reference of common and system-defined UTIs.

### Ready for More?

The Snow Leopard Reference Library holds plenty more resources that make you job easier. To narrow the list of resources, you can set filters to focus on specific resource types (such as guides or sample code) or on specific topics (such as user experience or data management).

