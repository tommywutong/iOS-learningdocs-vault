---
title: method_invoke
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/method_invoke
source_url: 'https://developer.apple.com/documentation/objectivec/method_invoke'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/method_invoke.json'
content_hash: 'sha256:14f02bef3fa9adf2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# method_invoke

<sub>Function</sub>

Calls the implementation of a specified method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void method_invoke();
```

## Parameters:

- **`receiver`** — A pointer to the instance of the class that you want to invoke the method on. This value must not be `nil`.
- **`m`** — The method whose implementation you want to call.
- **`...`** — A variable argument list containing the arguments to the method.

## Return Value

The return value of the method.

## Discussion

Using this function to call the implementation of a method is faster than calling [method_getImplementation](<method_getimplementation(__).md>) and [method_getName](<method_getname(__).md>).

## See Also

### Working with Methods

- [method_invoke_stret](method_invoke_stret.md) — Calls the implementation of a specified method that returns a data-structure.
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
