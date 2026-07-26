---
title: Control the ray tracing process using intersection queries
framework: Metal
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, Xcode 26.3+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/control-the-ray-tracing-process-using-intersection-queries
source_url: 'https://developer.apple.com/documentation/metal/control-the-ray-tracing-process-using-intersection-queries'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/control-the-ray-tracing-process-using-intersection-queries.json'
content_hash: 'sha256:887797ad720fe395'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Metal sample code library](metal-sample-code-library.md)

# Control the ray tracing process using intersection queries

<sub>Sample Code</sub>

Explicitly enumerate a ray’s intersections with acceleration structures by creating an intersection query object.

## Overview

> [!note] Note
> This sample code project is associated with WWDC21 session [10149: Enhance Your App with Metal Ray Tracing](https://developer.apple.com/wwdc21/10149/).

## See Also

### Ray tracing

- [Rendering reflections in real time using ray tracing](rendering-reflections-in-real-time-using-ray-tracing.md) — Implement realistic real-time lighting by dynamically generating reflection maps by encoding a ray-tracing compute pass.
- [Accelerating ray tracing using Metal](accelerating-ray-tracing-using-metal.md) — Implement ray-traced rendering using GPU-based parallel processing.
- [Accelerating ray tracing and motion blur using Metal](accelerating-ray-tracing-and-motion-blur-using-metal.md) — Generate ray-traced images with motion blur using GPU-based parallel processing.
- [Rendering a curve primitive in a ray tracing scene](rendering-a-curve-primitive-in-a-ray-tracing-scene.md) — Implement ray traced rendering using GPU-based parallel processing.

## Download

- [ControlTheRayTracingProcessUsingIntersectionQueries.zip](https://docs-assets.developer.apple.com/published/e103f06afb0b/ControlTheRayTracingProcessUsingIntersectionQueries.zip)
