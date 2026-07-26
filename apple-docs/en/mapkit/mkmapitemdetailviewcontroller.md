---
title: MKMapItemDetailViewController
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapitemdetailviewcontroller
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitemdetailviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitemdetailviewcontroller.json'
content_hash: 'sha256:31b21cf387a4e9c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapItemDetailViewController

<sub>Class</sub>

An object that displays detailed information about a map item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class MKMapItemDetailViewController
```

## Overview

The view controller presents modally and displays place information such as addresses and phone numbers.

This class doesn’t support subclassing. The view hierarchy for this class is private and must not be modified.

## Relationships

- **Inherits From**: [NSViewController](../appkit/nsviewcontroller.md), [UIViewController](../uikit/uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSEditor](../appkit/nseditor.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSeguePerforming](../appkit/nssegueperforming.md), [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md), [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UIContentContainer](../uikit/uicontentcontainer.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UIStateRestoring](../uikit/uistaterestoring.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Creating a map item detail view controller

- [- initWithMapItem:](<mkmapitemdetailviewcontroller/init(mapitem_).md>) — Create a map item detail view controller.
- [- initWithMapItem:displaysMap:](<mkmapitemdetailviewcontroller/init(mapitem_displaysmap_).md>) — Create a map item detail view controller

### Dismissing the map item detail interface

- [delegate](mkmapitemdetailviewcontroller/delegate.md) — The map item detail view controller’s delegate.

### Getting and setting the map item

- [mapItem](mkmapitemdetailviewcontroller/mapitem.md) — The map item to display.

## See Also

### Place information

- [MKMapItemDetailViewControllerDelegate](mkmapitemdetailviewcontrollerdelegate.md) — The methods that you use to receive events from an associated map view controller.
- [MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle.md) — The type of map item detail accessory presentation to use.
- [MKSelectionAccessory](mkselectionaccessory.md) — The type of accessory to display for a selected annotation.
- [CalloutStyle](mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle.md) — The style to use for a map item detail callout presentation.
