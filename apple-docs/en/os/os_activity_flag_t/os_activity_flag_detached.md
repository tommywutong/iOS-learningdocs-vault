---
title: OS_ACTIVITY_FLAG_DETACHED
framework: os
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_flag_t/os_activity_flag_detached
source_url: 'https://developer.apple.com/documentation/os/os_activity_flag_t/os_activity_flag_detached'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_flag_t/os_activity_flag_detached.json'
content_hash: 'sha256:038fdd712c97d10d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [os_activity_flag_t](../os_activity_flag_t.md)

# OS_ACTIVITY_FLAG_DETACHED

<sub>Enumeration Case</sub>

Creates a new activity that is independent of any provided parent activity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_ACTIVITY_FLAG_DETACHED
```

## Discussion

When you set this flag when creating an activity, the system creates the activity as a new top-level activity. If you provided a parent activity, the new activity notes this fact, allowing you to see which activity triggered the new activity without actually relating the activities.

Don’t pass [OS_ACTIVITY_FLAG_DETACHED](os_activity_flag_detached.md) and [OS_ACTIVITY_FLAG_IF_NONE_PRESENT](os_activity_flag_if_none_present.md) at the same time.

## See Also

### Adjusting Activity Creation

- [OS_ACTIVITY_FLAG_DEFAULT](os_activity_flag_default.md) — Creates a new activity and associates it as a child of any provided parent activity.
- [OS_ACTIVITY_FLAG_IF_NONE_PRESENT](os_activity_flag_if_none_present.md) — Creates a new activity only if one is not already present.
