---
title: Reading multiview 3D video files
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [macOS 14.0+, Xcode 15.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/reading-multiview-3d-video-files
source_url: 'https://developer.apple.com/documentation/avfoundation/reading-multiview-3d-video-files'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/reading-multiview-3d-video-files.json'
content_hash: 'sha256:69849c0a810ec0e3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media reading and writing](media-reading-and-writing.md)

# Reading multiview 3D video files

<sub>Sample Code</sub>

Render single images for the left eye and right eye from a multiview High Efficiency Video Coding format file by reading individual video frames.

## Overview

Multiview High Efficiency Video Coding (MV-HEVC) media files contain information to produce stereoscopic frames, one for the left eye and one for the right, to create an effect of depth and allow for 3D video. This is the standard format for presenting 3D video in visionOS, encoded as MPEG-4 or QuickTime files.

Previewing and testing MV-HEVC files without hardware requires the ability to load, view, and step through the video data on a timeline. This sample app opens a media file, checking for the MV-HEVC format, then presents a view containing the individual frames at the timestamp. Step through the timeline by dragging the slider to a specific timestamp, or advance to the next frame by pressing the Space bar.

For the full details of the MV-HEVC format, see [Apple HEVC Stereo Video - Interoperability Profile (PDF)](https://developer.apple.com/av-foundation/HEVC-Stereo-Video-Profile.pdf) and [ISO Base Media File Format and Apple HEVC Stereo Video (PDF)](https://developer.apple.com/av-foundation/Stereo-Video-ISOBMFF-Extensions.pdf).

### Load and inspect the media asset

The app first displays a button labeled Open MVHEVC File. When selected, the button presents an [NSOpenPanel](../appkit/nsopenpanel.md) for choosing video media. Next, the app initializes a `MediaDetailViewModel`, loading this file as an [AVURLAsset](avurlasset.md). Before opening the file to present any elements for a stereo video frame, the app ensures a playable, readable file, and gets its total length in time. This is all performed in the initializer.

```swift
init(filename: URL) {
    asset = AVURLAsset(url: filename)
    Task { @MainActor in
        do {
            let (duration, isPlayable, isReadable) = try await asset.load(.duration, .isPlayable, .isReadable)
            self.duration = duration.seconds
            self.isPlayable = isPlayable
            self.isReadable = isReadable
        } catch {
            self.error = error
        }
    }
}
```

### Load track data and timestamps

After confirming the track is readable video data, the app initializes a `StereoViewModel`by calling [- loadTracksWithMediaCharacteristic:completionHandler:](<avasset/loadtracks(withmediacharacteristic_completionhandler_).md>) requesting a [AVMediaCharacteristicContainsStereoMultiviewVideo](avmediacharacteristic/containsstereomultiviewvideo.md) track. This check confirms that the file meets the MV-HEVC specification and has valid stereo data.

```swift
if let track = try await asset.loadTracks(withMediaCharacteristic: .containsStereoMultiviewVideo).first {
    self.track = track
```

Next, the app pulls available timestamps for each frame in the track by calling `presentationTimesFor(track:asset:)`. The app places a video sample cursor at the start of the track with [- makeSampleCursorAtFirstSampleInDecodeOrder](<avassettrack/makesamplecursoratfirstsampleindecodeorder().md>), then creates a new [AVSampleBufferGenerator](avsamplebuffergenerator.md) and [AVSampleBufferRequest](avsamplebufferrequest.md).

```swift
guard let cursor = track.makeSampleCursorAtFirstSampleInDecodeOrder() else {
    return []
}
let sampleBufferGenerator = AVSampleBufferGenerator(asset: asset, timebase: nil)
var presentationTimes = [CMTime]()
let request = AVSampleBufferRequest(start: cursor)
var numSamples: Int64 = 0
```

To read the timestamps, obtain the sample buffer for the current cursor from [- createSampleBufferForRequest:error:](<avsamplebuffergenerator/makesamplebuffer(for_).md>), then add the [presentationTimeStamp](../coremedia/cmsamplebuffer/presentationtimestamp.md) for the frame. The cursor steps forward by calling [- stepInDecodeOrderByCount:](<avsamplecursor/stepindecodeorder(bycount_).md>), reading and caching timestamps for each frame in the buffer. When `stepInDecodeOrder(byCount:)` returns no next frame, sample times are in the cache and reading the video track completes.

```swift
repeat {
    let buf = try sampleBufferGenerator.makeSampleBuffer(for: request)
    presentationTimes.append(buf.presentationTimeStamp)
    numSamples = cursor.stepInDecodeOrder(byCount: 1)
} while numSamples == 1
```

### Load video layer information

After preparing timestamps, the app calls `loadVideoLayerIdsForTrack()` to get the layer IDs for the two tracks associated with the left and right eyes. The app calls [load(_:isolation:)](<avasynchronouskeyvalueloading/load(__isolation_).md>)to retrieve metadata, then filters the layer data out of the first available track’s [tagCollections](../coremedia/cmformatdescription/tagcollections.md). The filter predicate is [value(onlyIfMatching:)](<../coremedia/cmtag-swift.class/value(onlyifmatching_).md>), extracting only video layer IDs.

```swift
private func loadVideoLayerIdsForTrack(_ videoTrack: AVAssetTrack) async throws -> [Int64]? {
    let formatDescriptions = try await videoTrack.load(.formatDescriptions)
    var tags = [Int64]()
    if let tagCollections = formatDescriptions.first?.tagCollections {
        tags = tagCollections.flatMap({ $0 }).compactMap { tag in
            tag.value(onlyIfMatching: .videoLayerID)
        }
    }
    return tags
}
```

### Load video frames from buffers

With the timestamp and left eye and right eye video layers identified, `readBufferFromAsset(at:)` calls the `readNextBufferFromAsset()` method of the app to retrieve and display the frame data. The method starts with a series of `guard` checks to ensure read access to the track, creates a local copy of the sample buffer by calling [- copyNextSampleBuffer](<avassetreaderoutput/copynextsamplebuffer().md>), and retrieves the tagged video buffers from the track.

```swift
guard let assetReader, let trackOutput else {
    return
}
guard assetReader.status == .reading else {
    publishState(.error(message: "UNEXPECTED STATUS \(assetReader.status)"))
    return
}
guard let sampleBuffer = trackOutput.copyNextSampleBuffer() else {
    publishState(.error(message: "READING SAMPLE BUFFER, STATUS \(assetReader.status), ERROR \(String(describing: assetReader.error))"))
    return
}
guard let taggedBuffers = sampleBuffer.taggedBuffers else {
    publishState(.error(message: "SAMPLE BUFFER CONTAINS NO TAGGED BUFFERS: \(sampleBuffer)"))
    return
}
guard taggedBuffers.count == 2 else {
    publishState(.error(message: "EXPECTED 2 TAGGED BUFFERS, GOT \(taggedBuffers.count)"))
    return
}
```

The app parses each [CMTaggedBuffer.Buffer.pixelBuffer(_:)](<../coremedia/cmtaggedbuffer/buffer-swift.enum/pixelbuffer(__).md>) from the returned sample buffers into an image for display using [init(cvPixelBuffer:)](<../coreimage/ciimage/init(cvpixelbuffer_)-3wng7.md>). The app creates an [NSImage](../appkit/nsimage.md) and sets it to the view content as either `leftEye` or `rightEye` depending on whether the view contains a [stereoView(_:)](<../coremedia/cmtag-swift.class/stereoview(__).md>) for the left or right eye.

```swift
taggedBuffers.forEach { taggedBuffer in
    switch taggedBuffer.buffer {
    case let .pixelBuffer(pixelBuffer):
        let ciimage = CIImage(cvPixelBuffer: pixelBuffer)
        let context: CIContext = CIContext(options: nil)
        let cgImage: CGImage = context.createCGImage(ciimage, from: ciimage.extent)!
        let tags = taggedBuffer.tags
        Task {
            await MainActor.run {
                let nsImage = NSImage(cgImage: cgImage, size: NSSize(width: 320, height: 240))
                if tags.contains(.stereoView(.leftEye)) {
                    leftEye = nsImage
                } else if tags.contains(.stereoView(.rightEye)) {
                    rightEye = nsImage
                }
            }
        }
    case .sampleBuffer(let samp):
        publishState(.error(message: "EXPECTED PIXEL BUFFER, GOT SAMPLE BUFFER \(samp)"))
    @unknown default:
        publishState(.error(message: "EXPECTED PIXEL BUFFER TYPE, GOT \(taggedBuffer.buffer)"))
    }
}
```

## See Also

### Media reading

- [AVAssetReader](avassetreader.md) — An object that reads media data from an asset.
- [AVAssetReaderOutput](avassetreaderoutput.md) — An abstract class that defines the interface to read media samples from an asset reader.
- [AVAssetReaderTrackOutput](avassetreadertrackoutput.md) — An object that reads media data from a single track of an asset.
- [AVAssetReaderAudioMixOutput](avassetreaderaudiomixoutput.md) — An object that reads audio samples that result from mixing audio from one or more tracks.
- [AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md) — An object that reads composited video frames from one or more tracks of an asset.
- [AVAssetReaderSampleReferenceOutput](avassetreadersamplereferenceoutput.md) — An object that reads sample references from an asset track.
- [AVAssetReaderOutputMetadataAdaptor](avassetreaderoutputmetadataadaptor.md) — An object that creates timed metadata group objects for an asset track. _(deprecated)_

## Download

- [ReadingMultiview3DVideoFiles.zip](https://docs-assets.developer.apple.com/published/03b0a926288f/ReadingMultiview3DVideoFiles.zip)
