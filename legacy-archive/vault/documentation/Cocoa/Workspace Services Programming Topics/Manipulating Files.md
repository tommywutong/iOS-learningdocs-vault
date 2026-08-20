---
title: Workspace Services Programming Topics
apple_id: 10000100i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2009-06-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Workspace/Articles/ManipulatingFiles.html
archived_at: '2026-07-15T07:21:22.454501Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Workspace Services Programming Topics](Introduction%20to%20Workspace%20Services.md)


[Next](Manipulating%20Applications.md)[Previous](Retrieving%20Information%20About%20Files.md)

# Manipulating Files

This task explains how to perform Finder-like operations on files using `NSWorkspace`.

NSWorkspace provides several methods for opening files:

- To open a file with default behavior, as if the user had opened it from the Finder, use the `openFile:` method.
- To open the file with a specific application, use `openFile:withApplication:`.
- To open the file with a specific application and specify if the current application should deactivate (allowing the new application to become active), use `openFile:withApplication:andDeactivate:`.

To show a file in the Finder, use the `selectFile:inFileViewerRootedAtPath:` method.

To open a URL with the default handler for the resource type, use the `openURL:` method. The URL can be either local or remote. For example, a local files are opened as if double-clicked in the Finder, and a web addresses are opened in the default web browser.

The NSWorkspace method `performFileOperation:source:destination:files:tag:` performs various file system operations on files, such as moving and copying. The following code fragment shows how to copy a file at `fullPath` from `source` to `destination`:

```
NSInteger tag;
BOOL succeeded;
NSString *source, *destination, *fullPath;    // Assume these exist
NSWorkspace *workspace = [NSWorkspace sharedWorkspace];
NSArray *files = [NSArray arrayWithObject:fullPath];

succeeded = [workspace performFileOperation:NSWorkspaceCopyOperation
                       source:source destination:destination
                       files:files tag:&tag];
```

In this code fragment, on return `succeeded` contains `YES` if the operation succeeded, `NO` otherwise. Also, the method sets `tag` to a negative integer if the operation fails, `0` if the operation is performed synchronously and succeeds, and a positive integer if the operation is performed asynchronously and succeeds.

[Next](Manipulating%20Applications.md)[Previous](Retrieving%20Information%20About%20Files.md)

