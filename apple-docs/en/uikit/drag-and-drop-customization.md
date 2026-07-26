---
title: Drag and drop customization
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/drag-and-drop-customization
source_url: 'https://developer.apple.com/documentation/uikit/drag-and-drop-customization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/drag-and-drop-customization.json'
content_hash: 'sha256:22567a95dd701789'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Text display and fonts](text-display-and-fonts.md)

# Drag and drop customization

<sub>API Collection</sub>

Extend the standard drag and drop support for text views to include custom types of content.

## Overview

The [UITextField](uitextfield.md) and [UITextView](uitextview.md) classes provide built-in support for dragging and dropping text and images. You can extend this support to your own custom data types by adding a text drag delegate or text drop delegate to your views. Your text drag delegate adopts the [UITextDragDelegate](uitextdragdelegate.md) protocol and is responsible for providing the items to be dragged. Your text drop delegate adopts the [UITextDropDelegate](uitextdropdelegate.md) protocol and handles drops containing items with your custom data types.

## Topics

### Text view additions

- [UITextDragDelegate](uitextdragdelegate.md) — The interface for customizing the behavior of a drag activity for a text view.
- [UITextDropDelegate](uitextdropdelegate.md) — The interface for configuring a text view’s drop behavior.
- [UITextDraggable](uitextdraggable.md) — The interface that determines if a text view is a drag source.
- [UITextDragOptions](uitextdragoptions.md) — A set of options that determine the behavior of a draggable text view.
- [UITextDroppable](uitextdroppable.md) — The interface that determines if a text view is a drop destination.
- [UITextDropEditability](uitextdropeditability.md) — The text-drop editability styles for noneditable text views.

### Drag content

- [UITextDragRequest](uitextdragrequest.md) — The interface for describing the attributes of a drag activity originating in a text view.
- [UITextDragPreviewRenderer](uitextdragpreviewrenderer.md) — Renders previews of text dragged by the user.

### Drop management

- [UITextDropRequest](uitextdroprequest.md) — The interface for specifying the attributes of a drop request for a text view.
- [UITextDropProposal](uitextdropproposal.md) — A proposed configuration for the behavior of a text drop interaction.
- [Action](uitextdropproposal/action.md) — The text drop action styles for text views.
- [Performer](uitextdropproposal/performer.md) — The performers that are responsible for handling the drop operation.
- [ProgressMode](uitextdropproposal/progressmode.md) — The text drop progress styles for user-visible progress indication.

### Pasteboard support

- [UITextPasteItem](uitextpasteitem.md) — The interface for obtaining information about, and interacting with, a text item for pasting or dropping.
- [UISearchTextFieldPasteItem](uisearchtextfieldpasteitem.md) — A protocol that supports pasting tokens.
- [UITextPasteDelegate](uitextpastedelegate.md) — The interface for handling pasting and dropping of text, using item providers.
- [UITextPasteConfigurationSupporting](uitextpasteconfigurationsupporting.md) — The interface for text-oriented responder objects to participate in the unified paste and drop system in iOS.

## See Also

### Text views

- [UILabel](uilabel.md) — A view that displays one or more lines of informational text.
- [UITextField](uitextfield.md) — An object that displays an editable text area in your interface.
- [UITextView](uitextview.md) — A scrollable, multiline text region.
