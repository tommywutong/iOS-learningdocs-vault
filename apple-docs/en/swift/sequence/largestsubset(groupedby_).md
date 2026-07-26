---
title: 'largestSubset(groupedBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/sequence/largestsubset(groupedby:)'
source_url: 'https://developer.apple.com/documentation/swift/sequence/largestsubset(groupedby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/largestsubset%28groupedby%3A%29.json'
content_hash: 'sha256:97f06d305c35a5df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# largestSubset(groupedBy:)

<sub>Instance Method</sub>

Returns the largest group of donations when grouped by the specified key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func largestSubset<DonationInfo, Value>(groupedBy keyPath: KeyPath<DonationInfo, Value>) -> [Self.Element] where DonationInfo : Decodable, DonationInfo : Encodable, DonationInfo : Sendable, Value : Hashable, Self.Element == Tips.Event<DonationInfo>.Donation
```

## Parameters

- `keyPath` — A key path to a `Hashable` property on the donation value to group by.

## Return Value

An array of donations belonging to the largest group.

## Discussion

Use this method inside a `Tips/Rule` predicate to find the most frequently donated value for a given property.

```swift
#Rule(LandmarkDetail.didViewLandmarkDetail) {
    $0.donations.largestSubset(groupedBy: \.landmarkID).count >= 5
}
```
