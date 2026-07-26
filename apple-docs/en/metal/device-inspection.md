---
title: Device inspection
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/device-inspection
source_url: 'https://developer.apple.com/documentation/metal/device-inspection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/device-inspection.json'
content_hash: 'sha256:3768728fba242e51'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [GPU devices and work submission](gpu-devices-and-work-submission.md) · [MTLDevice](mtldevice.md)

# Device inspection

<sub>API Collection</sub>

Locate and identify a GPU and the features it supports, and sample its counters.

## Topics

### Checking a GPU device’s feature support

- [- supportsFamily:](<mtldevice/supportsfamily(__).md>) — Returns a Boolean value that indicates whether the GPU device supports the feature set of a specific GPU family.
- [MTLGPUFamily](mtlgpufamily.md) — Represents the functionality for families of GPUs.
- [- supportsFeatureSet:](<mtldevice/supportsfeatureset(__).md>) — Returns a Boolean value that indicates whether the GPU device supports a specific feature set. _(deprecated)_
- [MTLFeatureSet](mtlfeatureset.md) — The device feature sets that define specific platform, hardware, and software configurations. _(deprecated)_

### Checking compute support

- [maxThreadgroupMemoryLength](mtldevice/maxthreadgroupmemorylength.md) — The maximum threadgroup memory available to a compute kernel, in bytes.
- [maxThreadsPerThreadgroup](mtldevice/maxthreadsperthreadgroup.md) — The maximum number of threads along each dimension of a threadgroup.

### Checking render support

- [supportsRaytracing](mtldevice/supportsraytracing.md) — A Boolean value that indicates whether the GPU device supports ray tracing.
- [supportsPrimitiveMotionBlur](mtldevice/supportsprimitivemotionblur.md) — A Boolean value that indicates whether the GPU device supports motion blur for ray tracing.
- [supportsRaytracingFromRender](mtldevice/supportsraytracingfromrender.md) — A Boolean value that indicates whether you can call ray-tracing functions from a vertex or fragment shader.
- [supports32BitMSAA](mtldevice/supports32bitmsaa.md) — A Boolean value that indicates whether the GPU can allocate 32-bit integer texture formats and resolve to 32-bit floating-point texture formats.
- [supportsPullModelInterpolation](mtldevice/supportspullmodelinterpolation.md) — A Boolean value that indicates whether the GPU can compute multiple interpolations of a fragment function’s input.
- [supportsShaderBarycentricCoordinates](mtldevice/supportsshaderbarycentriccoordinates.md) — A Boolean value that indicates whether the GPU supports barycentric coordinates.
- [- supportsVertexAmplificationCount:](<mtldevice/supportsvertexamplificationcount(__).md>) — Returns a Boolean value that indicates whether the GPU supports an amplification factor.
- [programmableSamplePositionsSupported](mtldevice/areprogrammablesamplepositionssupported.md) — A Boolean value that indicates whether the GPU supports programmable sample positions.
- [rasterOrderGroupsSupported](mtldevice/arerasterordergroupssupported.md) — A Boolean value that indicates whether the GPU supports raster order groups.
- [barycentricCoordsSupported](mtldevice/arebarycentriccoordssupported.md) — A Boolean value that indicates whether the GPU supports barycentric coordinates. _(deprecated)_

### Checking texture and sampler support

- [supports32BitFloatFiltering](mtldevice/supports32bitfloatfiltering.md) — A Boolean value that indicates whether the GPU can filter a texture with a 32-bit floating-point format.
- [supportsBCTextureCompression](mtldevice/supportsbctexturecompression.md) — A Boolean value that indicates whether you can use textures that use BC compression.
- [depth24Stencil8PixelFormatSupported](mtldevice/isdepth24stencil8pixelformatsupported.md) — A Boolean value that indicates whether a device supports a packed depth-and-stencil pixel format. _(deprecated)_
- [supportsQueryTextureLOD](mtldevice/supportsquerytexturelod.md) — A Boolean value that indicates whether you can query the texture level of detail from within a shader.
- [readWriteTextureSupport](mtldevice/readwritetexturesupport.md) — The GPU device’s texture support tier.

### Checking function pointer support

- [supportsFunctionPointers](mtldevice/supportsfunctionpointers.md) — A Boolean value that indicates whether the device supports function pointers in compute kernel functions.
- [supportsFunctionPointersFromRender](mtldevice/supportsfunctionpointersfromrender.md) — A Boolean value that indicates whether the device supports function pointers in render functions.

### Checking a GPU device’s memory

- [currentAllocatedSize](mtldevice/currentallocatedsize.md) — The total amount of memory, in bytes, the GPU device is using for all of its resources.
- [recommendedMaxWorkingSetSize](mtldevice/recommendedmaxworkingsetsize.md) — An approximation of how much memory, in bytes, this GPU device can allocate without affecting its runtime performance.
- [hasUnifiedMemory](mtldevice/hasunifiedmemory.md) — A Boolean value that indicates whether the GPU shares all of its memory with the CPU.
- [maxTransferRate](mtldevice/maxtransferrate.md) — The highest theoretical rate, in bytes per second, the system can copy between system memory and the GPU’s dedicated memory (VRAM). _(deprecated)_

### Sampling a GPU device’s counters

- [counterSets](mtldevice/countersets.md) — The counter sets supported by the device object.
- [- supportsCounterSampling:](<mtldevice/supportscountersampling(__).md>) — Returns a Boolean value that indicates whether you can read GPU counters at the specified command boundary.
- [MTLCounterSamplingPoint](mtlcountersamplingpoint.md) — Options for different times when you can sample GPU counters.
- [- newCounterSampleBufferWithDescriptor:error:](<mtldevice/makecountersamplebuffer(descriptor_).md>) — Creates a counter sample buffer.

### Sampling GPU and CPU timestamps simultaneously

- [sampleTimestamps()](<mtldevice/sampletimestamps().md>) — Captures and returns a CPU timestamp and a GPU timestamp from the same moment in time.

### Identifying a GPU device

- [name](mtldevice/name.md) — The full name of the GPU device.
- [architecture](mtldevice/architecture.md) — The architectural details of the GPU device.
- [MTLArchitecture](mtlarchitecture.md) — A class that contains the architectural details of a GPU device.
- [registryID](mtldevice/registryid.md) — The GPU device’s registry identifier.
- [location](mtldevice/location.md) — The physical location of the GPU relative to the system. _(deprecated)_
- [MTLDeviceLocation](mtldevicelocation.md) — Indicates the location of the GPU relative to the system it’s connect to. _(deprecated)_
- [locationNumber](mtldevice/locationnumber.md) — A specific GPU position based on its general location. _(deprecated)_
- [lowPower](mtldevice/islowpower.md) — A Boolean value that indicates whether the GPU lowers its performance to conserve energy. _(deprecated)_
- [removable](mtldevice/isremovable.md) — A Boolean value that indicates whether the GPU is removable. _(deprecated)_
- [headless](mtldevice/isheadless.md) — A Boolean value that indicates whether a GPU device doesn’t have a connection to a display. _(deprecated)_
- [peerGroupID](mtldevice/peergroupid.md) — The peer group ID the GPU belongs to, if applicable. _(deprecated)_
- [peerCount](mtldevice/peercount.md) — The total number of GPUs in the peer group, if applicable. _(deprecated)_
- [peerIndex](mtldevice/peerindex.md) — The unique identifier for a GPU in a peer group. _(deprecated)_

## See Also

### Working with GPU devices

- [Work submission](work-submission.md) — Create queues that submit work to the GPU or load assets into GPU resources, and indirect command buffers that group your frequent commands together.
- [Pipeline state creation](pipeline-state-creation.md) — Create pipeline states for render and compute passes, samplers, depth and stencil states, and indirect command buffers.
- [Resource creation](resource-creation.md) — Load assets with input/output queues and make various resource instances, such as buffers, textures, acceleration structures, and memory heaps.
- [Shader library and archive creation](shader-library-and-archive-creation.md) — Create static and dynamic shader libraries, and binary shader archives.
