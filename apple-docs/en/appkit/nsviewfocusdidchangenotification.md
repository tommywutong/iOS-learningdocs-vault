---
title: NSViewFocusDidChangeNotification
framework: AppKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsviewfocusdidchangenotification
source_url: 'https://developer.apple.com/documentation/appkit/nsviewfocusdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsviewfocusdidchangenotification.json'
content_hash: 'sha256:2974eae99ce87e2b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSViewFocusDidChangeNotification

<sub>Global Variable</sub>

Deprecated in macOS 10.4 and later. Posted for an `NSView` object and each of its descendants (recursively) whenever the frame or bounds geometry of the view changed.

<sub>Mac Catalyst, macOS</sub>

```objc
extern NSNotificationName NSViewFocusDidChangeNotification;
```

## Discussion

Instead use `NSViewBoundsDidChangeNotification` and `NSViewFrameDidChangeNotification` to get the same information provided by this notification.

The notification object is the view whose geometry changed. This notification does not contain a `userInfo` dictionary.

## See Also

### Related Documentation

- [NSViewFrameDidChangeNotification](nsview/framedidchangenotification.md) — A notification that posts when the view’s frame rectangle changes to a new value.
- [NSViewBoundsDidChangeNotification](nsview/boundsdidchangenotification.md) — A notification that posts when the view’s bounds rectangle changes to a new value independently of the frame rectangle.

### Notifications

- [NSViewNoInstrinsicMetric](nsviewnoinstrinsicmetric.md) — Used to indicate that a view has no intrinsic metric for a given numeric property. _(deprecated)_
- [NSViewGlobalFrameDidChangeNotification](nsview/globalframedidchangenotification.md) — Posted whenever an `NSView` object that has attached surfaces (that is, `NSOpenGLContext` objects) moves to a different screen, or other cases where the `NSOpenGLContext` object needs to be updated. _(deprecated)_
