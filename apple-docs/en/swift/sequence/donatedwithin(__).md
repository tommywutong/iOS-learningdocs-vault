---
title: 'donatedWithin(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/sequence/donatedwithin(_:)'
source_url: 'https://developer.apple.com/documentation/swift/sequence/donatedwithin(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/donatedwithin%28_%3A%29.json'
content_hash: 'sha256:aa502d80e3621124'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# donatedWithin(_:)

<sub>Instance Method</sub>

Filters donations to only those that occurred within the specified time range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func donatedWithin<DonationInfo>(_ timeRange: Tips.DonationTimeRange) -> [Self.Element] where DonationInfo : Decodable, DonationInfo : Encodable, DonationInfo : Sendable, Self.Element == Tips.Event<DonationInfo>.Donation
```

## Parameters

- `timeRange` — The time range to filter donations by.

## Return Value

An array of donations that occurred within the given time range.

## Discussion

Use this method inside a `Tips/Rule` predicate to constrain which donations are considered when evaluating tip eligibility.

```swift
#Rule(AppEvents.didLogin) {
    $0.donations.donatedWithin(.week).count >= 3
}
```
