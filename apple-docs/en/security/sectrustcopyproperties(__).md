---
title: 'SecTrustCopyProperties(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, macOS 10.7+（12.0 起废弃）, tvOS 9.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（8.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectrustcopyproperties(_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustcopyproperties(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustcopyproperties%28_%3A%29.json'
content_hash: 'sha256:5cbb58379ab1c64d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustCopyProperties(_:)

<sub>Function</sub>

Returns an array containing the properties of a trust object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustCopyProperties(_ trust: SecTrust) -> CFArray?
```

## Parameters

- `trust` — The trust object from which properties should be copied.

## Return Value

An array, or `NULL` if the trust object has not yet been evaluated. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free this array’s memory when you are done with it.

## Discussion

The result is an ordered array of dictionaries, one per certificate in the chain, beginning with the leaf node at index zero (`0`) and continuing up to the anchor (or the last certificate in the chain if no anchor was found).

The property dictionary at index zero may also include general information about the entire chain’s validity in the context of this trust evaluation. See [Certificate Property Type Values](certificate-property-type-values.md) for a list of currently defined keys.
