---
title: NSFileProviderDomainDidChange
framework: File Provider
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 11.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/fileprovider/nsfileproviderdomaindidchange
source_url: 'https://developer.apple.com/documentation/fileprovider/nsfileproviderdomaindidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/fileprovider/nsfileproviderdomaindidchange.json'
content_hash: 'sha256:a90774e2fd3b4928'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [File Provider](../fileprovider.md)

# NSFileProviderDomainDidChange

<sub>Global Variable</sub>

A notification that posts when a file provider’s domain changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```objc
extern NSNotificationName const NSFileProviderDomainDidChange;
```

## Discussion

The system only posts this notification after the first call to [+ getDomainsWithCompletionHandler:](<nsfileprovidermanager/getdomainswithcompletionhandler(__).md>). After receiving this notification, call [+ getDomainsWithCompletionHandler:](<nsfileprovidermanager/getdomainswithcompletionhandler(__).md>) again to determine what the changes are.

## See Also

### Global variables

- [NSFileProviderMaterializedSetDidChange](nsfileprovidermaterializedsetdidchange.md) — A notification that the system posts when the set of materialized items changes for your file provider extension.
- [NSFileProviderPendingSetDidChange](nsfileproviderpendingsetdidchange.md) — A notification that the system posts when the set of pending items changes for your file provider extension.
