---
title: Quick Look Programming Guide
apple_id: TP40005020
resource_type: Guide
platform: macOS
topic: Data Management
technology: QuickLook
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Quicklook_Programming_Guide/Articles/QLCancelPreviewThumbnail.html
archived_at: '2026-07-18T02:12:34.673379Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quick Look Programming Guide](Introduction%20to%20Quick%20Look%20Programming%20Guide.md)


[Next](Debugging%20and%20Testing%20a%20Generator.md)[Previous](Assigning%20Core%20Graphics%20Images%20to%20Thumbnails.md)

# Canceling Previews and Thumbnails

A client application or the Quick Look daemon (`quicklookd`) may decide that it no longer needs a preview or thumbnail image that it has requested from a generator. Often this occurs because a user has indicated (for example, by closing a Finder window) that he or she is no interested in the listed documents. When the client or `quicklookd` decides it no longer needs a thumbnail or preview, Quick Look informs the appropriate generator in two ways, described in the following sections. The generator should look for this cancellation, stop any image generation in progress, and clean up any resources used in generating the preview or thumbnail.

When a client application no longer needs a thumbnail or preview that it has requested, it tells Quick Look, which then invokes one of two callback functions, depending on the type of item requested earlier:

- `CancelThumbnailGeneration` for canceling the generation of thumbnails
- `CancelPreviewGeneration` for canceling the generation of previews

The generator can implement these these functions to stop creating the previews and thumbnail images and clean up any resources so far used in their creation and return as quickly as possible.

However, it is not generally recommended that your code cancel the generation of previews and thumbnails by implementing one of these callback functions. Because Quick Look always calls these functions in a secondary thread, implementing it safely can be difficult. For example, you must be careful to match the cancellation request to the thread involved in the image generation. If you have any doubts about ensuring the thread-safety of your code, following the guidelines described in Canceling Through Polling.

When a client application no longer needs a thumbnail or preview that it has requested, it tells Quick Look, which then sets a Boolean flag for the request (in addition to invoking the `CancelThumbnailGeneration` or `CancelPreviewGeneration` callback function). A generator can access the value of this flag at any time by calling the [QLThumbnailRequestIsCancelled](https://developer.apple.com/documentation/quicklook/1402676-qlthumbnailrequestiscancelled) function (for thumbnails) or [QLPreviewRequestIsCancelled](https://developer.apple.com/documentation/quicklook/1402748-qlpreviewrequestiscancelled) function (for previews).

In your generator code you can periodically call these functions to poll Quick Look for the cancellation status of the current request. If a call returns a true value, clean up any resources used so far in the generation of the thumbnail or preview and return `noErr`. For most generators, this approach is recommended over the approach described in [Canceling Through a Callback Function](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamrqfvbuqmjtfvjvomy).

You should call `QLThumbnailRequestIsCancelled` and `QLPreviewRequestIsCancelled` at appropriate places in your generator code. Which places are appropriate depends on what the code is doing and how well-factored it is. Generally, you should test for request cancellation before doing some task that is time-consuming, especially when you won’t be able to query for cancellation status while that task is proceeding (for example, parsing a file).

An example is helpful here. The logic of a typical generator has the following structure in its `GeneratePreviewForURL` callback function:

1. Load document data.
2. Parse document data.
3. Composite the preview or convert it to a native Quick Look type.
4. Flush the graphics context or set the data in the response.

Given this structure, you probably should call `QLPreviewRequestIsCancelled` between steps 1 and 2 and again between steps 2 and 3. You don’t need to call the function between steps 3 and 4 because Quick Look will discard the preview when you complete step 4, after which you release your resources anyway.) The important idea is to poll for cancellation wisely; you shouldn’t poll too often, but at the same time you should poll often enough so that a cancelled preview or thumbnail doesn’t affect performance.

[Next](Debugging%20and%20Testing%20a%20Generator.md)[Previous](Assigning%20Core%20Graphics%20Images%20to%20Thumbnails.md)

