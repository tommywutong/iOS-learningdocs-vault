---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/WebScript/OOoverview.html
archived_at: '2026-07-15T07:48:03.966192Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.mif.book.md)
[!Previous Section](NoteToObjCDev.md)

# Object-Oriented Concepts: a Quick Overview

WebScript is object-orientedthat is, it operates on data as objects. This section provides a quick overview of object-oriented concepts for those unfamiliar with them.

### Object

An object is a programming unit that groups a data structure (instance variables) and the methods (operations) that can use or affect that data. Objects are the principal building blocks of object-oriented programs.

### Class

A class can be thought of as a factory that produces a particular kind of object. A class defines instance variables and defines methods for the objects it creates.

### Instance

An instance is an object that belongs to (is a member of) a particular class. For example, consider that you have a string class. Instances of the class would probably have different characteristics (for example, one string instance might have the value "Fred", while another string instance has the value "Ethel"). Despite their particular characteristics, however, all instances would be able to perform the same operations on their data (for example, all instances of a string class would probably be able to return their length).

### Message

Objects communicate with each other using messages. A message is a method name and accompanying arguments to tell the receiving object in a message expression what to do. For example, suppose you had a string object. You could send it messages asking it to append another string to itself, to return a representation of itself as an integer, and so on.

### Method

A method is a procedure that can be executed by an object. Messages get bound to methods when the message is evaluated.

[!Table of Contents](WebScript.mif.book.md)
[!Next Section](Origins.md)
