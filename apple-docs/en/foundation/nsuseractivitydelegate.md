---
title: NSUserActivityDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivitydelegate
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivitydelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivitydelegate.json'
content_hash: 'sha256:d4fe145f645d0c77'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUserActivityDelegate

<sub>Protocol</sub>

The interface through which a user activity instance notifies its delegate of updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSUserActivityDelegate : NSObjectProtocol
```

## Overview

An object conforming to the [NSUserActivityDelegate](nsuseractivitydelegate.md) protocol works with an [NSUserActivity](nsuseractivity.md) object, which encapsulates the state of a user activity in an application on a particular device and enables the same activity to be continued on another device. For example, a user browsing an article in Safari on a Mac can move to an iOS device where the same webpage automatically opens in Safari with the same scroll position.

The user activity delegate is responsible for updating the state of an activity and is also notified when an activity has been continued on another device. The user activity delegate is typically a top-level object in the app—such as a window, view controller, or the app delegate—that manages the activity’s interaction with the app.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Handling streams

- [- userActivity:didReceiveInputStream:outputStream:](<nsuseractivitydelegate/useractivity(__didreceive_outputstream_).md>) — Notifies the user activity delegate that an input and output streams are available to open.

### Managing activity continuation

- [- userActivityWasContinued:](<nsuseractivitydelegate/useractivitywascontinued(__).md>) — Notifies the delegate that the user activity was continued on another device.
- [- userActivityWillSave:](<nsuseractivitydelegate/useractivitywillsave(__).md>) — Notifies the delegate that the user activity will be saved to be continued or persisted.

## See Also

### Host App Interaction

- [NSUserActivity](nsuseractivity.md) — A representation of the state of your app at a moment in time.
