---
title: Cocoa Scripting Guide
apple_id: TP40002164
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: null
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/RevisionHistory.html
archived_at: '2026-07-15T07:18:47.901273Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Scripting Guide](Introduction%20to%20Cocoa%20Scripting%20Guide.md)


[Next](Glossary.md)[Previous](Script%20Suite%20and%20Script%20Terminology%20Files.md)

# Document Revision History

This table describes the changes to _Cocoa Scripting Guide_.

| __Date__ | __Notes__ |
| 2008-03-11 | Minor corrections for working with sdefs. |
|  | In the examples in [Class Elements](Preparing%20a%20Scripting%20Definition%20File.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzxfuytcmrxge2dg), now using the four-character code `"ricT"` for the `rich text` class. |
| 2007-10-31 | Added pointers to new information in OS X version 10.5. |
|  | Noted in several places that you can read about changes in Cocoa scripting support for OS X v10.5, including changes in sdef usage, in the Scripting section of OS X Tiger Developer Release Notes for Cocoa Foundation Framework. |
|  | Converted [Evolution of Cocoa Scriptability Information](Evolution%20of%20Cocoa%20Scriptability%20Information.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjzfvjvomi) to an Appendix. |
|  | Converted [Script Suite and Script Terminology Files](Script%20Suite%20and%20Script%20Terminology%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2dclkcijbueq2jjjcq) to an Appendix and noted that the information it contains is useful primarily if your scriptable application will run in versions of the Mac OS prior to version 10.4. (Otherwise, you can use the sdef format, described in [Preparing a Scripting Definition File](Preparing%20a%20Scripting%20Definition%20File.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzzfvbeeq2cineuuri).) |
| 2007-07-23 | Added information on handling the open application Apple event. |
|  | For details, see [Open Application](How%20Cocoa%20Applications%20Handle%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgiztsljrgeztemjzha) section. |
|  | In the section [Maintain KVC Compliance](Getting%20and%20Setting%20Properties%20and%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvona), added implementation details for your overrides of `valueIn<Key>WithName:` and `valueIn<Key>WithUniqueID:`. |
| 2006-04-04 | Added information about NSObject and the item AppleScript class. Added reference and related document links to the HTML table of contents. |
|  | Updated scriptability information in [Table 3-1](Implementing%20a%20Scriptable%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztolktk4zq). |
|  | Modified test script in [Listing 8-1](Testing%2C%20Debugging%2C%20and%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobrfvjvoni). |
| 2006-03-08 | Combines and updates information formerly in two documents, "Sdef Scriptability Guide for Cocoa" and "Scriptable Application Programming Guide for Cocoa." |
|  | Revised [Overview of Cocoa Support for Scriptable Applications](Overview%20of%20Cocoa%20Support%20for%20Scriptable%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzwfvbeeq2cineuuri) to provide a more complete introduction to Cocoa scripting. Changes include a description of the AppleScript object model, a table of the basic data types supported by Cocoa scripting, and expanded information on scriptability information formats. |
|  | Provided [Implementing a Scriptable Application](Implementing%20a%20Scriptable%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztolkcijbuurkfivbq), a revision to the former "Key Steps" chapter. It includes a revised set of implementation steps (in the section [Implementation Guidelines](Implementing%20a%20Scriptable%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztolktk4za)). |
|  | Provided [Preparing a Scripting Definition File](Preparing%20a%20Scripting%20Definition%20File.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzzfvbeeq2cineuuri), which revises and merges two former chapters, "Creating a Scripting Definition" and "Scripting Definition Reference." |
|  | Added the largely new chapters [Getting and Setting Properties and Elements](Getting%20and%20Setting%20Properties%20and%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvomi) and [Object Specifiers](Object%20Specifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmznknltc). The former provides many details on working with KVC (including revised accessor samples), as well as a section on the `properties` property. The latter includes new illustrations and code samples, and includes conceptual information previously located in [NSScriptObjectSpecifier](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier) and `NSScriptObjectSpecifiers`. |
|  | Revised and expanded the chapter [Script Commands](Script%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2delkcijbueq2jjjcq), adding an illustration, sample code, and a comprehensive table that describes default support for AppleScript commands and how to customize it ([Table 7-1](Script%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2delktk4yti)). |
|  | Revised the chapter [Testing, Debugging, and Performance](Testing%2C%20Debugging%2C%20and%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobrfvbeeq2kivcukqy), adding new testing tips and a section on performance. |
|  | Revised the chapters [Cocoa Scripting Classes and Categories](Cocoa%20Scripting%20Classes%20and%20Categories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztilkcijbuer2diveq), [How Cocoa Applications Handle Apple Events](How%20Cocoa%20Applications%20Handle%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgiztslkcijbueq2jjjcq), and [Evolution of Cocoa Scriptability Information](Evolution%20of%20Cocoa%20Scriptability%20Information.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjzfvjvomi) (formerly a section in "Scripting Definition File Reference"). |
|  | Merged script suite information into the chapter [Script Suite and Script Terminology Files](Script%20Suite%20and%20Script%20Terminology%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2dclkcijbueq2jjjcq). Added tables for enumerations and deleted deprecated information (such as "Working With ASCII Script Suite Files"). |

[Next](Glossary.md)[Previous](Script%20Suite%20and%20Script%20Terminology%20Files.md)

