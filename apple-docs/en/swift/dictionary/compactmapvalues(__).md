---
title: 'compactMapValues(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/compactmapvalues(_:)'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/compactmapvalues(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/compactmapvalues%28_%3A%29.json'
content_hash: 'sha256:ef77862c4776b602'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# compactMapValues(_:)

<sub>Instance Method</sub>

Returns a new dictionary containing only the key-value pairs that have non-`nil` values as the result of transformation by the given closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func compactMapValues<T>(_ transform: (Value) throws -> T?) rethrows -> Dictionary<Key, T>
```

## Parameters

- `transform` — A closure that transforms a value. `transform` accepts each value of the dictionary as its parameter and returns an optional transformed value of the same or of a different type.

## Return Value

A dictionary containing the keys and non-`nil` transformed values of this dictionary.

## Discussion

Use this method to receive a dictionary with non-optional values when your transformation produces optional values.

In this example, note the difference in the result of using `mapValues` and `compactMapValues` with a transformation that returns an optional `Int` value.

```swift
let data = ["a": "1", "b": "three", "c": "///4///"]

let m: [String: Int?] = data.mapValues { str in Int(str) }
// ["a": Optional(1), "b": nil, "c": nil]

let c: [String: Int] = data.compactMapValues { str in Int(str) }
// ["a": 1]
```

> [!abstract] Complexity
> O(_m_ + _n_), where _n_ is the length of the original dictionary and _m_ is the length of the resulting dictionary.

## See Also

### Transforming a Dictionary

- [mapValues(_:)](<mapvalues(__).md>) — Returns a new dictionary containing the keys of this dictionary with the values transformed by the given closure.
- [reduce(_:_:)](<reduce(____).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [reduce(into:_:)](<reduce(into___).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [compactMap(_:)](<compactmap(__).md>) — Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [flatMap(_:)](<flatmap(__)-i3ly.md>) — Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [flatMap(_:)](<flatmap(__)-6chv9.md>)
- [sorted(by:)](<sorted(by_).md>) — Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [shuffled()](<shuffled().md>) — Returns the elements of the sequence, shuffled.
- [shuffled(using:)](<shuffled(using_).md>) — Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
