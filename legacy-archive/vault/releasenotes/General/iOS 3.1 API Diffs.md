---
title: iOS 3.1 API Diffs
apple_id: TP40009060
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2010-07-07'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iPhone31APIDiffs/index.html
archived_at: '2026-07-18T02:57:18.097237Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)


# iOS 3.0 to iOS 3.1 API Differences

## AVFoundation

AVAudioSession.hAdded [AVAudioSessionCategoryAudioProcessing](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryaudioprocessing)

## AddressBook

No changes

## AddressBookUI

No changes

## AudioToolbox

AudioConverter.hAdded [kAudioConverterErr_HardwareInUse](https://developer.apple.com/documentation/audiotoolbox/1624334-anonymous/kaudioconvertererr_hardwareinuse)Added [kAudioConverterPropertyCanResumeFromInterruption](https://developer.apple.com/documentation/audiotoolbox/1624333-anonymous/kaudioconverterpropertycanresumefrominterruption)Modified [AudioConverterNewSpecific()](https://developer.apple.com/documentation/audiotoolbox/1503356-audioconverternewspecific)

|  | Declaration |
| --- | --- |
| From | OSStatus AudioConverterNewSpecific ( const AudioStreamBasicDescription \*inSourceFormat, const AudioStreamBasicDescription \*inDestinationFormat, UInt32 inNumberClassDescriptions, AudioClassDescription \*inClassDescriptions, AudioConverterRef \*outAudioConverter); |
| To | OSStatus AudioConverterNewSpecific ( const AudioStreamBasicDescription \*inSourceFormat, const AudioStreamBasicDescription \*inDestinationFormat, UInt32 inNumberClassDescriptions, const AudioClassDescription \*inClassDescriptions, AudioConverterRef \*outAudioConverter); |

AudioQueue.hAdded [kAudioQueueErr_InvalidOfflineMode](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_invalidofflinemode)AudioServices.hAdded [kAudioSessionCategory_AudioProcessing](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_audioprocessing)Added [kAudioSessionIncompatibleCategory](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionincompatiblecategory)Added [kAudioSessionNoCategorySet](https://developer.apple.com/documentation/audiotoolbox/1618373-anonymous/kaudiosessionnocategoryset)Added [kAudioSessionProperty_OverrideCategoryDefaultToSpeaker](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_overridecategorydefaulttospeaker)Added [kAudioSessionProperty_OverrideCategoryEnableBluetoothInput](https://developer.apple.com/documentation/audiotoolbox/1618455-audio_session_property_identifie/kaudiosessionproperty_overridecategoryenablebluetoothinput)Added [kAudioSessionRouteChangeReason_NoSuitableRouteForCategory](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionroutechangereason_nosuitablerouteforcategory)ExtendedAudioFile.hAdded [kExtAudioFileError_CodecUnavailableInputConsumed](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileerror_codecunavailableinputconsumed)Added [kExtAudioFileError_CodecUnavailableInputNotConsumed](https://developer.apple.com/documentation/audiotoolbox/1623673-anonymous/kextaudiofileerror_codecunavailableinputnotconsumed)

## AudioUnit

No changes

## CFNetwork

No changes

## CoreAudio

No changes

## CoreData

No changes

## CoreFoundation

No changes

## CoreGraphics

No changes

## CoreLocation

No changes

## ExternalAccessory

No changes

## Foundation

No changes

## GameKit

No changes

## MapKit

No changes

## MediaPlayer

MPMediaLibrary.hAdded MPMediaLibraryChangeTypePlaylistsKeyAdded MPMediaLibraryChangeTypesUserInfoKey

## MessageUI

No changes

## MobileCoreServices

No changes

## OpenAL

No changes

## OpenGLES

glext.hAdded [#def GL_BLEND_DST_ALPHA_OES](https://developer.apple.com/documentation/opengles/gl_blend_dst_alpha_oes)Added [#def GL_BLEND_DST_RGB_OES](https://developer.apple.com/documentation/opengles/gl_blend_dst_rgb_oes)Added [#def GL_BLEND_EQUATION_ALPHA_OES](https://developer.apple.com/documentation/opengles/gl_blend_equation_alpha_oes)Added [#def GL_BLEND_EQUATION_RGB_OES](https://developer.apple.com/documentation/opengles/gl_blend_equation_rgb_oes)Added [#def GL_BLEND_SRC_ALPHA_OES](https://developer.apple.com/documentation/opengles/gl_blend_src_alpha_oes)Added [#def GL_BLEND_SRC_RGB_OES](https://developer.apple.com/documentation/opengles/gl_blend_src_rgb_oes)Added [#def GL_EXT_blend_minmax](https://developer.apple.com/documentation/opengles/gl_ext_blend_minmax)Added [#def GL_MAX_EXT](https://developer.apple.com/documentation/opengles/gl_max_ext)Added [#def GL_MIN_EXT](https://developer.apple.com/documentation/opengles/gl_min_ext)Added [#def GL_OES_blend_equation_separate](https://developer.apple.com/documentation/opengles/gl_oes_blend_equation_separate)Added [#def GL_OES_blend_func_separate](https://developer.apple.com/documentation/opengles/gl_oes_blend_func_separate)Added [#def GL_OES_fbo_render_mipmap](https://developer.apple.com/documentation/opengles/gl_oes_fbo_render_mipmap)Added [glBlendEquationSeparateOES()](https://developer.apple.com/documentation/opengles/1614279-glblendequationseparateoes)Added [glBlendFuncSeparateOES()](https://developer.apple.com/documentation/opengles/1614227-glblendfuncseparateoes)

## QuartzCore

CADisplayLink.hAdded [CADisplayLink](https://developer.apple.com/documentation/quartzcore/cadisplaylink)Added [-[CADisplayLink addToRunLoop:forMode:]](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1621323-add)Added [+[CADisplayLink displayLinkWithTarget:selector:]](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1621228-displaylinkwithtarget)Added [CADisplayLink.duration](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1621292-duration)Added [CADisplayLink.frameInterval](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1621231-frameinterval)Added [-[CADisplayLink invalidate]](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1621293-invalidate)Added [CADisplayLink.paused](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1621229-paused)Added [-[CADisplayLink removeFromRunLoop:forMode:]](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1621325-remove)Added [CADisplayLink.timestamp](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1621257-timestamp)

## Security

No changes

## StoreKit

No changes

## SystemConfiguration

No changes

## UIKit

UIImagePickerController.hAdded [UIImagePickerController.allowsEditing](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619137-allowsediting)Added [UIImagePickerController.cameraOverlayView](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619113-cameraoverlayview)Added [UIImagePickerController.cameraViewTransform](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619142-cameraviewtransform)Added [UIImagePickerController.showsCameraControls](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619129-showscameracontrols)Added [-[UIImagePickerController takePicture]](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619160-takepicture)Added [UIImagePickerController.videoMaximumDuration](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619146-videomaximumduration)Added [UIImagePickerController.videoQuality](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619154-videoquality)Added [UIImagePickerControllerQualityType](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/qualitytype)Added [UIImagePickerControllerQualityTypeHigh](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerqualitytype/uiimagepickercontrollerqualitytypehigh)Added [UIImagePickerControllerQualityTypeLow](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerqualitytype/uiimagepickercontrollerqualitytypelow)Added [UIImagePickerControllerQualityTypeMedium](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/qualitytype/typemedium)Added [UISaveVideoAtPathToSavedPhotosAlbum()](https://developer.apple.com/documentation/uikit/1619162-uisavevideoatpathtosavedphotosal)Added [UIVideoAtPathIsCompatibleWithSavedPhotosAlbum()](https://developer.apple.com/documentation/uikit/1619158-uivideoatpathiscompatiblewithsav)Modified [UIImagePickerController.allowsImageEditing](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619115-allowsimageediting)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | iOS 3.1 |

UIVideoEditorController.hAdded [UIVideoEditorController](https://developer.apple.com/documentation/uikit/uivideoeditorcontroller)Added [+[UIVideoEditorController canEditVideoAtPath:]](https://developer.apple.com/documentation/uikit/uivideoeditorcontroller/1622340-caneditvideo)Added [UIVideoEditorController.delegate](https://developer.apple.com/documentation/uikit/uivideoeditorcontroller/1622341-delegate)Added [UIVideoEditorController.videoMaximumDuration](https://developer.apple.com/documentation/uikit/uivideoeditorcontroller/1622338-videomaximumduration)Added [UIVideoEditorController.videoPath](https://developer.apple.com/documentation/uikit/uivideoeditorcontroller/1622343-videopath)Added [UIVideoEditorController.videoQuality](https://developer.apple.com/documentation/uikit/uivideoeditorcontroller/1622339-videoquality)Added [UIVideoEditorControllerDelegate](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate)Added [-[UIVideoEditorControllerDelegate videoEditorController:didFailWithError:]](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/1622342-videoeditorcontroller)Added [-[UIVideoEditorControllerDelegate videoEditorController:didSaveEditedVideoToPath:]](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/1622336-videoeditorcontroller)Added [-[UIVideoEditorControllerDelegate videoEditorControllerDidCancel:]](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/1622335-videoeditorcontrollerdidcancel)UIView.hModified [UIView.backgroundColor](https://developer.apple.com/documentation/uikit/uiview/1622591-backgroundcolor)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain) UIColor \*backgroundColor |
| To | @property(nonatomic, copy) UIColor \*backgroundColor |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
