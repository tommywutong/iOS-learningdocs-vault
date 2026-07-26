---
title: GCControllerUserCustomizationsDidChangeNotification
framework: Game Controller
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/gamecontroller/gccontrollerusercustomizationsdidchangenotification
source_url: 'https://developer.apple.com/documentation/gamecontroller/gccontrollerusercustomizationsdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/gamecontroller/gccontrollerusercustomizationsdidchangenotification.json'
content_hash: 'sha256:0fab5f98c2006bb1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Game Controller](../gamecontroller.md)

# GCControllerUserCustomizationsDidChangeNotification

<sub>Global Variable</sub>

A notification that posts when the user customizes the button mappings or other settings of a controller.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
extern NSString * const GCControllerUserCustomizationsDidChangeNotification;
```

## Discussion

Use this notification to update your interface when the mappings change. The notification object is the [GCController](gccontroller.md) object that the user customizes.

The system posts this notification on the main thread.

## See Also

### Remapping input elements

- [hasRemappedElements](gcphysicalinputprofile/hasremappedelements.md) — A Boolean value that indicates whether the user remaps elements in this profile.
- [- mappedElementAliasForPhysicalInputName:](<gcphysicalinputprofile/mappedelementalias(forphysicalinputname_).md>) — Returns the name of the input element to which the user remaps the given physical element.
- [- mappedPhysicalInputNamesForElementAlias:](<gcphysicalinputprofile/mappedphysicalinputnames(forelementalias_).md>) — Returns the physical input elements to which the user remaps the given input element.
