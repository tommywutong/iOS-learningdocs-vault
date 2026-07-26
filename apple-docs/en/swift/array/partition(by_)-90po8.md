---
title: 'partition(by:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/partition(by:)-90po8'
source_url: 'https://developer.apple.com/documentation/swift/array/partition(by:)-90po8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/partition%28by%3A%29-90po8.json'
content_hash: 'sha256:828a1d9675217f2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# partition(by:)

<sub>Instance Method</sub>

Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func partition(by belongsInSecondPartition: (Self.Element) throws -> Bool) rethrows -> Self.Index
```

## Parameters

- `belongsInSecondPartition` — A predicate used to partition the collection. All elements satisfying this predicate are ordered after all elements not satisfying it.

## Return Value

The index of the first element in the reordered collection that matches `belongsInSecondPartition`. If no elements in the collection match `belongsInSecondPartition`, the returned index is equal to the collection’s `endIndex`.

## Discussion

After partitioning a collection, there is a pivot index `p` where no element before `p` satisfies the `belongsInSecondPartition` predicate and every element at or after `p` satisfies `belongsInSecondPartition`. This operation isn’t guaranteed to be stable, so the relative ordering of elements within the partitions might change.

In the following example, an array of numbers is partitioned by a predicate that matches elements greater than 30.

```swift
var numbers = [30, 40, 20, 30, 30, 60, 10]
let p = numbers.partition(by: { $0 > 30 })
// p == 5
// numbers == [30, 10, 20, 30, 30, 60, 40]
```

The `numbers` array is now arranged in two partitions. The first partition, `numbers[..<p]`, is made up of the elements that are not greater than 30. The second partition, `numbers[p...]`, is made up of the elements that _are_ greater than 30.

```swift
let first = numbers[..<p]
// first == [30, 10, 20, 30, 30]
let second = numbers[p...]
// second == [60, 40]
```

Note that the order of elements in both partitions changed. That is, `40` appears before `60` in the original collection, but, after calling `partition(by:)`, `60` appears before `40`.

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.

## See Also

### Reordering an Array’s Elements

- [sort()](<sort().md>) — Sorts the collection in place.
- [sort(by:)](<sort(by_).md>) — Sorts the collection in place, using the given predicate as the comparison between elements.
- [sorted()](<sorted().md>) — Returns the elements of the sequence, sorted.
- [sorted(by:)](<sorted(by_).md>) — Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [reverse()](<reverse().md>) — Reverses the elements of the collection in place.
- [reversed()](<reversed().md>) — Returns a view presenting the elements of the collection in reverse order.
- [shuffle()](<shuffle().md>) — Shuffles the collection in place.
- [shuffle(using:)](<shuffle(using_).md>) — Shuffles the collection in place, using the given generator as a source for randomness.
- [shuffled()](<shuffled().md>) — Returns the elements of the sequence, shuffled.
- [shuffled(using:)](<shuffled(using_).md>) — Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [swapAt(_:_:)](<swapat(____).md>) — Exchanges the values at the specified indices of the collection.
