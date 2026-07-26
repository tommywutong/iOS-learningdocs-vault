---
title: 'resetTextureAccessCounters(_:region:mipLevel:slice:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（26.4 起废弃）, iPadOS 13.0+（26.4 起废弃）, Mac Catalyst 14.0+（26.4 起废弃）, macOS 11.0+（26.4 起废弃）, tvOS 16.0+（26.4 起废弃）, visionOS 1.0+（26.4 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlblitcommandencoder/resettextureaccesscounters(_:region:miplevel:slice:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/resettextureaccesscounters(_:region:miplevel:slice:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/resettextureaccesscounters%28_%3Aregion%3Amiplevel%3Aslice%3A%29.json'
content_hash: 'sha256:93ff6f18c0779fde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# resetTextureAccessCounters(_:region:mipLevel:slice:)

<sub>Instance Method</sub>

Encodes a command that resets a sparse texture’s access data for a specific region, mipmap level, and slice.

> [!warning] Deprecated
> Access counters are no longer supported in Metal

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func resetTextureAccessCounters(_ texture: any MTLTexture, region: MTLRegion, mipLevel: Int, slice: Int)
```

<sub>Mac Catalyst, macOS</sub>

```swift
optional func resetTextureAccessCounters(_ texture: any MTLTexture, region: MTLRegion, mipLevel: Int, slice: Int)
```

## Parameters

- `texture` — A sparse texture instance.

- `region` — A region within the sparse texture’s `mipLevel`, in sparse tile coordinates.

- `mipLevel` — A mipmap level within the sparse texture.

- `slice` — A slice within the sparse texture.

## See Also

### Managing sparse texture access counters

- [- getTextureAccessCounters:region:mipLevel:slice:resetCounters:countersBuffer:countersBufferOffset:](<gettextureaccesscounters(__region_miplevel_slice_resetcounters_countersbuffer_countersbufferoffset_).md>) — Encodes a command that retrieves a sparse texture’s access data for a specific region, mipmap level, and slice. _(deprecated)_
