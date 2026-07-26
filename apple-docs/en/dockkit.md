---
title: DockKit
framework: DockKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dockkit
source_url: 'https://developer.apple.com/documentation/dockkit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dockkit.json'
content_hash: 'sha256:5195b092a2a213b8'
translated: false
---

> Navigation: [Technologies](technologies.md)

# DockKit

<sub>Framework</sub>

Interact with accessories that track subjects on camera as they move around.

## Overview

DockKit interfaces with DockKit-compatible motorized stands known as dock accessories to track the location of objects that appear in video frames. It determines how to best position the iPhone camera to frame and track objects, with improved person tracking using combined body and face tracking for human subjects. This feature, known as _system tracking_, automatically starts as soon as a person docks iPhone onto a compatible motorized stand and launches the Camera app. For example, system tracking is useful for content creators who want the camera to follow them while they move around their space, or instructors on a video call who are walking around a classroom.

![](../../attachments/790e7a21e706ee6445e00e2d6d12bdb3/dock@2x.png)

<sub>iPhone mounted in landscape orientation on a dock accessory with its back facing outward. A cocentric circle near the camera indicates that it is active.</sub>

![](../../attachments/d3211312df3276762f7038d194067169/move@2x.png)

<sub>iPhone mounted in landscape orientation on a dock accessory with its back facing outward. An arc around the base of the dock accessory indicates horizontal movement. An arc around the body of iPhone indicates up and down movement.</sub>

![](../../attachments/15cbb5e75993a385ce4167d291e2ca80/track@2x.png)

<sub>iPhone mounted in landscape orientation on a dock accessory with the back of the iPhone aimed at a person in a video frame. The person in the frame is in midair, in the process of jumping.</sub>

You can disable system tracking and implement your own tracking behavior by using [DockAccessoryManager](dockkit/dockaccessorymanager.md) and [DockAccessory](dockkit/dockaccessory.md). Implement your own tracking behavior to follow a location of a custom object such as a pet, or a pair of hands performing a task. DockKit accessories integrate with [AVCaptureSession](avfoundation/avcapturesession.md) so apps with camera permissions work seamlessly together.

## Topics

### Controlling the dock accessory

- [Controlling a DockKit accessory using your camera app](dockkit/controlling-a-dockkit-accessory-using-your-camera-app.md) — Follow subjects in real time using an iPhone that you mount on a DockKit accessory.
- [DockAccessoryManager](dockkit/dockaccessorymanager.md) — Observe the state of dock accessories and enable or disable system tracking.
- [DockAccessory](dockkit/dockaccessory.md) — Obtain accessory information and control tracking behavior.
- [DockKitError](dockkit/dockkiterror.md) — A list of errors that DockKit sends.

### Customizing tracking behavior

- [Modify rotation and positioning programmatically](dockkit/modify-rotation-and-positioning-behavior-programmatically.md) — Perform custom control of the dock accessory.
- [Track custom objects in a frame](dockkit/track-custom-objects-in-a-frame.md) — Use your machine learning model to focus on a specific subject.
