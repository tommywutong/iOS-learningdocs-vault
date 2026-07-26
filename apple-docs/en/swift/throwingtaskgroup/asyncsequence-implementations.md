---
title: AsyncSequence Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/throwingtaskgroup/asyncsequence-implementations
source_url: 'https://developer.apple.com/documentation/swift/throwingtaskgroup/asyncsequence-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingtaskgroup/asyncsequence-implementations.json'
content_hash: 'sha256:9b7564654ec87239'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Concurrency](../concurrency.md) · [ThrowingTaskGroup](../throwingtaskgroup.md)

# AsyncSequence Implementations

<sub>API Collection</sub>

## Topics

### Instance Methods

- [allSatisfy(_:)](<allsatisfy(__).md>) — Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [compactMap(_:)](<compactmap(__)-7mgi5.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [compactMap(_:)](<compactmap(__)-944nh.md>) — Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [contains(_:)](<contains(__).md>) — Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.
- [contains(where:)](<contains(where_).md>) — Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [drop(while:)](<drop(while_).md>) — Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [dropFirst(_:)](<dropfirst(__).md>) — Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [filter(_:)](<filter(__).md>) — Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [first(where:)](<first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [flatMap(_:)](<flatmap(__)-319er.md>) — Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.
- [flatMap(_:)](<flatmap(__)-8ved0.md>) — Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.
- [flatMap(_:)](<flatmap(__)-dwsi.md>) — Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.
- [flatMap(_:)](<flatmap(__)-vhiz.md>) — Creates an asynchronous sequence that concatenates the results of calling the given error-throwing transformation with each element of this sequence.
- [makeAsyncIterator()](<makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [map(_:)](<map(__)-4a4ju.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [map(_:)](<map(__)-58nrv.md>) — Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [max()](<max().md>) — Returns the maximum element in an asynchronous sequence of comparable elements.
- [max(by:)](<max(by_).md>) — Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [min()](<min().md>) — Returns the minimum element in an asynchronous sequence of comparable elements.
- [min(by:)](<min(by_).md>) — Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [prefix(_:)](<prefix(__).md>) — Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [prefix(while:)](<prefix(while_).md>) — Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
- [reduce(_:_:)](<reduce(____).md>) — Returns the result of combining the elements of the asynchronous sequence using the given closure.
- [reduce(into:_:)](<reduce(into___).md>) — Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.

### Type Aliases

- [AsyncIterator](asynciterator.md) — The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [Element](element.md) — The type of element produced by this asynchronous sequence.
