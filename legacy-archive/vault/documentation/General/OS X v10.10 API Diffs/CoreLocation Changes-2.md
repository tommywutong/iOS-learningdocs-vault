---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/CoreLocation.html
archived_at: '2026-07-15T07:34:51.746240Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# CoreLocation Changes

## CoreLocation (Added)

Added CLActivityType [enum]Added CLActivityType.AutomotiveNavigationAdded CLActivityType.FitnessAdded CLActivityType.OtherAdded CLActivityType.OtherNavigationAdded CLAuthorizationStatus [enum]Added CLAuthorizationStatus.AuthorizedAdded CLAuthorizationStatus.DeniedAdded CLAuthorizationStatus.NotDeterminedAdded CLAuthorizationStatus.RestrictedAdded CLCircularRegionAdded CLCircularRegion.centerAdded CLCircularRegion.init(center: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String!)Added CLCircularRegion.containsCoordinate(CLLocationCoordinate2D) -> BoolAdded CLCircularRegion.radiusAdded CLDeviceOrientation [enum]Added CLDeviceOrientation.FaceDownAdded CLDeviceOrientation.FaceUpAdded CLDeviceOrientation.LandscapeLeftAdded CLDeviceOrientation.LandscapeRightAdded CLDeviceOrientation.PortraitAdded CLDeviceOrientation.PortraitUpsideDownAdded CLDeviceOrientation.UnknownAdded CLError [enum]Added CLError.DeferredAccuracyTooLowAdded CLError.DeferredCanceledAdded CLError.DeferredDistanceFilteredAdded CLError.DeferredFailedAdded CLError.DeferredNotUpdatingLocationAdded CLError.DeniedAdded CLError.GeocodeCanceledAdded CLError.GeocodeFoundNoResultAdded CLError.GeocodeFoundPartialResultAdded CLError.HeadingFailureAdded CLError.LocationUnknownAdded CLError.NetworkAdded CLError.RangingFailureAdded CLError.RangingUnavailableAdded CLError.RegionMonitoringDeniedAdded CLError.RegionMonitoringFailureAdded CLError.RegionMonitoringResponseDelayedAdded CLError.RegionMonitoringSetupDelayedAdded CLGeocoderAdded CLGeocoder.cancelGeocode()Added CLGeocoder.geocodeAddressDictionary([NSObject: AnyObject]!, completionHandler: CLGeocodeCompletionHandler!)Added CLGeocoder.geocodeAddressString(String!, completionHandler: CLGeocodeCompletionHandler!)Added CLGeocoder.geocodeAddressString(String!, inRegion: CLRegion!, completionHandler: CLGeocodeCompletionHandler!)Added CLGeocoder.geocodingAdded CLGeocoder.reverseGeocodeLocation(CLLocation!, completionHandler: CLGeocodeCompletionHandler!)Added CLHeadingAdded CLHeading.descriptionAdded CLHeading.headingAccuracyAdded CLHeading.magneticHeadingAdded CLHeading.timestampAdded CLHeading.trueHeadingAdded CLHeading.xAdded CLHeading.yAdded CLHeading.zAdded CLLocationAdded CLLocation.altitudeAdded CLLocation.coordinateAdded CLLocation.init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, speed: CLLocationSpeed, timestamp: NSDate!)Added CLLocation.init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, timestamp: NSDate!)Added CLLocation.courseAdded CLLocation.descriptionAdded CLLocation.distanceFromLocation(CLLocation!) -> CLLocationDistanceAdded CLLocation.horizontalAccuracyAdded CLLocation.init(latitude: CLLocationDegrees, longitude: CLLocationDegrees)Added CLLocation.speedAdded CLLocation.timestampAdded CLLocation.verticalAccuracyAdded CLLocationCoordinate2D [struct]Added CLLocationCoordinate2D.latitudeAdded CLLocationCoordinate2D.longitudeAdded CLLocationManagerAdded CLLocationManager.authorizationStatus() -> CLAuthorizationStatus [class]Added CLLocationManager.deferredLocationUpdatesAvailable() -> Bool [class]Added CLLocationManager.delegateAdded CLLocationManager.desiredAccuracyAdded CLLocationManager.distanceFilterAdded CLLocationManager.headingAvailable() -> Bool [class]Added CLLocationManager.isMonitoringAvailableForClass(AnyClass!) -> Bool [class]Added CLLocationManager.locationAdded CLLocationManager.locationServicesEnabled() -> Bool [class]Added CLLocationManager.maximumRegionMonitoringDistanceAdded CLLocationManager.monitoredRegionsAdded CLLocationManager.purposeAdded CLLocationManager.regionMonitoringAvailable() -> Bool [class]Added CLLocationManager.regionMonitoringEnabled() -> Bool [class]Added CLLocationManager.requestStateForRegion(CLRegion!)Added CLLocationManager.significantLocationChangeMonitoringAvailable() -> Bool [class]Added CLLocationManager.startMonitoringForRegion(CLRegion!)Added CLLocationManager.startMonitoringSignificantLocationChanges()Added CLLocationManager.startUpdatingLocation()Added CLLocationManager.stopMonitoringForRegion(CLRegion!)Added CLLocationManager.stopMonitoringSignificantLocationChanges()Added CLLocationManager.stopUpdatingLocation()Added CLLocationManagerDelegateAdded CLLocationManagerDelegate.locationManager(CLLocationManager!, didChangeAuthorizationStatus: CLAuthorizationStatus)Added CLLocationManagerDelegate.locationManager(CLLocationManager!, didDetermineState: CLRegionState, forRegion: CLRegion!)Added CLLocationManagerDelegate.locationManager(CLLocationManager!, didEnterRegion: CLRegion!)Added CLLocationManagerDelegate.locationManager(CLLocationManager!, didExitRegion: CLRegion!)Added CLLocationManagerDelegate.locationManager(CLLocationManager!, didFailWithError: NSError!)Added CLLocationManagerDelegate.locationManager(CLLocationManager!, didFinishDeferredUpdatesWithError: NSError!)Added CLLocationManagerDelegate.locationManager(CLLocationManager!, didStartMonitoringForRegion: CLRegion!)Added CLLocationManagerDelegate.locationManager(CLLocationManager!, didUpdateLocations:[AnyObject]!)Added CLLocationManagerDelegate.locationManager(CLLocationManager!, didUpdateToLocation: CLLocation!, fromLocation: CLLocation!)Added CLLocationManagerDelegate.locationManager(CLLocationManager!, monitoringDidFailForRegion: CLRegion!, withError: NSError!)Added CLPlacemarkAdded CLPlacemark.ISOcountryCodeAdded CLPlacemark.addressDictionaryAdded CLPlacemark.administrativeAreaAdded CLPlacemark.areasOfInterestAdded CLPlacemark.countryAdded CLPlacemark.inlandWaterAdded CLPlacemark.localityAdded CLPlacemark.locationAdded CLPlacemark.nameAdded CLPlacemark.oceanAdded CLPlacemark.init(placemark: CLPlacemark!)Added CLPlacemark.postalCodeAdded CLPlacemark.regionAdded CLPlacemark.subAdministrativeAreaAdded CLPlacemark.subLocalityAdded CLPlacemark.subThoroughfareAdded CLPlacemark.thoroughfareAdded CLRegionAdded CLRegion.centerAdded CLRegion.init(circularRegionWithCenter: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String!)Added CLRegion.containsCoordinate(CLLocationCoordinate2D) -> BoolAdded CLRegion.identifierAdded CLRegion.notifyOnEntryAdded CLRegion.notifyOnExitAdded CLRegion.radiusAdded CLRegionState [enum]Added CLRegionState.InsideAdded CLRegionState.OutsideAdded CLRegionState.UnknownAdded CLBeaconMajorValueAdded CLBeaconMinorValueAdded CLGeocodeCompletionHandlerAdded CLHeadingComponentValueAdded CLLocationAccuracyAdded CLLocationCoordinate2DIsValid(CLLocationCoordinate2D) -> BoolAdded CLLocationCoordinate2DMake(CLLocationDegrees, CLLocationDegrees) -> CLLocationCoordinate2DAdded CLLocationDegreesAdded CLLocationDirectionAdded CLLocationDistanceAdded CLLocationSpeedAdded kCLDistanceFilterNoneAdded kCLErrorDomainAdded kCLErrorUserInfoAlternateRegionKeyAdded kCLHeadingFilterNoneAdded kCLLocationAccuracyBestAdded kCLLocationAccuracyBestForNavigationAdded kCLLocationAccuracyHundredMetersAdded kCLLocationAccuracyKilometerAdded kCLLocationAccuracyNearestTenMetersAdded kCLLocationAccuracyThreeKilometersAdded kCLLocationCoordinate2DInvalid

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
