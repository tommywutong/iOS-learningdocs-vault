---
title: 'replaceError(with:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/replaceerror(with:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/replaceerror(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/replaceerror%28with%3A%29.json'
content_hash: 'sha256:a0415d35d17a62eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# replaceError(with:)

<sub>Instance Method</sub>

Replaces any errors in the stream with the provided element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replaceError(with output: Self.Output) -> Publishers.ReplaceError<Self>
```

## Parameters

- `output` — An element to emit when the upstream publisher fails.

## Return Value

A publisher that replaces an error from the upstream publisher with the provided output element.

## Discussion

If the upstream publisher fails with an error, this publisher emits the provided element, then finishes normally.

In the example below, a publisher of strings fails with a `MyError` instance, which sends a failure completion downstream. The [replaceError(with:)](<replaceerror(with_).md>) operator handles the failure by publishing the string `(replacement element)` and completing normally.

```swift
struct MyError: Error {}
let fail = Fail<String, MyError>(error: MyError())
cancellable = fail
    .replaceError(with: "(replacement element)")
    .sink(
        receiveCompletion: { print ("\($0)") },
        receiveValue: { print ("\($0)", terminator: " ") }
    )

// Prints: "(replacement element) finished".
```

This [replaceError(with:)](<replaceerror(with_).md>) functionality is useful when you want to handle an error by sending a single replacement element and end the stream. Use [catch(_:)](<catch(__).md>) to recover from an error and provide a replacement publisher to continue providing elements to the downstream subscriber.

## See Also

### Filtering elements

- [filter(_:)](<filter(__).md>) — Republishes all elements that match a provided closure.
- [tryFilter(_:)](<tryfilter(__).md>) — Republishes all elements that match a provided error-throwing closure.
- [compactMap(_:)](<compactmap(__).md>) — Calls a closure with each received element and publishes any returned optional that has a value.
- [tryCompactMap(_:)](<trycompactmap(__).md>) — Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [removeDuplicates()](<removeduplicates().md>) — Publishes only elements that don’t match the previous element.
- [removeDuplicates(by:)](<removeduplicates(by_).md>) — Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [tryRemoveDuplicates(by:)](<tryremoveduplicates(by_).md>) — Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [replaceEmpty(with:)](<replaceempty(with_).md>) — Replaces an empty stream with the provided element.
