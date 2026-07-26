---
title: os_activity_get_identifier
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_get_identifier
source_url: 'https://developer.apple.com/documentation/os/os_activity_get_identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_get_identifier.json'
content_hash: 'sha256:7cfff765415a04ab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_activity_get_identifier

<sub>Function</sub>

Retrieves the identifier for a given activity object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern os_activity_id_t os_activity_get_identifier(os_activity_t activity, os_activity_id_t *parent_id);
```

## Parameters

- `activity` — The activity to be identified.

- `parent_id` — On return, contains the identifier of the parent of the activity object, if any. Pass `NULL` if you don’t need this identifier.

## Return Value

The current activity identifier.

## See Also

### Retrieving an Activity Identifier

- [os_activity_id_t](os_activity_id_t.md) — A number that uniquely identifies an activity.
