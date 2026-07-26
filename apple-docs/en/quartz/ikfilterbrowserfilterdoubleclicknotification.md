---
title: IKFilterBrowserFilterDoubleClickNotification
framework: Quartz
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.4+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/quartz/ikfilterbrowserfilterdoubleclicknotification
source_url: 'https://developer.apple.com/documentation/quartz/ikfilterbrowserfilterdoubleclicknotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartz/ikfilterbrowserfilterdoubleclicknotification.json'
content_hash: 'sha256:201993c25b6bff43'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Quartz](../quartz.md)

# IKFilterBrowserFilterDoubleClickNotification

<sub>Global Variable</sub>

Posted when the user double-clicks a filter in the filter browser.

<sub>macOS</sub>

```objc
extern NSString * const IKFilterBrowserFilterDoubleClickNotification;
```

## Discussion

The name of the selected filter is send as the object in the notification.

## See Also

### Notifications

- [IKFilterBrowserWillPreviewFilterNotification](ikfilterbrowserwillpreviewfilternotification.md) — Posted before showing a filter preview, allowing an application to set the parameters of a filter.
- [IKFilterBrowserFilterSelectedNotification](ikfilterbrowserfilterselectednotification.md) — Posted when the user clicks a filter name in the filter browser.
