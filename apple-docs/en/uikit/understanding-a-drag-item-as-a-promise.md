---
title: Understanding a drag item as a promise
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/understanding-a-drag-item-as-a-promise
source_url: 'https://developer.apple.com/documentation/uikit/understanding-a-drag-item-as-a-promise'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/understanding-a-drag-item-as-a-promise.json'
content_hash: 'sha256:b42a83936a73882b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Drag and drop](drag-and-drop.md)

# Understanding a drag item as a promise

<sub>Article</sub>

Use drag items to convey data representation promises between a source app and a destination app.

## Overview

When a user drags an onscreen visual representation of an item in your app, such as a photo, a Maps location, a Calendar event, or a text selection, your app associates the underlying data with a _drag item_. The drag item, in turn, uses an _item provider_. Your app populates the item provider’s [registeredTypeIdentifiers](../foundation/nsitemprovider/registeredtypeidentifiers.md) array with [uniform type identifiers (UTIs)](https://developer.apple.com/library/content/documentation/General/Conceptual/DevPedia-CocoaCore/UniformTypeIdentifier.html).

![A drag item with its contained item provider and array of uniform type identifiers](../../../attachments/f3295ba2321f55ef49342ac6d5c16a6e/media-2903721@2x.png)

The array of UTIs constitutes the source app’s promise about the specific data representations it can deliver, on request, to a destination app. The term _promise_ means that, at the time your app constructs a drag item, it commits to providing certain data representations but doesn’t yet perform the work to create them. Although it appears to the user that the item itself is being dragged, the drag item instead consists of promises along with a preview image that remains under the user’s touch point onscreen.

The portion of your app that constructs the drag item is the _drag interaction delegate_ ([UIDragInteractionDelegate](uidraginteractiondelegate.md)). On the destination side, an app’s _drop interaction delegate_ ([UIDropInteractionDelegate](uidropinteractiondelegate.md)) interacts with the drag item to consume promised data.

This table shows the protocols you implement to support constructing or consuming a drag item, depending on whether a view in your app is acting as a source or destination:

| Drag-and-drop role | Protocol | Your implementation |
|---|---|---|
| Source app | [NSItemProviderWriting](../foundation/nsitemproviderwriting.md) | Register UTIs |
| Destination app | [NSItemProviderReading](../foundation/nsitemproviderreading.md) | Request items |

The following classes automatically support these protocols: [NSString](../foundation/nsstring.md), [NSAttributedString](../foundation/nsattributedstring.md), [NSURL](../foundation/nsurl.md), [UIColor](uicolor.md), and [UIImage](uiimage.md).

## See Also

### Essentials

- [Making a view into a drag source](making-a-view-into-a-drag-source.md) — Adopt drag interaction APIs to provide items for dragging.
- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md) — Adopt drop interaction APIs to selectively consume dragged content.
- [Adopting drag and drop in a custom view](adopting-drag-and-drop-in-a-custom-view.md) — Demonstrates how to enable drag and drop for a `UIImageView` instance.
- [Adopting drag and drop in a table view](adopting-drag-and-drop-in-a-table-view.md) — Demonstrates how to enable and implement drag and drop for a table view.
