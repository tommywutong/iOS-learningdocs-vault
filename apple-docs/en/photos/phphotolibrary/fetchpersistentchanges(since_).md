---
title: 'fetchPersistentChanges(since:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phphotolibrary/fetchpersistentchanges(since:)'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/fetchpersistentchanges(since:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/fetchpersistentchanges%28since%3A%29.json'
content_hash: 'sha256:747cc77214de0d3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# fetchPersistentChanges(since:)

<sub>Instance Method</sub>

Retrieves the Photos library changes since the token you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func fetchPersistentChanges(since token: PHPersistentChangeToken) throws -> PHPersistentChangeFetchResult
```

## Parameters

- `token` — The token that represents the state of the Photos library to compare against.

## Return Value

A fetch result that contains library change details; otherwise, an error that indicates why the fetch fails (for example, [PHPhotosErrorPersistentChangeTokenExpired](../phphotoserror-swift.struct/code/persistentchangetokenexpired.md)).

## See Also

### Fetching Change History

- [PHPersistentChangeFetchResult](../phpersistentchangefetchresult.md) — An object that represents a fetch result and allows you to enumerate a very large set of change records.
- [currentChangeToken](currentchangetoken.md) — The opaque token that represents the current state of the Photos library.
- [PHPersistentChangeToken](../phpersistentchangetoken.md) — An opaque object that tracks the state of the Photos library between runs, and that you can copy and serialize for future use.
