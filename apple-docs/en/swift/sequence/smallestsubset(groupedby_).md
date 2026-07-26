---
title: 'smallestSubset(groupedBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/sequence/smallestsubset(groupedby:)'
source_url: 'https://developer.apple.com/documentation/swift/sequence/smallestsubset(groupedby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/smallestsubset%28groupedby%3A%29.json'
content_hash: 'sha256:48086a30471538e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# smallestSubset(groupedBy:)

<sub>Instance Method</sub>

Returns the smallest group of donations when grouped by the specified key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func smallestSubset<DonationInfo, Value>(groupedBy keyPath: KeyPath<DonationInfo, Value>) -> [Self.Element] where DonationInfo : Decodable, DonationInfo : Encodable, DonationInfo : Sendable, Value : Hashable, Self.Element == Tips.Event<DonationInfo>.Donation
```

## Parameters

- `keyPath` — A key path to a `Hashable` property on the donation value to group by.

## Return Value

An array of donations belonging to the smallest group.

## Discussion

Use this method inside a `Tips/Rule` predicate to find the least frequently donated value for a given property.

```swift
#Rule(LandmarkDetail.didViewLandmarkDetail) {
    $0.donations.smallestSubset(groupedBy: \.landmarkID).count >= 2
}
```
