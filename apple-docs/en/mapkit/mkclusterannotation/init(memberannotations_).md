---
title: 'init(memberAnnotations:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkclusterannotation/init(memberannotations:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkclusterannotation/init(memberannotations:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkclusterannotation/init%28memberannotations%3A%29.json'
content_hash: 'sha256:9a39848429f18a25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKClusterAnnotation](../mkclusterannotation.md)

# init(memberAnnotations:)

<sub>Initializer</sub>

Creates a cluster annotation with the specified individual annotations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(memberAnnotations: [any MKAnnotation])
```

## Parameters

- `memberAnnotations` — The annotations to group together as a single entity.

## Return Value

An initialized [MKClusterAnnotation](../mkclusterannotation.md) object or `nil` if the object could not be created.
