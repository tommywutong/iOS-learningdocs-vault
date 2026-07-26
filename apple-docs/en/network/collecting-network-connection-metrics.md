---
title: Collecting Network Connection Metrics
framework: Network
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, Xcode 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/collecting-network-connection-metrics
source_url: 'https://developer.apple.com/documentation/network/collecting-network-connection-metrics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/collecting-network-connection-metrics.json'
content_hash: 'sha256:a7833c3e0e51f45c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md) · [NWConnection](nwconnection.md)

# Collecting Network Connection Metrics

<sub>Sample Code</sub>

Use reports to understand how DNS and protocol handshakes impact connection establishment.

## Overview

> [!note] Note
> This sample code project is associated with WWDC 2019 session [713: Advances in Networking, Part 2](https://developer.apple.com/videos/play/wwdc19/713/).

## See Also

### Collecting Connection Metrics

- [requestEstablishmentReport(queue:completion:)](<nwconnection/requestestablishmentreport(queue_completion_).md>) — Requests a copy of the connection’s establishment report once the connection is in the ready state.
- [EstablishmentReport](nwconnection/establishmentreport.md) — A report that provides metrics about the establishment of a connection.
- [startDataTransferReport()](<nwconnection/startdatatransferreport().md>) — Begins a new data transfer report, which can later be collected.
- [PendingDataTransferReport](nwconnection/pendingdatatransferreport.md) — An outstanding data transfer report that has yet to be collected.
- [DataTransferReport](nwconnection/datatransferreport.md) — A report that provides metrics about data being sent and received on a connection.

## Download

- [CollectingNetworkConnectionMetrics.zip](https://docs-assets.developer.apple.com/published/017625187506/CollectingNetworkConnectionMetrics.zip)
