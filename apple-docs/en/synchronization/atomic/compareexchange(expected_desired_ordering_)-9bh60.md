---
title: 'compareExchange(expected:desired:ordering:)'
framework: Synchronization
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/synchronization/atomic/compareexchange(expected:desired:ordering:)-9bh60'
source_url: 'https://developer.apple.com/documentation/synchronization/atomic/compareexchange(expected:desired:ordering:)-9bh60'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomic/compareexchange%28expected%3Adesired%3Aordering%3A%29-9bh60.json'
content_hash: 'sha256:3aeec1240687e8f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [Atomic](../atomic.md)

# compareExchange(expected:desired:ordering:)

<sub>Instance Method</sub>

Perform an atomic compare and exchange operation on the current value, applying the specified memory ordering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func compareExchange(expected: consuming Value, desired: consuming Value, ordering: AtomicUpdateOrdering) -> (exchanged: Bool, original: Value)
```

## Parameters

- `expected` — The expected current value.

- `desired` — The desired new value.

- `ordering` — The memory ordering to apply on this operation.

## Return Value

A tuple `(exchanged, original)`, where `exchanged` is true if the exchange was successful, and `original` is the original value.

## Discussion

This operation performs the following algorithm as a single atomic transaction:

```swift
atomic(self) { currentValue in
  let original = currentValue
  guard original == expected else { return (false, original) }
  currentValue = desired
  return (true, original)
}
```

> [!note] Note
> This method implements a “strong” compare and exchange operation that does not permit spurious failures.
