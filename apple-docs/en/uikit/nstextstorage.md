---
title: NSTextStorage
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextstorage
source_url: 'https://developer.apple.com/documentation/uikit/nstextstorage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstorage.json'
content_hash: 'sha256:4dfc111ed8c623cb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextStorage

<sub>Class</sub>

The fundamental storage mechanism of TextKit that contains the text managed by the system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class NSTextStorage
```

## Overview

[NSTextStorage](nstextstorage.md) is a semi-concrete subclass of [NSMutableAttributedString](../foundation/nsmutableattributedstring.md) that adds behavior for managing a set of client [NSLayoutManager](nslayoutmanager.md) objects. A text storage object notifies its layout managers of changes to its characters or attributes, which lets the layout managers redisplay the text as needed.

You can access a text storage object from any thread of your app, but your app must guarantee access from only one thread at a time.

In macOS, this class also defines properties for getting and setting scriptable attributes of [NSTextStorage](nstextstorage.md) objects. Unless you’re dealing with scriptability, you shouldn’t access these properties directly. In particular, using the [characters](../appkit/nstextstorage/characters.md), [words](../appkit/nstextstorage/words.md), or [paragraphs](../appkit/nstextstorage/paragraphs.md) properties is an inefficient way to manipulate the text storage, since accessing these properties involves the creation of many objects. Instead, use the text access methods defined by [NSMutableAttributedString](../foundation/nsmutableattributedstring.md), [NSAttributedString](../foundation/nsattributedstring.md), [NSMutableString](../foundation/nsmutablestring.md), and [NSString](../foundation/nsstring.md) to perform character-level manipulation.

### Subclassing Notes

The [NSTextStorage](nstextstorage.md) class implements change management through the [beginEditing()](<../foundation/nsmutableattributedstring/beginediting().md>) and [endEditing()](<../foundation/nsmutableattributedstring/endediting().md>) methods, as well as verification of attributes, delegate handling, and layout management notification. The one aspect it doesn’t implement is managing the actual attributed string storage, which subclasses manage by overriding the two [NSAttributedString](../foundation/nsattributedstring.md) primitives:

- [string](../foundation/nsattributedstring/string.md)
- [attributes(at:effectiveRange:)](<../foundation/nsattributedstring/attributes(at_effectiverange_).md>)

Subclasses must also override two [NSMutableAttributedString](../foundation/nsmutableattributedstring.md) primitives:

- [replaceCharacters(in:with:)](<../foundation/nsmutableattributedstring/replacecharacters(in_with_)-6oq9r.md>)
- [setAttributes(_:range:)](<../foundation/nsmutableattributedstring/setattributes(__range_).md>)

These primitives should perform the change, then call [- edited:range:changeInLength:](<nstextstorage/edited(__range_changeinlength_).md>) to let the parent class know there are changes.

## Relationships

- **Inherits From**: [NSMutableAttributedString](../foundation/nsmutableattributedstring.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSItemProviderReading](../foundation/nsitemproviderreading.md), [NSItemProviderWriting](../foundation/nsitemproviderwriting.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Processing the editing actions

- [delegate](nstextstorage/delegate.md) — The delegate for the text storage object.
- [NSTextStorageDelegate](nstextstoragedelegate.md) — The optional methods that delegates of text storage objects implement to handle text-edit processing.

### Accessing the layout managers

- [layoutManagers](nstextstorage/layoutmanagers.md) — The layout managers for the text storage object.
- [- addLayoutManager:](<nstextstorage/addlayoutmanager(__).md>) — Adds a layout manager to the text storage object’s set of layout managers.
- [- removeLayoutManager:](<nstextstorage/removelayoutmanager(__).md>) — Removes a layout manager from the text storage object’s set of layout managers.

### Managing edits

- [- edited:range:changeInLength:](<nstextstorage/edited(__range_changeinlength_).md>) — Tracks changes made to the text storage object, allowing the text storage to record the full extent of changes.
- [- processEditing](<nstextstorage/processediting().md>) — Cleans up changes to the text storage object and notifies its delegate and layout managers of changes.

### Fixing the string attributes

- [- invalidateAttributesInRange:](<nstextstorage/invalidateattributes(in_).md>) — Invalidates attributes in the specified range.
- [- ensureAttributesAreFixedInRange:](<nstextstorage/ensureattributesarefixed(in_).md>) — Ensures that attribute fixing occurs in the specified range.
- [fixesAttributesLazily](nstextstorage/fixesattributeslazily.md) — A Boolean value that indicates whether the text storage object fixes attributes lazily.

### Determining the nature of changes

- [editedMask](nstextstorage/editedmask.md) — A mask that describes the kinds of edits pending for the text storage object.
- [editedRange](nstextstorage/editedrange.md) — The range of text that contains changes.
- [changeInLength](nstextstorage/changeinlength.md) — The difference between the current length of the edited range and its length before editing.

### Accessing scriptable properties

- [attributeRuns](../appkit/nstextstorage/attributeruns.md) — The text storage contents as an array of attribute runs.
- [paragraphs](../appkit/nstextstorage/paragraphs.md) — The text storage contents as an array of paragraphs.
- [words](../appkit/nstextstorage/words.md) — The text storage contents as an array of words.
- [characters](../appkit/nstextstorage/characters.md) — The text storage contents as an array of characters.
- [font](../appkit/nstextstorage/font.md) — The font for the text storage.
- [foregroundColor](../appkit/nstextstorage/foregroundcolor.md) — The color for the text.

### Constants

- [EditActions](nstextstorage/editactions.md) — Constants that indicate the types of changes.

### Notifications

- [NSTextStorageWillProcessEditingNotification](nstextstorage/willprocesseditingnotification.md) — A notification that posts before a text storage begins processing edits.
- [NSTextStorageDidProcessEditingNotification](nstextstorage/didprocesseditingnotification.md) — A notification that posts after a text storage finishes processing edits.

### Accessing the storage controller

- [textStorageObserver](nstextstorage/textstorageobserver.md) — The observer for the text storage object.
- [NSTextStorageObserving](nstextstorageobserving.md) — Optional methods that delegates implement to handle editing and transaction processing.

## See Also

### TextKit 1

- [NSLayoutManager](nslayoutmanager.md) — An object that coordinates the layout and display of text characters.
