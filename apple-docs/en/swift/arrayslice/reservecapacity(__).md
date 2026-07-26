---
title: 'reserveCapacity(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/arrayslice/reservecapacity(_:)'
source_url: 'https://developer.apple.com/documentation/swift/arrayslice/reservecapacity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/arrayslice/reservecapacity%28_%3A%29.json'
content_hash: 'sha256:5ebc59ea0806d202'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ArraySlice](../arrayslice.md)

# reserveCapacity(_:)

<sub>Instance Method</sub>

Reserves enough space to store the specified number of elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func reserveCapacity(_ minimumCapacity: Int)
```

## Parameters

- `minimumCapacity` — The requested number of elements to store.

## Discussion

If you are adding a known number of elements to an array, use this method to avoid multiple reallocations. This method ensures that the array has unique, mutable, contiguous storage, with space allocated for at least the requested number of elements.

Calling the `reserveCapacity(_:)` method on an array with bridged storage triggers a copy to contiguous storage even if the existing storage has room to store `minimumCapacity` elements.

For performance reasons, the size of the newly allocated storage might be greater than the requested capacity. Use the array’s `capacity` property to determine the size of the new storage.

## Preserving an Array’s Geometric Growth Strategy

If you implement a custom data structure backed by an array that grows dynamically, naively calling the `reserveCapacity(_:)` method can lead to worse than expected performance. Arrays need to follow a geometric allocation pattern for appending elements to achieve amortized constant-time performance. The `Array` type’s `append(_:)` and `append(contentsOf:)` methods take care of this detail for you, but `reserveCapacity(_:)` allocates only as much space as you tell it to (padded to a round value), and no more. This avoids over-allocation, but can result in insertion not having amortized constant-time performance.

The following code declares `values`, an array of integers, and the `addTenQuadratic()` function, which adds ten more values to the `values` array on each call.

```swift
  var values: [Int] = [0, 1, 2, 3]

  // Don't use 'reserveCapacity(_:)' like this
  func addTenQuadratic() {
      let newCount = values.count + 10
      values.reserveCapacity(newCount)
      for n in values.count..<newCount {
          values.append(n)
      }
  }
```

The call to `reserveCapacity(_:)` increases the `values` array’s capacity by exactly 10 elements on each pass through `addTenQuadratic()`, which is linear growth. Instead of having constant time when averaged over many calls, the function may decay to performance that is linear in `values.count`. This is almost certainly not what you want.

In cases like this, the simplest fix is often to simply remove the call to `reserveCapacity(_:)`, and let the `append(_:)` method grow the array for you.

```swift
  func addTen() {
      let newCount = values.count + 10
      for n in values.count..<newCount {
          values.append(n)
      }
  }
```

If you need more control over the capacity of your array, implement your own geometric growth strategy, passing the size you compute to `reserveCapacity(_:)`.

> [!abstract] Complexity
> O(_n_), where _n_ is the number of elements in the array.
