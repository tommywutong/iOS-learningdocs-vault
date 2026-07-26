---
title: QCCompositionLayer
framework: Quartz
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.5+（10.14 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/quartz/qccompositionlayer
source_url: 'https://developer.apple.com/documentation/quartz/qccompositionlayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartz/qccompositionlayer.json'
content_hash: 'sha256:5175726f9136c23f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Quartz](../quartz.md)

# QCCompositionLayer

<sub>Class</sub>

A layer that loads, plays, and controls Quartz Composer compositions in a Core Animation layer hierarchy.

> [!warning] Deprecated
> Quartz Composer OpenGL API deprecated. (Define QC_SILENCE_GL_DEPRECATION to silence these warnings)

<sub>macOS</sub>

```swift
class QCCompositionLayer
```

## Overview

The composition tracks the Core Animation layer time and is rendered directly at the current dimensions of the [QCCompositionLayer](qccompositionlayer.md) object.

An archived `QCCompositionLayer` object saves the composition that’s loaded at the time the layer is archived. It detects layer usage and pauses or resumes the composition appropriately. A `QCCompositionLayer` object starts rendering the composition automatically when the layer is placed in a visible layer hierarchy. The layer stops rendering when it is hidden or removed from the visible layer hierarchy.

You can pass data to the input ports, or retrieve data from the output ports, of the root patch of a composition by accessing the `patch` attribute of the `QCCompositionLayer` instance using methods provided by the [QCCompositionRenderer](qccompositionrenderer.md) protocol.

> [!note] Note
> You must not modify the `asynchronous` property of the superclass [CAOpenGLLayer](../quartzcore/caopengllayer.md).

## Relationships

- **Inherits From**: [CAOpenGLLayer](../quartzcore/caopengllayer.md)

- **Conforms To**: [CAMediaTiming](../quartzcore/camediatiming.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [QCCompositionRenderer](qccompositionrenderer.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Composition Layer

- [- initWithFile:](<qccompositionlayer/init(file_).md>) — Initializes and returns a composition layer using the Quartz Composer composition in the specified file. _(deprecated)_
- [- initWithComposition:](<qccompositionlayer/init(composition_).md>) — Initializes and returns a  composition layer using the provided Quartz Composer composition. _(deprecated)_

### Getting the Composition

- [- composition](<qccompositionlayer/composition().md>) — Returns the composition associated with the layer. _(deprecated)_

## See Also

### Classes

- [QCComposition](qccomposition.md) — The `QCComposition` class represents a Quartz Composer composition that either: _(deprecated)_
- [QCCompositionParameterView](qccompositionparameterview.md) — A class that allows users to edit the input parameters of a composition in real time. The composition can be rendering in any of the following objects: [QCRenderer](qcrenderer.md), [QCView](qcview.md), or [QCCompositionLayer](qccompositionlayer.md). _(deprecated)_
- [QCCompositionPickerPanel](qccompositionpickerpanel.md) — The `QCCompositionPickerPanel` class represents a utility window that allows users to browse compositions that are in the Quartz Composer composition repository and, if supported, preview the composition. The `QCCompositionPickerPanel` class cannot be subclassed. _(deprecated)_
- [QCCompositionPickerView](qccompositionpickerview.md) — The `QCCompositionPickerView` class allows users to browse compositions that are in the Quartz Composer composition repository, and to preview them. You can set the default input parameters for a composition preview  by using the method setDefaultValue:forInputKey:. _(deprecated)_
- [QCCompositionRepository](qccompositionrepository.md) — The `QCCompositionRepository` class represents a system-wide centralized repository of built-in and installed Quartz Composer compositions (`/Library/Compositions` and `~/Library/Compositions`). The `QCCompositionRepository` class cannot be subclassed. _(deprecated)_
- [QCPatchController](qcpatchcontroller.md) _(deprecated)_
- [QCPlugIn](qcplugin.md) — A base class to subclass for writing custom patches. _(deprecated)_
- [QCPlugInViewController](qcpluginviewcontroller.md) — The `QCPlugInViewController` class communicates (through Cocoa bindings) between a custom patch and the view used for the internal settings of the custom patch. Only custom patches that use internal settings exposed to the user need to use the `QCPlugInViewController` class. _(deprecated)_
- [QCRenderer](qcrenderer.md) — A base class for low-level rendering. _(deprecated)_
- [QCView](qcview.md) — The `QCView` class is a custom `NSView` class that loads, plays, and controls Quartz Composer compositions. It is an autonomous view that is driven by an internal timer running on the main thread. _(deprecated)_
