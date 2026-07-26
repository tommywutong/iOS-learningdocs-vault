---
title: method_invoke_stret
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/method_invoke_stret
source_url: 'https://developer.apple.com/documentation/objectivec/method_invoke_stret'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/method_invoke_stret.json'
content_hash: 'sha256:459b8abc8ea6a7d5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# method_invoke_stret

<sub>Function</sub>

Calls the implementation of a specified method that returns a data-structure.

<sub>macOS</sub>

```objc
extern void method_invoke_stret();
```

## Parameters

- **`receiver`** — A pointer to the instance of the class that you want to invoke the method on. This value must not be `nil`.
- **`method`** — The method whose implementation you want to call.
- **`...`** — A variable argument list containing the arguments to the method.

## Discussion

Using this function to call the implementation of a method is faster than calling [method_getImplementation](<method_getimplementation(__).md>) and [method_getName](<method_getname(__).md>).

## See Also

### Working with Methods

- [method_invoke](method_invoke.md) — Calls the implementation of a specified method.
- [method_getName](<method_getname(__).md>) — Returns the name of a method.
- [method_getImplementation](<method_getimplementation(__).md>) — Returns the implementation of a method.
- [method_getTypeEncoding](<method_gettypeencoding(__).md>) — Returns a string describing a method’s parameter and return types.
- [method_copyReturnType](<method_copyreturntype(__).md>) — Returns a string describing a method’s return type.
- [method_copyArgumentType](<method_copyargumenttype(____).md>) — Returns a string describing a single parameter type of a method.
- [method_getReturnType](<method_getreturntype(______).md>) — Returns by reference a string describing a method’s return type.
- [method_getNumberOfArguments](<method_getnumberofarguments(__).md>) — Returns the number of arguments accepted by a method.
- [method_getArgumentType](<method_getargumenttype(________).md>) — Returns by reference a string describing a single parameter type of a method.
- [method_getDescription](<method_getdescription(__).md>) — Returns a method description structure for a specified method. _(deprecated)_
- [method_setImplementation](<method_setimplementation(____).md>) — Sets the implementation of a method.
- [method_exchangeImplementations](<method_exchangeimplementations(____).md>) — Exchanges the implementations of two methods.
