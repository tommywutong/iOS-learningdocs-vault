---
title: SecTransformNoData()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectransformnodata()
source_url: 'https://developer.apple.com/documentation/security/sectransformnodata()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformnodata%28%29.json'
content_hash: 'sha256:2a588abddc81f626'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformNoData()

<sub>Function</sub>

Returns an object from inside a ProcessData override that says that although no data is being returned the transform is still active and awaiting data.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecTransformNoData() -> CFTypeRef
```

## Return Value

A ‘special’ value that allows that specifies that the transform is still active and awaiting data.

## Discussion

The standard behavior for the ProcessData override is that it will receive a [CFData](../corefoundation/cfdata.md) object and it processes that data and returns another data object that contains the processed data. When there is no more data to process the ProcessData override block is called one last time with a `NULL` data reference. The ProcessData block should/must return the `NULL` data reference to complete the processing. This model does not work well for some transforms. For example a digest transform needs to see ALL of the data that is being digested before it can send out the digest value.

If a ProcessData block has no data to return, it can return [SecTransformNoData](<sectransformnodata().md>), which informs the transform system that there is no data to pass on to the next transform.
