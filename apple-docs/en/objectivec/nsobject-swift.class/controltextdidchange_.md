---
title: 'controlTextDidChange:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/controltextdidchange:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/controltextdidchange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/controltextdidchange%3A.json'
content_hash: 'sha256:4eb14eb9168cc6b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# controlTextDidChange:

<sub>Instance Method</sub>

Sent when the text in the receiving control changes.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) controlTextDidChange:(NSNotification *) obj;
```

## Parameters

- `obj` — The notification object. The name of the notification is always [textDidChangeNotification](../../appkit/nscontrol/textdidchangenotification.md).

## Discussion

This method is invoked when text in a control such as a text field or form changes. The control posts a [textDidChangeNotification](../../appkit/nscontrol/textdidchangenotification.md) notification, and if the control’s delegate implements this method, it is automatically registered to receive the notification. Use the key `@"NSFieldEditor"` to obtain the field editor from the `userInfo` dictionary of the notification object.
