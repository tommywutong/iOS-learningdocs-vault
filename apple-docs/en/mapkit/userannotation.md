---
title: UserAnnotation
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/userannotation
source_url: 'https://developer.apple.com/documentation/mapkit/userannotation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/userannotation.json'
content_hash: 'sha256:ea5a0664f712ec2e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# UserAnnotation

<sub>Structure</sub>

Displays the person’s current location on the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct UserAnnotation<Content> where Content : View
```

## Overview

Displays the person’s current location using the system styled user location indicator.

## Relationships

- **Conforms To**: [MapContent](mapcontent.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a user annotation

- [init()](<userannotation/init().md>) — Creates an annotation that displays the person’s current location.
- [init(anchor:)](<userannotation/init(anchor_).md>) — Creates an annotation that displays the person’s current location using the system styled user location indicator with the specified anchor point.
- [init(anchor:content:)](<userannotation/init(anchor_content_)-8u3r4.md>) — Creates an annotation that displays a person’s current location using the system styled user location indicator with the specified anchor point using a custom view.
- [init(anchor:content:)](<userannotation/init(anchor_content_)-3e78j.md>) — Create an annotation that displays the person’s current location of the user using a custom view.

### Information about a person’s location

- [UserLocation](userlocation.md) — A structure that contains Information about the person’s current location.

## See Also

### Annotations and overlays

- [Annotation](annotation.md) — A customizable annotation used to indicate a location on a map.
- [MapCircle](mapcircle.md) — A circular overlay with a configurable radius that you center on a geographic coordinate.
- [MapPolygon](mappolygon.md) — A closed polygon overlay.
- [MapPolyline](mappolyline.md) — An open polygon overlay consisting of one or more connected line segments.
- [Marker](marker.md) — A balloon-shaped annotation that marks a map location.
