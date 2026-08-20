---
title: Extending Printing Dialogs
apple_id: TP30000979
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/documentation/Printing/Conceptual/ExtPrintingDialogs/Introduction/Introduction.html
archived_at: '2026-07-18T01:51:48.318531Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Printing%20Features%20and%20Printing%20Dialog%20Panes.md)

# Introduction to Extending Printing Dialogs

As printer vendors and application developers extend the printing capabilities of their hardware and software products, they need a way to extend the Mac OS X printing system to make new printing features available to their customers. To address this need, Mac OS X has introduced the _printing plug-in_—a component architecture based on Core Foundation Plug-in Services.

There are four types of printing plug-ins in Mac OS X:

- _I/O modules_ are used by the printing system to communicate with a printer using a standard transport-layer interface, such as AppleTalk or TCP/IP.
- _Printer browsers_ provide a way for people to discover available local and network printers.
- _Printer modules_ are used by the printing system to convert the graphics content in a print job for output to a specific printer or family of printers.
- _Printing dialog extensions_ provide a way for people to view and change the settings for a set of related printing features. The user interface of a printing dialog extension is a pane in one of the printing dialogs.

This book is a guide to developing printing dialog extensions—including basic concepts, theory of operation, and a documented Carbon-based sample project.

You should read this book if:

- You’re developing an application or a printer module, and you want to learn how to present your printing features using the Mac OS X printing dialogs.
- Your existing software already extends a printing dialog, and you want to improve the interface or take advantage of advanced features in the Mac OS X printing system.
- You want to see what’s involved in writing a printing plug-in.

The first part covers the basic concepts. Both Carbon and Cocoa developers will benefit from reading these chapters:

- [Printing Features and Printing Dialog Panes](Printing%20Features%20and%20Printing%20Dialog%20Panes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgiwviubz) discusses standard printing features, printing dialog panes, methods of extending a printing dialog, and the advantages of using a printing dialog extension.
- [Interface Guidelines for Custom Panes](Interface%20Guidelines%20for%20Custom%20Panes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgmwviubz) presents guidelines for designing an interface for a custom pane in a printing dialog.
- [Printing Dialog Extension Concepts](Printing%20Dialog%20Extension%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgqwviubz) discusses the printing dialog extension—its functional components, runtime behavior, and capabilities.

The second part is a tutorial that shows how to construct and use a printing dialog extension:

- [Creating a Plug-in Project](Creating%20a%20Plug-in%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqguwviubz) shows how Project Builder can help you create a plug-in project to build a printing dialog extension.
- [Core Tasks](Core%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgywviubz) shows how to implement much of the basic functionality in a printing dialog extension.
- [Custom Tasks](Custom%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqg4wviubz) shows how to implement the additional functionality that’s specific to a custom pane.
- [Integration Tasks](Integration%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqhawviubz) shows you how applications and printer modules install and communicate with their printing dialog extensions.

The appendixes cover a few remaining topics:

- [Utility Functions](Utility%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqhewviubr) shows how to implement several utility functions that all printing dialog extensions can use.
- [Printing Plug-in Header Functions](Printing%20Plug-in%20Header%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrrgawviubr) shows how to implement the three callback functions in the `PMPlugInHeader` interface.
- [Document Revision History](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrrgewviubr) contains a chronological list of the revisions to this book.

Carbon applications can also extend the printing dialogs using the `AppendDITL` function, an older approach. Cocoa applications can extend the printing dialogs by adding an accessory view to an `NSPageLayout` or `NSPrintPanel` object.

In both cases, the printing system displays your custom controls inside a new dialog pane that’s named for your application. Your application can host only a single custom pane in each dialog.

The section [Extending a Printing Dialog](Printing%20Features%20and%20Printing%20Dialog%20Panes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzzfvbuqmrqgiwugskiireecskf) discusses the various options in more detail, and makes some recommendations.

To get the most out of reading this book, you should first read _Mac OS X Printing System Overview_.

_Printing Plug-in Interfaces Reference_—the companion volume to this book—includes the reference documentation for the printing dialog extension API.

Both of these publications are available online in the ADC Reference Library.

You should also be familiar with Core Foundation plug-in concepts.

[Next](Printing%20Features%20and%20Printing%20Dialog%20Panes.md)

