---
title: File System Overview
apple_id: 10000185i
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFileSystem/Articles/FilenameExtensions.html
archived_at: '2026-07-15T08:15:27.088403Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Overview](Introduction%20to%20the%20File%20System%20Overview.md)


[Next](Display%20Names.md)[Previous](File%20System%20Guidelines.md)

# Filename Extensions

Some Macintosh software developers react to filename extensions with dismay. As a means for specifying document type and ownership, extensions seem primitive compared to the type and creator codes and the other rich metadata made possible by the multi-fork HFS and HFS+ volume formats. However, in the Internet age, documents frequently travel around a heterogeneous network. A document may move from a Macintosh to a Linux network server to a Windows computer. Each computer on this path may have a different notion of what constitutes a document type.

Many computer systems define document types solely by well-known filename extensions (such as `.jpg`, `.mp3`, and `.html`). These systems might not know what to do with a file that has no extension and may treat it as an unknown type. Other systems also have little or no knowledge of the HFS+ file system and the metadata it stores. When transferring files, they might strip out this metadata so that it is irretrievably lost.

In order to preserve the Macintosh user experience, Mac OS X provides a way to hide filename extensions on a per-file basis. Each file in the file system has a special flag identifying whether its extension is hidden or shown. Users can set this flag based on whether or not they want the filename extension shown. Users can adjust their Finder preferences to hide or show filename extensions for all files, regardless of the settings for individual files.

To ensure platform interoperability and retain the Mac OS X user experience, there are some basic guidelines you should follow to support filename extensions:

- Make sure all of your document types have an associated filename extension.
- Use the display name of a file whenever you display files in your user interface. (See [Getting Display Names in Your Code](Display%20Names.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4tqljrgeytkojs) for details.)
- Save dialogs should allow users to control whether to hide filename extensions.
- Applications should preserve the existing show/hide setting and filename extension when opening or saving a document.
- Applications should add an appropriate extension when saving a new file or when saving an existing file using the Save As command.
- Applications should not append an extension or change the show/hide setting of a file that does not have an extension.
- Applications should display an alert when the user tries to save a file after typing a known, incorrect filename extension.

For Carbon applications, you use Navigation Services to create a Save dialog. If you specify the `kNavPreserveSaveFileExtension` creation option, the dialog preserves and initially hides the filename extension of the default filename. You can also extend your dialog to give the user the choice of showing or hiding filename extensions. If you do, you can use the `NavDialogSetSaveFileExtensionHidden` function to set the current extension visibility and use the `NavDialogGetSaveFileExtensionHidden` function to determine the user’s choice. See [Save Dialog Scenarios](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4toljrgeydkobu) for more information on potential scenarios when saving files.

If the user does not type a filename extension in your Save dialog, your dialog code should leave the Hide Extension checkbox enabled.

For [Cocoa](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Cocoa.html#//apple_ref/doc/uid/TP40008195-CH9) applications, the NSSavePanel class also provides options for hiding and showing filename extensions. If you want the user to have the option of showing or hiding filename extensions, call the `setCanSelectHiddenExtension:` method of NSSavePanel prior to displaying the dialog. This method controls the display of a checkbox that enables the user to toggle the extension visibility. You can use the `isExtensionHidden` method to determine the user’s choice.

Carbon applications can also modify the visibility of filename extensions outside of Save dialogs using Launch Services. The `LSSetExtensionHiddenForRef` and `LSSetExtensionHiddenForURL` functions let you set the visibility of filename extensions using `FSRef` and `CFURLRef` types, respectively. Cocoa applications can similarly use the `changeFileAttributes:atPath:` method of NSFileManager.

When saving files, there are several scenarios to consider related to hiding and showing filename extensions:

- What happens when the user types a known, correct extension?
- What happens when the user types a known, incorrect extension?
- What happens when the user types no extension or an unknown extension?

The first scenario is the easiest to deal with. If the user types a known, correct extension, your dialog code should clear the hide extension flag and corresponding dialog controls. When saving the file, you should set the properties of the file to indicate that the extension should be shown.

For situations where the user types a known, incorrect extension, you should display an alert. In your alert, let the user know that an incorrect extension was entered and suggest a correct extension. The dialog box should then let the user cancel the operation, change the extension, or save the filename with both extensions, that is, with the correct extension appended to the user-entered text.

For situations where the user types no extension or an unknown extension, add an appropriate extension to the filename and mark it as hidden. For example, if the user saves a text document as `MyDocument.old`, you would create a file named “MyDocument.old.txt” and set the file attributes to indicate the extension is hidden. Thus, the user continues to see the name `MyDocument.old` in the Finder and in Open and Save dialogs.

In addition to filename extensions, applications should also set a file type and optionally a creator type for any files they create. Although these type codes are not strictly necessary, they do ensure interoperability with applications in the Classic environment. If a given file already has a file type or creator type, you should preserve that information.

Applications may set a creator type for documents they create. Doing so creates a tight binding between the document and the application that created it. Applications should not quietly change the creator type for documents that already have one. If you want to change the creator type of documents your application opens, your application should post a Save dialog when the user saves the file. This gives the user an opportunity to rename the file as needed. You might need to do this if editing a document in your application changes the type of the file. In this case, you should also assign an appropriate filename extension to the file in the Save dialog.

Applications that are not a primary editor for documents of a given type should not set a creator type for those documents. For example, an Internet browser may download and save files of many different types, but that does not mean it owns all of those files.

[Next](Display%20Names.md)[Previous](File%20System%20Guidelines.md)

