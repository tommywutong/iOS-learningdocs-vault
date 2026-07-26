---
title: Publishers.Breakpoint
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/breakpoint
source_url: 'https://developer.apple.com/documentation/combine/publishers/breakpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/breakpoint.json'
content_hash: 'sha256:39910cc77662dc5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Breakpoint

<sub>Structure</sub>

A publisher that raises a debugger signal when a provided closure needs to stop the process in the debugger.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Breakpoint<Upstream> where Upstream : Publisher
```

## Overview

When any of the provided closures returns `true`, this publisher raises the `SIGTRAP` signal to stop the process in the debugger. Otherwise, this publisher passes through values and completions as-is.

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a breakpoint publisher

- [init(upstream:receiveSubscription:receiveOutput:receiveCompletion:)](<breakpoint/init(upstream_receivesubscription_receiveoutput_receivecompletion_).md>) — Creates a breakpoint publisher with the provided upstream publisher and breakpoint-raising closures.

### Declaring supporting types

- [Output](breakpoint/output.md) — The kind of values published by this publisher.
- [Failure](breakpoint/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](breakpoint/upstream.md) — The publisher from which this publisher receives elements.
- [receiveSubscription](breakpoint/receivesubscription.md) — A closure that executes when the publisher receives a subscription, and can raise a debugger signal by returning a true Boolean value.
- [receiveOutput](breakpoint/receiveoutput.md) — A closure that executes when the publisher receives output from the upstream publisher, and can raise a debugger signal by returning a true Boolean value.
- [receiveCompletion](breakpoint/receivecompletion.md) — A closure that executes when the publisher receives completion, and can raise a debugger signal by returning a true Boolean value.

## See Also

### Debugging

- [HandleEvents](handleevents.md) — A publisher that performs the specified closures when publisher events occur.
- [Print](print.md) — A publisher that prints log messages for all publishing events, optionally prefixed with a given string.
