---
title: OS_ACTIVITY_CURRENT
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_current
source_url: 'https://developer.apple.com/documentation/os/os_activity_current'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_current.json'
content_hash: 'sha256:f8f32de6205c7fb6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# OS_ACTIVITY_CURRENT

<sub>Macro</sub>

A special value that selects the current activity, if there is one.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define OS_ACTIVITY_CURRENT
```

## Discussion

When creating a new activity, pass this value as the activity’s parent to create the new activity with the current activity as its parent. If there is no active activity, the creation function returns the new activity as a top-level activity without a parent.

## See Also

### Choosing a Special Activity

- [OS_ACTIVITY_NONE](os_activity_none.md) — A special value that indicates a nonexistent activity.
