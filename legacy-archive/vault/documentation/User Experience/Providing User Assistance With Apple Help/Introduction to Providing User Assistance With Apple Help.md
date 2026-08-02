---
title: Providing User Assistance With Apple Help
apple_id: TP40006563
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LegacyAppleHelpConcepts/user_help_intro/user_assistance_intro.html
archived_at: '2026-07-18T02:11:51.821905Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Apple%20Help%20Concepts.md)

# Introduction to Providing User Assistance With Apple Help

This document describes Apple Help, the HTML-based system for providing online user assistance in Mac OS X. Apple Help is the primary help system for the Mac OS and is designed to deliver online topic-based user help, such as is often provided in user manuals and lists of frequently asked questions (FAQ). Carbon, Cocoa, and Java applications can use Apple Help in Mac OS X. If you are creating an application, plug-in, or other software product with a user interface for Mac OS X v10.3 or earlier, you should read this document to learn how to create an Apple Help help book and display it in Help Viewer.

Apple Help offers significant advantages over static help documents, such as Read Me files or manuals in PDF, to teach your users how to use your products more effectively. The benefits of adopting Apple Help for user assistance include these:

- Searchability. Apple Help takes advantage of Sherlock technology to offer users sophisticated search capabilities, including full-text searching and the ability to search on synonyms and common misspellings.
- Full support for QuickTime media. Using QuickTime or other authoring tools, you can create animated sequences that showcase hidden or complex features of your software product and play these sequences as part of your help content.
- AppleScript automation. Using AppleScript, you can automate tasks and run them from your help content to guide users through a complex operation step by step.
- Ease of updating. Apple Help makes it simple to revise and expand your help content, page by page or all at once. Using Apple Help, you can even maintain up-to-date help pages and search indexes on your own server and have them downloaded via the Internet to update your help content.
- Ease of adoption. Many developers have recognized the advantages of browser-based help and implemented HTML solutions to provide user assistance. Apple Help makes it easy for you to adapt previously created HTML pages into the form used by Apple Help.

When you use Apple Help, you can supply HTML-based user assistance and integrate it into your application with relatively little effort. Apple Help manages and displays _help books_; a help book is the collection of HTML files that constitute the user help for your software product. When you supply a help book and register it with Apple Help, users can access your help from your user interface and view it in Help Viewer without any additional work on your part.

The Apple Help system includes these components:

- The Help Viewer application. This is the default application for viewing user assistance in the Mac OS. Help Viewer displays your HTML-based help book.
- The Apple Help application programming interface (API). This is a set of functions provided by Apple Help that allow you to access and load help in Help Viewer. You do not need to use these functions if you are providing only a basic help interface; however, if you wish to implement advanced help features (such as contextual menu help), you need to call the Apple Help functions. The Apple Help API, although a Carbon API, is available to all Carbon, Cocoa, and Java developers.
- The Apple Help Indexing Tool. This is a developer tool provided by Apple for indexing your help book. When you run the Apple Help Indexing Tool on your help book, the tool generates an index file that Help Viewer uses to make your help searchable.

Help Viewer and the Apple Help API are available in Mac OS X version 10.0 and later. They are also available in Mac OS 8.6 and later for Carbon applications. The Apple Help Indexing Tool is available in Mac OS X in `/Developer/Applications/Utilities` when the Developer package is installed.

This document includes the following chapters and appendixes:

- [Apple Help Concepts](Apple%20Help%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dknrtfvbuqmrqguwueqkcjfdugrcc) describes the Help Viewer application and introduces the Apple Help API.
- [Authoring User Help](Authoring%20User%20Help.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dknrtfvbuqmrqgywugskiivaucrci) shows how you can create a basic help book and describes how to use the Apple Help Indexing Tool to index your help book.
- [Registering Your Help Book](Registering%20Your%20Help%20Book.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dknrtfvbuqmrqg4wugscei5eeqrcg) describes how to register your help book with Help Viewer.
- [Opening Your Help Book in Help Viewer](Opening%20Your%20Help%20Book%20in%20Help%20Viewer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dknrtfvbuqmrqhawugskiizaueskf) shows how to use the Apple Help functions to access and display help book content from your application..
- [Apple Help Meta Tag Properties](Apple%20Help%20Meta%20Tag%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dknrtfvbuqmrqhewugsceizbeesck) lists the meta tags specific to Apple Help. You can use these tags to control how your help content is displayed.
- [Apple Help URLs](Apple%20Help%20URLs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dknrtfvbuqmrrgawuer2cijduercd) lists Apple Help URLs that you can use to link to help pages and other resources.
- [Apple Help Segments](Apple%20Help%20Segments.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dknrtfvbuqmrrgewugskiineucssh) lists the commands you can use to

For a detailed description of the Apple Help application programming interface, see the _Apple Help Reference_. For information on Carbon help tags, see_[Providing Help Tags in Carbon](../../Carbon/Providing%20Help%20Tags%20in%20Carbon/Introduction%20to%20Providing%20Help%20Tags%20in%20Carbon.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgmzdk)_ and the _Carbon Help Manager Reference_.

For information on help tags, or tooltips, in Cocoa applications, see_[Online Help](../../Cocoa/Online%20Help/Introduction%20to%20Online%20Help.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgayds2i)_.

For guidelines on how to use help effectively within your application, see _Apple Human Interface Guidelines_.

[Next](Apple%20Help%20Concepts.md)

