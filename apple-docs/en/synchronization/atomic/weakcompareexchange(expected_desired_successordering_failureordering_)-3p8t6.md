---
title: 'weakCompareExchange(expected:desired:successOrdering:failureOrdering:)'
framework: Synchronization
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/synchronization/atomic/weakcompareexchange(expected:desired:successordering:failureordering:)-3p8t6'
source_url: 'https://developer.apple.com/documentation/synchronization/atomic/weakcompareexchange(expected:desired:successordering:failureordering:)-3p8t6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomic/weakcompareexchange%28expected%3Adesired%3Asuccessordering%3Afailureordering%3A%29-3p8t6.json'
content_hash: 'sha256:4e17ed64871a3113'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [Atomic](../atomic.md)

# weakCompareExchange(expected:desired:successOrdering:failureOrdering:)

<sub>Instance Method</sub>

Perform an atomic weak compare and exchange operation on the current value, applying the specified success/failure memory orderings. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func weakCompareExchange(expected: consuming Value, desired: consuming Value, successOrdering: AtomicUpdateOrdering, failureOrdering: AtomicLoadOrdering) -> (exchanged: Bool, original: Value)
```

## Parameters

- `expected` — The expected current value.

- `desired` — The desired new value.

- `successOrdering` — The memory ordering to apply if this operation performs the exchange.

- `failureOrdering` — The memory ordering to apply on this operation does not perform the exchange.

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

The `ordering` argument specifies the memory ordering to use when the operation manages to update the current value, while `failureOrdering` will be used when the operation leaves the value intact.

> [!note] Note
> The weakCompareExchange form may sometimes return false even when the original and expected values are equal. (Such failures may happen when some transient condition prevents the underlying operation from succeeding – such as an incoming interrupt during a load-link/store-conditional instruction sequence.) This variant is designed to be called in a loop that only exits when the exchange is successful; in such loops, using weakCompareExchange may lead to a performance improvement by eliminating a nested loop in the regular, “strong”, compareExchange variants.
