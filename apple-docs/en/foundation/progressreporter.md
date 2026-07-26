---
title: ProgressReporter
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/foundation/progressreporter
source_url: 'https://developer.apple.com/documentation/foundation/progressreporter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressreporter.json'
content_hash: 'sha256:f3005d9e84015006'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# ProgressReporter

<sub>Class</sub>

ProgressReporter is a wrapper for ProgressManager that carries information about ProgressManager.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@dynamicMemberLookup final class ProgressReporter
```

## Overview

It is read-only and can be added as a child of another ProgressManager.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Observable](../observation/observable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [completedCount](progressreporter/completedcount.md) — The completed units of work. If `self` is indeterminate, the value will be 0. _(beta)_
- [debugDescription](progressreporter/debugdescription.md) — A textual representation of the progress reporter suitable for debugging. _(beta)_
- [description](progressreporter/description.md) — A textual representation of the progress reporter. _(beta)_
- [fractionCompleted](progressreporter/fractioncompleted.md) — The proportion of work completed. This takes into account the fraction completed in its children instances if children are present. If `self` is indeterminate, the value will be 0. _(beta)_
- [isFinished](progressreporter/isfinished.md) — The state of completion of work. If `completedCount` \>= `totalCount`, the value will be `true`. _(beta)_
- [isIndeterminate](progressreporter/isindeterminate.md) — The state of initialization of `totalCount`. If `totalCount` is `nil`, the value will be `true`. _(beta)_
- [totalCount](progressreporter/totalcount.md) — The total units of work. _(beta)_

### Instance Methods

- [summary(of:)](<progressreporter/summary(of_)-2qbq7.md>) — Returns a summary for the specified unsigned integer array property across the progress subtree. _(beta)_
- [summary(of:)](<progressreporter/summary(of_)-4lsh2.md>) — Returns a summary for the specified double property across the progress subtree. _(beta)_
- [summary(of:)](<progressreporter/summary(of_)-5klzp.md>) — Returns a summary for the specified string property across the progress subtree. _(beta)_
- [summary(of:)](<progressreporter/summary(of_)-6x2a5.md>) — Returns a summary for the specified URL property across the progress subtree. _(beta)_
- [summary(of:)](<progressreporter/summary(of_)-7u7bg.md>) — Returns a summary for the specified integer property across the progress subtree. _(beta)_
- [summary(of:)](<progressreporter/summary(of_)-7xg8c.md>) — Returns a summary for the specified unsigned integer property across the progress subtree. _(beta)_
- [summary(of:)](<progressreporter/summary(of_)-vlsj.md>) — Returns a summary for the specified duration property across the progress subtree. _(beta)_

### Subscripts

- [subscript(dynamicMember:)](<progressreporter/subscript(dynamicmember_)-114si.md>) — Gets or sets custom string properties. _(beta)_
- [subscript(dynamicMember:)](<progressreporter/subscript(dynamicmember_)-1ubk6.md>) — Gets or sets custom unsigned integer properties. _(beta)_
- [subscript(dynamicMember:)](<progressreporter/subscript(dynamicmember_)-45eys.md>) — Gets or sets custom unsigned integer properties. _(beta)_
- [subscript(dynamicMember:)](<progressreporter/subscript(dynamicmember_)-84opo.md>) — Gets or sets custom URL properties. _(beta)_
- [subscript(dynamicMember:)](<progressreporter/subscript(dynamicmember_)-9fd3u.md>) — Gets or sets custom double properties. _(beta)_
- [subscript(dynamicMember:)](<progressreporter/subscript(dynamicmember_)-9pcsi.md>) — Gets or sets custom integer properties. _(beta)_
- [subscript(dynamicMember:)](<progressreporter/subscript(dynamicmember_)-cjlx.md>) — Gets or sets custom duration properties. _(beta)_

### Type Aliases

- [Property](progressreporter/property.md) _(beta)_
