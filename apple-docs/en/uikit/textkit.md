---
title: TextKit
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/textkit
source_url: 'https://developer.apple.com/documentation/uikit/textkit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/textkit.json'
content_hash: 'sha256:776792db3f01a426'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# TextKit

<sub>API Collection</sub>

Manage text storage and perform custom layout of text-based content in your app’s views.

## Overview

TextKit is a powerful and versatile text layout and rendering engine available in UIKit and AppKit. It provides several classes to control the layout of text, including [NSTextLayoutManager](nstextlayoutmanager.md), [NSTextContentStorage](nstextcontentstorage.md), [NSTextViewportLayoutController](nstextviewportlayoutcontroller.md), and [NSTextContainer](nstextcontainer.md).

In UIKit, you can use [UITextView](uitextview.md), which packages TextKit capabilities to provide a convenient text rendering and editing experience. [UITextView](uitextview.md) uses [NSTextContentStorage](nstextcontentstorage.md) as the text backing store manager. [NSTextContentStorage](nstextcontentstorage.md) uses an instance of [NSTextStorage](nstextstorage.md) as the backing store, which is a subclass of [NSMutableAttributedString](../foundation/nsmutableattributedstring.md). For an example, see [Enriching your text in text views](enriching-your-text-in-text-views.md).

Alternatively, you can build custom text views using your own `UIView` or `CALayer` by rendering text provided by the TextKit text engine. Use [NSTextContentStorage](nstextcontentstorage.md) if you want an [NSAttributedString](../foundation/nsattributedstring.md)-related storage type, or subclass [NSTextContentManager](nstextcontentmanager.md) to use your own. For an example, see [Using TextKit 2 to interact with text](using-textkit-2-to-interact-with-text.md).

When using [UITextView](uitextview.md), access the TextKit engine through the view’s [textLayoutManager](uitextview/textlayoutmanager.md), [textContainer](uitextview/textcontainer.md), and [textStorage](uitextview/textstorage.md) properties. [UITextView](uitextview.md) provides access to two layout engines: the modern [textLayoutManager](uitextview/textlayoutmanager.md), which uses [NSTextLayoutManager](nstextlayoutmanager.md), and the legacy [layoutManager](uitextview/layoutmanager.md), which uses [NSLayoutManager](nslayoutmanager.md). Use [textLayoutManager](uitextview/textlayoutmanager.md) for better performance, and support for international languages. Because TextKit classes are available in both UIKit and AppKit, the same techniques apply across iOS, iPadOS, macOS, tvOS, and visionOS.

## Topics

### Text management

- [NSTextContentStorage](nstextcontentstorage.md) — A concrete object for managing your view’s text content and generating the text elements necessary for layout.
- [NSTextContentManager](nstextcontentmanager.md) — An abstract class that defines the interface and a default implementation for managing the text document contents.
- [NSAttributedString](../foundation/nsattributedstring.md) — A string of text that manages data, layout, and stylistic information for ranges of characters to support rendering.
- [NSMutableAttributedString](../foundation/nsmutableattributedstring.md) — A mutable string with associated attributes (such as visual style, hyperlinks, or accessibility data) for portions of its text.

### Formatting and attributes

- [NSParagraphStyle](nsparagraphstyle.md) — The paragraph or ruler attributes for an attributed string.
- [NSMutableParagraphStyle](nsmutableparagraphstyle.md) — An object for changing the values of the subattributes in a paragraph style attribute.
- [NSTextTab](nstexttab.md) — A tab in a paragraph.
- [NSTextList](nstextlist.md) — A section of text that forms a single list.
- [Adding tables to attributed strings in UIKit](adding-tables-to-attributed-strings.md) — Create and configure tables in attributed strings and display them in a text view.

### Tables

- [Adding tables to attributed strings in UIKit](adding-tables-to-attributed-strings.md) — Create and configure tables in attributed strings and display them in a text view.
- [NSTextTable](nstexttable.md) — An object that represents a table of rows and columns in an attributed string.
- [NSTextTableBlock](nstexttableblock.md) — A text block that represents a single cell in a text table.
- [NSTextBlock](nstextblock.md) — An object that defines the size, spacing, and appearance of a block of text in an attributed string.

### Content elements

- [Enriching your text in text views](enriching-your-text-in-text-views.md) — Support line numbering, section collapsing, inline attachment caching, exclusion paths, text attachments, and text lists in a text view.
- [NSTextParagraph](nstextparagraph.md) — A class that represents a single paragraph backed by an attributed string as the contents.
- [NSTextListElement](nstextlistelement.md) — A class that represents a text list node.
- [NSTextElement](nstextelement.md) — An abstract base class that represents the smallest units of text layout such as paragraphs or attachments.
- [NSTextElementProvider](nstextelementprovider.md) — A protocol the text content manager and its concrete subclasses conform to, which defines the interface for interacting with custom content types of a text document.

### Location and selection

- [NSTextRange](nstextrange.md) — A class that represents a contiguous range between two locations inside document contents.
- [NSTextSelection](nstextselection.md) — A class that represents a single logical selection context that corresponds to an insertion point.
- [NSTextSelectionNavigation](nstextselectionnavigation.md) — An interface you use to expose methods for obtaining results from actions performed on text selections.
- [NSTextLocation](nstextlocation.md) — An interface you implement that represents an abstract location inside your document’s content.

### Layout

- [Using TextKit 2 to interact with text](using-textkit-2-to-interact-with-text.md) — Interact with text by managing text selection and inserting custom text elements.
- [Display text with a custom layout](display-text-with-a-custom-layout.md) — Lay out text in a custom-shaped container and apply glyph substitutions.
- [Managing viewport layout and attachment reuse in text views](managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md) — Customize layout and preserve attachment views in your text view subclass.
- [NSTextLayoutManager](nstextlayoutmanager.md) — The primary class that you use to manage text layout and presentation for custom text displays.
- [NSTextContainer](nstextcontainer.md) — A region where text layout occurs.
- [NSTextLayoutFragment](nstextlayoutfragment.md) — A class that represents the layout fragment typically corresponding to a rendering surface, such as a layer or view subclass.
- [NSTextLineFragment](nstextlinefragment.md) — A class that represents a line fragment as a single textual layout and rendering unit inside a text layout fragment.
- [NSTextViewportLayoutController](nstextviewportlayoutcontroller.md) — Manages the layout process inside the viewport interacting with its delegate.
- [NSTextViewportRenderingSurface](nstextviewportrenderingsurface.md) — A protocol that identifies a view or layer as a drawable element for a text layout fragment. _(beta)_
- [NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md) — A protocol that lets you use an object to identify a rendering surface when storing or retrieving it.
- [NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md) — A set of methods that define the orientation of text for an object.

### Attachments

- [NSTextAttachment](nstextattachment.md) — The values for the attachment characteristics of attributed strings and related objects.
- [NSTextAttachmentViewProvider](nstextattachmentviewprovider.md) — A container object that associates a text attachment at a particular document location with a view object.
- [NSAdaptiveImageGlyph](nsadaptiveimageglyph.md) — A data object for an emoji-like image that can appear in attributed text.
- [NSTextAttachmentContainer](nstextattachmentcontainer.md) — A set of methods that defines the interface to text attachment objects from a layout manager.
- [NSTextAttachmentLayout](nstextattachmentlayout.md) — A set of methods that defines the interface to attachment objects from a text layout manager.

### TextKit 1

- [NSTextStorage](nstextstorage.md) — The fundamental storage mechanism of TextKit that contains the text managed by the system.
- [NSLayoutManager](nslayoutmanager.md) — An object that coordinates the layout and display of text characters.

## See Also

### Text

- [Text display and fonts](text-display-and-fonts.md) — Display text, manage fonts, and check spelling.
- [Keyboards and input](keyboards-and-input.md) — Configure the system keyboard, create your own keyboards to handle input, or detect key presses on a physical keyboard.
- [Writing Tools](writing-tools.md) — Add support for Writing Tools to your app’s text views.
- [Handwriting recognition](handwriting-recognition.md) — Configure text fields and custom views that accept text to handle input from Apple Pencil.
