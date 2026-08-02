---
title: Open Directory Plug-in Programming Guide
apple_id: TP40000918
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: DirectoryService
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Dir_Plugin/Introduction/Introduction.html
archived_at: '2026-07-27T06:57:05.753722Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Runtime%20Environment.md)

# Retired Document

__Important:__
Support for DirectoryService plug-ins has been deprecated and will be removed in a future release.

A new architecture was introduced in OS X v10.9 to allow the creation of native Open Directory modules. Unlike DirectoryService, `opendirectoryd` uses modules implemented as a standalone process that uses XPC to communicate with `opendirectoryd`. Implementing a module as an XPC service ensures a private address space and improves security and reliability, because modules cannot crash another module or `opendirectoryd`.

# Introduction

An Open Directory plug-in is an OS X dynamically loaded library that responds to requests for directory service from applications that are clients of Open Directory.

This book describes the runtime environment for Open Directory plug-ins and how to build and configure an Open Directory plug-in. It also describes the entry points that an Open Directory plug-in must provide, the requests that an Open Directory plug-in must be prepared to respond to, and the Open Directory callback routines that the plug-in can call to register and unregister nodes and to write in log files.

__Important__ Support for DirectoryService plug-ins has been deprecated and will be removed in a future release.

A new architecture was introduced in OS X v10.9 to allow the creation of native Open Directory modules. Unlike DirectoryService, `opendirectoryd` uses modules implemented as a standalone process that uses XPC to communicate with `opendirectoryd`. Implementing a module as an XPC service ensures a private address space and improves security and reliability, because modules cannot crash another module or `opendirectoryd`.

## Organization of This Document

This book contains the following chapters:

- [Runtime Environment](Runtime%20Environment.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjyfvbuqmznknltc) describes how Open Directory plug-ins are loaded.
- [Required Entry Points](Required%20Entry%20Points.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjyfvbuqnbnknltc) defines the required entry points for an Open Directory plug-in
- [Processing Open Directory Requests](Processing%20Open%20Directory%20Requests.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjyfvbuqnjnknltc) defines the requests an Open Directory plug-in must be prepared to handle.
- [Processing Concurrent Requests](Processing%20Concurrent%20Requests.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjyfvbuqnrnknltc) explains the asynchronous nature of Open Directory plug-ins
- [Open Directory Callbacks](Open%20Directory%20Callbacks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjyfvbuqnznknltc) defines the callback routines provided by Open Directory.
- [Calling OS X Functions](Calling%20OS%20X%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjyfvbuqobnknltc) explains the advantages and disadvantages of using OS X functions in an Open Directory plug-in.
- [Managing References](Managing%20References.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjyfvbuqojnknltc) describes how Open Directory plug-ins interact with object references.
- [Standard Record and Attribute Types](Standard%20Record%20and%20Attribute%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjyfvbuqmjqfvjvomi) explains what information needs to be maintained from record and attribute types.
- [Authentication](Authentication.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjyfvbuqmjrfvjvomi) defines what authentication methods an Open Directory plug-in needs to support.
- [Property List for an Open Directory Plug-in](Property%20List%20for%20an%20Open%20Directory%20Plug-in.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjyfvbuqmjsfvjvomi) explains the keys used in an Open Directory plug-in property list and how those keys are utilized.
- [Configuring an Open Directory Plug-in](Configuring%20an%20Open%20Directory%20Plug-in.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjyfvbuqmjtfvjvomi) describes the variety of configurations for setting up an Open Directory plug-in.
- [Client Side Buffer Parsing](Client%20Side%20Buffer%20Parsing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjyfvbuqmjufvjvomi) explains how to use a `tDataBuffer` object in an Open Directory plug-in.

## See Also

Refer to the following reference document for Open Directory plug-ins:

- _Open Directory Reference_

For more information about Open Directory client programming, and administration, see:

- _[Open Directory Programming Guide](../Open%20Directory%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjx)_
- OS X Server Open Directory Administration

[Next](Runtime%20Environment.md)
