---
title: NSStorePathKey
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.6+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coredata/nsstorepathkey
source_url: 'https://developer.apple.com/documentation/coredata/nsstorepathkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsstorepathkey.json'
content_hash: 'sha256:193231a216161d27'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSStorePathKey

<sub>Global Variable</sub>

Dictionary key for the store path (an instance of `NSURL`) extracted from an external record file.

> [!warning] Deprecated
> Spotlight integration is deprecated. Use CoreSpotlight integration instead.

<sub>macOS</sub>

```swift
let NSStorePathKey: String
```

## Discussion

This is resolved to the store-file path contained in the an external record file directory.

## See Also

### Constants

- [NSEntityNameInPathKey](nsentitynameinpathkey.md) — Dictionary key for the entity name extracted from an external record file. _(deprecated)_
- [NSStoreUUIDInPathKey](nsstoreuuidinpathkey.md) — Dictionary key for the store UUID extracted from an external record file. _(deprecated)_
- [NSModelPathKey](nsmodelpathkey.md) — Dictionary key for the managed object model path (an instance of `NSURL`) extracted from an external record file. _(deprecated)_
- [NSObjectURIKey](nsobjecturikey.md) — Dictionary key for the object URI extracted from an external record file. _(deprecated)_
