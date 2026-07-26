---
title: 'exportedAssetID(for:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/photos/phassetresourcemanager/exportedassetid(for:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcemanager/exportedassetid(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcemanager/exportedassetid%28for%3A%29.json'
content_hash: 'sha256:cd53c22f0dc14f6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceManager](../phassetresourcemanager.md)

# exportedAssetID(for:)

<sub>Instance Method</sub>

Returns the exported asset ID for the specified asset resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func exportedAssetID(for resource: PHAssetResource) async throws -> CKAsset.ExportedAssetID
```

## Parameters

- `resource` — The asset resource to get an exported asset ID for.

## Return Value

The exported asset ID for the resource.

## Discussion

The returned `CKAsset.ExportedAssetID` can be used to create a `CKAsset` that references the asset resource data without copying it. Network access is required; the request will fail if the resource cannot be resolved in CloudKit. Only resources belonging to `PHAssetResource.TypeGroup.coreComponents` are valid. The photo library must be cloud-enabled; requests against a local-only library will fail with `PHPhotosError.requestNotSupportedForAsset`.

This method supports task cancellation. If the calling task is cancelled, the underlying network request is cancelled and this method throws `CancellationError`.

> [!danger] Throws
> `CancellationError` if the task is cancelled, or another error if the request fails.
