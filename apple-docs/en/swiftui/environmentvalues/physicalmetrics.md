---
title: physicalMetrics
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/physicalmetrics
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/physicalmetrics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/physicalmetrics.json'
content_hash: 'sha256:b60a380e061fb1ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# physicalMetrics

<sub>Instance Property</sub>

The physical metrics associated with a scene.

<sub>visionOS</sub>

```swift
var physicalMetrics: PhysicalMetricsConverter { get set }
```

## Discussion

Reading this value returns a `PhysicalMetricsConverter` corresponding to the window scene associated with the environment’s reader. The converter can convert point sizes into physical measurements of length, and vice versa.

Reading this value is only supported in the body of a [View](../view.md) or of a type that inherits a [View](../view.md)’s environment.

## See Also

### View attributes

- [allowedDynamicRange](alloweddynamicrange.md) — The allowed dynamic range for the view, or nil.
- [backgroundMaterial](backgroundmaterial.md) — The material underneath the current view.
- [backgroundProminence](backgroundprominence.md) — The prominence of the background underneath views associated with this environment.
- [backgroundStyle](backgroundstyle.md) — An optional style that overrides the default system background style when set.
- [badgeProminence](badgeprominence.md) — The prominence to apply to badges associated with this environment.
- [contentTransition](contenttransition.md) — The current method of animating the contents of views.
- [contentTransitionAddsDrawingGroup](contenttransitionaddsdrawinggroup.md) — A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.
- [defaultMinListHeaderHeight](defaultminlistheaderheight.md) — The default minimum height of a header in a list.
- [defaultMinListRowHeight](defaultminlistrowheight.md) — The default minimum height of rows in a list.
- [headerProminence](headerprominence.md) — The prominence to apply to section headers within a view.
- [realityKitScene](realitykitscene.md)
- [realityViewCameraControls](realityviewcameracontrols.md) — The camera controls for the reality view.
- [redactionReasons](redactionreasons.md) — The current redaction reasons applied to the view hierarchy.
- [springLoadingBehavior](springloadingbehavior.md) — The behavior of spring loaded interactions for the views associated with this environment.
- [symbolRenderingMode](symbolrenderingmode.md) — The current symbol rendering mode, or `nil` denoting that the mode is picked automatically using the current image and foreground style as parameters.
