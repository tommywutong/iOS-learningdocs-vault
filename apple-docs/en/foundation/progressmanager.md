---
title: ProgressManager
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/foundation/progressmanager
source_url: 'https://developer.apple.com/documentation/foundation/progressmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressmanager.json'
content_hash: 'sha256:9838f186bf4deff7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# ProgressManager

<sub>Class</sub>

An object that conveys ongoing progress to the user for a specified task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@dynamicMemberLookup final class ProgressManager
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Observable](../observation/observable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Protocols

- [Property](progressmanager/property.md) — A type that conveys additional task-specific information on progress. _(beta)_

### Initializers

- [init(totalCount:)](<progressmanager/init(totalcount_).md>) — Initializes `self` with `totalCount`. _(beta)_

### Instance Properties

- [completedCount](progressmanager/completedcount.md) — The completed units of work. _(beta)_
- [fractionCompleted](progressmanager/fractioncompleted.md) — The proportion of work completed. This takes into account the fraction completed in its children instances if children are present. If `self` is indeterminate, the value will be 0.0. _(beta)_
- [isFinished](progressmanager/isfinished.md) — The state of completion of work. If `completedCount` \>= `totalCount`, the value will be `true`. _(beta)_
- [isIndeterminate](progressmanager/isindeterminate.md) — The state of initialization of `totalCount`. If `totalCount` is `nil`, the value will be `true`. _(beta)_
- [reporter](progressmanager/reporter.md) — A `ProgressReporter` instance, used for providing read-only observation of progress updates or composing into other `ProgressManager`s. _(beta)_
- [totalCount](progressmanager/totalcount.md) — The total units of work. _(beta)_

### Instance Methods

- [assign(count:to:)](<progressmanager/assign(count_to_)-87zdf.md>) — Adds a Foundation’s `Progress` instance as a child which constitutes a certain `count` of `self`’s `totalCount`. _(beta)_
- [assign(count:to:)](<progressmanager/assign(count_to_)-98a77.md>) — Adds a `ProgressReporter` as a child, with its progress representing a portion of `self`’s progress. _(beta)_
- [complete(count:)](<progressmanager/complete(count_).md>) — Increases `completedCount` by `count`. _(beta)_
- [setCounts(_:)](<progressmanager/setcounts(__).md>) _(beta)_
- [subprogress(assigningCount:)](<progressmanager/subprogress(assigningcount_).md>) — Returns a `Subprogress` representing a portion of `self` which can be passed to any method that reports progress. _(beta)_
- [summary(of:)](<progressmanager/summary(of_)-3kyy8.md>) — Returns a summary for a custom URL property across the progress subtree. _(beta)_
- [summary(of:)](<progressmanager/summary(of_)-3r60q.md>) — Returns a summary for a custom integer property across the progress subtree. _(beta)_
- [summary(of:)](<progressmanager/summary(of_)-3voby.md>) — Returns a summary for a custom double property across the progress subtree. _(beta)_
- [summary(of:)](<progressmanager/summary(of_)-73lzs.md>) — Returns a summary for a custom duration property across the progress subtree. _(beta)_
- [summary(of:)](<progressmanager/summary(of_)-7jb53.md>) — Returns a summary for a custom unsigned integer property across the progress subtree. _(beta)_
- [summary(of:)](<progressmanager/summary(of_)-bfr7.md>) — Returns a summary for a custom string property across the progress subtree. _(beta)_
- [summary(of:)](<progressmanager/summary(of_)-txm5.md>) — Returns a summary for a custom unsigned integer property across the progress subtree. _(beta)_

### Subscripts

- [subscript(dynamicMember:)](<progressmanager/subscript(dynamicmember_)-1qb7p.md>) — Gets or sets custom integer properties. _(beta)_
- [subscript(dynamicMember:)](<progressmanager/subscript(dynamicmember_)-5rh0j.md>) — Gets or sets custom string properties. _(beta)_
- [subscript(dynamicMember:)](<progressmanager/subscript(dynamicmember_)-5rw99.md>) — Gets or sets custom duration properties. _(beta)_
- [subscript(dynamicMember:)](<progressmanager/subscript(dynamicmember_)-62at9.md>) — Gets or sets custom double properties. _(beta)_
- [subscript(dynamicMember:)](<progressmanager/subscript(dynamicmember_)-7h16n.md>) — Gets or sets custom unsigned integer properties. _(beta)_
- [subscript(dynamicMember:)](<progressmanager/subscript(dynamicmember_)-7r4v2.md>) — Gets or sets custom URL properties. _(beta)_
- [subscript(dynamicMember:)](<progressmanager/subscript(dynamicmember_)-8tb3b.md>) — Gets or sets custom unsigned integer properties. _(beta)_

### Enumerations

- [Properties](progressmanager/properties.md) _(beta)_

### Default Implementations

- [CustomDebugStringConvertible Implementations](progressmanager/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](progressmanager/customstringconvertible-implementations.md)
- [Equatable Implementations](progressmanager/equatable-implementations.md)
