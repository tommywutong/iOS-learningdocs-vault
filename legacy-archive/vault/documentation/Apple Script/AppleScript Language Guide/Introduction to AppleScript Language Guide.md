---
title: AppleScript Language Guide
apple_id: TP40000983
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-01-25'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html
archived_at: '2026-07-15T05:19:31.541546Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](AppleScript%20Lexical%20Conventions.md)

# Introduction to AppleScript Language Guide

This document is a guide to the AppleScript language—its lexical conventions, syntax, keywords, and other elements. It is intended primarily for use with AppleScript 2.0 or later and macOS version 10.5 or later.

AppleScript 2.0 can use scripts developed for any version of AppleScript from 1.1 through 1.10.7, any scripting addition created for AppleScript 1.5 or later for macOS, and any scriptable application for Mac OS v7.1 or later. A script created with AppleScript 2.0 can be used by any version of AppleScript back to version 1.1, provided it does not use features of AppleScript, scripting additions, or scriptable applications that are unavailable in that version.

AppleScript is a scripting language created by Apple. It allows users to directly control scriptable Macintosh applications, as well as parts of macOS itself. You can create scripts—sets of written instructions—to automate repetitive tasks, combine features from multiple scriptable applications, and create complex workflows.

A scriptable application is one that can be controlled by a script. For AppleScript, that means being responsive to interapplication messages, called _Apple events_, sent when a script command targets the application. (Apple events can also be sent directly from other applications and macOS.)

AppleScript itself provides a very small number of commands, but it provides a framework into which you can plug many task-specific commands—those provided by scriptable applications and scriptable parts of macOS.

Most script samples and script fragments in this guide use scriptable features of the Finder application, scriptable parts of macOS, or scriptable applications distributed with macOS, such as TextEdit (located in `/Applications`).

You should use this document if you write or modify AppleScript scripts, or if you create scriptable applications and need to know how scripts should work.

_AppleScript Language Guide_ assumes you are familiar with the high-level information about AppleScript found in _[AppleScript Overview](../AppleScript%20Overview/Introduction%20to%20AppleScript%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tm2i)_.

This guide describes the AppleScript language in a series of chapters and appendixes.

The first five chapters introduce components of the language and basic concepts for using it, then provide additional overview on working with script objects and handler routines:

- [AppleScript Lexical Conventions](AppleScript%20Lexical%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzr) describes the characters, symbols, keywords, and other language elements that make up statements in an AppleScript script.
- [AppleScript Fundamentals](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvzs) describes basic concepts that underly the terminology and rules covered in the rest of this guide.
- [Variables and Properties](Variables%20and%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgmwvgvzrga) describes common issues in working with variables and properties, including how to declare them and how AppleScript interprets their scope.
- [Script Objects](Script%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wueqkkjjbusqkb) describes how to define, initialize, send commands to, and use inheritance with script objects.
- [About Handlers](About%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqgywugsscjfceessi) provides information on using handlers (a type of function available in AppleScript) to factor and reuse code.

The following chapters provide reference for the AppleScript Language:

- [Class Reference](Class%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfuzdinrtha2a) describes the classes AppleScript defines for common objects used in scripts.
- [Commands Reference](Commands%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvhe) describes the commands that are available to any script.
- [Reference Forms](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfuytembvgiza) describes the syntax for specifying an object or group of objects in an application or other container.
- [Operators Reference](Operators%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfuytenbqg4ya) provides a list of the operators AppleScript supports and the rules for using them, along with sections that provide additional detail for commonly used operators.
- [Control Statements Reference](Control%20Statements%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuytknztgmza) describes statements that control when and how other statements are executed. It covers standard conditional statements, as well as statements used in error handling and other operations.
- [Handler Reference](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfuytmmzxgyza) shows the syntax for defining and calling handlers and describes other statements you use with handlers.

The following chapter describes an AppleScript-related feature of macOS:

- [Folder Actions Reference](Folder%20Actions%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhewvgvzs) describes how you can write and attach script handlers to specific folders, such that the handlers are invoked when the folders are modified.

The following appendixes provide additional information about the AppleScript language and how to work with errors in scripts:

- [AppleScript Keywords](AppleScript%20Keywords.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgiwvgvzs) lists the keywords of the AppleScript language, provides a brief description for each, and points to related information.
- [Error Numbers and Error Messages](Error%20Numbers%20and%20Error%20Messages.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgawvgvzv) describes error numbers and error messages you may see in working with AppleScript scripts.
- [Working with Errors](Working%20with%20Errors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgewvgvzr) provides detailed examples of handling errors with [try Statements](Control%20Statements%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuyteobzg4zq) and [error Statements](Control%20Statements%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuyteojwgu3q).
- [Double Angle Brackets](Double%20Angle%20Brackets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsguwvgvzr) describes when you are likely to see double angle brackets (or chevrons—`«»`) in scripts and how you can work with them.
- [Libraries using Load Script](Libraries%20using%20Load%20Script.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsg4wvgvzr) describes how to save libraries of handlers and access them from other scripts.
- [Unsupported Terms](Unsupported%20Terms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgqwvgvzr) lists terms that are no longer supported in AppleScript.

Glossary terms are shown in _boldface_ where they are defined.

The following conventions are used in syntax descriptions:

|  |  |
| --- | --- |
| `language element` | Plain computer font indicates an element that you type exactly as shown. If there are special symbols (for example, `+` or `&`), you also type them exactly as shown. |
| _placeholder_ | Italic text indicates a placeholder that you replace with an appropriate value. |
| [optional] | Brackets indicate that the enclosed language element or elements are optional. |
| (a group) | Parentheses group elements together.  However, the parentheses shown in [Handler Syntax (Positional Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfuytmnrygeza) are part of the syntax. |
| [optional]... | Three ellipsis points (...) after a group defined by brackets indicate that you can repeat the group of elements within brackets 0 or more times. |
| a | b | c | Vertical bars separate elements in a group from which you must choose a single element. The elements are often grouped within parentheses or brackets. |
| Filenames shown in scripts | Most filenames shown in examples in this document include extensions, such as `rtf` for a TextEdit document. Use of extensions in scripts is generally dependent on the “Show all file extensions” setting in the Advanced pane of Finder Preferences.  To work with the examples on your computer, you may need to modify either that setting or the filenames. |

These Apple documents provide additional information for working with AppleScript:

- See _Getting Started with AppleScript_ for a guided quick start, useful to both scripters and developers.
- See _[AppleScript Overview](../AppleScript%20Overview/Introduction%20to%20AppleScript%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tm2i)_, including the chapter [Scripting with AppleScript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptX/Concepts/work_with_as.html#//apple_ref/doc/uid/TP40001568), for a high-level overview of AppleScript and its related technologies.
- See _Getting Started With Scripting & Automation_ for information on the universe of scripting technologies available in macOS.
- See [AppleScript Terminology and Apple Event Codes](https://developer.apple.com/releasenotes/AppleScript/ASTerminology_AppleEventCodes/TermsAndCodes.html) for a list of many of the scripting terms defined by Apple.

For additional information on working with the AppleScript language and creating scripts, see one of the comprehensive third-party documents available in bookstores and online.

[Next](AppleScript%20Lexical%20Conventions.md)

