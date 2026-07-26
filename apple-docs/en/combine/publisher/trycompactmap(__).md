---
title: 'tryCompactMap(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/trycompactmap(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/trycompactmap(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/trycompactmap%28_%3A%29.json'
content_hash: 'sha256:9ee8be86c35ec101'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# tryCompactMap(_:)

<sub>Instance Method</sub>

Calls an error-throwing closure with each received element and publishes any returned optional that has a value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryCompactMap<T>(_ transform: @escaping (Self.Output) throws -> T?) -> Publishers.TryCompactMap<Self, T>
```

## Parameters

- `transform` — An error-throwing closure that receives a value and returns an optional value.

## Return Value

Any non-`nil` optional results of calling the supplied closure.

## Discussion

Use [tryCompactMap(_:)](<trycompactmap(__).md>) to remove `nil` elements from a publisher’s stream based on an error-throwing closure you provide. If the closure throws an error, the publisher cancels the upstream publisher and sends the thrown error to the downstream subscriber as a [Failure](failure.md).

The following example uses an array of numbers as the source for a collection-based publisher. A [tryCompactMap(_:)](<trycompactmap(__).md>) operator consumes each integer from the publisher and uses a dictionary to transform the numbers from its Arabic to Roman numerals, as an optional [String](../../swift/string.md).

If the closure called by [tryCompactMap(_:)](<trycompactmap(__).md>) fails to look up a Roman numeral, it returns the optional String `(unknown)`.

If the closure called by [tryCompactMap(_:)](<trycompactmap(__).md>) determines the input is `0`, it throws an error. The [tryCompactMap(_:)](<trycompactmap(__).md>) operator catches this error and stops publishing, sending a [Subscribers.Completion.failure(_:)](<../subscribers/completion/failure(__).md>) that wraps the error.

```swift
struct ParseError: Error {}
func romanNumeral(from: Int) throws -> String? {
    let romanNumeralDict: [Int : String] =
        [1: "I", 2: "II", 3: "III", 4: "IV", 5: "V"]
    guard from != 0 else { throw ParseError() }
    return romanNumeralDict[from]
}
let numbers = [6, 5, 4, 3, 2, 1, 0]
cancellable = numbers.publisher
    .tryCompactMap { try romanNumeral(from: $0) }
    .sink(
          receiveCompletion: { print ("\($0)") },
          receiveValue: { print ("\($0)", terminator: " ") }
     )

// Prints: "(Unknown) V IV III II I failure(ParseError())"
```

## See Also

### Filtering elements

- [filter(_:)](<filter(__).md>) — Republishes all elements that match a provided closure.
- [tryFilter(_:)](<tryfilter(__).md>) — Republishes all elements that match a provided error-throwing closure.
- [compactMap(_:)](<compactmap(__).md>) — Calls a closure with each received element and publishes any returned optional that has a value.
- [removeDuplicates()](<removeduplicates().md>) — Publishes only elements that don’t match the previous element.
- [removeDuplicates(by:)](<removeduplicates(by_).md>) — Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [tryRemoveDuplicates(by:)](<tryremoveduplicates(by_).md>) — Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [replaceEmpty(with:)](<replaceempty(with_).md>) — Replaces an empty stream with the provided element.
- [replaceError(with:)](<replaceerror(with_).md>) — Replaces any errors in the stream with the provided element.
