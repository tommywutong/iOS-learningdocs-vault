---
title: CIAreaAverageMaximumRed
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciareaaveragemaximumred
source_url: 'https://developer.apple.com/documentation/coreimage/ciareaaveragemaximumred'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciareaaveragemaximumred.json'
content_hash: 'sha256:c3b414ffacaac18c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIAreaAverageMaximumRed

<sub>Protocol</sub>

The protocol for the Area Average and Maximum Red filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIAreaAverageMaximumRed : CIAreaReductionFilter
```

## Overview

Calculates the average and maximum red component value for the specified area in an image. The result is returned in the red and green channels of a one pixel image.

## Relationships

- **Inherits From**: [CIAreaReductionFilter](ciareareductionfilter.md), [CIFilterProtocol](cifilterprotocol.md)
