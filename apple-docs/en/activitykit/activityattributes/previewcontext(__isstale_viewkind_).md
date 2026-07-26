---
title: 'previewContext(_:isStale:viewKind:)'
framework: ActivityKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.2+, iPadOS 16.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/activitykit/activityattributes/previewcontext(_:isstale:viewkind:)'
source_url: 'https://developer.apple.com/documentation/activitykit/activityattributes/previewcontext(_:isstale:viewkind:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activityattributes/previewcontext%28_%3Aisstale%3Aviewkind%3A%29.json'
content_hash: 'sha256:061124fa98a0fdbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [ActivityAttributes](../activityattributes.md)

# previewContext(_:isStale:viewKind:)

<sub>Instance Method</sub>

Generates a preview for a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func previewContext(_ contentState: Self.ContentState, isStale: Bool = false, viewKind: ActivityPreviewViewKind) -> some View

```

## Parameters

- `contentState` — The dynamic content of the Live Activity.

- `isStale` — A Boolean that indicates whether the content of a Live Activity is out of date.

- `viewKind` — A value that determines which Live Activity presentation to render for this preview.
