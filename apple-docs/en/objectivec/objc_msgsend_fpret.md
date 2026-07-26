---
title: objc_msgSend_fpret
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_msgsend_fpret
source_url: 'https://developer.apple.com/documentation/objectivec/objc_msgsend_fpret'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_msgsend_fpret.json'
content_hash: 'sha256:b4b1d31195ac45a1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_msgSend_fpret

<sub>Function</sub>

Sends a message with a floating-point return value to an instance of a class.

<sub>macOS</sub>

```objc
extern void objc_msgSend_fpret();
```

## Parameters

- **`self`** — A pointer that points to the instance of the class that is to receive the message.
- **`op`** — The selector of the method that handles the message.
- **`...`** — A variable argument list containing the arguments to the method.

## Discussion

On the i386 platform, the ABI for functions returning a floating-point value is incompatible with that for functions returning an integral type. On the i386 platform, therefore, you _must_ use `objc_msgSend_fpret` for functions that for functions returning non-integral type. For `float` or `long double` return types, cast the function to an appropriate function pointer type first.

This function is not used on the PPC or PPC64 platforms.

## See Also

### Sending Messages

- [objc_msgSend](objc_msgsend.md) — Sends a message with a simple return value to an instance of a class.
- [objc_msgSend_stret](objc_msgsend_stret.md) — Sends a message with a data-structure return value to an instance of a class.
- [objc_msgSendSuper](objc_msgsendsuper.md) — Sends a message with a simple return value to the superclass of an instance of a class.
- [objc_msgSendSuper_stret](objc_msgsendsuper_stret.md) — Sends a message with a data-structure return value to the superclass of an instance of a class.
