---
title: 'controlTextDidEndEditing:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/controltextdidendediting:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/controltextdidendediting:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/controltextdidendediting%3A.json'
content_hash: 'sha256:f15bc55a2ed0bcdb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# controlTextDidEndEditing:

<sub>Instance Method</sub>

Sent when a control with editable text ends an editing session.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) controlTextDidEndEditing:(NSNotification *) obj;
```

## Parameters

- `obj` — The notification object. The name of the notification is always [textDidEndEditingNotification](../../appkit/nscontrol/textdidendeditingnotification.md).

## Discussion

This method is invoked when the user stops editing text in a control such as a text field or form. The control posts a [textDidEndEditingNotification](../../appkit/nscontrol/textdidendeditingnotification.md) notification, and if the control’s delegate implements this method, it is automatically registered to receive the notification. Use the key `@"NSFieldEditor"` to obtain the field editor from the `userInfo` dictionary of the notification object.

> [!warning] Warning
> In some cases, such as when editing within an instance of `NSOutlineView`, this method may be invoked without a previous invocation of [controlTextDidBeginEditing:](controltextdidbeginediting_.md). You will only get the `controlTextDidBeginEditing:` notification if the user actually types something, but you can get the `controlTextDidEndEditing:` notification if the user just double-clicks the field and then clicks outside the field, without typing.
