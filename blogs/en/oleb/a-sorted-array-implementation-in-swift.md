---
title: A Sorted Array Implementation in Swift
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/02/sorted-array/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:e00f9c36a538f066'
translated: false
---

> 原文：[A Sorted Array Implementation in Swift](https://oleb.net/blog/2017/02/sorted-array/)　·　Ole Begemann

# A Sorted Array Implementation in Swift

In [last week’s Swift Talk episode](https://talk.objc.io/episodes/S01E35-sorted-arrays-collections-3), Florian and Chris wrote a `SortedArray` type: an array that keeps its elements sorted according to a given sort predicate at all times. This is great because it encodes one more [invariant](https://en.wikipedia.org/wiki/Invariant_(computer_science)) in the type system — clients that use this type in place of a regular [`Array`](https://developer.apple.com/reference/swift/array) never have to worry about accidentally forgetting to keep the array sorted manually.

Florian and Chris intentionally left some desirable features out in order to keep the video reasonably short. I’d like to show you an implementation here that is more efficient for some operations and has some nice additional features. None of this is particularly difficult to write, but I think it shows quite well how you can approach writing a custom collection type that fits in seamlessly with the rest of the standard library.

You can look at the [full code on GitHub](https://github.com/ole/SortedArray), but here are some highlights.

# Specialized collection protocols

In addition to the [`Collection`](https://developer.apple.com/reference/swift/collection) conformance shown in the video, `SortedArray` conforms to [`RandomAccessCollection`](https://developer.apple.com/reference/swift/randomaccesscollection). It makes accessing elements at arbitrary indices much faster, and we need this later to implement an efficient binary search algorithm.

The implementation is straightforward because we can forward everything to the array we use for backing storage. Because we use `Int` as our `Index` type, we don’t even have to implement the otherwise required `index(_:offsetBy:)` and `distance(from:to:)` methods — the standard library provides default implementations for `Strideable` indices.

`SortedArray` _can’t_ conform to either [MutableCollection](https://developer.apple.com/reference/swift/mutablecollection) or [`RangeReplaceableCollection`](https://developer.apple.com/reference/swift/rangereplaceablecollection) because [their semantics](https://oleb.net/blog/2017/02/why-is-dictionary-not-a-mutablecollection/) of inserting/replacing elements at specific positions are incompatible with our invariant to keep elements sorted.

# `ExpressibleByArrayLiteral`

`SortedArray` does _not_ conform to [`ExpressibleByArrayLiteral`](https://developer.apple.com/reference/swift/expressiblebyarrayliteral), i.e. you can’t do this:

```
let sorted: SortedArray = [3,1,2]
```

This would be nice to have, but since you can’t pass an explicit sort predicate alongside the array literal, it would only work with elements that are [`Comparable`](https://developer.apple.com/reference/swift/comparable), and Swift 3 doesn’t support [conditional protocol conformance](https://github.com/apple/swift-evolution/blob/master/proposals/0143-conditional-conformances.md) yet, which is needed to write:

```
extension SortedArray: ExpressibleByArrayLiteral where Element: Comparable {
    ...
}
```

Maybe in Swift 4.

# Binary search

One of the big advantages of having a sorted collection is that you can find an element very efficiently using [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm). Binary search finds an element in [logarithmic rather than linear time](https://en.wikipedia.org/wiki/Time_complexity#Logarithmic_time).

To implement this I first wrote a helper method named `search(for:)`. You can check out [the full code on GitHub](https://github.com/ole/SortedArray/blob/master/Sources/SortedArray.swift#L176-L198); here I’d like to specifically discuss the return type:

```
fileprivate enum Match<Index: Comparable> {
    case found(at: Index)
    case notFound(insertAt: Index)
}

extension SortedArray {
    /// Searches the array for `newElement` using binary search.
    ///
    /// - Returns: If `newElement` is in the array, returns `.found(at: index)`
    ///   where `index` is the index of the element in the array.
    ///   If `newElement` is not in the array, returns `.notFound(insertAt: index)`
    ///   where `index` is the index where the element should be inserted to 
    ///   preserve the sort order.
    ///   If the array contains multiple elements that are equal to `newElement`,
    ///   there is no guarantee which of these is found.
    ///
    /// - Complexity: O(_log(n)_), where _n_ is the size of the array.
    fileprivate func search(for newElement: Element) -> Match<Index> {
        ...
    }
}
```

The standard library’s [`index(of:)`](https://developer.apple.com/reference/swift/collection/1641318-index) method returns an `Optional<Index>`, which is `nil` if no match was found. `search(for:)` does something similar, but its return type is a custom enum that carries an element index as payload in both the `.found` and the `.notFound` case. This allows us to use the same algorithm for searching and inserting: the returned index is where we need to insert a new element to maintain the sort order.

With the algorithm in place, here are the implementations for `index(of:)` and [`contains(_:)`](https://developer.apple.com/reference/swift/sequence/1641180-contains):

```
extension SortedArray {
    /// Returns the first index where the specified value appears
    /// in the collection.
    ///
    /// - Complexity: O(_log(n)_), where _n_ is the size of the array.
    public func index(of element: Element) -> Index? {
        switch search(for: element) {
        case let .found(at: index): return index
        case .notFound(insertAt: _): return nil
        }
    }

    /// Returns a Boolean value indicating whether the sequence contains
    /// the given element.
    ///
    /// - Complexity: O(_log(n)_), where _n_ is the size of the array.
    public func contains(_ element: Element) -> Bool {
        return index(of: element) != nil
    }
}
```

Note that these are not just more efficient than the default implementations in the standard library — they are also more generic. The standard library’s versions of these methods require a `where Iterator.Element: Comparable` constraint that we can omit because `SortedArray` always has a sort predicate.

# Inserting elements

The next task is to improve the efficiency of inserting elements by taking advantage of binary search. I decided to provide two insert methods: the first inserts a single element at the correct position to maintain the sort order. It uses binary search to find the correct insertion index in O(_log n_). Inserting the new element into the backing store array takes at worst O(_n_) time because all subsequent elements have to be moved to make room.

The second method inserts a sequence of new elements. Here I opted to append the new elements to the backing array first and then re-sort it once. This can be much faster than finding the correct insertion index repeatedly (if the inserted sequence is longer than _log n_ elements).

```
extension SortedArray {
    /// Inserts a new element into the array, preserving the sort order.
    ///
    /// - Returns: the index where the new element was inserted.
    /// - Complexity: O(_n_) where _n_ is the size of the array. O(_log n_) if the new
    /// element can be appended, i.e. if it is ordered last in the resulting array.
    @discardableResult
    public mutating func insert(_ newElement: Element) -> Index {
        let index = insertionIndex(for: newElement)
        // This should be O(1) if the element is to be inserted at the end,
        // O(_n) in the worst case (inserted at the front).
        _elements.insert(newElement, at: index)
        return index
    }

    /// Inserts all elements from `elements` into `self`, preserving the sort order.
    ///
    /// This can be faster than inserting the individual elements one after another because
    /// we only need to re-sort once.
    ///
    /// - Complexity: O(_n * log(n)_) where _n_ is the size of the resulting array.
    public mutating func insert<S: Sequence>(contentsOf newElements: S) where S.Iterator.Element == Element {
        _elements.append(contentsOf: newElements)
        _elements.sort(by: areInIncreasingOrder)
    }
}
```

# Other efficiency gains

Chris and Florian already showed in the episode that we can provide more efficient variants of [`min()`](https://developer.apple.com/reference/swift/sequence/1641174-min) and [`max()`](https://developer.apple.com/reference/swift/sequence/1641492-max) because the minimum and maximum elements in a sorted collection are always the first and last:[1](#fn:minmax)

```
extension SortedArray {
    /// Returns the minimum element in the sequence.
    ///
    /// - Complexity: O(1).
    @warn_unqualified_access
    public func min() -> Element? {
        return first
    }

    /// Returns the maximum element in the sequence.
    ///
    /// - Complexity: O(1).
    @warn_unqualified_access
    public func max() -> Element? {
        return last
    }
}
```

The `@warn_unqualified_access` directive [tells the compiler to issue a warning](http://stackoverflow.com/a/36110284/116862) when you call one of these methods from inside the type’s implementation (or an extension) without an explicit `self.` prefix. This helps avoid confusion between the methods and the free functions [`min(_:_:)`](https://developer.apple.com/reference/swift/1538339-min) and [`max(_:_:)`](https://developer.apple.com/reference/swift/1538951-max).

As with `index(of:)` and `contains(_:)`, our `min()` and `max()` variants are more generic because they don’t rely on the element type being `Comparable`. We get higher performance with fewer constraints.

## Only protocol requirements create customization points

Note that none of these four methods are _protocol requirements_ of the `Sequence` or `Collection` protocols, i.e. they _aren’t_ part of the protocols’ definitions. They are only _default implementations_ without being requirements. As a consequence, calls to these methods are statically dispatched because they aren’t [_customization points_](https://developer.apple.com/videos/play/wwdc2015-408/?time=1767)[2](#fn:1).

The implementations in `SortedArray` don’t _override_ the default implementations (because only requirements can be overridden), they only _shadow_ them. Your code will take advantage of the more efficient implementations when you work directly with a variable of type `SortedArray`, but they will never be called in a generic context. Example:

```
let numbers = SortedArray(unsorted: [3,2,1])

// This will call SortedArray.max(), as expected:
let a = numbers.max()

func myMax<S: Sequence>(_ sequence: S ) -> S.Iterator.Element?
    where S.Iterator.Element: Comparable {
    return sequence.max()
}

// This will call Sequence.max() (less efficient):
let b = myMax(numbers)
```

There’s nothing we can do about this, short of lobbying on [swift-evolution](https://swift.org/community/#mailing-lists) to make these methods protocol requirements (and I’m not sure it’s a good idea).

**Update February 9, 2017:** I missed that methods like `index(of:)`, `contains(_:)` etc. _can’t_ currently be requirements on `Sequence` or `Collection` because they need an `Iterator.Element: Equatable` constraint and there’s no way to define a protocol requirement with a generic constraint. [Becca Royal-Gordon raised this issue on swift-evolution](https://forums.swift.org/t/protocol-requirement-where-clauses-constraining-associated-types/5133) and asks if this is something that should be added to the language.

# Slicing

I toyed with making `SortedArray`’s backing store an [`ArraySlice`](https://developer.apple.com/reference/swift/arrayslice) rather than an `Array`. The advantage would be that it would be very easy to define `SortedArray.SubSequence = ArraySlice`, i.e. to make `SortedArray` its own slice type. This would make working with slices very convenient because something like `sortedArray.prefix(5)` would return another `SortedArray` and not the default type [`RandomAccessSlice`](https://developer.apple.com/reference/swift/randomaccessslice).

In the end I decided against it because it is discouraged to hold `ArraySlice` instances for long periods of time. Even a tiny slice of a very large array holds on to its base array forever, and this can lead to high memory usage the user doesn’t expect — even if the base array’s memory technically hasn’t leaked, the slice prevents it from being freed in a timely manner.

# Performance of generic types imported from other modules

If you intend to use the `SortedArray` type in your own code (or any other performance-critical generic type, for that matter), I suggest you don’t import it as a third-party module but [add the source file directly to your module](https://github.com/apple/swift/blob/master/docs/OptimizationTips.rst#advice-put-generic-declarations-in-the-same-module-where-they-are-used).

As of Swift 3, Swift can’t perform generics specialization across module boundaries. In other words, if you use a `SortedArray<Int>` in your code and `SortedArray` is defined in another module, the compiler can’t generate optimized code for an array of `Int` elements — it can only use the standard code path that boxes each generic value in a container and performs method dispatch through an associated witness table. This can easily slow down your code by [one or two orders of magitude](https://github.com/lorentey/BTree#remark-on-performance-of-imported-generics):

> Current versions of the Swift compiler are unable to specialize generic types that are imported from external modules other than the standard library. … This limitation puts a considerable limit on the raw performance achievable by collection types imported from external modules, especially if they are parameterized with simple, extremely optimizable value types such as `Int` or even `String`. Relying on import will incur _a 10-200x slowdown_ when your collection is holding these most basic value types. (The effect is much reduced for reference types, though.)

The standard library is the only module that is exempt from this limitation. Standard library types are always available for specialization from any module.

I hope the Swift compiler team finds a way around this in the future. I don’t know how that would work, though. The compiler currently ships with an [unoffical attribute called `@_specialize`](https://oleb.net/blog/2017/02/sorted-array/attribute) (which will [get a new syntax soon](https://github.com/apple/swift/pull/6486), it seems). Annotating a function with this attribute and a list of types instructs the compiler to emit specialized code for the specified types. The in-progress version of the attribute also seems to support constraints like `_Trivial64` to cover all trivial value types of a certain size.

# Conclusion

[The full implementation](https://github.com/ole/SortedArray) is 200 lines including comments, plus about the same in tests.

As you can see, there is a lot to consider in a custom collection type. And it’s all about the interface — we haven’t even touched the underlying implementation (that’s done by our backing array). But I think it’s worth it for the result. We end up with a type that behaves almost exactly like the built-in collection types and can be passed interchangeably to any algorithm that operates on `Sequence` or `Collection`.

The very real performance impact of using generic types across module boundaries is a bummer, though.

1. The semantics of the `min()` and `max()` methods I present here are not the same as [`Sequence.min()`](https://developer.apple.com/reference/swift/sequence/1641174-min) and [`Sequence.max()`](https://developer.apple.com/reference/swift/sequence/1641492-max). While the `Sequence` methods always use [`<`](https://developer.apple.com/reference/swift/comparable/1538311) as the comparison predicate, the variants for `SortedArray` use the type’s own comparison predicate.

  As a result, if you initialize a `SortedArray` with a different predicate than `<`, the methods will return different results than the `Sequence` methods (but consistent with `SortedArray`’s semantics):

  ```
  let numbers = SortedArray(unsorted: [3,5,1],
      areInIncreasingOrder: >)
  numbers.min() // → 5
  Array(numbers).min() // → 1
  ```

  (The standard library provides [`min(by:)`](https://developer.apple.com/reference/swift/sequence/2295620-min) and [`max(by:)`](https://developer.apple.com/reference/swift/sequence/2299297-max) to give you the option to use a custom comparison predicate.)

  If this distinction is important to you, it can make sense to introduce a `SortedCollection` protocol that codifies these semantics. The protocol would include the comparison predicate as one of its requirements:

  ```
  protocol SortedCollection: Collection {
      var areInIncreasingOrder: (Iterator.Element, Iterator.Element) -> Bool { get }
      ...
  }
  ```

  [↩︎](#fnref:minmax)
2. Search for “customization point” in the transcript of the linked WWDC session:

  > The answer is that a protocol requirement creates a customization point.

  [↩︎](#fnref:1)
