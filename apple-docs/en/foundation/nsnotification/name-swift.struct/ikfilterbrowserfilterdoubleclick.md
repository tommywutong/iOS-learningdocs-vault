---
title: IKFilterBrowserFilterDoubleClick
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/ikfilterbrowserfilterdoubleclick
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/ikfilterbrowserfilterdoubleclick'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/ikfilterbrowserfilterdoubleclick.json'
content_hash: 'sha256:982312e9aa5efc5c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# IKFilterBrowserFilterDoubleClick

<sub>Type Property</sub>

Posted when the user double-clicks a filter in the filter browser.

<sub>macOS</sub>

```swift
static let IKFilterBrowserFilterDoubleClick: NSNotification.Name
```

## Discussion

The name of the selected filter is send as the object in the notification.

## See Also

### Quartz

- [IKFilterBrowserFilterSelected](ikfilterbrowserfilterselected.md) — Posted when the user clicks a filter name in the filter browser.
- [IKFilterBrowserWillPreviewFilter](ikfilterbrowserwillpreviewfilter.md) — Posted before showing a filter preview, allowing an application to set the parameters of a filter.
- [quartzFilterManagerDidAddFilter](quartzfiltermanagerdidaddfilter.md)
- [quartzFilterManagerDidModifyFilter](quartzfiltermanagerdidmodifyfilter.md)
- [quartzFilterManagerDidRemoveFilter](quartzfiltermanagerdidremovefilter.md)
- [quartzFilterManagerDidSelectFilter](quartzfiltermanagerdidselectfilter.md)
- [QCCompositionPickerPanelDidSelectComposition](qccompositionpickerpaneldidselectcomposition.md) — Posted when the user chooses a composition. _(deprecated)_
- [QCCompositionPickerViewDidSelectComposition](qccompositionpickerviewdidselectcomposition.md) — Posted when the user selects a composition in the picker view. _(deprecated)_
- [QCCompositionRepositoryDidUpdate](qccompositionrepositorydidupdate.md) — Posted whenever the list of compositions in the composition repository is updated. _(deprecated)_
- [QCViewDidStartRendering](qcviewdidstartrendering.md) — Posted when the view starts rendering. _(deprecated)_
- [QCViewDidStopRendering](qcviewdidstoprendering.md) — Posted when the view stops rendering. _(deprecated)_
