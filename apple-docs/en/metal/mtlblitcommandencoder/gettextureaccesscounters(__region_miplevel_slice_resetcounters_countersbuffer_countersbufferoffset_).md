---
title: 'getTextureAccessCounters(_:region:mipLevel:slice:resetCounters:countersBuffer:countersBufferOffset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（26.4 起废弃）, iPadOS 13.0+（26.4 起废弃）, Mac Catalyst 14.0+（26.4 起废弃）, macOS 11.0+（26.4 起废弃）, tvOS 16.0+（26.4 起废弃）, visionOS 1.0+（26.4 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlblitcommandencoder/gettextureaccesscounters(_:region:miplevel:slice:resetcounters:countersbuffer:countersbufferoffset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/gettextureaccesscounters(_:region:miplevel:slice:resetcounters:countersbuffer:countersbufferoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/gettextureaccesscounters%28_%3Aregion%3Amiplevel%3Aslice%3Aresetcounters%3Acountersbuffer%3Acountersbufferoffset%3A%29.json'
content_hash: 'sha256:75b0ec0bbd41dd73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# getTextureAccessCounters(_:region:mipLevel:slice:resetCounters:countersBuffer:countersBufferOffset:)

<sub>Instance Method</sub>

Encodes a command that retrieves a sparse texture’s access data for a specific region, mipmap level, and slice.

> [!warning] Deprecated
> Access counters are no longer supported in Metal

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func getTextureAccessCounters(_ texture: any MTLTexture, region: MTLRegion, mipLevel: Int, slice: Int, resetCounters: Bool, countersBuffer: any MTLBuffer, countersBufferOffset: Int)
```

<sub>Mac Catalyst, macOS</sub>

```swift
optional func getTextureAccessCounters(_ texture: any MTLTexture, region: MTLRegion, mipLevel: Int, slice: Int, resetCounters: Bool, countersBuffer: any MTLBuffer, countersBufferOffset: Int)
```

## Parameters

- `texture` — A sparse texture instance.

- `region` — A region within the sparse texture’s `mipLevel`, in sparse tile coordinates.

- `mipLevel` — A mipmap level within the sparse texture.

- `slice` — A slice within the sparse texture.

- `resetCounters` — A Boolean value that indicates whether the command resets the counters after it completes.

- `countersBuffer` — A destination buffer where the command stores the sparse texture’s access counter data.

- `countersBufferOffset` — A starting offset, in bytes, within `countersBuffer` where the command writes the first byte of the sparse texture’s access counter data.

## Discussion

The GPU returns a counter for each sparse tile in the region you specify. Each counter is a [uint32_t](../../kernel/uint32_t.md) in row-major order. Provide space in the buffer for each counter you request.

When the GPU samples a texture and fails to find data in its internal caches, the GPU increments the access counter for the sparse tile. The GPU then attempts to fetch a new cache line from device memory that contains those pixels.

The counter doesn’t track memory operations to data that’s already in the GPU’s caches. You can ignore differences in cache line sizes or pixel formats because the GPU driver normalizes the access counts. Each count represents the number of pixels the GPU fetches into memory.

## See Also

### Managing sparse texture access counters

- [- resetTextureAccessCounters:region:mipLevel:slice:](<resettextureaccesscounters(__region_miplevel_slice_).md>) — Encodes a command that resets a sparse texture’s access data for a specific region, mipmap level, and slice. _(deprecated)_
