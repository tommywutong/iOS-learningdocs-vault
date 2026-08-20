---
title: What's New in macOS
apple_id: TP40001812
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/WhatsNewInOSX/Articles/macOS_10_13_0.html
archived_at: '2026-07-18T02:58:55.550300Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [What's New in macOS](Introduction.md)


[Next](macOS%20Sierra%2010.12.1.md)[Previous](Introduction.md)

# macOS 10.13

This article summarizes the key developer-related features introduced in macOS 10.13, which runs on currently shipping Macs. The article also lists the documents that describe new features in more detail.

For late-breaking news and information about known issues, see _[macOS 10.13 High Sierra Release Notes](https://developer.apple.com/library/archive/releasenotes/General/RN-macOSSDK-10.13/index.html#//apple_ref/doc/uid/TP40017672)_.

For a complete list of new, modified, and deprecated APIs, see [Apple Developer Documentation](https://developer.apple.com/documentation?changes=latest_major).

To learn about what’s new in Swift, see [Swift Language](../../What%27s%20New%20in%20Xcode%204.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmzvfvjvomy) in _[What’s New in Xcode](../../../documentation/Developer%20Tools/What%E2%80%99s%20New%20in%20Xcode/What%27s%20New%20in%20Xcode%209.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmrw)_ and _The Swift Programming Language (Swift 4)_.

- __New in macOS 10.13 - Support for binary (nontext) barcodes.__

  - Added APIs to AV Foundation, Core Image, and SiriKit to support detection, decoding, and creation of barcodes with binary content.
  - Added a new barcode descriptor object, [CIBarcodeDescriptor](https://developer.apple.com/documentation/coreimage/cibarcodedescriptor) to Core Image to provide interoperability with AV Foundation and the Vision APIs.

- __New in macOS 10.13 - Download font assets.__

  - Added a font asset request API to App Kit. Use [NSFontAssetRequest](https://developer.apple.com/documentation/appkit/nsfontassetrequest) to request asynchronous downloading of font assets. Download progress can be tracked using [NSProgress](https://developer.apple.com/documentation/foundation/nsprogress).
- Improved API for available storage space.

  - Added new keys to the [URL](https://developer.apple.com/documentation/foundation/url) class for different usage scenarios.

    - The [volumeAvailableCapacityForImportantUsageKey](https://developer.apple.com/documentation/foundation/urlresourcekey/2887126-volumeavailablecapacityforimport) key returns total amount of bytes available for operations explicitly requested by user or essential to proper functioning of your apps.
    - The [volumeAvailableCapacityForOpportunisticUsageKey](https://developer.apple.com/documentation/foundation/urlresourcekey/2887125-volumeavailablecapacityforopport) key returns total amount of bytes available for storing nonessential items, such as content predownloaded for performance that may or may not get used by the user.

- __New in macOS 10.13 - High performance image analysis.__

  - Added the [Vision framework](https://developer.apple.com/documentation/vision) for detecting faces, bar codes, text, image horizon, and rectangular regions.
  - Provided support for integrating the Vision framework with Core ML to run custom models on images.
  - Added object-tracking in video.
  - Added support for image registration.
- __New in macOS 10.13 - Ability to write custom image blending kernels for Core Image.__

  - Added [CIBlendKernel](https://developer.apple.com/documentation/coreimage/ciblendkernel), a special type of [CIColorKernel](https://developer.apple.com/documentation/coreimage/cicolorkernel) to blend two images (supported by [CIRenderDestination](https://developer.apple.com/documentation/coreimage/cirenderdestination) and [CIImageAccumulator](https://developer.apple.com/documentation/coreimage/ciimageaccumulator)).
  - Added [init(functionName:fromMetalLibraryData:)](https://developer.apple.com/documentation/coreimage/cikernel/2880194-init) to [CIKernel](https://developer.apple.com/documentation/coreimage/cikernel) for writing kernels using Metal to benefit from the improved language features and the reduced compile time.
- __New in macOS 10.13 - Lightweight render destination.__

  - Added [CIRenderDestination](https://developer.apple.com/documentation/coreimage/cirenderdestination), an object for creating renderers that return to the caller after the work has been issued. You can specify all the destination attributes of the renderer for different destinations, including a surface ([IOSurface](https://developer.apple.com/documentation/iosurface/iosurfaceref)), Core Video pixel buffer ([CVPixelBuffer](https://developer.apple.com/documentation/corevideo/cvpixelbufferref)), GL textures, Metal textures, and memory.
- Added new Core Image filters `CITextImageGenerator`, `CIColorCurves`, `CILabDeltaE`, `CIBokehBlur`, `CIMinMaxRed`, and `CIBicubicScaleTransform`.

Metal 2 contains significant additions and updates to Metal, the Metal Shading Language, and the Metal Performance Shaders framework. Items below indicate where the updates occur:

  – MTL: An update in the [Metal framework](https://developer.apple.com/documentation/metal).

  – MSL: An update in the [Metal Shading Language](https://developer.apple.com/metal/metal-shading-language-specification.pdf).

  – MPS: An update in the [Metal Performance Shaders framework](https://developer.apple.com/documentation/metalperformanceshaders).

- __MTL: New in macOS 10.13 - VR support.__

  - Added support for displaying Metal content on head-mounted displays (HMDs).
  - Added a direct-to-display fast path to bypass the macOS window server.
  - Improved performance to help target 90 FPS frame rates.
- __MPS: New in Metal 2 - Cross-platform Metal Performance Shaders support.__

  - All Metal Performance Shaders functionality is available in iOS 11.0, tvOS 11.0, and macOS 10.13.
- __MPS: New in macOS 10.13 - Neural network support.__

  - Added support for neural networks to the Metal Performance Shaders framework.
  - Added graphs to offer a higher level API for simplifying the creation of neural networks, including objects that allow state to be transferred between nodes in a neural network.
  - Added convolutional neural networks (CNN) to support implementing and running deep learning using previously obtained training data.
  - Added recurrent neural networks for implementing inference on images and matrices.
- __New in macOS 10.13 - Argument Buffers.__ Group your resources into an argument buffer (AB) to reduce CPU overhead.

  - MSL: Added the `[[id(n)]]` attribute qualifier to identify resources in an AB structure.
  - MTL: Added the [MTLArgumentEncoder](https://developer.apple.com/documentation/metal/mtlargumentencoder) protocol to encode resources into an AB.
- __MTL: New in macOS 10.13 - Programmable sample positions.__ Configure the position of samples when rendering to a multisampled render target.

  - Updated the [MTLRenderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor) class to set and get sample positions for a render pass.
- __MSL: New in macOS 10.13 - Uniform type.__

  - Added the `uniform` type to declare variables that are uniform for all threads that execute the graphics or compute function of a draw or dispatch call.
- __MSL: New in macOS 10.13 - Array of samplers.__

  - Added the `array<sampler, size_t N>` type to store an array of samplers.
- __MTL: New in macOS 10.13 - BGR10A2 pixel format.__

  - Added the [bgr10A2Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatbgr10a2unorm) pixel format to present wide color content on P3 displays.
- __MSL: New in macOS 10.13 - Raster order groups.__

  - Added support for organizing access to fragment function resources by using explicit raster order groups.
  - Added the `[[raster_order_group(index)]]` attribute qualifier to assign resources to a raster order group.
- __MTL: New in macOS 10.13 - Nonuniform threadgroup size.__

  - Added the [dispatchThreads(_:threadsPerThreadgroup:)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/2866532-dispatchthreads) method to the [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder) protocol to execute a compute pass that uses a grid with an arbitrary number of threads.
- __New in macOS 10.13 - Multiple viewports.__

  - Added support for multiple active viewports for a draw call and for selective drawing to separate areas of a render target.
  - MTL: Added the [setViewports(_:count:)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/2869738-setviewports) method to the [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) protocol to specify an array of viewports for a render pass.
  - MSL: Added the `[[viewport_array_index]]` attribute qualifier to select a specific viewport for transformation and clip operations.
- __MTL: New in macOS 10.13 - Device notifications.__

  - Added `MTLNotificationName` values for Metal apps to respond to a GPU that is added to or removed from the system.
- MPS: Added new filters.

  - Added filters for image statistics, such as computing the mean and variance for an image region.
  - Added filters for combining two images together, such as an element-wise sum.
  - Added filters for matrix decomposition and solving, such as decomposition using Cholesky or LU (lower upper) factorization.
- MSL: Extended function specialization. Members of a structure used in a graphics, compute, or user function can be used with function constants.

  - Extended `[[color(n)]]` and `[[raster_order_group(index)]]` attribute qualifiers to work with function constants.
- MTL: Extended vertex formats.

  - Added new [MTLVertexFormat](https://developer.apple.com/documentation/metal/mtlvertexformat) values for small formats such as `char`, `short`, and `half`.
- MTL: Updated the Metal framework to support resource heaps on macOS.

  - Added support for allocating resources from a shared memory pool.
  - Added the [MTLHeap](https://developer.apple.com/documentation/metal/mtlheap) protocol to create shared memory allocations from which aliasable or non-aliasable resources can sub-allocated.
  - Added the [MTLFence](https://developer.apple.com/documentation/metal/mtlfence) protocol to track sub-allocated resource dependencies across command encoders.
- MSL: Updated the Metal Shading Language to support arrays of textures on macOS.

  - Added the `array<typename T, size_t N>` type to store an array of textures.
- MTL: Updated the Metal framework to support linear textures on macOS.

  - Added the `makeTexture(descriptor:offset:bytesPerRow:)` method to the [MTLBuffer](https://developer.apple.com/documentation/metal/mtlbuffer) protocol to create 2D linear textures that share their storage with a source buffer.
- MSL: Extended SIMD-group thread synchronization.

  - Added new functions and attribute qualifiers for SIMD-group variables for SIMD-group threads.

- __New in macOS 10.13 - Support for machine learning models.__

  - Added the [Core ML framework](https://developer.apple.com/documentation/coreml) for easily integrating machine learning models into apps.
- Updated MapKit for clearer display of developer data.

  - Added [mutedStandard](https://developer.apple.com/documentation/mapkit/mkmaptype/mkmaptypemutedstandard), a new map display mode that emphasizes developer data.
  - Added properties to customize how annotations behave when collisions occur. Developers use a combination of [displayPriority](https://developer.apple.com/documentation/mapkit/mkannotationview/2867298-displaypriority), [collisionMode](https://developer.apple.com/documentation/mapkit/mkannotationview/2873315-collisionmode), and [clusteringIdentifier](https://developer.apple.com/documentation/mapkit/mkannotationview/2867297-clusteringidentifier) to influence which annotations remain on the map.

- __New in macOS 10.13 - Support for High Efficiency Video Coding (HEVC).__ High Efficiency Video Coding (HEVC) is a new standard for video encoding that offers substantially better compression than H.264 at the same level of visual quality.

  - Added support for using AV Foundation to play back movies containing HEVC-encoded tracks, and to capture and export videos.
  - Added support for using `VideoToolbox` clients to encode and decode HEVC video bitstreams.
- __New in macOS 10.13 - Support for adding project creation extensions to the Photos app.__

  - Added `com.apple.photo-project`, a new extension point that enables adding project creation features to the Photos app.
  - Added `PHProject` and `PHProjectInfo` to the [Photos framework](https://developer.apple.com/documentation/photos) for adding and managing photo creation projects.
  - Added `PHProjectChangeRequest`, an object for saving session state of photo creation projects.
  - Added [PHAsset](https://developer.apple.com/documentation/photokit/phasset), [PHPhotoLibrary](https://developer.apple.com/documentation/photokit/phphotolibrary), and `PHFetchRequest` to enable fetching of assets for a project.
- __New in macOS 10.13 - AirPlay 2.__

  - Improved AirPlay reliability for some audio playback interfaces in AV Foundation. To take advantage of the increased reliability, play audio using [AVPlayer](https://developer.apple.com/documentation/avfoundation/avplayer) or the new [AVSampleBufferAudioRenderer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer) object.
  - Added multiple speaker support to AirPlay for long-form audio such as music and podcasts. To mark your application as presenting long-form audio, invoke the [AVAudioSession](https://developer.apple.com/documentation/avfoundation/avaudiosession) method `-setRouteSharingPolicy:error:` and use [AVAudioSessionRouteSharingPolicyLongForm](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutesharingpolicy/avaudiosessionroutesharingpolicylongform) as the parameter value.
  - Added [AVRoutePickerView](https://developer.apple.com/documentation/avkit/avroutepickerview) to the AVKit framework and [AVRouteDetector](https://developer.apple.com/documentation/avfoundation/avroutedetector) to the AVFoundation framework for enabling users to choose the route for playing content when multiple routes are available. Use `AVRouteDetector` to determine if multiple routes are available when route detection is enabled. If multiple routes are available, use `AVRoutePickerView` to present an interface for the user to choose the routes.
- Added FairPlay streaming key management.

  - Improved the functionality of [AVContentKeySession](https://developer.apple.com/documentation/avfoundation/avcontentkeysession). Use `AVContentKeySession` to initiate content key requests independent of playback or downloading of media assets. Objects conforming to the [AVContentKeyRecipient](https://developer.apple.com/documentation/avfoundation/avcontentkeyrecipient) protocol, such as [AVURLAsset](https://developer.apple.com/documentation/avfoundation/avurlasset), can be added as a recipient to `AVContentKeySession` to obtain access to existing content keys and initiate new content key requests.

- __New in macOS 10.13 - APFS support.__ The OS Installer will automatically convert your system/root volume to APFS as a part of the installation process. The following formats are converted to APFS: plain HFS+, CoreStorage, and FileVault encrypted systems.

  - Added support for APFS as a boot volume with full, native EFI support.
  - Added full support for File Vault.
  - Added support for case-insensitive and case-sensitive variants.
  - Added support for an on-disk format change to allow for normalization-insensitive Case Sensitive volumes. This means that file names in either Unicode NFC or NFD will point to the same files.
  - Updated the volume format for APFS to be normalization insensitive. File names in either Unicode NFC or NFD point to the same files.
  - Added backup support for APFS source volumes. The backup destination should still remain HFS+ in this release.
  - APFS supports up to Unicode revision 9 for filenames. HFS+ supported only up to revision 3.2.
  - APFS supports exporting of volumes over SMB and NFS.
- Updated the APIs in the [Core Bluetooth framework](https://developer.apple.com/documentation/corebluetooth) to match across iOS, tvOS, watchOS, and macOS, and marked the platform availability of each API.

[Next](macOS%20Sierra%2010.12.1.md)[Previous](Introduction.md)

