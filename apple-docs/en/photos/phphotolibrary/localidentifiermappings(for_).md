---
title: 'localIdentifierMappings(for:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phphotolibrary/localidentifiermappings(for:)'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/localidentifiermappings(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/localidentifiermappings%28for%3A%29.json'
content_hash: 'sha256:bbaf99aec6adde58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# localIdentifierMappings(for:)

<sub>Instance Method</sub>

Retrieves the local identifier mappings for the list of cloud identifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func localIdentifierMappings(for cloudIdentifiers: [PHCloudIdentifier]) -> [PHCloudIdentifier : Result<String, any Error>]
```

## Parameters

- `cloudIdentifiers` — A list of cloud identifiers for which to retrieve local identifier mappings.

## Return Value

A dictionary that contains a map of cloud identifiers to their corresponding local mappings.

## Discussion

Retrieving local identifiers can be an expensive operation, so perform this lookup sparingly. Instead, work with local identifiers and perform mapping work at load and save points. Then store and share the cloud identifiers to make them available on other devices.

If the attempt to look up a local identifier fails, the error parameter indicates the reason.

## See Also

### Converting Between Local and iCloud Identifiers

- [cloudIdentifierMappings(forLocalIdentifiers:)](<cloudidentifiermappings(forlocalidentifiers_).md>) — Retrieves the cloud identifier mappings for the list of local identifiers.
- [PHCloudIdentifier](../phcloudidentifier.md) — An object that identifies an asset or collection that syncs through iCloud Photos.
- [- cloudIdentifiersForLocalIdentifiers:](<cloudidentifiers(forlocalidentifiers_).md>) — Retrieves the equivalent iCloud identifiers for the list of local identifiers. _(deprecated)_
- [- localIdentifiersForCloudIdentifiers:](<localidentifiers(for_).md>) — Retrieves the equivalent local identifiers for the list of iCloud identifiers. _(deprecated)_
- [PHLocalIdentifierNotFound](../phlocalidentifiernotfound.md) — A constant value that indicates that the system can’t resolve a local object from a global identifier. _(deprecated)_
