---
title: Final Cut Pro X Workflows Developer Guide
apple_id: TP40013781
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/FinalCutProX/Conceptual/FinalCutProXWorkflowsGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:32:29.699370Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Importing.md)

# About Final Cut Pro X Workflows

This document describes how Final Cut Pro X works with other applications as part of a workflow, and the requirements for such applications to exchange data and interact with Final Cut Pro X. The discussion applies to Final Cut Pro X v10.3 or later.

This document is intended for application developers who wish to enable their application to collaborate with Final Cut Pro X.

Final Cut Pro X works with other applications in various workflows, for example:

- An application ingests footage from an external device for editing in Final Cut Pro X.
- An application that performs color grading or graphic composting on a Final Cut Pro X edit result.
- An asset management system manages the media assets used by Final Cut Pro X.

Final Cut Pro X exchanges media data and edit descriptions with other applications as shown in Figure I-1.

__Figure I-1__  Final Cut Pro X workflow

!

Final Cut Pro X exchanges media data and edit descriptions with other applications through importing and exporting:

- Importing—incorporating media assets, along with additional information such as metadata and rough cuts, from another application into Final Cut Pro X.
- Exporting—delivering edits from Final Cut Pro X to another application as rendered media and/or a description of the edits.

In both cases, you use Final Cut Pro X XML Format (FCPXML) to represent rough cuts, edit descriptions, and metadata.

Final Cut Pro X interacts with another application through Apple events requesting information or triggering an action to automate the exchange. Your application must respond to incoming Apple events.

In particular, to control the export process, Final Cut Pro X uses the events and classes defined in the ProVideo Asset Management scripting terminology suite.

Starting with Final Cut Pro 10.3, you can use the following:

- Drag-and-drop—Drag and drop libraries, projects, events, and clips between Final Cut Pro X and another application that supports drag-and-drop functionality. The dragged objects are represented as XML in the pasteboard.
- Incremental Import—Import FCPXML into one or more existing events by adding new clips or replacing existing clips. (This is now the default behavior in Final Cut Pro X regardless of the imported FCPXML’s DTD version.)

The following custom share destination enhancements were added after Final Cut Pro X 10.1.2:

- Library archive integration (Final Cut Pro X v10.2.2)—Include an archive of the library, excluding media and temporary files, along with the FCPXML in the export output.
- FCPXML DTD version (Final Cut Pro X v10.2)—Export FCPXML in either the current FCPXML DTD version or the previous FCPXML DTD version.

In addition to experience with Final Cut Pro X, it is assumed that you are familiar with:

- Final Cut Pro X XML Format (FCPXML)
- Cocoa Scripting support for handling Apple events
- How to implement drag-and-drop

The following resources may be helpful while integrating your application with the Final Cut Pro X workflow:

- _[Final Cut Pro X XML Format](https://developer.apple.com/library/archive/documentation/FinalCutProX/Reference/FinalCutProXXMLFormat/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011227)_
- [Final Cut Pro X Help](http://help.apple.com/finalcutpro/)
- _[Cocoa Scripting Guide](../../Cocoa/Cocoa%20Scripting%20Guide/Introduction%20to%20Cocoa%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnru)_
- _[AVFoundation Programming Guide](../../Audio%20Video/AVFoundation%20Programming%20Guide/About%20AVFoundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcoby)_
- _[Launch Services Programming Guide](../../Carbon/Launch%20Services%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojz)_
- _[Drag and Drop Programming Topics](../../Cocoa/Drag%20and%20Drop%20Programming%20Topics/Introduction%20to%20Drag%20and%20Drop.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3ds2i)_
- _[Pasteboard Programming Guide](../../Cocoa/Pasteboard%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojz)_
[Next](Importing.md)

