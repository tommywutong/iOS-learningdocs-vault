---
title: 'init(contentsOf:error:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsapplescript/init(contentsof:error:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsapplescript/init(contentsof:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsapplescript/init%28contentsof%3Aerror%3A%29.json'
content_hash: 'sha256:f19f983a929b852a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleScript](../nsapplescript.md)

# init(contentsOf:error:)

<sub>Initializer</sub>

Initializes a newly allocated script instance from the source identified by the passed URL.

<sub>Mac Catalyst, macOS</sub>

```swift
init?(contentsOf url: URL, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

## Parameters

- `url` — A URL that locates a script, in either text or compiled form.

- `errorInfo` — On return, if an error occurs, a pointer to an error information dictionary.

## Return Value

The initialized script object, `nil` if an error occurs.

## Discussion

This method is a designated initializer for `NSAppleScript`.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

### Initializing a Script

- [- initWithSource:](<init(source_).md>) — Initializes a newly allocated script instance from the passed source.
