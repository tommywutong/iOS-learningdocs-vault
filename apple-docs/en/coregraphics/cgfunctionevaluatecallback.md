---
title: CGFunctionEvaluateCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfunctionevaluatecallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfunctionevaluatecallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfunctionevaluatecallback.json'
content_hash: 'sha256:ce91d1fa654b31ed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGFunctionEvaluateCallback

<sub>Type Alias</sub>

Performs custom operations on the supplied input data to produce output data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CGFunctionEvaluateCallback = (UnsafeMutableRawPointer?, UnsafePointer<CGFloat>, UnsafeMutablePointer<CGFloat>) -> Void
```

## Parameters

- `info` — The `info` parameter passed to [CGFunctionCreate](<cgfunction/init(info_domaindimension_domain_rangedimension_range_callbacks_).md>).

- `inData` — An array of floats. The size of the array is that specified by the `domainDimension` parameter passed to the [CGFunctionCreate](<cgfunction/init(info_domaindimension_domain_rangedimension_range_callbacks_).md>) function.

- `outData` — An array of floats. The size of the array is that specified by the `rangeDimension` parameter passed to the [CGFunctionCreate](<cgfunction/init(info_domaindimension_domain_rangedimension_range_callbacks_).md>) function.

## Discussion

The callback you write is responsible for implementing thecalculation of output values from the supplied input values. Forexample, if you want to implement a simple “squaring” functionof one input argument to one output argument, your evaluation functionmight be:

```objc
void evaluateSquare(void *info, const float *inData, float *outData)
{
    outData[0] = inData[0] * inData[0];
}
```

## See Also

### Callbacks

- [CGFunctionCallbacks](cgfunctioncallbacks.md) — A structure that contains callbacks needed by a `CGFunctionRef` object.
- [CGFunctionReleaseInfoCallback](cgfunctionreleaseinfocallback.md) — Performs custom clean-up tasks when Core Graphics deallocates a `CGFunctionRef` object.
