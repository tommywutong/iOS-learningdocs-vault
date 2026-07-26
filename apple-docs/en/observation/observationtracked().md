---
title: ObservationTracked()
framework: Observation
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/observation/observationtracked()
source_url: 'https://developer.apple.com/documentation/observation/observationtracked()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/observation/observationtracked%28%29.json'
content_hash: 'sha256:5073851a385e2169'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Observation](../observation.md)

# ObservationTracked()

<sub>Macro</sub>

Synthesizes a property for accessors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@attached(accessor, names: named(init), named(get), named(set), named(_modify)) @attached(peer, names: prefixed(`_`)) macro ObservationTracked()
```

## Overview

The [Observation](../observation.md) module uses this macro. Its use outside of the framework isn’t necessary.
