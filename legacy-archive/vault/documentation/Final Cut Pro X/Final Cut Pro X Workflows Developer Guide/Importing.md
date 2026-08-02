---
title: Final Cut Pro X Workflows Developer Guide
apple_id: TP40013781
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/FinalCutProX/Conceptual/FinalCutProXWorkflowsGuide/Importing/Importing.html
archived_at: '2026-07-15T07:32:29.688340Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Final Cut Pro X Workflows Developer Guide](About%20Final%20Cut%20Pro%20X%20Workflows.md)


[Next](Exporting.md)[Previous](About%20Final%20Cut%20Pro%20X%20Workflows.md)

# Importing

Final Cut Pro X can incorporate media that another application produces or manages as a collection of media files. You use FCPXML to bundle them along with keywords, markers, and metadata, or to describe rough cuts.

There are three ways to do this:

- The user imports an FCPXML document manually
- The other application initiates the importing process
- The user drags and drops objects from another application into Final Cut Pro X (new in version 10.3)

In Final Cut Pro 10.3 the import process is incremental. You can add or replace clips in existing events in a Final Cut Pro X library using FCPXML.

FCPXML allows you to transfer the following items from your application into Final Cut Pro X:

- A group of media assets
- A timeline sequence
- Keywords, markers, and metadata

The above items are organized into an event or a library in an FCPXML document that represents one of the following:

- A single library
- A group of events
- A group of clips, which may contain keywords or smart collections

Refer to _[Final Cut Pro X XML Format](https://developer.apple.com/library/archive/documentation/FinalCutProX/Reference/FinalCutProXXMLFormat/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011227)_ for details about FCPXML documents, and to [Final Cut Pro X Help](http://help.apple.com/finalcutpro/) for more information on how to import FCPXML document in Final Cut Pro X.

Final Cut Pro X imports the contents of an FCPXML document when:

- The user initiates the import process through the Final Cut Pro X File > Import XML menu item. Then the user chooses the target library in the Open File dialog.
- Another application initiates the import process by sending an FCPXML document to Final Cut Pro X through an _Open Document_ Apple event, such as when the user double clicks an FCPXML document in Finder, or instructs another application to send an FCPXML document to Final Cut Pro X.

  Final Cut Pro X displays the library chooser dialog where the user can choose an existing library known to Final Cut Pro X, or select one using the Open File dialog. The user can also create a new library. The selected library opens in Final Cut Pro X if it is not already open.

When an FCPXML document representing a library is imported, the content is merged into a library that is already open in Final Cut Pro X. You can also specify the target library in the FCPXML document itself through an import option. Refer to _[Final Cut Pro X XML Format](https://developer.apple.com/library/archive/documentation/FinalCutProX/Reference/FinalCutProXXMLFormat/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011227)_ for more details.

Final Cut Pro X imports FCPXML into events with matching names. For example, if the FCPXML has an event named _MyEvent_, and the specified target library already has an event named _MyEvent_, the contents of the FCPXML are imported into the existing _MyEvent_ event. If names conflict with event items in the FCPXML and the existing event, the user is given the choice to replace the existing event items with the items from the FCPXML, or keep both (the items in the existing event and the items in the FCPXML). If both are kept, the imported items are renamed. Refer to _[Final Cut Pro X XML Format](https://developer.apple.com/library/archive/documentation/FinalCutProX/Reference/FinalCutProXXMLFormat/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011227)_ for more details.

Your application can initiate the import process programatically using the `open` AppleScript command via the `-[NSApplication executeAndReturnError:]` method.

The following AppleScript opens the FCPXML document named `MyEvents` in Final Cut Pro X:

```
tell application "Final Cut Pro"
    activate
    open POSIX file ”/Users/JohnDoe/Documents/UberMAM/MyEvents.fcpxml”
end tell
```

Use the following code snippet to run the above AppleScript fragment to send the FCPXML document referenced above from your application to Final Cut Pro X:

```
// source contains the AppleScript source above
NSAppleScript* script = [[NSAppleScript alloc] initWithSource:source];
NSDictionary* errorInfo = nil;

NSAppleEventDescriptor* result = [script executeAndReturnError:&errorInfo];

// result: a sentinel representing no value is returned
[script release];
```


Final Cut Pro X allows importing the following objects from another application that supports drag-and-drop as XML:

- A group of events.
- A group of event items, such as clips, optionally with keywords and/or smart collections.

Refer to the [Final Cut Pro X Help](http://help.apple.com/finalcutpro/) for more information about events and event items.

The user can drag a group of events and drop them on to a library in the Final Cut Pro X sidebar. These events are added to the library if they don’t exist in the library. Otherwise, the contents of each event in the FCPXML are merged into the existing event with the same name.

The user can drag a group of event items and drop them on to an event in the Final Cut Pro X sidebar. These event items are added to the event if they don’t exist in the event. If there are existing event items with the same names, the user is prompted to replace the existing clips or to keep both the existing and the imported clips.

The user can also drag a group of event items and drop them into the Final Cut Pro X browser. When a single event is selected in the sidebar, the clips are brought into the event according to the rules above. The drop is not accepted if the selection in the sidebar is a library, one or more collection items, or more than one event.

The dragged objects must be represented as a valid FCPXML document encoded in Unicode and in a supported DTD version. The pasteboard type is `com.apple.finalcutpro.xml`. Refer to _[Final Cut Pro X XML Format](https://developer.apple.com/library/archive/documentation/FinalCutProX/Reference/FinalCutProXXMLFormat/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011227)_ for more details.

Your application can create the FCPXML representation of the objects selected when the user starts dragging them. However, a better approach is to create a _promise_ when the user starts dragging, and generate the actual FCPXML when Final Cut Pro X starts consuming the data. See _[Pasteboard Programming Guide](../../Cocoa/Pasteboard%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojz)_ for more details.

Sometimes, the user may want to start editing a clip while it is still being recorded or ingested.

Final Cut Pro X supports the import of the following types of media files while additional media is still being recorded or ingested onto them by other devices or applications:

- QuickTime Movie files with movie fragments
- MXF files, with an unknown duration or the essence duration shorter than the file duration

Final Cut Pro X supports growing files by keeping track of the file modification date and updating the information of the imported asset, including duration, when it detects that the file has been modified.

[Next](Exporting.md)[Previous](About%20Final%20Cut%20Pro%20X%20Workflows.md)

