---
title: CMSSignerStatus.needsDetachedContent
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/cmssignerstatus/needsdetachedcontent
source_url: 'https://developer.apple.com/documentation/security/cmssignerstatus/needsdetachedcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmssignerstatus/needsdetachedcontent.json'
content_hash: 'sha256:a5de94b8114355b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [CMSSignerStatus](../cmssignerstatus.md)

# CMSSignerStatus.needsDetachedContent

<sub>Case</sub>

The message was signed but has detached content. You must call the [CMSDecoderSetDetachedContent](<../cmsdecodersetdetachedcontent(____).md>) function before ascertaining the signature status.

<sub>Mac Catalyst, macOS</sub>

```swift
case needsDetachedContent
```
