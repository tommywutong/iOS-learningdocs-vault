---
title: IKFilterBrowserWillPreviewFilterNotification
framework: Quartz
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.4+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/quartz/ikfilterbrowserwillpreviewfilternotification
source_url: 'https://developer.apple.com/documentation/quartz/ikfilterbrowserwillpreviewfilternotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartz/ikfilterbrowserwillpreviewfilternotification.json'
content_hash: 'sha256:4c7320ca766e2ae6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Quartz](../quartz.md)

# IKFilterBrowserWillPreviewFilterNotification

<sub>Global Variable</sub>

Posted before showing a filter preview, allowing an application to set the parameters of a filter.

<sub>macOS</sub>

```objc
extern NSString * const IKFilterBrowserWillPreviewFilterNotification;
```

## Discussion

The selected filter is sent as the object in the notification.

## See Also

### Notifications

- [IKFilterBrowserFilterSelectedNotification](ikfilterbrowserfilterselectednotification.md) — Posted when the user clicks a filter name in the filter browser.
- [IKFilterBrowserFilterDoubleClickNotification](ikfilterbrowserfilterdoubleclicknotification.md) — Posted when the user double-clicks a filter in the filter browser.
