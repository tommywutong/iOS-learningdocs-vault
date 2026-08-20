---
title: iOS 7.1 API Diffs
apple_id: TP40013973
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS71APIDiffs/index.html
archived_at: '2026-07-18T02:55:52.816945Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)


# iOS 7.0 to iOS 7.1 API Differences

## General Headers

/usr/include/dispatch/introspection.hAdded [dispatch_introspection_hook_queue_item_complete()](https://developer.apple.com/documentation/dispatch/1452972-dispatch_introspection_hook_queu)

## Accelerate

No changes

## Accounts

No changes

## AddressBook

No changes

## AddressBookUI

No changes

## AdSupport

No changes

## AssetsLibrary

No changes

## AudioToolbox

No changes

## AudioUnit

No changes

## AVFoundation

AVAudioSession.hAdded [AVAudioSessionErrorCodeCannotStartRecording](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/cannotstartrecording)Added [AVAudioSessionPortCarAudio](https://developer.apple.com/documentation/avfoundation/avaudiosessionportcaraudio)

## CFNetwork

No changes

## CoreAudio

No changes

## CoreBluetooth

CBError.hAdded [CBErrorConnectionFailed](https://developer.apple.com/documentation/corebluetooth/cberror/code/connectionfailed)CBUUID.hAdded [CBUUID.UUIDString](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518742-uuidstring)

## CoreData

No changes

## CoreFoundation

No changes

## CoreGraphics

No changes

## CoreImage

No changes

## CoreLocation

No changes

## CoreMedia

CMBufferQueue.hAdded [CMBufferGetSizeCallback](https://developer.apple.com/documentation/coremedia/cmbuffergetsizecallback)Added [CMBufferQueueGetTotalSize()](https://developer.apple.com/documentation/coremedia/1489793-cmbufferqueuegettotalsize)CMTime.hAdded [CMTimeMultiplyByRatio()](https://developer.apple.com/documentation/coremedia/1400891-cmtimemultiplybyratio)

## CoreMIDI

No changes

## CoreMotion

No changes

## CoreTelephony

No changes

## CoreText

No changes

## CoreVideo

No changes

## EventKit

No changes

## EventKitUI

No changes

## ExternalAccessory

No changes

## Foundation

No changes

## GameController

No changes

## GameKit

No changes

## GLKit

No changes

## GSS

No changes

## iAd

ADClient.h (Added)Added [ADClient](https://developer.apple.com/documentation/iad/adclient)Added [-[ADClient determineAppInstallationAttributionWithCompletionHandler:]](https://developer.apple.com/documentation/iad/adclient/1614672-determineappinstallationattribut)Added [+[ADClient sharedClient]](https://developer.apple.com/documentation/iad/adclient/1614686-sharedclient)

## ImageIO

No changes

## IOKit

No changes

## JavaScriptCore

No changes

## MapKit

MKAnnotationView.hModified [MKAnnotationView.annotation](https://developer.apple.com/documentation/mapkit/mkannotationview/1452613-annotation)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain) id<MKAnnotation> annotation |
| To | @property(nonatomic, strong) id<MKAnnotation> annotation |

Modified [MKAnnotationView.image](https://developer.apple.com/documentation/mapkit/mkannotationview/1452094-image)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain) UIImage \*image |
| To | @property(nonatomic, strong) UIImage \*image |

Modified [MKAnnotationView.leftCalloutAccessoryView](https://developer.apple.com/documentation/mapkit/mkannotationview/1452423-leftcalloutaccessoryview)

|  | Declaration |
| --- | --- |
| From | @property(retain, nonatomic) UIView \*leftCalloutAccessoryView |
| To | @property(strong, nonatomic) UIView \*leftCalloutAccessoryView |

Modified [MKAnnotationView.rightCalloutAccessoryView](https://developer.apple.com/documentation/mapkit/mkannotationview/1452233-rightcalloutaccessoryview)

|  | Declaration |
| --- | --- |
| From | @property(retain, nonatomic) UIView \*rightCalloutAccessoryView |
| To | @property(strong, nonatomic) UIView \*rightCalloutAccessoryView |

MKMapItem.hAdded [MKLaunchOptionsCameraKey](https://developer.apple.com/documentation/mapkit/mklaunchoptionscamerakey)Modified [MKMapItem.placemark](https://developer.apple.com/documentation/mapkit/mkmapitem/1452134-placemark)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, readonly, retain) MKPlacemark \*placemark |
| To | @property(nonatomic, readonly) MKPlacemark \*placemark |

Modified [MKMapItem.url](https://developer.apple.com/documentation/mapkit/mkmapitem/1452746-url)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain) NSURL \*url |
| To | @property(nonatomic, strong) NSURL \*url |

MKMapView.hModified [MKMapView.delegate](https://developer.apple.com/documentation/mapkit/mkmapview/1452115-delegate)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign) id<MKMapViewDelegate> delegate |
| To | @property(nonatomic, weak) id<MKMapViewDelegate> delegate |

MKMultiPoint.hRemoved MKMultiPoint.pointsAdded [-[MKMultiPoint points]](https://developer.apple.com/documentation/mapkit/mkmultipoint/1452425-points)MKOverlayPathRenderer.hModified [MKOverlayPathRenderer.fillColor](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452668-fillcolor)

|  | Declaration |
| --- | --- |
| From | @property(retain) UIColor \*fillColor |
| To | @property(strong) UIColor \*fillColor |

Modified [MKOverlayPathRenderer.strokeColor](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452175-strokecolor)

|  | Declaration |
| --- | --- |
| From | @property(retain) UIColor \*strokeColor |
| To | @property(strong) UIColor \*strokeColor |

MKOverlayPathView.hModified [MKOverlayPathView.fillColor](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/1617215-fillcolor)

|  | Declaration |
| --- | --- |
| From | @property(retain) UIColor \*fillColor |
| To | @property(strong) UIColor \*fillColor |

Modified [MKOverlayPathView.strokeColor](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/1617209-strokecolor)

|  | Declaration |
| --- | --- |
| From | @property(retain) UIColor \*strokeColor |
| To | @property(strong) UIColor \*strokeColor |

MKReverseGeocoder.hModified [MKReverseGeocoder.delegate](https://developer.apple.com/documentation/mapkit/mkreversegeocoder/1618478-delegate)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, assign) id<MKReverseGeocoderDelegate> delegate |
| To | @property(nonatomic, weak) id<MKReverseGeocoderDelegate> delegate |

MKUserLocation.hModified [MKUserLocation.heading](https://developer.apple.com/documentation/mapkit/mkuserlocation/1452721-heading)

|  | Declaration |
| --- | --- |
| From | @property(readonly, nonatomic, retain) CLHeading \*heading |
| To | @property(readonly, nonatomic) CLHeading \*heading |

Modified [MKUserLocation.location](https://developer.apple.com/documentation/mapkit/mkuserlocation/1452415-location)

|  | Declaration |
| --- | --- |
| From | @property(readonly, retain, nonatomic) CLLocation \*location |
| To | @property(readonly, nonatomic) CLLocation \*location |

MKUserTrackingBarButtonItem.hModified [MKUserTrackingBarButtonItem.mapView](https://developer.apple.com/documentation/mapkit/mkusertrackingbarbuttonitem/1620161-mapview)

|  | Declaration |
| --- | --- |
| From | @property(nonatomic, retain) MKMapView \*mapView |
| To | @property(nonatomic, strong) MKMapView \*mapView |

## MediaAccessibility

No changes

## MediaPlayer

MPContentItem.h (Added)Added [MPContentItem](https://developer.apple.com/documentation/mediaplayer/mpcontentitem)Added [MPContentItem.artwork](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620160-artwork)Added [MPContentItem.container](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620154-iscontainer)Added [MPContentItem.identifier](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620157-identifier)Added [-[MPContentItem initWithIdentifier:]](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620152-initwithidentifier)Added [MPContentItem.playable](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620158-isplayable)Added [MPContentItem.playbackProgress](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620153-playbackprogress)Added [MPContentItem.subtitle](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620155-subtitle)Added [MPContentItem.title](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620156-title)MPPlayableContentDataSource.h (Added)Added [MPPlayableContentDataSource](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource)Added [-[MPPlayableContentDataSource beginLoadingChildItemsAtIndexPath:completionHandler:]](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/1619508-beginloadingchilditemsatindexpat)Added [-[MPPlayableContentDataSource childItemsDisplayPlaybackProgressAtIndexPath:]](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/1619509-childitemsdisplayplaybackprogres)Added [-[MPPlayableContentDataSource contentItemAtIndexPath:]](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/1619505-contentitematindexpath)Added [-[MPPlayableContentDataSource numberOfChildItemsAtIndexPath:]](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/1619506-numberofchilditemsatindexpath)MPPlayableContentDelegate.h (Added)Added [MPPlayableContentDelegate](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate)Added [-[MPPlayableContentDelegate playableContentManager:initiatePlaybackOfContentItemAtIndexPath:completionHandler:]](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate/1620292-playablecontentmanager)MPPlayableContentManager.h (Added)Added [MPPlayableContentManager](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager)Added [-[MPPlayableContentManager beginUpdates]](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/1614801-beginupdates)Added [MPPlayableContentManager.dataSource](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/1614805-datasource)Added [MPPlayableContentManager.delegate](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/1614803-delegate)Added [-[MPPlayableContentManager endUpdates]](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/1614804-endupdates)Added [-[MPPlayableContentManager reloadData]](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/1614807-reloaddata)Added [+[MPPlayableContentManager sharedContentManager]](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/1614806-sharedcontentmanager)MPRemoteCommand.h (Added)Added [MPChangePlaybackRateCommand](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackratecommand)Added [MPChangePlaybackRateCommand.supportedPlaybackRates](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackratecommand/1622915-supportedplaybackrates)Added [MPFeedbackCommand](https://developer.apple.com/documentation/mediaplayer/mpfeedbackcommand)Added [MPFeedbackCommand.active](https://developer.apple.com/documentation/mediaplayer/mpfeedbackcommand/1622900-active)Added [MPFeedbackCommand.localizedTitle](https://developer.apple.com/documentation/mediaplayer/mpfeedbackcommand/1622905-localizedtitle)Added [MPRatingCommand](https://developer.apple.com/documentation/mediaplayer/mpratingcommand)Added [MPRatingCommand.maximumRating](https://developer.apple.com/documentation/mediaplayer/mpratingcommand/1622898-maximumrating)Added [MPRatingCommand.minimumRating](https://developer.apple.com/documentation/mediaplayer/mpratingcommand/1622902-minimumrating)Added [MPRemoteCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommand)Added [-[MPRemoteCommand addTarget:action:]](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/1622895-addtarget)Added [-[MPRemoteCommand addTargetWithHandler:]](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/1622910-addtargetwithhandler)Added [MPRemoteCommand.enabled](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/1622908-isenabled)Added [-[MPRemoteCommand removeTarget:]](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/1622903-removetarget)Added [-[MPRemoteCommand removeTarget:action:]](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/1622896-removetarget)Added [MPSkipIntervalCommand](https://developer.apple.com/documentation/mediaplayer/mpskipintervalcommand)Added [MPSkipIntervalCommand.preferredIntervals](https://developer.apple.com/documentation/mediaplayer/mpskipintervalcommand/1622899-preferredintervals)Added [MPRemoteCommandHandlerStatus](https://developer.apple.com/documentation/mediaplayer/mpremotecommandhandlerstatus)Added [MPRemoteCommandHandlerStatusCommandFailed](https://developer.apple.com/documentation/mediaplayer/mpremotecommandhandlerstatus/mpremotecommandhandlerstatuscommandfailed)Added [MPRemoteCommandHandlerStatusNoSuchContent](https://developer.apple.com/documentation/mediaplayer/mpremotecommandhandlerstatus/nosuchcontent)Added [MPRemoteCommandHandlerStatusSuccess](https://developer.apple.com/documentation/mediaplayer/mpremotecommandhandlerstatus/mpremotecommandhandlerstatussuccess)MPRemoteCommandCenter.h (Added)Added [MPRemoteCommandCenter](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter)Added [MPRemoteCommandCenter.bookmarkCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1619002-bookmarkcommand)Added [MPRemoteCommandCenter.changePlaybackRateCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618991-changeplaybackratecommand)Added [MPRemoteCommandCenter.dislikeCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618995-dislikecommand)Added [MPRemoteCommandCenter.likeCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618998-likecommand)Added [MPRemoteCommandCenter.nextTrackCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618999-nexttrackcommand)Added [MPRemoteCommandCenter.pauseCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618979-pausecommand)Added [MPRemoteCommandCenter.playCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1619000-playcommand)Added [MPRemoteCommandCenter.previousTrackCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618978-previoustrackcommand)Added [MPRemoteCommandCenter.ratingCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618986-ratingcommand)Added [MPRemoteCommandCenter.seekBackwardCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618982-seekbackwardcommand)Added [MPRemoteCommandCenter.seekForwardCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618981-seekforwardcommand)Added [+[MPRemoteCommandCenter sharedCommandCenter]](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618994-shared)Added [MPRemoteCommandCenter.skipBackwardCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618996-skipbackwardcommand)Added [MPRemoteCommandCenter.skipForwardCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618990-skipforwardcommand)Added [MPRemoteCommandCenter.stopCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618984-stopcommand)Added [MPRemoteCommandCenter.togglePlayPauseCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618992-toggleplaypausecommand)MPRemoteCommandEvent.h (Added)Added [MPChangePlaybackRateCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackratecommandevent)Added [MPChangePlaybackRateCommandEvent.playbackRate](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackratecommandevent/1616782-playbackrate)Added [MPFeedbackCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpfeedbackcommandevent)Added [MPFeedbackCommandEvent.negative](https://developer.apple.com/documentation/mediaplayer/mpfeedbackcommandevent/1616773-isnegative)Added [MPRatingCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpratingcommandevent)Added [MPRatingCommandEvent.rating](https://developer.apple.com/documentation/mediaplayer/mpratingcommandevent/1616764-rating)Added [MPRemoteCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpremotecommandevent)Added [MPRemoteCommandEvent.command](https://developer.apple.com/documentation/mediaplayer/mpremotecommandevent/1616776-command)Added [MPRemoteCommandEvent.timestamp](https://developer.apple.com/documentation/mediaplayer/mpremotecommandevent/1616784-timestamp)Added [MPSeekCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpseekcommandevent)Added [MPSeekCommandEvent.type](https://developer.apple.com/documentation/mediaplayer/mpseekcommandevent/1616783-type)Added [MPSkipIntervalCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpskipintervalcommandevent)Added [MPSkipIntervalCommandEvent.interval](https://developer.apple.com/documentation/mediaplayer/mpskipintervalcommandevent/1616767-interval)Added [MPSeekCommandEventType](https://developer.apple.com/documentation/mediaplayer/mpseekcommandeventtype)Added [MPSeekCommandEventTypeBeginSeeking](https://developer.apple.com/documentation/mediaplayer/mpseekcommandeventtype/mpseekcommandeventtypebeginseeking)Added [MPSeekCommandEventTypeEndSeeking](https://developer.apple.com/documentation/mediaplayer/mpseekcommandeventtype/mpseekcommandeventtypeendseeking)

## MediaToolbox

No changes

## MessageUI

No changes

## MobileCoreServices

No changes

## MultipeerConnectivity

No changes

## NewsstandKit

No changes

## OpenAL

No changes

## OpenGLES

EAGL.hAdded [EAGLContext.multiThreaded](https://developer.apple.com/documentation/opengles/eaglcontext/1624881-multithreaded)

## PassKit

No changes

## QuartzCore

No changes

## QuickLook

No changes

## SafariServices

No changes

## Security

No changes

## Social

No changes

## SpriteKit

SKAction.hAdded [+[SKAction setTexture:resize:]](https://developer.apple.com/documentation/spritekit/skaction/1417743-settexture)SKPhysicsBody.hAdded [+[SKPhysicsBody bodyWithBodies:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519736-bodywithbodies)Added [+[SKPhysicsBody bodyWithCircleOfRadius:center:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519692-init)Added [+[SKPhysicsBody bodyWithRectangleOfSize:center:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519936-bodywithrectangleofsize)SKView.hAdded [SKView.showsPhysics](https://developer.apple.com/documentation/spritekit/skview/1520389-showsphysics)

## StoreKit

SKReceiptRefreshRequest.hAdded [SKTerminateForInvalidReceipt()](https://developer.apple.com/documentation/storekit/1620081-skterminateforinvalidreceipt)

## SystemConfiguration

No changes

## Twitter

No changes

## UIKit

No changes

## VideoToolbox

No changes

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
