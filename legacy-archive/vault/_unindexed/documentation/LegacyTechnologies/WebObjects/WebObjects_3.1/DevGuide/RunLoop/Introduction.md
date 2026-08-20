---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/RunLoop/Introduction.html
archived_at: '2026-07-15T07:47:28.856892Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](RunLoop.book.md)

# Introduction

Most of your program's activity is a reaction to messages the application sends out during cycles of the request-response loop. These messages travel through the objects of an application: from application to session object, from session to component object, and from a component to its static and dynamic HTML elements. They enable the application to store user input, trigger action methods, and generate a response, usually in the form of an HTML page.

For background on the request-response loop, and on the roles the various WebObjects classes play in request handling, see
"[How WebObjects Works](../HowWOWorks/HowWOWorks.mif.book.md)".

For WebObjects developers, the emitted messages are _hooks_ into the request-response loop allowing them to invoke custom application behavior. You can influence what happens during request handling by taking advantage of these hooks. For example, you can determine what page to return based on user input, modify the header lines of a generated HTTP response, initialize variables from database records, or substitute a page for the requested page.

There are three types of hooks that can be implemented in either scripts or compiled classes:

- _Initialization methods_ establish the beginning state and behavior of objects. The __init__ method is invoked when one of the objects involved in request handling is created. On the other hand, __awake__ is invoked when an object becomes involved in each cycle of request handling.
- _Action methods_ are associated with a particular user action such as clicking a button or hyperlink.
- _Request-handling methods_ that are invoked at a particular point in the request-response loop if you implement them in a subclass or a script:

  : takeValuesFromRequest:inContext:

  invokeActionForRequest:inContext:

  appendToResponse:inContext:

[!Table of Contents](RunLoop.book.md)
[!Next Section](InitializationMethods.md)
