---
title: 'setActionQueue:action:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureindexpicker/setactionqueue:action:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureindexpicker/setactionqueue:action:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureindexpicker/setactionqueue%3Aaction%3A.json'
content_hash: 'sha256:5a89360adb3eab6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureIndexPicker](../avcaptureindexpicker.md)

# setActionQueue:action:

<sub>Instance Method</sub>

Sets the action to perform on the specified dispatch queue when the control’s value changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) setActionQueue:(dispatch_queue_t) actionQueue action:(void (^)(NSInteger selectedIndex)) action;
```

## Parameters

- `actionQueue` — A dispatch queue on which to call the action.

- `action` — The action to perform in response to changes to the control’s value.

## Discussion

If the action modifies a property of the camera system, the specified dispatch queue must represent the camera system’s same exclusive execution context (see [isSameExclusiveExecutionContext(other:)](<../../swift/serialexecutor/issameexclusiveexecutioncontext(other_).md>)).
