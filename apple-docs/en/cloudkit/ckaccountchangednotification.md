---
title: CKAccountChangedNotification
framework: CloudKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/cloudkit/ckaccountchangednotification
source_url: 'https://developer.apple.com/documentation/cloudkit/ckaccountchangednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cloudkit/ckaccountchangednotification.json'
content_hash: 'sha256:437e42e54a8c6062'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [CloudKit](../cloudkit.md)

# CKAccountChangedNotification

<sub>Global Variable</sub>

A notification that a container posts when the status of an iCloud account changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSString * const CKAccountChangedNotification;
```

## Discussion

Create an instance of [CKContainer](ckcontainer.md) to receive this notification. The container posts the notification using an arbitrary queue. Use the [- accountStatusWithCompletionHandler:](<ckcontainer/accountstatus(completionhandler_).md>) method to obtain the account’s status.

## See Also

### Accessing Container Metadata

- [- fetchShareMetadataWithURL:completionHandler:](<ckcontainer/fetchsharemetadata(with_completionhandler_).md>) — Fetches the share metadata for the specified share URL.
- [- acceptShareMetadata:completionHandler:](<ckcontainer/accept(__completionhandler_)-949ea.md>) — Accepts the specified share metadata.
