---
title: AVCaptureDevice.Format
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format.json'
content_hash: 'sha256:d62f606f194b9fd9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.Format

<sub>Class</sub>

A class that defines media formats and capture settings that capture devices support.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class Format
```

## Overview

A format object provides information about a media capture format to use with a capture device, such as video frame rates and zoom factors.

You can find more information about a capture format using its associated Core Media format description (see [CMFormatDescription](../../coremedia/cmformatdescription.md)), available using the [formatDescription](format/formatdescription.md) property.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Determining spatial capture support

- [spatialVideoCaptureSupported](format/isspatialvideocapturesupported.md) — A Boolean value that indicates whether the format supports capturing spatial video to a file.

### Determining background replacement support

- [backgroundReplacementSupported](format/isbackgroundreplacementsupported.md) — A Boolean value that indicates whether the format supports background replacement.
- [videoFrameRateRangeForBackgroundReplacement](format/videoframeraterangeforbackgroundreplacement.md) — The minimum and maximum frame rates available when Background Replacement is active.

### Determining video capture support

- [autoVideoFrameRateSupported](format/isautovideoframeratesupported.md) — A Boolean value that Indicates whether the format supports performing automatic video frame rate adjustments.
- [videoSupportedFrameRateRanges](format/videosupportedframerateranges.md) — A list of frame rate ranges that a format supports.
- [AVFrameRateRange](../avframeraterange.md) — An immutable type that represents a range of valid frame rates.
- [videoBinned](format/isvideobinned.md) — A Boolean value that indicates whether the format produces video data in a binned format.
- [videoHDRSupported](format/isvideohdrsupported.md) — A Boolean value that indicates whether the format supports high dynamic range streaming.
- [multiCamSupported](format/ismulticamsupported.md) — A Boolean value that indicates whether a multi-camera capture session supports this format.

### Determining reaction effects support

- [reactionEffectsSupported](format/reactioneffectssupported.md) — A Boolean value that indicates whether the device supports reaction effects.
- [videoFrameRateRangeForReactionEffectsInProgress](format/videoframeraterangeforreactioneffectsinprogress.md) — Indicates the minimum and maximum frame rates available when a reaction effect runs.

### Determining supported media formats

- [mediaType](format/mediatype.md) — A constant describing the media type of an `AVCaptureDevice` active or supported format.
- [formatDescription](format/formatdescription.md) — An object describing the capture format.

### Determining output support

- [unsupportedCaptureOutputClasses](format/unsupportedcaptureoutputclasses.md) — The list of capture output subclasses not allowed for capture with this format, if any.

### Determining field of view

- [videoFieldOfView](format/videofieldofview.md) — Indicates the format’s horizontal field of view in degrees.
- [geometricDistortionCorrectedVideoFieldOfView](format/geometricdistortioncorrectedvideofieldofview.md) — A horizontal field of view for the format after correction for geometric distortion.

### Determining video stabilization support

- [- isVideoStabilizationModeSupported:](<format/isvideostabilizationmodesupported(__).md>) — A Boolean value that indicates whether the format supports a given video stabilization mode.
- [AVCaptureVideoStabilizationMode](../avcapturevideostabilizationmode.md) — An enumeration of video stabilization modes that capture devices and formats support.

### Determining photo quality

- [supportedMaxPhotoDimensions](format/supportedmaxphotodimensions.md) — The maximum photo dimension this format supports.
- [highPhotoQualitySupported](format/ishighphotoqualitysupported.md) — A Boolean value that indicates whether this format supports high-quality capture with the current quality prioritization setting.
- [highestPhotoQualitySupported](format/ishighestphotoqualitysupported.md) — A Boolean value that indicates whether this format supports the highest photo quality that the platform delivers.

### Determining color support

- [globalToneMappingSupported](format/isglobaltonemappingsupported.md) — A Boolean value that indicates whether the format supports global tone mapping.
- [supportedColorSpaces](format/supportedcolorspaces.md) — The list of the device’s supported color spaces.

### Determining exposure support

- [systemRecommendedExposureBiasRange](format/systemrecommendedexposurebiasrange.md) — The system’s recommended exposure bias range for this device format.
- [minISO](format/miniso.md) — A floating-point number that indicates the minimum supported exposure ISO value.
- [maxISO](format/maxiso.md) — A floating-point number that indicates the maximum supported exposure ISO value.
- [minExposureDuration](format/minexposureduration.md) — A time value that indicates the minimum supported exposure duration.
- [maxExposureDuration](format/maxexposureduration.md) — A time value that indicates the maximum supported exposure duration.

### Determining zoom capabilities

- [systemRecommendedVideoZoomRange](format/systemrecommendedvideozoomrange.md) — The system’s recommended zoom range for this device format.
- [videoMaxZoomFactor](format/videomaxzoomfactor.md) — A maximum zoom factor the format allows.
- [videoZoomFactorUpscaleThreshold](format/videozoomfactorupscalethreshold.md) — A threshold at which the system upscales pixel data.
- [secondaryNativeResolutionZoomFactors](format/secondarynativeresolutionzoomfactors.md) — The zoom factors at which this device transitions to secondary native resolution modes.
- [supportedVideoZoomRangesForDepthDataDelivery](format/supportedvideozoomrangesfordepthdatadelivery.md) — The zoom ranges that support the delivery of depth data.
- [zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported](format/zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported.md) — A Boolean value that indicates whether the format supports zoom factors outside the range supported for depth delivery.

### Determining the auto focus system

- [autoFocusSystem](format/autofocussystem-swift.property.md) — The auto focus system the format uses.
- [AutoFocusSystem](format/autofocussystem-swift.enum.md) — An enumeration of auto focus systems.

### Determining Cinematic video support

- [cinematicVideoCaptureSupported](format/iscinematicvideocapturesupported.md) — Indicates whether the format supports Cinematic Video capture.
- [defaultSimulatedAperture](format/defaultsimulatedaperture.md) — Default shallow depth of field simulated aperture.
- [minSimulatedAperture](format/minsimulatedaperture.md) — Minimum supported shallow depth of field simulated aperture.
- [maxSimulatedAperture](format/maxsimulatedaperture.md) — Maximum supported shallow depth of field simulated aperture.
- [videoMaxZoomFactorForCinematicVideo](format/videomaxzoomfactorforcinematicvideo.md) — Indicates the maximum zoom factor available for the [videoZoomFactor](videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [videoMinZoomFactorForCinematicVideo](format/videominzoomfactorforcinematicvideo.md) — Indicates the minimum zoom factor available for the [videoZoomFactor](videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [videoFrameRateRangeForCinematicVideo](format/videoframeraterangeforcinematicvideo.md) — Indicates the minimum / maximum frame rates available when Cinematic Video capture is enabled on the device input.

### Determining lens smudge detection support

- [cameraLensSmudgeDetectionSupported](format/iscameralenssmudgedetectionsupported.md) — Whether camera lens smudge detection is supported.

### Determining smart framing support

- [smartFramingSupported](format/issmartframingsupported.md) — Returns `true` if smart framing is supported by the current format.

### Determining dynamic aspect ratio support

- [supportedDynamicAspectRatios](format/supporteddynamicaspectratios.md) — Indicates the supported aspect ratios for the device format.
- [- videoFieldOfViewForAspectRatio:geometricDistortionCorrected:](<format/videofieldofview(for_geometricdistortioncorrected_).md>) — Indicates the horizontal field of view for an aspect ratio, either uncorrected or corrected for geometric distortion.

### Determining Center Stage support

- [centerStageSupported](format/iscenterstagesupported.md) — A Boolean value that indicates whether the format supports Center Stage.
- [videoFrameRateRangeForCenterStage](format/videoframeraterangeforcenterstage.md) — The range of frame rates available when Center Stage is active.
- [videoMinZoomFactorForCenterStage](format/videominzoomfactorforcenterstage.md) — The minimum zoom factor available when Center Stage is active.
- [videoMaxZoomFactorForCenterStage](format/videomaxzoomfactorforcenterstage.md) — The maximum zoom factor available when Center Stage is active.

### Determining Portrait Effects support

- [portraitEffectSupported](format/isportraiteffectsupported.md) — A Boolean value that indicates whether the format supports the Portrait Effect feature.
- [portraitEffectsMatteStillImageDeliverySupported](format/isportraiteffectsmattestillimagedeliverysupported.md) — A Boolean indicating whether the device supports portrait matte effects in still-image capture.
- [videoFrameRateRangeForPortraitEffect](format/videoframeraterangeforportraiteffect.md) — The range of frame rates available when Portrait Effect is active.

### Determining Studio Light support

- [studioLightSupported](format/isstudiolightsupported.md) — A Boolean value that indicates whether the format supports Studio Light.
- [videoFrameRateRangeForStudioLight](format/videoframeraterangeforstudiolight.md) — A value that indicates the minimum and maximum frame rates available when a user enables Studio Light.

### Determining depth capture support

- [supportedDepthDataFormats](format/supporteddepthdataformats.md) — The list of data formats compatible with this video format.
- [supportedVideoZoomFactorsForDepthDataDelivery](format/supportedvideozoomfactorsfordepthdatadelivery.md) — The zoom factors that a format supports for depth data delivery. _(deprecated)_

### Deprecated

- [Deprecated symbols](../avcapturedevice-format-deprecated-symbols.md) — Review unsupported symbols and their replacements.

### Instance Properties

- [edgeLightSupported](format/isedgelightsupported.md) — Indicates whether the format supports the Edge Light feature.

## See Also

### Configuring capture formats

- [formats](formats.md) — The capture formats a device supports.
- [activeFormat](activeformat.md) — The capture format in use by the device.
- [activeDepthDataFormat](activedepthdataformat.md) — The currently active depth data format of the capture device.
