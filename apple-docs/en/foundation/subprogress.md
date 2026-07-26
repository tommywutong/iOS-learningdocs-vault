---
title: Subprogress
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/foundation/subprogress
source_url: 'https://developer.apple.com/documentation/foundation/subprogress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/subprogress.json'
content_hash: 'sha256:f8e20dcaa8fe91ee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Subprogress

<sub>Structure</sub>

Subprogress is used to establish parent-child relationship between two instances of `ProgressManager`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Subprogress
```

## Overview

Subprogress is returned from a call to `subprogress(assigningCount:)` by a parent ProgressManager. A child ProgressManager is then returned by calling `start(totalCount:)` on a Subprogress.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Methods

- [start(totalCount:)](<subprogress/start(totalcount_).md>) — Instantiates a ProgressManager which is a child to the parent from which `self` is returned. _(beta)_
