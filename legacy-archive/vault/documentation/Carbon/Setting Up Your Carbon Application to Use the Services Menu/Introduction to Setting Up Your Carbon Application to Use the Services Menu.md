---
title: Setting Up Your Carbon Application to Use the Services Menu
apple_id: TP30000993
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2003-12-10'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/appservices/intro/servintro.html
archived_at: '2026-07-15T05:24:51.035186Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Application%20Services%20Concepts.md)

# Introduction to Setting Up Your Carbon Application to Use the Services Menu

Application services give applications an open-ended way to extend each other’s functionality by allowing them to:

- Provide services to other applications
- Access functionality provided by other applications

An application that provides a service advertises the operation it can perform on a particular type of data—for example, encryption of text, optical character recognition of a bitmapped image, or generating text such as a message of the day. Any application that signs up to use services automatically accesses the advertised functionality through its Services menu. An application doesn’t need to know in advance what operations are available; it merely needs to indicate the types of data it uses, and the Services menu makes available the operations that apply to those types of data.

This document describes how application services work, shows some typical Services menus, and provides instructions on how you can use services in your application. You should read this document if you are an application developer and want to provide your application’s services to other applications or make services from other applications available to your application.

Before you read this document, you should be familiar with information property lists. You need to know what they are and how to add properties to a list. Carbon developers should also know how to write and install Carbon event handlers.

This document is organized as follows:

- [Application Services Concepts](Application%20Services%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojtfvbuqmrqguwviucykjcummjqge), discusses the types of services, the Services menu, services properties, and what happens when a service is invoked.
- [Application Services Tasks](Application%20Services%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojtfvbuqmrqgywviucykjcummjqge), provides instructions on how to set up your application to use services provided by other applications and how to provide your services to other applications.
- [Carbon Events for Services](Carbon%20Events%20for%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojtfvbuqmrqg4wviucykjcummjqge), describes the Carbon event classes, kinds, and event parameters defined for services events.

- _Aqua Human Interface Guidelines_ in User Experience Documentation provides guidelines on naming menu items and designing the interface for a services application.
- [Handling Carbon Events](../Carbon%20Event%20Manager%20Programming%20Guide/Introduction%20to%20Carbon%20Event%20Manager%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobz) in Carbon Events & Other Input Documentation describes how to implement Carbon events in your application.
- System Overview in Mac OS X Documentation contains information on property lists and how they are used in Mac OS X.
- _Learning Carbon_, available through [O’Reilly and Associates](http://www.oreilly.com/), contains information on writing and using Carbon event handlers as well as information on how to set up and use property lists.
[Next](Application%20Services%20Concepts.md)

