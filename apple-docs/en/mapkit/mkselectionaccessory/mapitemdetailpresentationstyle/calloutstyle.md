---
title: MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle
framework: MapKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle
source_url: 'https://developer.apple.com/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle.json'
content_hash: 'sha256:9b08a598a1d3bc89'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKSelectionAccessory](../../mkselectionaccessory.md) · [MapItemDetailPresentationStyle](../mapitemdetailpresentationstyle.md)

# MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle

<sub>Enumeration</sub>

The style to use for a map item detail callout presentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
enum CalloutStyle
```

## Overview

In Swift, use [MKMapItemDetailSelectionAccessoryCalloutStyleFull](calloutstyle/full.md) for map views on iPadOS and macOS. Use a sheet presentation to display full detail place information on iOS.

In Objective-C, use [MKMapItemDetailSelectionAccessoryCalloutStyleFull](calloutstyle/full.md) for map views on iPadOS and macOS. Use a sheet presentation to display full detail place information on iOS.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [RawRepresentable](../../../swift/rawrepresentable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [MKMapItemDetailSelectionAccessoryCalloutStyleAutomatic](calloutstyle/automatic.md) — A value that allows the framework to choose an appropriate callout style automatically.
- [MKMapItemDetailSelectionAccessoryCalloutStyleCompact](calloutstyle/compact.md) — A compact, space-saving callout style.
- [MKMapItemDetailSelectionAccessoryCalloutStyleFull](calloutstyle/full.md) — A rich, detailed callout style that is suitable for large map views.

### Initializers

- [init(rawValue:)](<calloutstyle/init(rawvalue_).md>)

## See Also

### Place information

- [MKMapItemDetailViewControllerDelegate](../../mkmapitemdetailviewcontrollerdelegate.md) — The methods that you use to receive events from an associated map view controller.
- [MKMapItemDetailViewController](../../mkmapitemdetailviewcontroller.md) — An object that displays detailed information about a map item.
- [MapItemDetailPresentationStyle](../mapitemdetailpresentationstyle.md) — The type of map item detail accessory presentation to use.
- [MKSelectionAccessory](../../mkselectionaccessory.md) — The type of accessory to display for a selected annotation.
