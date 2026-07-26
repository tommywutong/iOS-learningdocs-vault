---
title: CoreLocationUI
framework: CoreLocationUI
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocationui
source_url: 'https://developer.apple.com/documentation/corelocationui'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocationui.json'
content_hash: 'sha256:90990d1a4d22cd58'
translated: false
---

> Navigation: [Technologies](technologies.md)

# CoreLocationUI

<sub>Framework</sub>

Streamline access to users’ location data through a standard, secure UI.

## Overview

The CoreLocationUI framework contains a standardized UI that interacts securely with [Core Location](corelocation.md) to request authorization to access location data.

CoreLocationUI provides [LocationButton](corelocationui/locationbutton.md) for SwiftUI apps and [CLLocationButton](corelocationui/cllocationbutton.md) for UIKit apps. Add these buttons to your UI when you want someone to grant one-time authorization for your app to fetch their location. The button’s style is consistent with the standard Core Location design language, giving users a sense of familiarity and trust when they interact with it.

> [!note] Note
> The location button ignores user input on Mac apps built with Mac Catalyst, and on compatible iPad and iPhone apps running in visionOS.

## Topics

### Location authorization

- [Sharing Your Location to Find a Park](corelocationui/sharing-your-location-to-find-a-park.md) — Ask for location access using a customizable location button.
- [LocationButton](corelocationui/locationbutton.md) — A SwiftUI button that grants one-time location authorization.
- [CLLocationButton](corelocationui/cllocationbutton.md) — A button that grants one-time location authorization.

### Button customization

- [CLLocationButtonIcon](corelocationui/cllocationbuttonicon.md) — Constants that specify styles for the location arrow icon on the button.
- [CLLocationButtonLabel](corelocationui/cllocationbuttonlabel.md) — Constants that specify the text of the button label.
