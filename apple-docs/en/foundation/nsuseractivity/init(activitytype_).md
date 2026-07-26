---
title: 'init(activityType:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuseractivity/init(activitytype:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/init(activitytype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/init%28activitytype%3A%29.json'
content_hash: 'sha256:672f74fb2da586f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# init(activityType:)

<sub>Initializer</sub>

Creates a user activity object with the specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(activityType: String)
```

## Parameters

- `activityType` — The type of the activity. The value is a developer-defined string in reverse-DNS format by convention, for example, `com.myCompany.myEditor.editing`.

## Return Value

An [NSUserActivity](../nsuseractivity.md) object.

## See Also

### Related Documentation

- [Handoff Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Handoff/HandoffFundamentals/HandoffFundamentals.html#//apple_ref/doc/uid/TP40014338)
