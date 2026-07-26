---
title: heading
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.15+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/heading
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/heading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/heading.json'
content_hash: 'sha256:2ef360f0e12e64c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# heading

<sub>Instance Property</sub>

The most recently reported heading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@NSCopying var heading: CLHeading? { get }
```

## Discussion

The value of this property is `nil` if heading updates have never been initiated.

## See Also

### Getting recent location and heading data

- [location](location.md) — The most recently retrieved user location.
