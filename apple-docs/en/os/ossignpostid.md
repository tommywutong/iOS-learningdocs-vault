---
title: OSSignpostID
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/ossignpostid
source_url: 'https://developer.apple.com/documentation/os/ossignpostid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignpostid.json'
content_hash: 'sha256:f00bee167b4e9bf3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# OSSignpostID

<sub>Structure</sub>

An identifier that disambiguates signposted intervals.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct OSSignpostID
```

## Overview

Multiple intervals that have matching names, subsystems, and categories, and that exist in the same scope can be in-flight simultaneously. To match a pair of interval calls, you need to identify each interval with a unique signpost identifier. Use the first strategy in the list below that matches your use case:

- If identical intervals can never overlap, use the [exclusive](ossignpostid/exclusive.md) signpost ID.
- If you have data that uniquely identifies each instance of the measured task, create a signpost ID using the [init(_:)](<ossignpostid/init(__).md>) method. The value you provide must not match that of any of the system-defined signpost IDs.
- If you have an object that uniquely identifies a pair of interval calls, such as the object you’re measuring, create a signpost ID using the [makeSignpostID(from:)](<ossignposter/makesignpostid(from_).md>) method. Don’t use this method for signposts that cross process boundaries.
- Otherwise, create a signpost ID using the [makeSignpostID()](<ossignposter/makesignpostid().md>) method.

## Relationships

- **Conforms To**: [Comparable](../swift/comparable.md), [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting Signpost Identifiers

- [exclusive](ossignpostid/exclusive.md) — A signpost identifier that indicates no overlap among different signpost time intervals.
- [invalid](ossignpostid/invalid.md) — A signpost identifier that indicates an error.
- [null](ossignpostid/null.md) — A signpost identifier that indicates a disabled signpost.

### Creating a Signpost Identifier

- [init(_:)](<ossignpostid/init(__).md>) — Creates a signpost ID from an arbitrary 64-bit integer value.
- [init(log:)](<ossignpostid/init(log_).md>) — Creates a signpost ID for the specified log. _(deprecated)_
- [init(log:object:)](<ossignpostid/init(log_object_).md>) — Creates a signpost ID and associates it with the specified object. _(deprecated)_

### Getting an Identifier’s Raw Value

- [rawValue](ossignpostid/rawvalue.md) — The signpost ID’s raw value.

## See Also

### Generating Signpost IDs

- [makeSignpostID()](<ossignposter/makesignpostid().md>) — Returns an identifier that’s unique within the scope of the signposter.
- [makeSignpostID(from:)](<ossignposter/makesignpostid(from_).md>) — Returns an identifier that the signposter derives from the specified object.
