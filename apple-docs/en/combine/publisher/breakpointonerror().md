---
title: breakpointOnError()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publisher/breakpointonerror()
source_url: 'https://developer.apple.com/documentation/combine/publisher/breakpointonerror()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/breakpointonerror%28%29.json'
content_hash: 'sha256:1d91482fdfdad0fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# breakpointOnError()

<sub>Instance Method</sub>

Raises a debugger signal upon receiving a failure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func breakpointOnError() -> Publishers.Breakpoint<Self>
```

## Return Value

A publisher that raises a debugger signal upon receiving a failure.

## Discussion

When the upstream publisher fails with an error, this publisher raises the `SIGTRAP` signal, which stops the process in the debugger. Otherwise, this publisher passes through values and completions as-is.

In this example a [PassthroughSubject](../passthroughsubject.md) publishes strings, but its downstream [tryMap(_:)](<trymap(__).md>) operator throws an error. This sends the error downstream as a [Subscribers.Completion.failure(_:)](<../subscribers/completion/failure(__).md>). The [breakpointOnError()](<breakpointonerror().md>) operator receives this completion and stops the app in the debugger.

```swift
 struct CustomError : Error {}
 let publisher = PassthroughSubject<String?, Error>()
 cancellable = publisher
     .tryMap { stringValue in
         throw CustomError()
     }
     .breakpointOnError()
     .sink(
         receiveCompletion: { completion in print("Completion: \(String(describing: completion))") },
         receiveValue: { aValue in print("Result: \(String(describing: aValue))") }
     )

 publisher.send("TEST DATA")

 // Prints: "error: Execution was interrupted, reason: signal SIGTRAP."
 // Depending on your specific environment, the console messages may
 // also include stack trace information, which is not shown here.
```

## See Also

### Debugging

- [breakpoint(receiveSubscription:receiveOutput:receiveCompletion:)](<breakpoint(receivesubscription_receiveoutput_receivecompletion_).md>) — Raises a debugger signal when a provided closure needs to stop the process in the debugger.
- [handleEvents(receiveSubscription:receiveOutput:receiveCompletion:receiveCancel:receiveRequest:)](<handleevents(receivesubscription_receiveoutput_receivecompletion_receivecancel_receiverequest_).md>) — Performs the specified closures when publisher events occur.
- [print(_:to:)](<print(__to_).md>) — Prints log messages for all publishing events.
