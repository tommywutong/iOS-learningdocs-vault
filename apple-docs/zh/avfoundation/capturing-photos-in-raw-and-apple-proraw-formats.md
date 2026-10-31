---
title: 以 RAW 和 Apple ProRAW 格式拍摄照片
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capturing-photos-in-raw-and-apple-proraw-formats
source_url: 'https://developer.apple.com/documentation/avfoundation/capturing-photos-in-raw-and-apple-proraw-formats'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capturing-photos-in-raw-and-apple-proraw-formats.json'
content_hash: 'sha256:b9cb07e3a547d711'
translated: true
---

> 导航： [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Photo capture](photo-capture.md)

# 以 RAW 和 Apple ProRAW 格式拍摄照片

<sub>文章</sub>

在你的相机 App 中启用最少处理的图像拍摄，支持专业摄影工作流程。

## 概述

默认情况下，图像拍摄管线使用先进的计算摄影技术来获得最高质量的图像，并以压缩格式把处理后的结果交付给你的 App，便于高效存储和显示。在很多情况下，处理后的格式是很好的选择，但 RAW 格式包含来自相机传感器的最少处理的图像数据，这让你的 App 用户拥有更多创作控制权。

以 RAW 格式拍摄图像会产生比压缩格式大得多的文件，但会极大地扩展后期制作的编辑能力。以标准 RAW 格式拍摄的一个缺点是，它会绕过图像拍摄管线提供的先进处理。

从 iOS 14.3 开始，在 iPhone 12 Pro 和 Pro Max 上可以使用 Apple ProRAW 格式。Apple ProRAW 格式兼具 RAW 拍摄的优势，并应用了许多此前 RAW 工作流程无法使用的多图像融合技术。

> [!tip] 提示
> 你可以使用 Core Image 显示和编辑 RAW 与 Apple ProRAW 文件。更多信息参见 [CIRAWFilter](../coreimage/cirawfilter.md) 类的 [init(imageURL:)](<../coreimage/cirawfilter/init(imageurl_).md>) 初始化方法。

### 启用 Apple ProRAW 支持

要判断你的 App 的照片输出在当前环境下是否支持 Apple ProRAW 格式，请把该输出添加到一个已连接视频源的采集会话，然后查询它的 [appleProRAWSupported](avcapturephotooutput/isappleprorawsupported.md) 属性。如果当前环境支持 Apple ProRAW 格式，你可以像下面的示例那样，把它的 [appleProRAWEnabled](avcapturephotooutput/isappleprorawenabled.md) 属性设为 [true](../swift/true.md) 来启用它：

```swift
private let captureSession = AVCaptureSession()
private let photoOutput = AVCapturePhotoOutput()

private func setupSession() throws {
    
    // Start the capture session configuration.
    captureSession.beginConfiguration()
    
    // Configure the session for photo capture.
    captureSession.sessionPreset = .photo
    
    // Connect the default video device.
    let videoInput = try AVCaptureDeviceInput(device: defaultVideoDevice)
    if captureSession.canAddInput(videoInput) {
        captureSession.addInput(videoInput)
        currentVideoInput = videoInput
    } else {
        throw CameraError.setupFailed
    }
    
    // Connect and configure the capture output.
    if captureSession.canAddOutput(photoOutput) {
        captureSession.addOutput(photoOutput)
        
        // Use the Apple ProRAW format when the environment supports it.
        photoOutput.isAppleProRAWEnabled = photoOutput.isAppleProRAWSupported
    } else {
        throw CameraError.setupFailed
    }
    
    // Session configuration is complete. Commit the configuration.
    captureSession.commitConfiguration()
}

```

启用 Apple ProRAW 格式后，照片输出的 [availableRawPhotoPixelFormatTypes](avcapturephotooutput/availablerawphotopixelformattypes-5fatm.md) 数组中会增加一个条目。你可以通过查询输出的 [+ isAppleProRAWPixelFormat:](<avcapturephotooutput/isappleprorawpixelformat(__).md>) 或 [+ isBayerRAWPixelFormat:](<avcapturephotooutput/isbayerrawpixelformat(__).md>) 方法，判断数组中的某个特定格式是 Apple ProRAW 还是拜耳 RAW 格式。

> [!important] 重要
> 为避免对采集管线进行耗时的重新配置，请在启动采集会话之前启用 Apple ProRAW 拍摄。

### 拍摄 RAW 和 Apple ProRAW 照片

以 RAW 和 Apple ProRAW 格式拍摄照片，只需对[拍摄静态照片和实况照片](capturing-still-and-live-photos.md)中的基础拍摄工作流程做少量修改。首先创建一个 [AVCapturePhotoSettings](avcapturephotosettings.md) 对象，指定要拍摄的 RAW 格式，以及（如果你的 App 支持创建 RAW+JPEG 文件）一个可选的要拍摄的处理后格式。采集管线只支持照片输出的 [availableRawPhotoPixelFormatTypes](avcapturephotooutput/availablerawphotopixelformattypes-5fatm.md) 数组中的 RAW 格式。

下面的示例会找到合适的 RAW 格式：当 Apple ProRAW 处于启用状态时选择它，否则选择拜耳 RAW 格式。它创建一个指定 RAW 和处理后格式的照片设置对象，以及一个监视拍摄进度的代理对象。最后，它调用照片输出的 [- capturePhotoWithSettings:delegate:](<avcapturephotooutput/capturephoto(with_delegate_).md>) 方法，向它传入照片设置和代理对象。

```swift
let query = photoOutput.isAppleProRAWEnabled ?
    { AVCapturePhotoOutput.isAppleProRAWPixelFormat($0) } :
    { AVCapturePhotoOutput.isBayerRAWPixelFormat($0) }

// Retrieve the RAW format, favoring the Apple ProRAW format when it's in an enabled state.
guard let rawFormat =
        photoOutput.availableRawPhotoPixelFormatTypes.first(where: query) else {
    fatalError("No RAW format found.")
}

// Capture a RAW format photo, along with a processed format photo.
let processedFormat = [AVVideoCodecKey: AVVideoCodecType.hevc]
let photoSettings = AVCapturePhotoSettings(rawPixelFormatType: rawFormat,
                                           processedFormat: processedFormat)

// Create a delegate to monitor the capture process.
let delegate = RAWCaptureDelegate()
captureDelegates[photoSettings.uniqueID] = delegate

// Remove the delegate reference when it finishes its processing.
delegate.didFinish = {
    self.captureDelegates[photoSettings.uniqueID] = nil
}

// Tell the output to capture the photo.
photoOutput.capturePhoto(with: photoSettings, delegate: delegate)
```

Apple ProRAW 格式支持拍摄最高全分辨率的 JPEG 图像作为缩略图照片。像下面的示例那样，在你的照片设置对象上设置 [rawEmbeddedThumbnailPhotoFormat](avcapturephotosettings/rawembeddedthumbnailphotoformat.md)：

```swift
// Select the first available codec type, which is JPEG.
guard let thumbnailPhotoCodecType =
    photoSettings.availableRawEmbeddedThumbnailPhotoCodecTypes.first else {
    // Handle the failure to find an available thumbnail photo codec type.
}

// Select the maximum photo dimensions as thumbnail dimensions if a full-size thumbnail is desired.
// The system clamps these dimensions to the photo dimensions if the capture produces a photo with smaller than maximum dimensions.
let dimensions = photoSettings.maxPhotoDimensions

photoSettings.rawEmbeddedThumbnailPhotoFormat = [
    AVVideoCodecKey: thumbnailPhotoCodecType,
    AVVideoWidthKey: dimensions.width,
    AVVideoHeightKey: dimensions.height
]
```

### 处理拍摄的照片

照片输出会为你请求的每种格式至少调用一次其代理的 [- captureOutput:didFinishProcessingPhoto:error:](<avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) 方法，并且根据你的拍摄设置可能调用更多次。使用上一节中的拍摄设置会让照片输出调用该代理方法两次：一次针对 RAW 或 Apple ProRAW 图像，另一次针对处理后的图像。在每次调用中，通过调用照片的 [- fileDataRepresentation](<avcapturephoto/filedatarepresentation().md>) 方法获取照片的文件数据，并按需存储。如果你对 RAW 或 Apple ProRAW 照片调用该方法，它会返回行业标准 DNG 文件格式的数据。如果你对处理后的图像调用它，它会返回压缩的位图图像数据。

以下代码展示了 [- captureOutput:didFinishProcessingPhoto:error:](<avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) 方法的一个示例实现。它把 RAW 文件写入磁盘，并存储指向处理后照片的压缩位图数据的引用以供日后使用。

```swift
class RAWCaptureDelegate: NSObject, AVCapturePhotoCaptureDelegate {
    
    private var rawFileURL: URL?
    private var compressedData: Data?
    
    var didFinish: (() -> Void)?
    
    // Store the RAW file and compressed photo data until the capture finishes.
    func photoOutput(_ output: AVCapturePhotoOutput,
                     didFinishProcessingPhoto photo: AVCapturePhoto,
                     error: Error?) {
        
        guard error == nil else {
            print("Error capturing photo: \(error!)")
            return
        }
        
        // Access the file data representation of this photo.
        guard let photoData = photo.fileDataRepresentation() else {
            print("No photo data to write.")
            return
        }
        
        if photo.isRawPhoto {
            // Generate a unique URL to write the RAW file.
            rawFileURL = makeUniqueDNGFileURL()
            do {
                // Write the RAW (DNG) file data to a URL.
                try photoData.write(to: rawFileURL!)
            } catch {
                fatalError("Couldn't write DNG file to the URL.")
            }
        } else {
            // Store compressed bitmap data.
            compressedData = photoData
        }
    }
    
    private func makeUniqueDNGFileURL() -> URL {
        let tempDir = FileManager.default.temporaryDirectory
        let fileName = ProcessInfo.processInfo.globallyUniqueString
        return tempDir.appendingPathComponent(fileName).appendingPathExtension("dng")
    }
}
```

### 自定 Apple ProRAW 输出

默认情况下，当你请求一张 Apple ProRAW 照片的文件数据表示时，得到的是完全无损质量的数据。如果你愿意接受一定的有损压缩来获得更小的文件体积，可以调用 [- fileDataRepresentationWithCustomizer:](<avcapturephoto/filedatarepresentation(with_).md>) 并传入一个遵循 [AVCapturePhotoFileDataRepresentationCustomizer](avcapturephotofiledatarepresentationcustomizer.md) 协议的自定对象来定制压缩设置。以下代码展示了该协议的一个示例实现，它对输出图像应用最小的压缩：

```swift
class AppleProRAWCustomizer: NSObject, AVCapturePhotoFileDataRepresentationCustomizer {
    
    // Customize the compression settings.
    func replacementAppleProRAWCompressionSettings(for photo: AVCapturePhoto, 
                                                   defaultSettings: [String : Any], 
                                                   maximumBitDepth: Int) -> [String : Any] {
        
        // Reduce the bit depth and quality of the final file.
        return [AVVideoAppleProRAWBitDepthKey: maximumBitDepth - 2, 
                AVVideoQualityKey: 0.95]
    }
}
```

要在获取 ProRAW 照片的文件数据表示时使用这个自定器，创建你的自定器的一个新实例，并像下面的示例那样把它传给 [- fileDataRepresentationWithCustomizer:](<avcapturephoto/filedatarepresentation(with_).md>) 方法：

```swift
// Get a minimally compressed representation of the file data.
let customizer = AppleProRAWCustomizer()
let photoData = photo.fileDataRepresentation(with: customizer)
```

### 把照片保存到照片图库

照片输出会通过调用代理的 [- captureOutput:didFinishCaptureForResolvedSettings:error:](<avcapturephotocapturedelegate/photooutput(__didfinishcapturefor_error_).md>) 方法来表明它完成了拍摄请求。这个回调提供了把拍摄的照片保存到用户照片图库的机会。有关配置你的 App 以访问用户照片图库的更多信息，参见[保存拍摄的照片](saving-captured-photos.md)。

要把拍摄的照片保存到用户的照片图库，需要创建一个单独的照片资产，把 RAW 或 Apple ProRAW 数据与处理后的数据关联起来。创建一个 [PHAssetCreationRequest](../photos/phassetcreationrequest.md) 实例，然后把 DNG 版本指定为该资产的主 [PHAssetResourceType.photo](../photos/phassetresourcetype/photo.md) 资源，把处理后的图像指定为 [PHAssetResourceType.alternatePhoto](../photos/phassetresourcetype/alternatephoto.md) 资源。像下面的示例那样，在一个更改块中执行该请求：

```swift
// After both RAW and compressed versions are complete, add them to the Photos library.
func photoOutput(_ output: AVCapturePhotoOutput,
                 didFinishCaptureFor resolvedSettings: AVCaptureResolvedPhotoSettings,
                 error: Error?) {
    
    // Call the "finished" closure, if you set it.
    defer { didFinish?() }
    
    guard error == nil else {
        print("Error capturing photo: \(error!)")
        return
    }
    
    // Ensure the RAW and processed photo data exists.
    guard let rawFileURL = rawFileURL,
          let compressedData = compressedData else {
        print("The expected photo data isn't available.")
        return
    }
    
    // Request add-only access to the user's Photos library (if the user hasn't already granted that access).
    PHPhotoLibrary.requestAuthorization(for: .addOnly) { status in
        
        // Don't continue unless the user granted access.
        guard status == .authorized else { return }
        
        PHPhotoLibrary.shared().performChanges {
            
            let creationRequest = PHAssetCreationRequest.forAsset()
            
            // Save the RAW (DNG) file as the main resource for the Photos asset.
            let options = PHAssetResourceCreationOptions()
            options.shouldMoveFile = true
            creationRequest.addResource(with: .photo,
                                        fileURL: rawFileURL,
                                        options: options)
            
            
            // Add the compressed (HEIF) data as an alternative resource.
            creationRequest.addResource(with: .alternatePhoto,
                                        data: compressedData,
                                        options: nil)
            
        } completionHandler: { success, error in
            // Process the Photos library error.
        }
    }
}
```

## 另请参阅

### 照片拍摄

- [拍摄色彩一致的照片](capturing-consistent-color-images.md) — 使用新的 Constant Color API 为你的 App 带来摄影棚和灯光设备的能力。
- [拍摄静态照片和实况照片](capturing-still-and-live-photos.md) — 配置并拍摄单张或多张静态图像、实况照片以及其他形式的摄影内容。
- [在你的 Mac App 中支持连续互通相机](../appkit/supporting-continuity-camera-in-your-mac-app.md) — 使用连续互通相机把用户 iPhone、iPad 或 iPod touch 上扫描的文稿和照片融入你的 Mac App。
- [AVCapturePhoto](avcapturephoto.md) — 来自照片拍摄输出的图像数据的容器。
- [AVCaptureDeferredPhotoProxy](avcapturedeferredphotoproxy.md) — 一种轻度处理的照片，其中的数据可供系统日后用于处理和获取更高分辨率的资产。
- [AVCapturePhotoOutput](avcapturephotooutput.md) — 用于静态图像、实况照片和其他摄影工作流程的拍摄输出。
- [AVCapturePhotoCaptureDelegate](avcapturephotocapturedelegate.md) — 用于监视照片拍摄输出的进度并接收其结果的方法。
- [AVCapturePhotoOutputReadinessCoordinator](avcapturephotooutputreadinesscoordinator.md) — 一个监视照片输出的拍摄就绪状态变化的对象。
- [AVCapturePhotoOutputReadinessCoordinatorDelegate](avcapturephotooutputreadinesscoordinatordelegate.md) — 用于接收照片输出拍摄就绪状态更新的代理协议。
- [AVCaptureStillImageOutput](avcapturestillimageoutput.md) — 用于拍摄静态照片的拍摄输出。 _(已废弃)_
