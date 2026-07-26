---
title: OS_ACTIVITY_NONE
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_none
source_url: 'https://developer.apple.com/documentation/os/os_activity_none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_none.json'
content_hash: 'sha256:1513259a1b2cead1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# OS_ACTIVITY_NONE

<sub>Macro</sub>

A special value that indicates a nonexistent activity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define OS_ACTIVITY_NONE
```

## Discussion

When creating a new activity, pass this value as the activity’s parent to create the new activity as a top-level activity without a parent.

## See Also

### Choosing a Special Activity

- [OS_ACTIVITY_CURRENT](os_activity_current.md) — A special value that selects the current activity, if there is one.
