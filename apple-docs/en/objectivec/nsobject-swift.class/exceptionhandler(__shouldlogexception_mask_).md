---
title: 'exceptionHandler(_:shouldLogException:mask:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/exceptionhandler(_:shouldlogexception:mask:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/exceptionhandler(_:shouldlogexception:mask:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/exceptionhandler%28_%3Ashouldlogexception%3Amask%3A%29.json'
content_hash: 'sha256:5e2abbe388b6d4d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# exceptionHandler(_:shouldLogException:mask:)

<sub>Instance Method</sub>

Implemented by the delegate to evaluate whether the delegating exception hangler should log a given exception.

<sub>macOS</sub>

```swift
func exceptionHandler(_ sender: NSExceptionHandler!, shouldLogException exception: NSException!, mask aMask: Int) -> Bool
```

## Parameters

- `sender` — The [NSExceptionHandler](../../exceptionhandling/nsexceptionhandler.md) object sending the message.

- `exception` — An [NSException](../../foundation/nsexception.md) object describing the exception to be evaluated.

- `aMask` — The bit mask indicating the types of exceptions logged by the [NSExceptionHandler](../../exceptionhandling/nsexceptionhandler.md) object. See Logging and Handling Constants and System Hang Constants for descriptions of the possible `enum` constants.

## Return Value

[YES](../yes.md) to have the [NSExceptionHandler](../../exceptionhandling/nsexceptionhandler.md) object log the exception, [NO](../no.md) otherwise.
