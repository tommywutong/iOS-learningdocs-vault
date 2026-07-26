---
title: SWHighlightCenter
framework: Shared with You
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/sharedwithyou/swhighlightcenter
source_url: 'https://developer.apple.com/documentation/sharedwithyou/swhighlightcenter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/sharedwithyou/swhighlightcenter.json'
content_hash: 'sha256:54a6fa95a0efc5ce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Shared with You](../sharedwithyou.md)

# SWHighlightCenter

<sub>Class</sub>

An object that contains a priority-ordered list of universal links to share with the current user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class SWHighlightCenter
```

## Overview

The system determines which links it surfaces. The app is responsible for updating its UI to reflect the latest highlights list that the system provides.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Setting the delegate

- [delegate](swhighlightcenter/delegate.md) — The delegate object for the highlight center.
- [SWHighlightCenterDelegate](swhighlightcenterdelegate.md) — The protocol you use to notify the delegate when the list or rank order of surfaced highlights changes.

### Accessing highlights

- [highlights](swhighlightcenter/highlights.md) — An array of shared highlights.
- [highlightCollectionTitle](swhighlightcenter/highlightcollectiontitle.md) — A localized title to display with a collection of highlights.

### Retrieving collaboration highlights

- [systemCollaborationSupportAvailable](swhighlightcenter/issystemcollaborationsupportavailable.md) — A Boolean value that represents full support for Messages collaboration features.
- [- collaborationHighlightForIdentifier:error:](<swhighlightcenter/collaborationhighlight(foridentifier_)-23ytv.md>) — Returns a collaboration highlight for a specified collaboration identifier.
- [collaborationHighlight(forIdentifier:)](<swhighlightcenter/collaborationhighlight(foridentifier_)-87lhr.md>) — Returns a collaboration highlight for a specified identifier string.
- [- getCollaborationHighlightForURL:completionHandler:](<swhighlightcenter/getcollaborationhighlight(for_completionhandler_).md>) — Returns a collaboration highlight for a specified URL.
- [- getHighlightForURL:completionHandler:](<swhighlightcenter/gethighlightfor(__completionhandler_).md>) — Returns a highlight for a specified URL.
- [- getSignedIdentityProofForCollaborationHighlight:usingData:completionHandler:](<swhighlightcenter/getsignedidentityproof(for_using_completionhandler_).md>) — Signs passed-in data with the local device’s private key.

### Posting highlight events

- [- postNoticeForHighlightEvent:](<swhighlightcenter/postnotice(for_).md>) — Posts a specified event to the highlight center for display.
- [- clearNoticesForHighlight:](<swhighlightcenter/clearnotices(for_).md>) — Clears the notices for a specified collaboration highlight.

### Handling errors

- [SWHighlightCenterErrorCode](swhighlightcentererrorcode.md) — The error codes for the highlight center.

## See Also

### Highlights

- [SWHighlight](swhighlight.md) — An object that represents a universal link to share by any number of contacts in one or more conversations.
