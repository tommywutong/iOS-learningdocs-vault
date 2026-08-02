---
title: AppleScript Overview
apple_id: 10000156i
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptX/RevisionHistory.html
archived_at: '2026-07-15T05:19:37.499018Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AppleScript Overview](Introduction%20to%20AppleScript%20Overview.md)


[Previous](AppleScript%20Utilities%20and%20Applications.md)

# Document Revision History

This table describes the changes to _AppleScript Overview_.

| __Date__ | __Notes__ |
| 2007-10-31 | Updated to reflect AppleScript changes for OS X version 10.5. |
|  | Added a chapter to describe the [Scripting Bridge](Scripting%20Bridge.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinrxfvjvomi) technology that was introduced in OS X v10.5. In several places, noted that using Scripting Bridge can be easier and more efficient than using native Apple events to use the services of scriptable applications. |
|  | In [Open Scripting Architecture](Open%20Scripting%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknzrfvbecqsfijdugrq), added a section [Faceless Background Applications](Open%20Scripting%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknzrfvjvomi) that describes this mechanism for extending AppleScript. |
|  | In the renamed chapter [AppleScript Utilities and Applications](AppleScript%20Utilities%20and%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknzqfvbecqsfijdugrq), added a section to describe the AppleScript helper application [Database Events](AppleScript%20Utilities%20and%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknzqfvjvomi), which is available beginning in OS X v10.4. In the same chapter, noted that the AppleScript Utility and Folder Actions Setup applications are themselves scriptable. Also added information on new terminology supported by the System Events application, including the Desktop, Dock Preferences, Network Preferences, Security, and other new suites. |
|  | Combined information that was previously in several places into the renamed chapter [Scriptable Applications](Scriptable%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknrzfvbecqsfijdugrq). The section [Support for Cocoa Applications](Scriptable%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknrzfuytcnjrgu3do) now provides links to sample code projects. |
|  | Added various information to the section [Specifying Scripting Terminology](Scriptable%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknrzfuytcnjwge3dk), including a note that changes to sdef usage in Cocoa applications for OS X v10.5 are described in the Scripting section of _[Foundation Release Notes for macOS 10.13 and iOS 11](../../../releasenotes/Foundation/Foundation%20Release%20Notes%20for%20macOS%2010.13%20and%20iOS%2011.md)_. |
|  | In the section [Executing AppleScript Scripts as Shell Commands](Scripting%20with%20AppleScript.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknryfuytcnbyge4ds), noted that in OS X v10.5, you can use the # symbol as a comment-to-end-of-line token, providing a way to make a plain AppleScript script into a Unix executable. Also noted that in OS X v10.5 there is a command-line tool to display compiled scripts as text, `osadecompile`. |
|  | In the section [The Parts of the Open Scripting Architecture](Open%20Scripting%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknzrfuytcnbxha2ts), noted that in OS X v10.5, the Apple event framework, `AE.framework`, is now part of `CoreServices.framework`. |
|  | Updated [Figure 1](Scripting%20with%20AppleScript.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknryfuytcnjtgazdglkcijbugrceifda) showing a Finder dictionary. |
| 2006-03-08 | Made minor editorial corrections and updated links. |
|  | In several places that refer to how AppleScript works with Cocoa applications, added or revised links to _[Cocoa Scripting Guide](../../Cocoa/Cocoa%20Scripting%20Guide/Introduction%20to%20Cocoa%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnru)_. |
|  | In the section [Resolving Objects in the Application](Scriptable%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknrzfuytcnjtg43ds), added information about the AppleScript object model and about resolving objects in Cocoa applications. |
| 2005-04-29 | Added information on Open Scripting Architecture (OSA) and the Automator, Script Utility, System Events, and Image Events applications. Changed title from "AppleScript for OS X." |
| 2004-05-27 | Added section [Determining What to Make Scriptable](Scriptable%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknzrfuytcnjvg4zta). |
|  | Moved some existing material into a new section, [Scriptable Applications](Scriptable%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknrzfvbecqsfijdugrq). |
|  | Made minor text revisions to avoid duplication with _Getting Started with AppleScript_. |
|  | Made some document references into links. |
| 2003-09-17 | Updated some links to other documentation. |
| 2003-05-15 | Moved this material into a separate document. |
|  | Reorganized some sections, added documentation links, and made minor corrections. |

[Previous](AppleScript%20Utilities%20and%20Applications.md)

