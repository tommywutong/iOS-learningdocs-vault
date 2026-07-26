---
title: 'nextAvailableURLs(withPathExtensions:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avexternalstoragedevice/nextavailableurls(withpathextensions:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice/nextavailableurls(withpathextensions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalstoragedevice/nextavailableurls%28withpathextensions%3A%29.json'
content_hash: 'sha256:093a1746dff5d113'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExternalStorageDevice](../avexternalstoragedevice.md)

# nextAvailableURLs(withPathExtensions:)

<sub>Instance Method</sub>

Generates an array of security scoped URLs that are compliant for digital camera formats, where each element has a different path extension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func nextAvailableURLs(withPathExtensions extensionArray: [String]) throws -> [URL]
```

## Parameters

- `extensionArray` — An array of path extensions the method generates URLs for.

## Return Value

An array of digital camera format (DCF) compliant URLs with security scoping, one for each path extension element in `extensionArray`.

## Discussion

The method generates a digital camera format (DCF) compliant URL with security scoping for each file extension element in `extensionArray`. It does this by configuring the folder structure and, if necessary, creates a digital camera image (DCIM) folder on the external storage device.

> [!important] Important
> The method generates an error if [authorizationStatus](authorizationstatus.md) isn’t [AVAuthorizationStatusAuthorized](../avauthorizationstatus/authorized.md).

### Request access to the storage device before request

Your app can request authorization before calling the method if [authorizationStatus](authorizationstatus.md) is [AVAuthorizationStatusNotDetermined](../avauthorizationstatus/notdetermined.md) by calling the [+ requestAccessWithCompletionHandler:](<requestaccess(completionhandler_).md>) method first.

### Start and stop access to a URL around your code

To access one of the security-scoped URLs the method returns, you need to call the [startAccessingSecurityScopedResource()](<../../foundation/url/startaccessingsecurityscopedresource().md>), and [stopAccessingSecurityScopedResource()](<../../foundation/url/stopaccessingsecurityscopedresource().md>) methods before and after your code.

**Swift**

```swift
securityScopedURL.startAccessingSecurityScopedResource()

// Your code that accesses the URL goes in between the start and stop calls.
...

securityScopedURL.stopAccessingSecurityScopedResource()
```

**Objective-C**

```objc
[securityScopedURL startAccessingSecurityScopedResource];

// Your code that accesses the URL goes in between the start and stop calls.
...

[securityScopedURL stopAccessingSecurityScopedResource];

```
