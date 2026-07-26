---
title: 'controlTextDidBeginEditing:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/controltextdidbeginediting:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/controltextdidbeginediting:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/controltextdidbeginediting%3A.json'
content_hash: 'sha256:e3b691380cd9052a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# controlTextDidBeginEditing:

<sub>Instance Method</sub>

Sent when a control with editable text begins an editing session.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) controlTextDidBeginEditing:(NSNotification *) obj;
```

## Parameters

- `obj` — The notification object. The name of the notification is always [textDidBeginEditingNotification](../../appkit/nscontrol/textdidbegineditingnotification.md).

## Discussion

This method is invoked when the user begins editing text in a control such as a text field or a form field. The control posts a [textDidBeginEditingNotification](../../appkit/nscontrol/textdidbegineditingnotification.md) notification, and if the control’s delegate implements this method, it is automatically registered to receive the notification. Use the key `@"NSFieldEditor"` to obtain the field editor from the `userInfo` dictionary of the notification object.

See [controlTextDidEndEditing:](controltextdidendediting_.md) for an explanation of why you may not always get one invocation of [controlTextDidBeginEditing:](controltextdidbeginediting_.md) for each invocation of [controlTextDidEndEditing:](controltextdidendediting_.md).
