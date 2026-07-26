---
title: 'assertNoFailure(_:file:line:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/assertnofailure(_:file:line:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/assertnofailure(_:file:line:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/assertnofailure%28_%3Afile%3Aline%3A%29.json'
content_hash: 'sha256:22625d38bd6507e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# assertNoFailure(_:file:line:)

<sub>Instance Method</sub>

Raises a fatal error when its upstream publisher fails, and otherwise republishes all received input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func assertNoFailure(_ prefix: String = "", file: StaticString = #file, line: UInt = #line) -> Publishers.AssertNoFailure<Self>
```

## Parameters

- `prefix` — A string used at the beginning of the fatal error message.

- `file` — A filename used in the error message. This defaults to `#file`.

- `line` — A line number used in the error message. This defaults to `#line`.

## Return Value

A publisher that raises a fatal error when its upstream publisher fails.

## Discussion

Use `assertNoFailure()` for internal integrity checks that are active during testing. However, it is important to note that, like its Swift counterpart `fatalError(_:)`, the `assertNoFailure()` operator asserts a fatal exception when triggered during development and testing, _and_ in shipping versions of code.

In the example below, a `CurrentValueSubject` publishes the initial and second values successfully. The third value, containing a `genericSubjectError`, causes the `assertNoFailure()` operator to assert a fatal exception stopping the process:

```swift
public enum SubjectError: Error {
    case genericSubjectError
}

let subject = CurrentValueSubject<String, Error>("initial value")
subject
    .assertNoFailure()
    .sink(receiveCompletion: { print ("completion: \($0)") },
          receiveValue: { print ("value: \($0).") }
    )

subject.send("second value")
subject.send(completion: Subscribers.Completion<Error>.failure(SubjectError.genericSubjectError))

// Prints:
//  value: initial value.
//  value: second value.
//  The process then terminates in the debugger as the assertNoFailure operator catches the genericSubjectError.
```

## See Also

### Handling errors

- [catch(_:)](<catch(__).md>) — Handles errors from an upstream publisher by replacing it with another publisher.
- [tryCatch(_:)](<trycatch(__).md>) — Handles errors from an upstream publisher by either replacing it with another publisher or throwing a new error.
- [retry(_:)](<retry(__).md>) — Attempts to recreate a failed subscription with the upstream publisher up to the number of times you specify.
