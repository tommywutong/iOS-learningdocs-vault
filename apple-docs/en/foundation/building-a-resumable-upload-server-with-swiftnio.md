---
title: Building a resumable upload server with SwiftNIO
framework: Foundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/building-a-resumable-upload-server-with-swiftnio
source_url: 'https://developer.apple.com/documentation/foundation/building-a-resumable-upload-server-with-swiftnio'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/building-a-resumable-upload-server-with-swiftnio.json'
content_hash: 'sha256:e53d65532e02a93a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md)

# Building a resumable upload server with SwiftNIO

<sub>Sample Code</sub>

Support HTTP resumable upload protocol in SwiftNIO by translating resumable uploads to regular uploads.

## Overview

> [!note] Note
> This sample code project is associated with WWDC23 session 10006: [Build robust and resumable file transfers](https://developer.apple.com/wwdc23/10006/).

### Configure the sample code project

Before you run the sample code project:

1. In the `Package.swift` file of an existing HTTP server project, add `.package(path: "/path/to/swift-nio-resumable-upload")` as one of the dependencies.
2. Import `NIOResumableUpload` in your SwiftNIO bootstrapping code.
3. Create an upload context: `let uploadContext = HTTPResumableUploadContext(origin: "https://example.com")`.
4. Wrap your HTTP server channel handler within `HTTPResumableUploadHandler`.

## See Also

### Uploading

- [Uploading data to a website](uploading-data-to-a-website.md) — Post data from your app to servers.
- [Uploading streams of data](uploading-streams-of-data.md) — Send a stream of data to a server.
- [Pausing and resuming uploads](pausing-and-resuming-uploads.md) — Pause and resume an upload without starting over, even when the connection is interrupted.

## Download

- [BuildingAResumableUploadServerWithSwiftNIO.zip](https://docs-assets.developer.apple.com/published/eecdd62f298f/BuildingAResumableUploadServerWithSwiftNIO.zip)
