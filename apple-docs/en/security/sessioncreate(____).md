---
title: 'SessionCreate(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sessioncreate(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sessioncreate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sessioncreate%28_%3A_%3A%29.json'
content_hash: 'sha256:bfeb4523c736ad53'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SessionCreate(_:_:)

<sub>Function</sub>

Creates a security session.

<sub>Mac Catalyst, macOS</sub>

```swift
func SessionCreate(_ flags: SessionCreationFlags, _ attributes: SessionAttributeBits) -> OSStatus
```

## Parameters

- `flags` — Flags controlling how the session is created. See [SessionCreationFlags](sessioncreationflags.md) for valid values.

- `attributes` — The set of attribute bits to set for the new session. Not all bits can be set this way. See [SessionAttributeBits](sessionattributebits.md) for valid values.

## Return Value

A result code. See [Sessions API Result Codes](sessions-api-result-codes.md).

## Discussion

Upon completion, the new session contains the calling process (and none other). You can’t create a session for someone else, and can’t avoid being placed into the new session. This is (currently) the only call that changes a process’s session membership.

By default, a new bootstrap subset port is created for the calling process. The process acquires this new port as its bootstrap port, which all its children will inherit. If you happen to have created the subset port on your own, you can pass the [sessionKeepCurrentBootstrap](sessioncreationflags/sessionkeepcurrentbootstrap.md) flag, and [SessionCreate](<sessioncreate(____).md>) will use it. Note however that you cannot supersede a prior [SessionCreate](<sessioncreate(____).md>) call that way; only a single [SessionCreate](<sessioncreate(____).md>) call is allowed for each session (however made).

This call will discard any security information established for the calling process. In particular, any authorization handles acquired will become invalid, and so will any keychain related information. Call [SessionCreate](<sessioncreate(____).md>) before making any other security-related calls that establish rights of any kind, to the extent this is practical. Also, do not perform security-related calls in any other threads while calling [SessionCreate](<sessioncreate(____).md>).
