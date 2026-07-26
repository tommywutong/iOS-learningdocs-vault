---
title: pathReports
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/datatransferreport/pathreports
source_url: 'https://developer.apple.com/documentation/network/nwconnection/datatransferreport/pathreports'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/datatransferreport/pathreports.json'
content_hash: 'sha256:f1e29f4344db4b18'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnection](../../nwconnection.md) · [DataTransferReport](../datatransferreport.md)

# pathReports

<sub>Instance Property</sub>

An array of reports for each network path the connection used.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let pathReports: [NWConnection.DataTransferReport.PathReport]
```

## See Also

### Examining Data Transfer

- [aggregatePathReport](aggregatepathreport.md) — A report that sums counts across all network paths.
- [PathReport](pathreport.md) — A report that contains details about data transfer over a single network path.
