---
title: shuffled()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/dictionary/shuffled()
source_url: 'https://developer.apple.com/documentation/swift/dictionary/shuffled()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/shuffled%28%29.json'
content_hash: 'sha256:90effd328e796a4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# shuffled()

<sub>Instance Method</sub>

Returns the elements of the sequence, shuffled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func shuffled() -> [Self.Element]
```

## Return Value

A shuffled array of this sequence’s elements.

## Discussion

For example, you can shuffle the numbers between `0` and `9` by calling the `shuffled()` method on that range:

```swift
let numbers = 0...9
let shuffledNumbers = numbers.shuffled()
// shuffledNumbers == [1, 7, 6, 2, 8, 9, 4, 3, 5, 0]
```

This method is equivalent to calling `shuffled(using:)`, passing in the system’s default random generator.

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the sequence.

## See Also

### Transforming a Dictionary

- [mapValues(_:)](<mapvalues(__).md>) — Returns a new dictionary containing the keys of this dictionary with the values transformed by the given closure.
- [reduce(_:_:)](<reduce(____).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [reduce(into:_:)](<reduce(into___).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [compactMap(_:)](<compactmap(__).md>) — Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [compactMapValues(_:)](<compactmapvalues(__).md>) — Returns a new dictionary containing only the key-value pairs that have non-`nil` values as the result of transformation by the given closure.
- [flatMap(_:)](<flatmap(__)-i3ly.md>) — Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [flatMap(_:)](<flatmap(__)-6chv9.md>)
- [sorted(by:)](<sorted(by_).md>) — Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [shuffled(using:)](<shuffled(using_).md>) — Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
