---
title: WebObjects Enterprise Objects Programming Guide
apple_id: TP30001011
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-07-11'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/About/About.html
archived_at: '2026-07-18T02:20:56.480067Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Introduction/Introduction.html)

# Introduction to WebObjects Enterprise Objects Programming Guide

The Enterprise Object technology brings the benefits of object-oriented programming to database application development. You can use the Enterprise Objects frameworks to build feature-rich database applications that encapsulate your business logic, yet are independent of any particular data source. Enterprise Objects allows you to focus on writing business logic that brings your stored data to life rather than on writing SQL or other database code to access that data.

There are many solutions on the market that provide technology to feed today’s information-hungry applications from vast amounts of data in various data sources. However, almost all these solutions are vendor-specific and force the applications you write to depend on a particular data source.

As your application and business needs evolve, these restraints will likely prevent your applications from reaching their full potential. With Enterprise Objects, however, you can build data-driven applications that are independent of any particular data source or data access mechanism. An application built with Enterprise Objects can more easily adapt to new requirements and changing business needs.

This document is appropriate for Enterprise Objects developers of all levels, but much of the material is more relevant to intermediate and advanced users who are working with fairly complex applications. However, the appendix [Principal Methods](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/CommonMethods/CommonMethods.html#//apple_ref/doc/uid/TP30001011-CH213-TP1) and many of the tasks sections throughout the document provide introductory information to help new users get started with the Enterprise Objects frameworks.

New Enterprise Objects developers should consider the document _[EOModeler User Guide](EOModeler%20User%20Guide/Introduction%20to%20EOModeler%20User%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjy)_ a prerequisite to this document. As well as teaching you how to use EOModeler, it is the best way to familiarize yourself with general database concepts and with the core concepts in the Enterprise Objects frameworks such as data modeling. It also discusses the most important characteristics of EOEnterpriseObjects, rather than discussing the mechanics of the Enterprise Objects frameworks, as this book does.

[Road Map to Concepts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjrfvbuqmrqgewviucykjcummjvhe) and [Road Map to Tasks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjrfvbuqmrqgewviucykjcummjtgu) provide road maps to help you decide which sections of this document are most relevant to you.

This section provides a key to some of the overloaded terms in the Enterprise Objects frameworks:

- the Enterprise Object technology is also referred to as “Enterprise Objects” (note capitalization) or as the “Enterprise Objects frameworks”
- classes or instances of classes that implement the EOEnterpriseObject interface are referred to as “enterprise objects” (note capitalization)

The terms “Enterprise Objects,” “the Enterprise Objects frameworks,” and “the Enterprise Object technology” refer to all of the classes in WebObjects that begin with the prefix “EO.” This document speaks specifically to the core Enterprise Objects frameworks: classes in the package `com.webobjects.eocontrol` (referred to as the _control layer_) and classes in the package `com.webobjects.eoaccess` (referred to as the _access layer_).

The Enterprise Objects frameworks provide a great deal of flexibility through an extensive API—most of which you’ll never need to use or know about. You can go far in building an Enterprise Objects application if you’re familiar with a handful of classes and a few dozen methods. The best way to learn about these particular classes and methods is by performing small, focused tasks to gradually get acquainted with the commonly used ones. By learning the technology through these tasks, you build up a set of mental tools that you can later use to build real, data-driven applications. This document provides a number of these tasks to help you get started.

While learning the technology, don’t be tempted to use classes and methods that you either don’t need or don’t understand. You’ll probably ever use only 10% of the public API throughout the technology, so don’t be too adventurous in the beginning. An axiom of Enterprise Objects development is that “he who writes the least code wins.” That is, if in dealing with a particular problem, you end up writing a lot of complicated, custom code, you’ve probably overlooked functionality that the frameworks provide.

When learning this technology, keep in mind that the learning curve is high but the productivity that results allows you to rapidly build sophisticated, elegant business solutions in a fraction of the time that other database application development systems require. To help tackle the high learning curve, don’t try to understand the whole system at once. Fortunately, the layered design of Enterprise Objects facilitates this approach. By working with one layer at a time, the whole system gradually comes into focus.

Part of the difficultly in learning Enterprise Objects is its abstract architecture. It is designed to allow you to work with data sources at an abstract level; it allows you to work with objects that are abstractions of data sources. The objects within the frameworks provide abstract representations of databases, of database transactions, and of the data retrieved from databases.

Although the abstractions within Enterprise Objects contribute to its high learning curve, once you understand the architecture, you’ll see that its abstract design provides huge benefits in terms of portability to different data sources and to various client-server application configurations. So if all the abstraction at first seems confusing, be patient—you’ll eventually come to appreciate it.

If you’ve read _Using EOModeler_ or have a little experience building Enterprise Objects applications, you should read these chapters first:

- [Enterprise Objects Overview](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001011-CH202-TP1)
- [Business Objects](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/EnterpriseObjects/EnterpriseObjects.html#//apple_ref/doc/uid/TP30001011-CH203-TP1)
- [Business Logic](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/BusinessLogic/BusinessLogic.html#//apple_ref/doc/uid/TP30001011-CH204-TP1)

If you are an intermediate developer who wants to know more about the mechanics of Enterprise Objects, read these chapters:

- [Fetching Data](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Fetching/Fetching.html#//apple_ref/doc/uid/TP30001011-CH206-TP1)
- [Working With the Object Graph](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Managing/Managing.html#//apple_ref/doc/uid/TP30001011-CH207-TP1)
- [Saving Data](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Saving/Saving.html#//apple_ref/doc/uid/TP30001011-CH208-TP1)

If you are an advanced developer, you may be interested in these chapters, which discuss advanced topics:

- [Core Framework Stack](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Geography/Geography.html#//apple_ref/doc/uid/TP30001011-CH205-TP1)
- [Update Strategies](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/UpdateStrategies/UpdateStrategies.html#//apple_ref/doc/uid/TP30001011-CH209-TP1)
- [Connecting to a Database](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Connecting/Connecting.html#//apple_ref/doc/uid/TP30001011-CH210-TP1)
- [Concurrency](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Concurrency/Concurrency.html#//apple_ref/doc/uid/TP30001011-CH211-TP1)

If you’ve read _Using EOModeler_ or have a little experience building Enterprise Objects applications, you are probably interested in the tasks described in these sections:

- [Synchronizing Model Changes to Class Files](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/EnterpriseObjects/EnterpriseObjects.html#//apple_ref/doc/uid/TP30001011-CH203-TPXREF145)
- [Instantiating Enterprise Objects](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/EnterpriseObjects/EnterpriseObjects.html#//apple_ref/doc/uid/TP30001011-CH203-TPXREF146)
- [Providing Initial Values](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/BusinessLogic/BusinessLogic.html#//apple_ref/doc/uid/TP30001011-CH204-TPXREF140)
- [Adding Validation](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/BusinessLogic/BusinessLogic.html#//apple_ref/doc/uid/TP30001011-CH204-TPXREF141)
- [Writing Business Methods](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/BusinessLogic/BusinessLogic.html#//apple_ref/doc/uid/TP30001011-CH204-TPXREF143)
- [Manipulating Relationships](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/BusinessLogic/BusinessLogic.html#//apple_ref/doc/uid/TP30001011-CH204-CBGJCJAC)
- [Building a Reusable Framework](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/BusinessLogic/BusinessLogic.html#//apple_ref/doc/uid/TP30001011-CH204-CDBCJAIA)
- [Constructing Fetch Specifications](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Fetching/Fetching.html#//apple_ref/doc/uid/TP30001011-CH206-TPXREF153)
- [Filtering Fetch Results in Memory](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Fetching/Fetching.html#//apple_ref/doc/uid/TP30001011-CH206-TPXREF156)
- [Sorting Fetch Results in Memory](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Fetching/Fetching.html#//apple_ref/doc/uid/TP30001011-CH206-TPXREF172)
- [Accessing WebObjects in Enterprise Objects](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Appendix/Appendix.html#//apple_ref/doc/uid/TP30001011-CH212-TPXREF139)

Intermediate and advanced developers are probably interested in the tasks in these sections:

- [Providing Separate Stacks](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Geography/Geography.html#//apple_ref/doc/uid/TP30001011-CH205-TPXREF146)
- [Accessing Lower-Level Objects](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Geography/Geography.html#//apple_ref/doc/uid/TP30001011-CH205-TPXREF147)
- [Generating Custom Primary Keys](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Saving/Saving.html#//apple_ref/doc/uid/TP30001011-CH208-TPXREF153)
- [Using Compound Primary Keys](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Saving/Saving.html#//apple_ref/doc/uid/TP30001011-CH208-BADJEBIB)
- [Recovering and Refaulting](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/UpdateStrategies/UpdateStrategies.html#//apple_ref/doc/uid/TP30001011-CH209-BHAHFAFH)
- [Recovering and Last Write Wins](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/UpdateStrategies/UpdateStrategies.html#//apple_ref/doc/uid/TP30001011-CH209-BHADAIHE)
- [Providing a Connection Dictionary in Code](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Connecting/Connecting.html#//apple_ref/doc/uid/TP30001011-CH210-TPXREF144)
- [Providing Multiple Database Channels](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Connecting/Connecting.html#//apple_ref/doc/uid/TP30001011-CH210-TPXREF145)
- [Closing Database Channels](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Connecting/Connecting.html#//apple_ref/doc/uid/TP30001011-CH210-TPXREF146)
- [Accessing Database Keys](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Fetching/Fetching.html#//apple_ref/doc/uid/TP30001011-CH206-BIECEEAB)

You can find further documentation for WebObjects and Java Client in three places:

- Project Builder’s Developer Help Center, accessible through the Help menu
- Apple’s WebObjects documentation site: [http://developer.apple.com/documentation/WebObjects/index.html](https://developer.apple.com/documentation/WebObjects/index.html)
- The WebObjects CD-ROM, which contains the WebObjects API reference, various documents in HTML and PDF, examples, what’s new, and legacy documentation
[Next](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_Objects/Introduction/Introduction.html)

