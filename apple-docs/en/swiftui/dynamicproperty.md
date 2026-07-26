---
title: DynamicProperty
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dynamicproperty
source_url: 'https://developer.apple.com/documentation/swiftui/dynamicproperty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dynamicproperty.json'
content_hash: 'sha256:bdf05b139c1f2041'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DynamicProperty

<sub>Protocol</sub>

An interface for a stored variable that updates an external property of a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DynamicProperty
```

## Overview

The view gives values to these properties prior to recomputing the view’s [body](view/body-8kl5o.md).

## Relationships

- **Conforming Types**: [AccessibilityFocusState](accessibilityfocusstate.md), [AppStorage](appstorage.md), [Binding](binding.md), [Environment](environment.md), [EnvironmentObject](environmentobject.md), [FetchRequest](fetchrequest.md), [FocusState](focusstate.md), [FocusedBinding](focusedbinding.md), [FocusedObject](focusedobject.md), [FocusedValue](focusedvalue.md), [GestureState](gesturestate.md), [NSApplicationDelegateAdaptor](nsapplicationdelegateadaptor.md), [Namespace](namespace.md), [ObservedObject](observedobject.md), [PhysicalMetric](physicalmetric.md), [ScaledMetric](scaledmetric.md), [SceneStorage](scenestorage.md), [SectionedFetchRequest](sectionedfetchrequest.md), [State](state.md), [StateObject](stateobject.md), [UIApplicationDelegateAdaptor](uiapplicationdelegateadaptor.md), [WKApplicationDelegateAdaptor](wkapplicationdelegateadaptor.md), [WKExtensionDelegateAdaptor](wkextensiondelegateadaptor.md)

## Topics

### Updating the value

- [update()](<dynamicproperty/update().md>) — Updates the underlying value of the stored value.
