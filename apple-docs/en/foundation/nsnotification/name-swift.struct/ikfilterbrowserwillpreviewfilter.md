---
title: IKFilterBrowserWillPreviewFilter
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/ikfilterbrowserwillpreviewfilter
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/ikfilterbrowserwillpreviewfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/ikfilterbrowserwillpreviewfilter.json'
content_hash: 'sha256:7fa66e29a9526459'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# IKFilterBrowserWillPreviewFilter

<sub>Type Property</sub>

Posted before showing a filter preview, allowing an application to set the parameters of a filter.

<sub>macOS</sub>

```swift
static let IKFilterBrowserWillPreviewFilter: NSNotification.Name
```

## Discussion

The selected filter is sent as the object in the notification.

## See Also

### Quartz

- [IKFilterBrowserFilterDoubleClick](ikfilterbrowserfilterdoubleclick.md) — Posted when the user double-clicks a filter in the filter browser.
- [IKFilterBrowserFilterSelected](ikfilterbrowserfilterselected.md) — Posted when the user clicks a filter name in the filter browser.
- [quartzFilterManagerDidAddFilter](quartzfiltermanagerdidaddfilter.md)
- [quartzFilterManagerDidModifyFilter](quartzfiltermanagerdidmodifyfilter.md)
- [quartzFilterManagerDidRemoveFilter](quartzfiltermanagerdidremovefilter.md)
- [quartzFilterManagerDidSelectFilter](quartzfiltermanagerdidselectfilter.md)
- [QCCompositionPickerPanelDidSelectComposition](qccompositionpickerpaneldidselectcomposition.md) — Posted when the user chooses a composition. _(deprecated)_
- [QCCompositionPickerViewDidSelectComposition](qccompositionpickerviewdidselectcomposition.md) — Posted when the user selects a composition in the picker view. _(deprecated)_
- [QCCompositionRepositoryDidUpdate](qccompositionrepositorydidupdate.md) — Posted whenever the list of compositions in the composition repository is updated. _(deprecated)_
- [QCViewDidStartRendering](qcviewdidstartrendering.md) — Posted when the view starts rendering. _(deprecated)_
- [QCViewDidStopRendering](qcviewdidstoprendering.md) — Posted when the view stops rendering. _(deprecated)_
