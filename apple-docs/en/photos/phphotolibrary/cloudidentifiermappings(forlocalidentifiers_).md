---
title: 'cloudIdentifierMappings(forLocalIdentifiers:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phphotolibrary/cloudidentifiermappings(forlocalidentifiers:)'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/cloudidentifiermappings(forlocalidentifiers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/cloudidentifiermappings%28forlocalidentifiers%3A%29.json'
content_hash: 'sha256:c362877285d46509'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# cloudIdentifierMappings(forLocalIdentifiers:)

<sub>Instance Method</sub>

Retrieves the cloud identifier mappings for the list of local identifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func cloudIdentifierMappings(forLocalIdentifiers localIdentifiers: [String]) -> [String : Result<PHCloudIdentifier, any Error>]
```

## Parameters

- `localIdentifiers` — A list of local identifiers for which to retrieve cloud identifiers mappings.

## Return Value

A dictionary that contains a map of local identifiers to their corresponding cloud mappings.

## Discussion

Retrieving cloud identifiers can be an expensive operation, so perform this lookup sparingly. Instead, work with local identifiers and perform mapping work at load and save points. Then store and share the cloud identifiers to make them available on other devices.

If the attempt to look up a cloud identifier fails, the error parameter indicates the reason.

## See Also

### Converting Between Local and iCloud Identifiers

- [localIdentifierMappings(for:)](<localidentifiermappings(for_).md>) — Retrieves the local identifier mappings for the list of cloud identifiers.
- [PHCloudIdentifier](../phcloudidentifier.md) — An object that identifies an asset or collection that syncs through iCloud Photos.
- [- cloudIdentifiersForLocalIdentifiers:](<cloudidentifiers(forlocalidentifiers_).md>) — Retrieves the equivalent iCloud identifiers for the list of local identifiers. _(deprecated)_
- [- localIdentifiersForCloudIdentifiers:](<localidentifiers(for_).md>) — Retrieves the equivalent local identifiers for the list of iCloud identifiers. _(deprecated)_
- [PHLocalIdentifierNotFound](../phlocalidentifiernotfound.md) — A constant value that indicates that the system can’t resolve a local object from a global identifier. _(deprecated)_
