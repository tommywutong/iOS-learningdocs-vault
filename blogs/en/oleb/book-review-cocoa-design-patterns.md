---
title: 'Book Review: Cocoa Design Patterns'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/01/book-review-cocoa-design-patterns/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:34642431b962cddc'
translated: false
---

> 原文：[Book Review: Cocoa Design Patterns](https://oleb.net/blog/2010/01/book-review-cocoa-design-patterns/)　·　Ole Begemann

# Book Review: Cocoa Design Patterns

![Cover of Cocoa Design Patterns by Erik M. Buck and Donald A. Yacktman](https://oleb.net/media/cocoa-design-patterns-cover-155x200.jpg)

Although I [pointed out a minor mistake](https://oleb.net/blog/2009/11/mutable-properties-of-immutable-objects/) in the book in an earlier post, I highly recommend Erik M. Buck’s and Donald A. Yacktman’s [Cocoa Design Patterns](https://www.amazon.com/Cocoa-Design-Patterns-Erik-Buck/dp/0321535022/) (released in late 2009) to every Cocoa programmer who has worked through one or more beginner books to Objective-C and the Cocoa framework.

# Many ways to structure a book

Many books about Cocoa introduce the framework’s features by talking about one class (or a group of related classes) per chapter and creating a small sample application to show how a programmer would integrate this class into their own project. An example is Aaron Hillegass’s wildly popular [Cocoa Programming for Mac OS X](https://www.amazon.com/Cocoa-Programming-Mac-OS-3rd/dp/0321503619/). After a general introduction to some of Cocoa’s key concepts, Hillegass mostly introduces specific features like `NSUndoManager`, window controllers, `NSUserDefaults`, table views, event handling etc. by explaining the class interfaces of these features and how to implement them. If a feature requires a further explanation how it works under the hood, this is worked into the flow of the chapter. This practical approach is a great way for programmers to learn how to use a framework like Cocoa (and _Cooca Programming for Mac OS X_ is a very good book, everyone should read it). However, sometimes it can leave you a little in the dark about what is going on under the hood.

# How does it work and why did they design it this way?

In contrast, _Cocoa Design Patterns_ is built around the questions, _How does it work and why did they design it this way?_, with specific applications of the design patterns mentioned in the relevant places. Each chapter of the book is devoted to one specific design pattern and its implementation in Cocoa. This is especially beneficial because in Cocoa, many problems are solved a little differently than in other popular frameworks, partly due to the dynamic nature of Objective-C. The authors spend a great deal explaining the motivation behind both the patterns themselves and their implementation. If you have read the classic [“Gang of Four” book](https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612/) on design patterns, you will recognize most of the patterns (even if they often have different names), and this book is a perfect addition.

Here are a few of the patterns discussed in the book that I found most helpful:

- Model-View-Controller as the grand pattern that structures the entire framework.
- Dynamic Creation of objects and the many places throughout the framework this feature of the Objective-C runtime is used, from scripting to unarchiving to plug-in architectures.
- The ever-present Delegate pattern.
- The target-action mechanism.
- Invocations and their role in the undo/redo process.
- and

  to save memory and performance.
- Proxies and Forwarding and how this can be used to implement Higher Order Messaging.

The book is a little Mac-centric in that it does not specifically talk about the iPhone and some of the examples mentioned only apply to the Mac. That part is small, though, and I would say _Cocoa Design Patterns_ is equally useful to iPhone developers. Again, highly recommended for intermediate Cocoa developers.
