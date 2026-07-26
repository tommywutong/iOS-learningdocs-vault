---
title: Touch Controller
framework: Touch Controller
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/touchcontroller
source_url: 'https://developer.apple.com/documentation/touchcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/touchcontroller.json'
content_hash: 'sha256:e708b0ac0cb9fa89'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Touch Controller

<sub>Framework</sub>

Integrate onscreen touch controls into your Metal-based games.

## Overview

Use Touch Controller to add custom and interactive touch controls for your games. The framework offers a suite of controls that enable support for a variety of control schemes, like buttons, directional pads, thumbsticks, throttle controls, and touchpads. The Game Controller framework supports each control and surfaces them through a [GCController](gamecontroller/gccontroller.md) instance.

Use the [TCTouchController](touchcontroller/tctouchcontroller.md) class as the central point to manage and render your touch controls. To configure the appearance of your controls, use [TCControlContents](touchcontroller/tccontrolcontents.md) and [TCControlImage](touchcontroller/tccontrolimage.md). Use [TCControlContents](touchcontroller/tccontrolcontents.md) to create a consistent look and feel with system-provided assets.

## Topics

### Essentials

- [TCTouchController](touchcontroller/tctouchcontroller.md) — An object that allows you to create and customize on-screen touch controls for a game that uses Metal.

### Controls

- [TCControl](touchcontroller/tccontrol.md) — A protocol that defines the base properties and methods for all touch controls.
- [TCButton](touchcontroller/tcbutton.md) — A control that represents a single on-screen button.
- [TCDirectionPad](touchcontroller/tcdirectionpad.md) — An object that represents a direction pad.
- [TCSwitch](touchcontroller/tcswitch.md) — A control that represents a single on-screen switch.
- [TCThumbstick](touchcontroller/tcthumbstick.md) — Represents a single on-screen thumbstick.
- [TCThrottle](touchcontroller/tcthrottle.md) — Represents a single on-screen throttle - a one axis input.
- [TCTouchpad](touchcontroller/tctouchpad.md) — Represents a single on-screen touchpad that reports absolute coordinates or delta movements.

### Visuals

- [TCControlContents](touchcontroller/tccontrolcontents.md) — Represents the visual contents of a touch control.
- [TCControlImage](touchcontroller/tccontrolimage.md) — Represents an image to be rendered using Metal.
- [TCControlLayout](touchcontroller/tccontrollayout.md) — A protocol defining the controlLayout properties for a control.

### System content

- [ButtonShape](touchcontroller/tccontrolcontents/buttonshape.md) — Defines the visual shape of a button.
- [DpadDirection](touchcontroller/tccontrolcontents/dpaddirection.md) — Defines the direction of a direction pad visual.
- [DpadElementStyle](touchcontroller/tccontrolcontents/dpadelementstyle.md) — Defines the visual style of the individual up/down/left/right elements of a direction pad.
