---
title: Launch Services Programming Guide
apple_id: TP30000999
resource_type: Guide
platform: macOS
topic: Data Management
technology: ApplicationServices
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/LaunchServicesConcepts/LSCTasks/LSCTasks.html
archived_at: '2026-07-15T05:23:18.527860Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Launch Services Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Launch%20Services%20Concepts.md)

# Launch Services Tasks

This chapter summarizes how to use Launch Services to perform common tasks in your application.

The most common operation you’ll want to perform with Launch Services is opening applications, document files, and URLs. Depending on the circumstances, you can use any of four Launch Services functions for this purpose: `LSOpenFSRef`, `LSOpenFromRefSpec`, `LSOpenCFURLRef`, or `LSOpenFromURLSpec`.

When an item you wish to open is identified by a file-system reference (`FSRef`), the simplest way to open it is with `LSOpenFSRef`. You simply supply the file-system reference and Launch Services opens the item in a straightforward, no-frills, default way:

- If the designated item is an application:

  - If the application is not already running, it is launched and sent an `'oapp'` (“open application”) Apple event.
  - If the application is already running, it is activated (brought to the front of the screen) and sent an `'rapp'` (“reopen application”) Apple event.
- If the designated item is a document, its preferred application is launched (or activated if it was already running) and sent an `'odoc'` (“open document”) Apple event instructing it to open the document.

`LSOpenFSRef` in turn calls the more general function `LSOpenFromRefSpec`, a “Swiss Army knife” function that provides access to the full range of options for opening applications and documents. You can call this function directly yourself if you need to request something other than the default behavior. For instance, you can use it to:

- Open more than one document at a time, in either the same or different applications
- Force a document to open in an application other than its own preferred application
- Open documents for printing rather than for simple viewing or editing
- Force an application to open in the Classic emulation environment
- Open a specified application and hide all others
- Prevent an application or document from being added to the Finder’s Recent Items menu

Instead of a direct file-system reference to an item to be opened, you supply a pointer to a _launch specification,_ a data structure of type `LSLaunchFSRefSpec` that identifies one or more items along with additional information about how to open them:

- To open one or more documents, pass an array of file-system references in the launch specification’s `itemRefs` field; the `numDocs` field tells how many there are. If the `appRef` field is also non-null, it specifies the application in which to open the documents; otherwise, each document will be opened in its own preferred application.
- To open an application without specifying any documents, pass a file-system reference to the application in the launch specification’s `appRef` field and set the `itemRefs` field to `NULL` and `numDocs` to `0`.

The additional information in the launch specification includes:

- A flag word (`launchFlags`) containing various launch options to control the manner in which the application is opened; see [Launch Options](Launch%20Services%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqgiwueqkcijfeqske)
- A pointer to an optional Apple event descriptor record (`passThruParams`) containing parameter information to be passed with the Apple event the application receives on opening
- An optional reference constant (`asyncRefCon`) to be passed to your Carbon event handler routine for asynchronous launch notifications, as described under [Synchronous and Asynchronous Launch](Launch%20Services%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqgiwueqkcirdekq2i)

For both `LSOpenFSRef` and `LSOpenFromRefSpec`, the output parameter `outLaunchedRef` holds a pointer to a file-system reference that the function will set to indicate the application that was opened (or the first such application, in the case of multiple documents opened in different applications). If this information is not of interest, you can set this parameter to `NULL`.

To open a URL, you use the Launch Services function `LSOpenCFURLRef` or `LSOpenFromURLSpec`. These are analogous to `LSOpenFSRef` and `LSOpenFromRefSpec`, but accept Core Foundation URL references (`CFURLRef`) instead of file-system references. These functions also are often useful when you have a file-system pathname to an application or document to be opened: you can construct a URL with scheme `file` containing the path and then use this URL in place of a file-system reference to open the item. The `LSOpenCFURLRef` and `LSOpenFromURLSpec` functions are the only way to open URLs with other schemes, such as `http`, `ftp`, or `mailto`.

Like `LSOpenFSRef` for file-system references, `LSOpenCFURLRef` opens a designated URL in its preferred application in the default way. The more general function `LSOpenFromURLSpec` accepts a launch specification (analogous to the one for `LSOpenFromRefSpec` but of type `LSLaunchURLSpec` rather than `LSLaunchFSRefSpec`) specifying in greater detail the manner in which the URL is to be opened. As with `LSOpenFromRefSpec`, you can call this function directly yourself if you need to request something other than the default behavior provided by `LSOpenCFURLRef`.

Both `LSOpenCFURLRef` and `LSOpenFromURLSpec` determine what application to use to open a specified URL, launch the application (or activate it if it is already running), and send it an Apple event instructing it to open the URL. (With `LSOpenFromURLSpec`, you can override the URL’s preferred application by explicitly designating another application in the launch specification’s `appURL` field.) Ordinarily, the application receives a `'GURL'` (“get URL”) Apple event; but if the URL’s scheme is `file` and the application doesn’t claim to accept URLs with this scheme, it is sent an `'odoc'` (“open document”) Apple event instead.

Like their counterparts for file-system references, both of the URL-based functions can optionally return information about which application was actually opened (or the first, in the case of multiple URLs opened in different applications). This information is passed back via a Core Foundation URL reference to which you supply a pointer in the output parameter `outLaunchedURL`. You can set this parameter to `NULL` if the identity of the application is not of interest.

To find the preferred application for a document file, URL, or MIME type without opening it, use the Launch Services function `LSGetApplicationForItem`, `LSGetApplicationForURL`, or `LSCopyApplicationForMIMEType`, respectively. You identify the item of interest with a file-system reference (`FSRef`) to the document, a Core Foundation URL reference (`CFURLRef`) to the URL, or a Core Foundation string reference (`CFStringRef`) to a string specifying the MIME type. Another Launch Services function, `LSGetApplicationForInfo`, finds the preferred application for a family of documents defined by their file type, creator signature, filename extension, or any combination of these characteristics.

In each case, you must supply a _role mask_ (`LSRolesMask`) specifying one or more roles (`Editor`, `Viewer`, or `None`) that the application should claim with respect to the given item or family of items. (Note that `None` does not mean “no role at all,” but rather refers to a specific role that the application can claim with respect to the item: that of providing identifying information such as a display name and icon file without actually being able to open the item itself.) If you don’t care what role the application claims, use the mask value `kLSRolesAll`.

To receive the result, you pass a pointer to a file-system reference (in the `outAppRef` parameter), a Core Foundation URL reference (in the `outAppURL` parameter), or both; Launch Services will set the designated data structure to refer to the item’s preferred application. You can pass a null pointer for either of these parameters if you don’t care to receive the result in that form, but at least one of the two pointers must be non-null. (In the case of `LSCopyApplicationForMIMEType`, only the URL option is available; there is no `outAppRef` parameter.)

To find all known applications that can open a given item with a specified role, use the Launch Services function `LSCopyApplicationURLsForURL`. Although this function can only accept a URL reference and not a file-system reference, you can use it for document files as well, by passing a URL with scheme `file` referring to the desired document.

The Launch Services function `LSFindApplicationForInfo` locates an application based on its name, creator signature, bundle ID, or any combination of these characteristics. (Note that this differs from `LSGetApplicationForInfo` in that the specified characteristics apply to the application itself, rather than to the document files it can open.) As with other Launch Services functions discussed earlier, you can receive the result as either a file-system reference, a URL, or both, by passing pointers to the appropriate data structures to be filled with the information.

Often it is useful to find out whether a given application claims the ability to open a particular document or URL. The Launch Services functions `LSCanRefAcceptItem` and `LSCanURLAcceptURL` provide this information. You supply either file-system references or URL references to the item and the target application, along with a role mask and a flag word controlling certain technical aspects of the function’s behavior; the function responds by setting a Boolean variable, to which you provide a pointer, to indicate whether the application can accept the designated item.

It isn’t ordinarily necessary to register an application explicitly with Launch Services, since this is done for you automatically whenever the application becomes known to the Finder, the system is booted, or a new user logs in (see [Application Registration](Launch%20Services%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqgiwueqkcivfemq2e)). On those rare occasions when you do need to register an application explicitly (such as in a custom installer program), you can use the Launch Services function `LSRegisterFSRef` or `LSRegisterURL`, depending on whether the application is identified with a file-system reference or a Core Foundation URL reference. In either case, the application and its document binding information are copied into the Launch Services database, making the application available for opening documents and URLs.

You can use the Launch Services functions `LSCopyItemInfoForRef` and `LSCopyItemInfoForURL` to obtain a variety of information about file-system objects such as applications, documents, folders, or volumes. You supply a file-system reference or a Core Foundation URL reference (with scheme `file`) to identify the item of interest, along with a flag word (`LSRequestedInfo`) specifying the information you want and a pointer to an _item information record_ (`LSItemInfoRecord`) in which to receive back the information. The information in this record can include the item’s file type, creator signature, filename extension, and various flags describing attributes of the item (see [Item Information](Launch%20Services%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqgiwueqkcirauiqkk)).

Two other pieces of information about an item that you may find useful are its display name (used for displaying its name to the user on the screen) and its kind string (used, for instance in the Finder’s Get Info window or the Kind column of the Finder’s list view, to characterize the item’s general nature, such as `Application`, `Folder`, `Alias`, `JPEG Picture`, `QuickTime Movie`, or `FrameMaker Document`). You can obtain the display name with the Launch Services function `LSCopyDisplayNameForRef` or `LSCopyDisplayNameForURL` and the kind string with `LSCopyKindStringForRef`, `LSCopyKindStringForURL`, `LSCopyKindStringForTypeInfo`, or `LSCopyKindStringForMIMEType`.

[Next](Document%20Revision%20History.md)[Previous](Launch%20Services%20Concepts.md)

