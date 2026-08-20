---
title: QuickTime 7.1 Update Reference
apple_id: TP40004221
resource_type: Release Note
platform: macOS
topic: null
technology: QuickTime
published: '2006-08-14'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/Reference/QT7-1_Update_Reference/Constants.html
archived_at: '2026-07-26T19:54:15.493979Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [QuickTime 7.1 Update Reference](index.md)


[Next](RevisionHistory.md)[Previous](DataTypes.md)

# Constants

Inherits From

---

Not Applicable

Conforms To

---

Not Applicable

Import Statement

---

Not applicable

Availability

---

Not Applicable- [Visual Context Constants](#apple-f4xwc4dqnrsv64tfmyxwi33df5rw63ttorqw45c7m5zg65lqf5lgs43vmfwf6q3pnz2gk6dul5bw63ttorqw45dt "The following are values for kQTVisualContextTypeKey , a read-only CFStringRef that defines the type of the visual context:")

  The following are values for `kQTVisualContextTypeKey`, a read-only `CFStringRef` that defines the type of the visual context:

  #### Declaration

  #### Constants

  - `kQTVisualContextExpectedReadAheadKey`

    A `CFNumberRef` that defines the number of seconds ahead of real time that the client expects to pull images out of a visual context. Applications using the Core Video display link should set this attribute according to the value returned by `CVDisplayLinkGetOutputVideoLatency`.
  - `kQTVisualContextPixelBufferAttributesKey`

    A `CFDictionaryRef` that defines the dictionary containing pixel buffer attributes. See `kICMCompressionSessionPropertyID_PixelBufferPool` in ICM Compression Session Properties.
  - `kQTVisualContextTargetDimensionsKey`

    A `CFDictionaryRef` that defines the dictionary containing `kQTVisualContextTargetDimensions_WidthKey` and `kQTVisualContextTargetDimensions_HeightKey` values. This key is used as a hint to optimize certain media types, such as text, that can be rendered at any resolution. If this attribute is not set, the movie will be rendered at its native resolution.
  - `kQTVisualContextTargetDimensions_WidthKey`

    A `CFNumberRef` that defines the width, in pixels, of the rendering target.
  - `kQTVisualContextTargetDimensions_HeightKey`

    A `CFNumberRef` that defines the height, in pixels, of the rendering target.
  - `kQTVisualContextType_Direct3DTexture`

    The `CFString` value for use in dictionaries for identifying Direct3DTexture visual contexts.
- [kQTPropertyClass_ImageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df5rw63ttorqw45c7m5zg65lqf5vvcvcqojxxazlsor4ug3dbonzv6slnmftwkrdfonrxe2lqoruw63q "The following are aperture mode properties of image descriptions in QuickTime 7.1.")

  The following are aperture mode properties of image descriptions in QuickTime 7.1.

  #### Declaration

  `enum {
  kQTPropertyClass_ImageDescription = 'idsc',
  kICMImageDescriptionPropertyID_EncodedWidth = 'encw',
  kICMImageDescriptionPropertyID_EncodedHeight = 'ench',
  kICMImageDescriptionPropertyID_CleanAperture = 'clap',
  kICMImageDescriptionPropertyID_PixelAspectRatio = 'pasp',
  kICMImageDescriptionPropertyID_CleanApertureDisplayDimensions = 'cadi',
  kICMImageDescriptionPropertyID_ProductionApertureDisplayDimensions = 'prdi',
  kICMImageDescriptionPropertyID_EncodedPixelsDimensions = 'endi',
  kICMImageDescriptionPropertyID_DisplayWidth = 'disw',
  kICMImageDescriptionPropertyID_DisplayHeight = 'dish',
  kICMImageDescriptionPropertyID_ProductionDisplayWidth = 'pdsw',
  kICMImageDescriptionPropertyID_ProductionDisplayHeight = 'pdsh',
  kICMImageDescriptionPropertyID_NCLCColorInfo = 'nclc',
  kICMImageDescriptionPropertyID_FieldInfo = 'fiel',
  kICMImageDescriptionPropertyID_ClassicTrackWidth = 'claw',
  kICMImageDescriptionPropertyID_ClassicTrackHeight = 'clah',
  kICMImageDescriptionPropertyID_GammaLevel = 'gama',
  kICMImageDescriptionPropertyID_RowBytes = 'rowb',
  kICMImageDescriptionPropertyID_StepDuration = 'step',
  kICMImageDescriptionPropertyID_CleanApertureClipRect = 'cacr',
  kICMImageDescriptionPropertyID_CleanApertureMatrix = 'camx',
  kICMImageDescriptionPropertyID_ProductionApertureMatrix = 'pamx',
  kICMImageDescriptionPropertyID_SummaryString = 'isum',
  };`

  #### Constants

  - `kQTPropertyClass_ImageDescription`

    Class identifier for image description properties.
  - `kICMImageDescriptionPropertyID_EncodedWidth`

    The width of the encoded image. Usually, but not always, this is the ImageDescription's width field.
  - `kICMImageDescriptionPropertyID_EncodedHeight`

    The height of the encoded image. Usually, but not always, this is the ImageDescription's height field.
  - `kICMImageDescriptionPropertyID_CleanAperture`

    Describes the clean aperture of the buffer. If not specified explicitly in the image description, the default clean aperture (full encoded width and height) will be returned.
  - `kICMImageDescriptionPropertyID_PixelAspectRatio`

    Describes the pixel aspect ratio. If not specified explicitly in the image description, a square (1:1) pixel aspect ratio will be returned.
  - `kICMImageDescriptionPropertyID_CleanApertureDisplayDimensions`

    The dimensions at which the image can be displayed on a square-pixel display, generally calculated using the clean aperture and pixel aspect ratio. Note that this value is returned as a FixedPoint; the width and height can also be read separately as rounded SInt32s via `kICMImageDescriptionPropertyID_CleanApertureDisplayWidth` and `kICMImageDescriptionPropertyID_CleanApertureDisplayHeight`.
  - `kICMImageDescriptionPropertyID_ProductionApertureDisplayDimensions`

    The dimensions at which the image could be displayed on a square-pixel display, disregarding any clean aperture but honoring the pixel aspect ratio. This may be useful for authoring applications that want to expose the edge-processing region. For general viewing, use `kICMImageDescriptionPropertyID_CleanApertureDimensions` instead. Note that this value is returned as a FixedPoint; the width and height can also be read separately as rounded SInt32s via `kICMImageDescriptionPropertyID_ProductionApertureDisplayWidth` and `kICMImageDescriptionPropertyID_ProductionApertureDisplayHeight`.
  - `kICMImageDescriptionPropertyID_EncodedPixelsDimensions`

    Describes the dimensions of the encoded image. Note that this value is returned as a FixedPoint for convenience; the width and height can also be read separately as SInt32s via `kICMImageDescriptionPropertyID_EncodedWidth` and `kICMImageDescriptionPropertyID_EncodedHeight`.
  - `kICMImageDescriptionPropertyID_CleanApertureDisplayWidth`

    A width at which the buffer's image could be displayed on a square-pixel display, possibly calculated using the clean aperture and pixel aspect ratio.
  - `kICMImageDescriptionPropertyID_CleanApertureDisplayHeight`

    A height at which the buffer's image could be displayed on a square-pixel display, possibly calculated using the clean aperture and pixel aspect ratio.
  - `kICMImageDescriptionPropertyID_ProductionApertureDisplayWidth`

    A width at which the image could be displayed on a square-pixel display, disregarding any clean aperture but honoring the pixel aspect ratio. This may be useful for authoring applications that want to expose the edge processing region. For general viewing, use `kICMImageDescriptionPropertyID_DisplayWidth` instead.
  - `kICMImageDescriptionPropertyID_ProductionApertureDisplayHeight`

    A height at which the image could be displayed on a square-pixel display, disregarding any clean aperture but honoring the pixel aspect ratio. This may be useful for authoring applications that want to expose the edge processing region. For general viewing, use `kICMImageDescriptionPropertyID_DisplayHeight` instead.
  - `kICMImageDescriptionPropertyID_DisplayWidth`

    Synonym for `kICMImageDescriptionPropertyID_CleanApertureDisplayHeight`.
  - `kICMImageDescriptionPropertyID_DisplayHeight`

    Synonym for `kICMImageDescriptionPropertyID_CleanApertureDisplayHeight`.
  - `kICMImageDescriptionPropertyID_ProductionDisplayWidth`

    Synonym for `kICMImageDescriptionPropertyID_ProductionApertureDisplayWidth`.
  - `kICMImageDescriptionPropertyID_ProductionDisplayHeight`

    Synonym for `kICMImageDescriptionPropertyID_ProductionApertureDisplayHeight`.
  - `kICMImageDescriptionPropertyID_NCLCColorInfo`

    Color information, if available in the `NCLCColorInfoImageDescriptionExtension` format.
  - `kICMImageDescriptionPropertyID_CGColorSpace`

    A CGColorSpaceRef for the colorspace described by the image description, constructed from video color information or ICC Profile. It is important to note that the YCbCr matrix from the video color info is _not_ represented in the `CGColorSpaceRef`. The caller of `GetProperty` is responsible for releasing this, for example, by calling `CGColorSpaceRelease`. Only supported on Mac OS X.
  - `kICMImageDescriptionPropertyID_ICCProfile`

    A CFDataRef containing the serialized ICC profile described by the image description. The caller of `GetProperty` is responsible for releasing this, for example, by calling `CFRelease`.
  - `kICMImageDescriptionPropertyID_FieldInfo`

    Information about the number and order of fields, if available.
  - `kICMImageDescriptionPropertyID_ClassicTrackWidth`

    A track width suitable for passing to `NewMovieTrack` when creating a new track to hold this image data.
  - `kICMImageDescriptionPropertyID_ClassicTrackHeight`

    A track height suitable for passing to `NewMovieTrack` when creating a new track to hold this image data.
  - `kICMImageDescriptionPropertyID_GammaLevel`

    A Fixed for the gammma level described by the image description.
  - `kICMImageDescriptionPropertyID_RowBytes`

    The offset in bytes from the start of one row to the next. Only valid if the codec type is a chunky pixel format.
  - `kICMImageDescriptionPropertyID_StepDuration`

    Defines a duration for quantizing time. This is applicable for cases where a single media sample generates visual output that varies continuously through its duration. By interpreting this property, such a sample may be considered to have internal "step points" at multiples of the stepping duration. This can be used to throttle frame generation during playback, and when stepping using InterestingTime APIs. Setting a step duration with value zero removes any current step duration.
  - `kICMImageDescriptionPropertyID_CleanApertureClipRect`

    The clean aperture as a FixedRect in source coordinates, within the rectangle defined by the image description width and height, suitable for use as a source rectangle in a decompression sequence. For historical reasons, the DVCPROHD codecs store the production aperture display dimensions in the image description width and height; the actual encoded dimensions are smaller. For DVCPROHD, the clip rect will be relative to the image description width and height, not the encoded dimensions.
  - `kICMImageDescriptionPropertyID_CleanApertureMatrix`

    A matrix transforming the clean aperture clip rect to the origin, scaled to the clean aperture display dimensions. For historical reasons, the DVCPROHD codecs store the production aperture display dimensions in the image description width and height; the actual encoded dimensions are smaller. For DVCPROHD, the matrix will be relative to the image description width and height, not the encoded dimensions.
  - `kICMImageDescriptionPropertyID_ProductionApertureMatrix`

    A matrix transforming the image to the origin, scaled to the production aperture display dimensions. For historical reasons, the DVCPROHD codecs store the production aperture display dimensions in the image description width and height; the actual encoded dimensions are smaller. For DVCPROHD, the matrix will be relative to the image description width and height, not the encoded dimensions.
  - `kICMImageDescriptionPropertyID_SummaryString`

    A localized, human readable string summarizing the image as a CFString, that is, "Apple DV, 720 x 480 (640 x 480), Millions". The elements are: the codec name, the encoded pixels dimensions, then parenthetically the clean aperture mode dimensions, but only if they are different from the encoded pixels dimensions; then the depth. The codec name shall be from the localized decompressor component name string if exactly one decompressor with the correct cType is available; otherwise the string in the image description shall be used. The caller of GetProperty is responsible for releasing this CFString, for example, by calling CFRelease.
- [kQTPropertyClass_DVCompressor](#apple-f4xwc4dqnrsv64tfmyxwi33df5rw63ttorqw45c7m5zg65lqf5vvcvcqojxxazlsor4ug3dbonzv6rcwinxw24dsmvzxg33s "The following are DV Compressor component properties in QuickTime 7.1.")

  The following are DV Compressor component properties in QuickTime 7.1.

  #### Declaration

  `enum {
  kQTPropertyClass_DVCompressor = 'dvco',
  kDVCompressorPropertyID_ProgressiveScan = 'prog',
  kDVCompressorPropertyID_AspectRatio16x9 = '16x9',
  };`

  #### Constants

  - `kQTPropertyClass_DVCompressor`

    The property class for DV compressors. (Applicable to DV25, DV50, NTSC, PAL, PROPAL.)
  - `kDVCompressorPropertyID_ProgressiveScan`

    If set, indicates that the compressed frames should be marked as progressive-scan. By default, this flag is clear, meaning that frames should be marked as interlaced.
  - `kDVCompressorPropertyID_AspectRatio16x9`

    If set, indicates that the compressor should use a 16:9 picture aspect ratio. If clear, the compressor will use the default 4:3 picture aspect ratio.
- [kQTVisualPropertyID_ApertureMode](#apple-f4xwc4dqnrsv64tfmyxwi33df5rw63ttorqw45c7m5zg65lqf5vvcvcwnfzxkylmkbzg64dfoj2hsskel5axazlsor2xezknn5sgk "The following are visual properties of movies for aperture modes in QuickTime 7.1.")

  The following are visual properties of movies for aperture modes in QuickTime 7.1.

  #### Declaration

  `enum {
  kQTVisualPropertyID_ApertureMode = 'apmd',
  };`

  #### Constants

  - `kQTVisualPropertyID_ApertureMode`

    You can set the aperture mode property on a movie to indicate whether aspect ratio and clean aperture correction should be performed (`kQTPropertyClass_Visual` / `kQTVisualPropertyID_ApertureMode`). When a movie is in clean, production or encoded pixels aperture mode, each track's dimensions are overriden by special dimensions for that mode. The original track dimensions are preserved and can be restored by setting the movie into classic aperture mode. Aperture modes are not saved in movies. You can set the aperture mode property on a decompression session options object to indicate whether pixel buffers should be tagged to enable aspect ratio and clean aperture correction (`kQTPropertyClass_ICMDecompressionSessionOptions` / `kICMDecompressionSessionOptionsPropertyID_ApertureMode`).
- [Aperture Mode Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df5rw63ttorqw45c7m5zg65lqf5axazlsor2xezk7jvxwizk7kbzg64dfoj2gszlt "You can set the aperture mode property on a movie to indicate whether aspect ratio and clean aperture correction should be performed ( kQTPropertyClass_Visual/kQTVisualPropertyID_ApertureMode) . When a movie is in clean, production or encoded pixels aperture mode, each track’s dimensions are overriden by special dimensions for that mode. The original track dimensions are preserved and can be restored by setting the movie into classic aperture mode. Aperture modes are not saved in movies. You can set the aperture mode property on a decompression session options object to indicate whether pixel buffers should be tagged to enable aspect ratio and clean aperture correction ( kQTPropertyClass_ICMDecompressionSessionOptions / kICMDecompressionSessionOptionsPropertyID_ApertureMode ). The movie will be recalculated (laid out again) after one of the following happens: the movie’s aperture mode is changed; a track property corresponding to the current aperture mode is changed (that is, kQTVisualPropertyID_EncodedWidth for kQTApertureMode_EncodedPixels ). Track and movie matrices will stay constant unless explicitly changed. The aperture mode of a movie can be set during NewMovieFromProperties , and set/get using SetMovieProperties and GetMovieProperties . NewMovieFromProperties defaults to kQTApertureMode_Classic . Decompression session options also support this property.")

  You can set the aperture mode property on a movie to indicate whether aspect ratio and clean aperture correction should be performed (`kQTPropertyClass_Visual/kQTVisualPropertyID_ApertureMode)`. When a movie is in clean, production or encoded pixels aperture mode, each track’s dimensions are overriden by special dimensions for that mode. The original track dimensions are preserved and can be restored by setting the movie into classic aperture mode. Aperture modes are not saved in movies. You can set the aperture mode property on a decompression session options object to indicate whether pixel buffers should be tagged to enable aspect ratio and clean aperture correction (`kQTPropertyClass_ICMDecompressionSessionOptions` / `kICMDecompressionSessionOptionsPropertyID_ApertureMode`). The movie will be recalculated (laid out again) after one of the following happens: the movie’s aperture mode is changed; a track property corresponding to the current aperture mode is changed (that is, `kQTVisualPropertyID_EncodedWidth` for `kQTApertureMode_EncodedPixels`). Track and movie matrices will stay constant unless explicitly changed. The aperture mode of a movie can be set during `NewMovieFromProperties`, and set/get using `SetMovieProperties` and `GetMovieProperties`. `NewMovieFromProperties` defaults to `kQTApertureMode_Classic`. Decompression session options also support this property.

  #### Declaration

  `enum {
  kQTApertureMode_Classic = 'clas',
  kQTApertureMode_CleanAperture = 'clea',
  kQTApertureMode_ProductionAperture = 'prod',
  kQTApertureMode_EncodedPixels = 'enco'
  };`

  #### Constants

  - `kQTApertureMode_Classic`

    An aperture mode which gives compatibility with behavior in QuickTime 7.0.x and earlier. A movie in classic aperture mode uses track dimensions as set in `NewMovieTrack` and `SetTrackDimensions`. A decompression session in classic aperture mode does not set the clean aperture or pixel aspect ratio attachments on emitted pixel buffers. Movies default to classic aperture mode. If you call `SetTrackDimensions` on a track, the movie is automatically switched into classic aperture mode.
  - `kQTApertureMode_CleanAperture`

    An aperture mode for general display. Where possible, video will be displayed at the correct pixel aspect ratio, trimmed to the clean aperture. A movie in clean aperture mode sets each track's dimensions to match its `kQTVisualPropertyID_CleanApertureDimensions`. A decompression session in clean aperture mode sets the clean aperture and pixel aspect ratio attachments on emitted pixel buffers based on the image description.
  - `kQTApertureMode_ProductionAperture`

    An aperture mode for modal use in authoring applications. Where possible, video will be displayed at the correct pixel aspect ratio, but without trimming to the clean aperture so that the edge processing region can be viewed. A movie in production aperture mode sets each track's dimensions to match its `kQTVisualPropertyID_ProductionApertureDimensions`. A decompression session in production aperture mode sets the pixel aspect ratio attachments on emitted pixel buffers based on the image description.
  - `kQTApertureMode_EncodedPixels`

    An aperture mode for technical use. Displays all encoded pixels with no aspect ratio or clean aperture compensation. A movie in encoded pixels aperture mode sets each track's dimensions to match its `kQTVisualPropertyID_EncodedPixelsDimensions`. A decompression session in encoded pixels aperture mode does not set the clean aperture or pixel aspect ratio attachments on emitted pixel buffers.
- [Track Aperture Mode Dimension Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df5rw63ttorqw45c7m5zg65lqf5kheyldnnpuc4dfoj2hk4tfl5gw6zdfl5cgs3lfnzzws33ol5ihe33qmvzhi2lfom "The following are the vsual properties of tracks for aperture modes. A track's dimensions may vary depending on the movie's aperture mode. The dimensions for a given aperture mode may be accessed using these properties.")

  The following are the vsual properties of tracks for aperture modes. A track's dimensions may vary depending on the movie's aperture mode. The dimensions for a given aperture mode may be accessed using these properties.

  #### Declaration

  `enum {
  kQTVisualPropertyID_ClassicDimensions = 'cldi',
  kQTVisualPropertyID_CleanApertureDimensions = 'cadi',
  kQTVisualPropertyID_ProductionApertureDimensions = 'prdi',
  kQTVisualPropertyID_EncodedPixelsDimensions = 'endi',
  kQTVisualPropertyID_HasApertureModeDimensions = 'hamd',
  };`

  #### Constants

  - `kQTVisualPropertyID_ClassicDimensions`

    The track dimensions used in QuickTime 7.0.x and earlier. Setting this property is equivalent to calling SetTrackDimensions, except that SetTrackDimensions also changes the aperture mode to `kQTApertureMode_Classic`, and setting this property does not.
  - `kQTVisualPropertyID_CleanApertureDimensions`

    The track dimensions to use in clean aperture mode.
  - `kQTVisualPropertyID_ProductionApertureDimensions`

    The track dimensions to use in production aperture mode.
  - `kQTVisualPropertyID_EncodedPixelsDimensions`

    The track dimensions to use in encoded pixels aperture mode.
  - `kQTVisualPropertyID_HasApertureModeDimensions`

    True if aperture mode dimensions have been set on this movie, even if they are all identical to the classic dimensions (as is the case for content with square pixels and no edge processing region). This property can also be tested on a movie, where it is true if any track has aperture mode dimensions.
- [kCharacteristicSupportsApertureModes](#apple-f4xwc4dqnrsv64tfmyxwi33df5rw63ttorqw45c7m5zg65lqf5vug2dbojqwg5dfojuxg5djmnjxk4dqn5zhi42bobsxe5dvojsu233emvzq "Defines media characteristics for aperture modes.")

  Defines media characteristics for aperture modes.

  #### Declaration

  `enum {
  kCharacteristicSupportsApertureModes = 'apmd',
  }`

  #### Constants

  - `kCharacteristicSupportsApertureModes`

    Indicates that a media handler supports aperture modes, which enable video to be automatically scaled and cropped to compensate for non-square pixel aspect ratios and to trim possibly-dirty edge processing regions. The dimensions of such a track may change when the movie’s aperture mode is changed.
- [kQTSpecialScalingMode_FitWithinDimensions](#apple-f4xwc4dqnrsv64tfmyxwi33df5rw63ttorqw45c7m5zg65lqf5vvcvctobswg2lbnrjwgylmnfxgotlpmrsv6rtjorlws5dinfxei2lnmvxhg2lpnzzq "Defines scaling modes.")

  Defines scaling modes.

  #### Declaration

  `enum {
  kQTSpecialScalingMode_FitWithinDimensions = 'fit '
  };`

  #### Constants

  - `kQTSpecialScalingMode_FitWithinDimensions`

    Adjusts destination dimensions so that the source fits within the dimensions specified with `kQTSettingsImageWidth` and `kQTSettingsImageHeight` by fitting to the shortest side, and scales the source to the destination. Internally, the default scaling mode, which is based on the source aperture mode, is used for compression session, instead of this scaling mode..
- [QT Settings for Video, Image, Clean Aperture, and Pixel Aspect Ratio](#apple-f4xwc4dqnrsv64tfmyxwi33df5rw63ttorqw45c7m5zg65lqf5ivix2tmv2hi2lom5zv6ztpojpvm2lemvxv6slnmftwkx2dnrswc3s7ifygk4tuovzgkx3bnzsf6udjpbswyx2bonygky3ul5jgc5djn4 "Defines settings for video and image sizes, clean aperture and pixel aspect ratios.")

  Defines settings for video and image sizes, clean aperture and pixel aspect ratios.

  #### Declaration

  `enum {
  kQTSettingsVideoSize = 'isiz'
  kQTSettingsImageWidth = 'iwdt'
  QTSettingsImageHeight = 'ihgt'
  kQTSettingsCleanAperture = 'clap'
  kQTSettingsPixelAspectRatio = 'pasp'
  kQTSettingsScalingMode = 'scam'
  kQTSettingsUseCodecEnforcedDimensions = 'uenf'
  kQTSettingsDeinterlaceSource = 'dint'
  };`

  #### Constants

  - `kQTSettingsVideoSize`

    The video size-related container.
  - `kQTSettingsImageWidth`

    The destination width. If this is zero, it means the source width.
  - `QTSettingsImageHeight`

    The destination height. If this is zero, it means the source height.
  - `kQTSettingsCleanAperture`

    The clean aperture for compression sessions. If this is all zeros, it means no clean aperture (that is, full width and height).
  - `kQTSettingsPixelAspectRatio`

    The pixel aspect ratio for compression sessions. If this is all zeros, it means square pixels (that is, 1:1).
  - `kQTSettingsScalingMode`

    The scaling mode for compression sessions. If this is zero, it means scaling mode based on the source aperture mode.
  - `kQTSettingsUseCodecEnforcedDimensions`

    If `TRUE`, compressor’s enforced dimension overrides the image size settings.
  - `kQTSettingsDeinterlaceSource`

    If `TRUE`, deinterlacing is applied to source frames.
- [kICMDecompressionSessionOptionsPropertyID_ApertureMode](#apple-f4xwc4dqnrsv64tfmyxwi33df5rw63ttorqw45c7m5zg65lqf5vusq2nirswg33nobzgk43tnfxw4u3fonzws33oj5yhi2lpnzzva4tpobsxe5dzjfcf6qlqmvzhi5lsmvgw6zdf "Defines properties of decompression session options objects.")

  Defines properties of decompression session options objects.

  #### Declaration

  `enum {
  kICMDecompressionSessionOptionsPropertyID_ApertureMode = 'apmd', // OSType,
  Read/Write
  };`

  #### Constants

  - `kICMDecompressionSessionOptionsPropertyID_ApertureMode`

    You can set the aperture mode property on a decompression session options object to indicate whether pixel buffers should be tagged to enable aspect ratio and clean aperture correction. The default aperture mode for a decompression session is clean aperture mode.
- [kICMCompressionSessionOptionsPropertyID_ExtraAspectRatioStretchFactor](#apple-f4xwc4dqnrsv64tfmyxwi33df5rw63ttorqw45c7m5zg65lqf5vusq2ninxw24dsmvzxg2lpnzjwk43tnfxw4t3qoruw63ttkbzg64dfoj2hsskel5cxq5dsmfaxg4dfmn2feylunfxvg5dsmv2gg2cgmfrxi33s "Defines properties of compression sessions options objects.")

  Defines properties of compression sessions options objects.

  #### Declaration

  `enum {
  kICMCompressionSessionOptionsPropertyID_ExtraAspectRatioStretchFactor = 'exsf', // Fixed,
  Default fixed1,
  Read/Write
  };`

  #### Constants

  - `kICMCompressionSessionOptionsPropertyID_ExtraAspectRatioStretchFactor`

    Requests additional distortion to be applied to the aspect ratio in the `kICMScalingMode_Letterbox` and `kICMScalingMode_Trim` scaling modes. Values greater than fixed1 mean wider, values less than fixed1 mean narrower. For example, a value of X2Fix(2.0) would make the picture aspect ratio twice as wide.
- [Aperture scaling modes](#apple-f4xwc4dqnrsv64tfmyxwi33df5rw63ttorqw45c7m5zg65lqf5axazlsor2xezk7onrwc3djnztv63lpmrsxg "These constants indicate how source frames to a compression session should be scaled if the dimensions and/or display aspect ratio do not match.")

  These constants indicate how source frames to a compression session should be scaled if the dimensions and/or display aspect ratio do not match.

  #### Declaration

  `enum {
  kICMScalingMode_StretchCleanAperture = 'sc2c',
  kICMScalingMode_StretchProductionAperture = 'sp2p',
  kICMScalingMode_Letterbox = 'lett',
  kICMScalingMode_Trim = 'trim'
  };`

  #### Constants

  - `kICMScalingMode_StretchCleanAperture`

    The clean aperture of the source frames is scaled to the clean aperture of the destination.
  - `kICMScalingMode_StretchProductionAperture`

    The full width and height of source frames is scaled to the full width and height of the destination. This is the default if no other scaling mode is specified.
  - `kICMScalingMode_Letterbox`

    The clean aperture of the source frames is scaled to fit inside the clean aperture of the destination, preserving the original display aspect ratio. If the display aspect ratios are different, the source frames are centered with black bars above and below, or to the left and right.
  - `kICMScalingMode_Trim`

    The clean aperture of the source frames is scaled to cover the clean aperture of the destination, preserving the original display aspect ratio. If the display aspect ratios are different, the source frames are centered and cropped.
- [TrackApertureModeDimensionsAID](#apple-f4xwc4dqnrsv64tfmyxwi33df5rw63ttorqw45c7m5zg65lqf5kheyldnnaxazlsor2xezknn5sgkrdjnvsw443jn5xhgqkjiq "The type of atom that stores information for video correction in the movie resource. A child of the 'track' atom.")

  The type of atom that stores information for video correction in the movie resource. A child of the `'track'` atom.

  #### Declaration

  `enum {
  TrackApertureModeDimensionsAID = 'tapt',
  TrackCleanApertureDimensionsAID = 'clef',
  TrackProductionApertureDimensionsAID = 'prof',
  TrackEncodedPixelsDimensionsAID = 'enof',
  };`

  #### Constants

  - `TrackApertureModeDimensionsAID`

    The container atom.
  - `TrackCleanApertureDimensionsAID`

    The container atom.
  - `TrackProductionApertureDimensionsAID`

    The container atom.
  - `TrackEncodedPixelsDimensionsAID`

    The container atom.
- [kQTPropertyClass_ImageCompressor](#apple-f4xwc4dqnrsv64tfmyxwi33df5rw63ttorqw45c7m5zg65lqf5vvcvcqojxxazlsor4ug3dbonzv6slnmftwkq3pnvyhezltonxxe "The following is a property for image compressor components.")

  The following is a property for image compressor components.

  #### Declaration

  `enum {
  kQTPropertyClass_ImageCompressor = 'imco',
  };`

  #### Constants

  - `kQTPropertyClass_ImageCompressor`

    Property class for image compressor components.
- [movieExportSourceApertureMode](#apple-f4xwc4dqnrsv64tfmyxwi33df5rw63ttorqw45c7m5zg65lqf5ww65tjmvcxq4dpoj2fg33vojrwkqlqmvzhi5lsmvgw6zdf "The following sets the aperture mode on the decompression session.")

  The following sets the aperture mode on the decompression session.

  #### Declaration

  `enum {
  movieExportSourceApertureMode = 'srap',
  };`

  #### Constants

  - `movieExportSourceApertureMode`

    A pointer to an OSType. The source movie’s aperture mode.
- [kICMImageCompressorPropertyID_Enforced](#apple-f4xwc4dqnrsv64tfmyxwi33df5rw63ttorqw45c7m5zg65lqf5vusq2njfwwcz3finxw24dsmvzxg33skbzg64dfoj2hsskel5cw4ztpojrwkza "The following are enforced properties (introduced in QuickTime 7.0.4) for image compressor components. Image compressors that sometimes or always restrict image dimensions, clean aperture and/or pixel aspect ratio should support these properties. If these properties can change dynamically for a compressor (for example, in response to user interaction) then the properties should be listenable, and the compressor should call the listeners whenever the properties change. (In this case, the component's GetComponentPropertyInfo function should set the kComponentPropertyFlagWillNotifyListeners flag.) If a compressor has a mode in which these properties are flexible, then when the component is in that mode, (a) the component's GetComponentProperty function should return kQTPropertyAskLaterErr for these properties, and (b) the component's GetComponentPropertyInfo function should set the kComponentPropertyFlagCanGetLater flag for these properties.")

  The following are enforced properties (introduced in QuickTime 7.0.4) for image compressor components. Image compressors that sometimes or always restrict image dimensions, clean aperture and/or pixel aspect ratio should support these properties. If these properties can change dynamically for a compressor (for example, in response to user interaction) then the properties should be listenable, and the compressor should call the listeners whenever the properties change. (In this case, the component's `GetComponentPropertyInfo` function should set the `kComponentPropertyFlagWillNotifyListeners` flag.) If a compressor has a mode in which these properties are flexible, then when the component is in that mode, (a) the component's `GetComponentProperty` function should return `kQTPropertyAskLaterErr` for these properties, and (b) the component's `GetComponentPropertyInfo` function should set the `kComponentPropertyFlagCanGetLater` flag for these properties.

  #### Declaration

  `enum {
  kICMImageCompressorPropertyID_EnforcedEncodedWidth = 'enwi',
  kICMImageCompressorPropertyID_EnforcedEncodedHeight = 'enhe',
  kICMImageCompressorPropertyID_EnforcedCleanAperture = 'encl',
  kICMImageCompressorPropertyID_EnforcedPixelAspectRatio = 'enpa',
  kICMImageCompressorPropertyID_EnforcedFieldInfo = 'enfi',
  };`

  #### Constants

  - `kICMImageCompressorPropertyID_EnforcedEncodedWidth`

    The encoded width enforced for compressed frames.
  - `kICMImageCompressorPropertyID_EnforcedEncodedHeight`

    The encoded height enforced for compressed frames.
  - `kICMImageCompressorPropertyID_EnforcedCleanAperture`

    The clean aperture enforced for compressed frames.
  - `kICMImageCompressorPropertyID_EnforcedPixelAspectRatio`

    The pixel aspect ratio enforced for compressed frames.
  - `kICMImageCompressorPropertyID_EnforcedFieldInfo`

    The number and order of fields enforced for compressed frames.
- [Audio Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df5rw63ttorqw45c7m5zg65lqf5axkzdjn5pva4tpobsxe5djmvzq "The following is a list of the new audio properties available in QuickTime 7.1.")

  The following is a list of the new audio properties available in QuickTime 7.1.

  #### Declaration

  `enum {
  kQTAudioRenderQuality_PlaybackDefault = 0x8000,
  kQTAudioPropertyID_RenderQuality = 'qual',
  kQTMovieAudioExtractionAudioPropertyID_RenderQuality = 'qual',
  kQTAudioPropertyID_DeviceASBD = 'dasd',
  kQTAudioPropertyID_SummaryASBD = 'sasd',
  kQTAudioPropertyID_RateChangesPreservePitch = 'aucp',
  kQTAudioPropertyID_Pitch = 'pitc',
  kQTSCAudioPropertyID_RenderQuality = 'qlty',
  };`

  #### Constants

  - `kQTAudioPropertyID_DeviceASBD`

    This is a get-only property and returns the `AudioStreamBasicDescription` of the device the movie is playing to. The interesting fields are the sample rate, which reflects device’s current state, and the number of channels, which matches what is reported by `kQTAudioPropertyID_DeviceChannelLayout`.
  - `kQTAudioPropertyID_SummaryASBD`

    Get-only. Returns the `AudioStreamBasicDescription` corresponding to the Summary Mix of a movie. This describes non-interleaved, `Float32` linear PCM data, with a sample rate equal to the highest audio sample rate found among the sound tracks contributing to the AudioContext mix, and a number of channels that matches what is reported by `kQTAudioPropertyID_SummaryChannelLayout`.
  - `kQTAudioPropertyID_RateChangesPreservePitch`

    This property was introduced in QuickTime 7 and must be set in order for pitch changes to take effect. When the playback rate is not unity, audio must be resampled in order to play at the new rate. The default resampling affects the pitch of the audio (for example, playing at 2x speed raises the pitch by an octave, 1/2x lowers an octave). If this property is set on the Movie, an alternative algorithm may be used, which alters the speed without changing the pitch. Because this is more computationally expensive, this property may be silently ignored on some slow CPUs. Media handlers may query this movie property and honor it when performing Scaled Edits. This property can be specified as a property to the [NewMovieFromProperties](../QuickTime%207%20for%20Windows%20Update%20Guide/New%20Functions%2C%20Data%20Types%2C%20and%20Constants%20in%20QuickTime%207%20for%20Windows.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2omv3u233wnfsum4tpnvihe33qmvzhi2lfom) API. Currently, it has no effect when set on an open movie.
  - `kQTAudioPropertyID_Pitch`

    The movie pitch adjustment. This adjusts the pitch of all audio tracks that contribute to the AudioContext mix. Pitch control takes effect only if `kQTAudioPropertyID_RateChangesPreservePitch` is in effect; otherwise, returns `kQTMessageNotHandledErr`. The `Float32` value is specified in cents: 0.0 == no change, 1.0 == one cent up, 100.0 == one semi-tone up, -1.0 == one cent down. The most useful ranges for pitch are +/- 1200, that is, one octave.
  - `kQTAudioPropertyID_RenderQuality`

    Movie audio render quality takes effect for movie playback. `UInt32` values are as defined in AudioUnit/AudioUnitProperties.h and vary from 0x00 (`kRenderQuality_Min`) to 0x7F (`kRenderQuality_Max`). A special value `kQTAudioRenderQuality_PlaybackDefault`) is also defined which resets the quality settings of the playback processing chain to values that are chosen to be an optimal balance of performance and quality.
  - `kQTMovieAudioExtractionAudioPropertyID_RenderQuality`

    Sets the render quality to be used for this audio extraction session. `UInt32` values are as defined in AudioUnit/AudioUnitProperties.h and vary from 0x00(`kRenderQuality_Min`) to 0x7F (`kRenderQuality_Max`). A special value (`kQTAudioRenderQuality_PlaybackDefault`) is also defined which resets the quality settings to the same values that were chosen by default for playback.
  - `kQTSCAudioPropertyID_RenderQuality`

    Specifies the quality with which QuickTime should render the audio stream during the compression/decompression/transcode operation. Accepted constants are those used by AudioUnits (defined in AudioUnitProperties.h): `kRenderQuality_Max`, `kRenderQuality_High`, `kRenderQuality_Medium`, `kRenderQuality_Low`, `kRenderQuality_Min`. Available in QuickTimeComponents.h.
- [Metadata Constants](#apple-f4xwc4dqnrsv64tfmyxwi33df5rw63ttorqw45c7m5zg65lqf5gwk5dbmrqxiyk7inxw443umfxhi4y "The following is a list of new metadata constants available in QuickTime 7.1:")

  The following is a list of new metadata constants available in QuickTime 7.1:

  #### Declaration

  `enum {
  kQTMetaDataCommonKeyAlbum = 'albm',
  kQTMetaDataCommonKeyArtist = 'arts',
  kQTMetaDataCommonKeyArtwork = 'artw',
  kQTMetaDataCommonKeyChapterName = 'chap',
  kQTMetaDataCommonKeyComposer = 'comp',
  kQTMetaDataCommonKeyDescription = 'desc',
  kQTMetaDataCommonKeyGenre = 'genr',
  kQTMetaDataCommonKeyOriginalFormat = 'orif',
  kQTMetaDataCommonKeyOriginalSource = 'oris',
  kQTMetaDataCommonKeyPerformers = 'perf',
  kQTMetaDataCommonKeySoftware = 'soft',
  kQTMetaDataCommonKeyWriter = 'wrtr'
  };`

  #### Constants

  - `kQTMetaDataCommonKeyAlbum`

    Information to come.

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2006-08-14](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2demrrfvbuqmrnirxw45cmnfxgwrlmmvwwk3tujfcf6njr)

[Next](RevisionHistory.md)[Previous](DataTypes.md)

