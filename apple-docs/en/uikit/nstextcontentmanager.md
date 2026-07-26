---
title: NSTextContentManager
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontentmanager
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentmanager.json'
content_hash: 'sha256:114cebcbd2bf1492'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextContentManager

<sub>Class</sub>

An abstract class that defines the interface and a default implementation for managing the text document contents.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class NSTextContentManager
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSTextContentStorage](nstextcontentstorage.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [NSTextElementProvider](nstextelementprovider.md)

## Topics

### Creating a content manager

- [- init](<nstextcontentmanager/init().md>) — Creates a new content manager.
- [- initWithCoder:](<nstextcontentmanager/init(coder_).md>) — Creates a new content manager object from data in an unarchiver.

### Controlling backing store synchronization

- [automaticallySynchronizesToBackingStore](nstextcontentmanager/automaticallysynchronizestobackingstore.md) — Determines whether to automatically synchronize with the backing store when an editing transaction finishes.

### Performing transactions

- [hasEditingTransaction](nstextcontentmanager/haseditingtransaction.md) — Indicates there’s an active editing transaction from the primary text layout manager.
- [- performEditingTransactionUsingBlock:](<nstextcontentmanager/performeditingtransaction(__).md>) — Performs an editing transaction and invokes a block upon completion.
- [- recordEditActionInRange:newTextRange:](<nstextcontentmanager/recordeditaction(in_newtextrange_).md>) — Records information about an edit action to the transaction.

### Working with layout managers

- [primaryTextLayoutManager](nstextcontentmanager/primarytextlayoutmanager.md) — The primary text layout manager for this content.
- [textLayoutManagers](nstextcontentmanager/textlayoutmanagers.md) — The array of text layout managers associated with this text content manager.
- [automaticallySynchronizesTextLayoutManagers](nstextcontentmanager/automaticallysynchronizestextlayoutmanagers.md) — Determines if the framework should automatically synchronize all text layout managers when exiting an editing transaction.
- [- addTextLayoutManager:](<nstextcontentmanager/addtextlayoutmanager(__).md>) — Adds the layout manager you provide to the list of layout managers.
- [- removeTextLayoutManager:](<nstextcontentmanager/removetextlayoutmanager(__).md>) — Removes the layout manager you specifiy from the list of layout managers.
- [- synchronizeTextLayoutManagers:](<nstextcontentmanager/synchronizetextlayoutmanagers(__).md>) — Synchronizes changes to all nonprimary text layout managers.

### Customizing and validating text elements

- [delegate](nstextcontentmanager/delegate.md) — The delegate for the content manager object.
- [NSTextContentManagerDelegate](nstextcontentmanagerdelegate.md) — The optional methods that delegates of content manager objects implement for customizing or validating text elements.
- [EnumerationOptions](nstextcontentmanager/enumerationoptions.md) — Values that control the order in which the framework enumerates text elements.

### Finding a specific text element

- [- textElementsForRange:](<nstextcontentmanager/textelements(for_).md>) — Returns an array of text elements that intersect with the range you specify.

## See Also

### Text management

- [NSTextContentStorage](nstextcontentstorage.md) — A concrete object for managing your view’s text content and generating the text elements necessary for layout.
- [NSAttributedString](../foundation/nsattributedstring.md) — A string of text that manages data, layout, and stylistic information for ranges of characters to support rendering.
- [NSMutableAttributedString](../foundation/nsmutableattributedstring.md) — A mutable string with associated attributes (such as visual style, hyperlinks, or accessibility data) for portions of its text.
