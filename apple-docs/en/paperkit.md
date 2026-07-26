---
title: PaperKit
framework: PaperKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/paperkit
source_url: 'https://developer.apple.com/documentation/paperkit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/paperkit.json'
content_hash: 'sha256:ce1007395d7cddb0'
translated: false
---

> Navigation: [Technologies](technologies.md)

# PaperKit

<sub>Framework</sub>

Add drawings, shapes, and a consistent markup experience to your app.

## Overview

PaperKit builds on top of [PencilKit](pencilkit.md) to deliver a comprehensive markup experience. It adds a layer of elements — including shapes, images, and text boxes — to help create a unified canvas that supports both drawing and annotation. PaperKit powers the markup experience across all Apple platforms, and provides an easy way to add rich markup capabilities to any app.

PaperKit consists of three main components that work together to deliver a complete markup experience. [PaperMarkupViewController](paperkit/papermarkupviewcontroller.md) serves as the primary markup controller that interactively creates and displays PaperKit elements alongside PencilKit content. [PaperMarkup](paperkit/papermarkup.md) acts as the data model container that handles saving, loading, and rendering both markup elements and PencilKit drawing data. [MarkupEditViewController](paperkit/markupeditviewcontroller.md) (in iOS, iPadOS, and visionOS) and [MarkupToolbarViewController](paperkit/markuptoolbarviewcontroller.md) (in macOS) provide platform-specific insertion menus for adding markup elements.

Configure PaperKit to match your app’s specific needs by providing a [FeatureSet](paperkit/featureset.md) to control which markup tools and capabilities are available. Enable HDR support for stunning visual content, set custom background views, and fine-tune the markup experience to align perfectly with your app’s design and functionality.

## Topics

### Essentials

- [Integrating PaperKit into your app](paperkit/getting-started-with-paperkit.md) — Create your first markup experience by setting up a view controller, adding markup editing tools, and implementing data persistence.

### View controllers

- [PaperMarkupViewController](paperkit/papermarkupviewcontroller.md) — A view controller for interactively creating and showing markup.
- [MarkupEditViewController](paperkit/markupeditviewcontroller.md) — A view controller that manages the interface for inserting content into a canvas.
- [MarkupToolbarViewController](paperkit/markuptoolbarviewcontroller.md)

### Configuration

- [FeatureSet](paperkit/featureset.md) — The features PaperKit supports in its UI and data models.
- [ShapeConfiguration](paperkit/shapeconfiguration.md) — A configuration that specifies the appearance of a shape.
- [RenderingOptions](paperkit/renderingoptions.md) — The rendering options for drawing paper data models.
- [MarkupAutoresizing](paperkit/markupautoresizing.md) — Automatic sizing behaviors for this markup. _(beta)_

### Data model

- [PaperMarkup](paperkit/papermarkup.md) — The data model object for storing markup data created from a `PaperViewController`.
- [MarkupOrderedSet](paperkit/markuporderedset.md) — An ordered set of markup elements. _(beta)_
- [MarkupID](paperkit/markupid.md) — An opaque ID for markup elements. _(beta)_

### Markup elements

- [Markup](paperkit/markup.md) — A markup component. _(beta)_
- [ImageMarkup](paperkit/imagemarkup.md) — A markup element that represents an image. _(beta)_
- [ShapeMarkup](paperkit/shapemarkup.md) — A markup element that represents a shape or text box with customizable appearance and behavior. _(beta)_
- [LinkMarkup](paperkit/linkmarkup.md) — A URL link that a person can tap on in the canvas. _(beta)_
- [LoupeMarkup](paperkit/loupemarkup.md) — A loupe magnifier that magnifies the content below the loupe. _(beta)_
- [MarkupInteractions](paperkit/markupinteractions.md) — Interactions that people can perform on markup elements. _(beta)_

### Adornments

- [MarkupAdornment](paperkit/markupadornment.md) — A visual adornment that appears on top of markup content within a markup view controller. _(beta)_

### Error handling

- [MarkupError](paperkit/markuperror.md) — The error thrown for encoding / decoding data models.

### Type Aliases

- [PKStrokeRenderStateReference](paperkit/pkstrokerenderstatereference.md) _(beta)_
