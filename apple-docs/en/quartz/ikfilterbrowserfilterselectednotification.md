---
title: IKFilterBrowserFilterSelectedNotification
framework: Quartz
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.4+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/quartz/ikfilterbrowserfilterselectednotification
source_url: 'https://developer.apple.com/documentation/quartz/ikfilterbrowserfilterselectednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartz/ikfilterbrowserfilterselectednotification.json'
content_hash: 'sha256:8025a7824ddd5e28'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Quartz](../quartz.md)

# IKFilterBrowserFilterSelectedNotification

<sub>Global Variable</sub>

Posted when the user clicks a filter name in the filter browser.

<sub>macOS</sub>

```objc
extern NSString * const IKFilterBrowserFilterSelectedNotification;
```

## Discussion

The name of the selected filter is sent as the object in the notification.

## See Also

### Notifications

- [IKFilterBrowserWillPreviewFilterNotification](ikfilterbrowserwillpreviewfilternotification.md) — Posted before showing a filter preview, allowing an application to set the parameters of a filter.
- [IKFilterBrowserFilterDoubleClickNotification](ikfilterbrowserfilterdoubleclicknotification.md) — Posted when the user double-clicks a filter in the filter browser.
