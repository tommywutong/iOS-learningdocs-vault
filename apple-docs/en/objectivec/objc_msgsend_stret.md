---
title: objc_msgSend_stret
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_msgsend_stret
source_url: 'https://developer.apple.com/documentation/objectivec/objc_msgsend_stret'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_msgsend_stret.json'
content_hash: 'sha256:fb4106b6b084f095'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_msgSend_stret

<sub>Function</sub>

Sends a message with a data-structure return value to an instance of a class.

<sub>macOS</sub>

```objc
extern void objc_msgSend_stret();
```

## Parameters:

- stretAddr: On input, a pointer that points to a block of memory large enough to contain the return value of the method. On output, contains the return value of the method.
- theReceiver: A pointer to the instance of the class that is to receive the message.
- theSelector: A pointer of type [SEL](sel.md). Pass the selector of the method that handles the message.
- …: A variable argument list containing the arguments to the method.

## Discussion

When it encounters a method call, the compiler generates a call to one of the functions `objc_msgSend`, `objc_msgSend_stret`, `objc_msgSendSuper`, or `objc_msgSendSuper_stret`. Messages sent to an object’s superclass (using the `super` keyword) are sent using `objc_msgSendSuper`; other messages are sent using `objc_msgSend`. Methods that have data structures as return values are sent using `objc_msgSendSuper_stret` and `objc_msgSend_stret`.

## See Also

### Sending Messages

- [objc_msgSend](objc_msgsend.md) — Sends a message with a simple return value to an instance of a class.
- [objc_msgSend_fpret](objc_msgsend_fpret.md) — Sends a message with a floating-point return value to an instance of a class.
- [objc_msgSendSuper](objc_msgsendsuper.md) — Sends a message with a simple return value to the superclass of an instance of a class.
- [objc_msgSendSuper_stret](objc_msgsendsuper_stret.md) — Sends a message with a data-structure return value to the superclass of an instance of a class.
