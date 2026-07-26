---
title: 'init(filePresenter:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilecoordinator/init(filepresenter:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/init(filepresenter:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/init%28filepresenter%3A%29.json'
content_hash: 'sha256:34ea66bca492c598'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileCoordinator](../nsfilecoordinator.md)

# init(filePresenter:)

<sub>Initializer</sub>

Initializes and returns a file coordinator object using the specified file presenter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(filePresenter filePresenterOrNil: (any NSFilePresenter)?)
```

## Parameters

- `filePresenterOrNil` — The file presenter object that is initiating some action on its file or directory. This object is assumed to be performing the relevant file or directory operations and therefore does not receive notifications about those operations from the returned file coordinator object. This parameter may be `nil`.

## Return Value

A file coordinator object to use to coordinate file-related operations.

## Discussion

Specifying a file presenter at initialization time is strongly recommended, especially if the file presenter is initiating the file operation. Otherwise, the file presenter itself would receive notifications when it made changes to the file and would have to compensate for that fact. Receiving such notifications could also deadlock if the file presenter’s code and its notifications run on the same thread.

Specifically, associating an NSFileCoordinator with an NSFilePresenter accomplishes the following:

- Prevents the file coordinator from sending messages to the file presenter. This means that the file presenter won’t receive notifications about its own file operations. There is one exception: Messages about versions of the presented item being added, remove, or resolved during coordinated writing are sent to every relevant file presenter.
- Prevents deadlocks that could occur when the file presenter performs a coordinated write operation in response to a [- savePresentedItemChangesWithCompletionHandler:](<../nsfilepresenter/savepresenteditemchanges(completionhandler_).md>) message. Usually, coordinated writes must wait for all the coordinated read operations on the same file or directory. However, when a coordinated read forces a file presenter to write its contents, the write operation must proceed before the read operation can finish.
- Prevents race conditions that could occur when the file presenter is sent a [- presentedItemDidMoveToURL:](<../nsfilepresenter/presenteditemdidmove(to_).md>) message and at the same time—but before this message is dequeued—the file presenter enqueues an operation using the old URL on a different queue. For the file coordinators to work effectively, however, the coordinator must be initialized on the same operation queue that the file presenter uses to receive its messages.
- Allows the file coordination mechanism to gracefully handle file presenters that initially contain `nil` in the [presentedItemURL](../nsfilepresenter/presenteditemurl.md) property, but that can later contain a non-`nil` value after creating the item using a coordinated write operation. For example, AppKit uses this feature to instantiate new [NSDocument](../../appkit/nsdocument.md) objects immediately, instead of waiting until after the user saves the document.
