---
title: OS_ACTIVITY_FLAG_IF_NONE_PRESENT
framework: os
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_flag_t/os_activity_flag_if_none_present
source_url: 'https://developer.apple.com/documentation/os/os_activity_flag_t/os_activity_flag_if_none_present'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_flag_t/os_activity_flag_if_none_present.json'
content_hash: 'sha256:5c32b336638dfdeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [os_activity_flag_t](../os_activity_flag_t.md)

# OS_ACTIVITY_FLAG_IF_NONE_PRESENT

<sub>Enumeration Case</sub>

Creates a new activity only if one is not already present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_ACTIVITY_FLAG_IF_NONE_PRESENT
```

## Discussion

When you include this flag when calling a function that creates an activity, if an activity already exists, the function returns that activity. Otherwise, the function creates and returns a new activity.

Don’t pass [OS_ACTIVITY_FLAG_DETACHED](os_activity_flag_detached.md) and [OS_ACTIVITY_FLAG_IF_NONE_PRESENT](os_activity_flag_if_none_present.md) at the same time.

## See Also

### Adjusting Activity Creation

- [OS_ACTIVITY_FLAG_DEFAULT](os_activity_flag_default.md) — Creates a new activity and associates it as a child of any provided parent activity.
- [OS_ACTIVITY_FLAG_DETACHED](os_activity_flag_detached.md) — Creates a new activity that is independent of any provided parent activity.
