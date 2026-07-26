---
title: QCCompositionRepositoryDidUpdate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.4+（10.15 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsnotification/name-swift.struct/qccompositionrepositorydidupdate
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/qccompositionrepositorydidupdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/qccompositionrepositorydidupdate.json'
content_hash: 'sha256:2e93078b73101d3a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# QCCompositionRepositoryDidUpdate

<sub>Type Property</sub>

Posted whenever the list of compositions in the composition repository is updated.

> [!warning] Deprecated
> QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

<sub>macOS</sub>

```swift
static let QCCompositionRepositoryDidUpdate: NSNotification.Name
```

## See Also

### Quartz

- [IKFilterBrowserFilterDoubleClick](ikfilterbrowserfilterdoubleclick.md) — Posted when the user double-clicks a filter in the filter browser.
- [IKFilterBrowserFilterSelected](ikfilterbrowserfilterselected.md) — Posted when the user clicks a filter name in the filter browser.
- [IKFilterBrowserWillPreviewFilter](ikfilterbrowserwillpreviewfilter.md) — Posted before showing a filter preview, allowing an application to set the parameters of a filter.
- [quartzFilterManagerDidAddFilter](quartzfiltermanagerdidaddfilter.md)
- [quartzFilterManagerDidModifyFilter](quartzfiltermanagerdidmodifyfilter.md)
- [quartzFilterManagerDidRemoveFilter](quartzfiltermanagerdidremovefilter.md)
- [quartzFilterManagerDidSelectFilter](quartzfiltermanagerdidselectfilter.md)
- [QCCompositionPickerPanelDidSelectComposition](qccompositionpickerpaneldidselectcomposition.md) — Posted when the user chooses a composition. _(deprecated)_
- [QCCompositionPickerViewDidSelectComposition](qccompositionpickerviewdidselectcomposition.md) — Posted when the user selects a composition in the picker view. _(deprecated)_
- [QCViewDidStartRendering](qcviewdidstartrendering.md) — Posted when the view starts rendering. _(deprecated)_
- [QCViewDidStopRendering](qcviewdidstoprendering.md) — Posted when the view stops rendering. _(deprecated)_
