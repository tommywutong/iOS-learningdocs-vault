---
title: 'Breadcrumb: Using CoreLocation to track user movement'
apple_id: DTS40010048
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: CoreLocation
published: '2018-05-17'
source_url: https://developer.apple.com/library/archive/samplecode/Breadcrumb/Listings/Breadcrumb_BreadcrumbViewController_m.html
archived_at: '2026-07-27T06:57:01.898338Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Breadcrumb: Using CoreLocation to track user movement](Breadcrumb-%20Using%20CoreLocation%20to%20track%20user%20movement.md)


[Next](Breadcrumb-SettingsViewController.m.md)[Previous](Breadcrumb-BreadcrumbViewController.h.md)

# Breadcrumb/BreadcrumbViewController.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Main view controller for the application.
  Displays the user location along with the path traveled on an MKMapView.
  Implements the MKMapViewDelegate messages for tracking user location and managing overlays.
 */

#import "BreadcrumbViewController.h"

#import "CrumbPath.h"
#import "CrumbPathRenderer.h"
#import "SettingsKeys.h" // For keys: LocationTrackingAccuracyPrefsKey, LocationTrackingAccuracyPrefsKey, TrackLocationInBackgroundPrefsKey, PlaySoundOnLocationUpdatePrefsKey.

@import AVFoundation; // For AVAudioPlayer, AVAudioPlayerDelegate, and AVAudioSession.

#define kDebugShowArea 0 // For debugging purposes, draw the map polygon area in which the breacrumbs path is drawn.

@interface BreadcrumbViewController() <MKMapViewDelegate, CLLocationManagerDelegate, AVAudioPlayerDelegate>

@property (nonatomic, strong) AVAudioPlayer *audioPlayer;

@property (nonatomic, strong) CrumbPath *crumbs;
@property (nonatomic, strong) CrumbPathRenderer *crumbPathRenderer;
@property (nonatomic, strong) MKPolygonRenderer *drawingAreaRenderer; // Shown if kDebugShowArea is set to 1

@property (nonatomic, weak) IBOutlet MKMapView *map;

@property (nonatomic, strong) CLLocationManager *locationManager;

@end

#pragma mark -

@implementation BreadcrumbViewController

// Called for NSUserDefaultsDidChangeNotification.
- (void)settingsDidChange:(NSNotification *)notification
{
    NSUserDefaults *settings = [NSUserDefaults standardUserDefaults];

    // Update our location manager for these settings changes:

    // Accuracy (CLLocationAccuracy)
    CLLocationAccuracy desiredAccuracy = [settings doubleForKey:LocationTrackingAccuracyPrefsKey];
    self.locationManager.desiredAccuracy = desiredAccuracy;

    // Note:
    // For "PlaySoundOnLocationUpdatePrefsKey", code to play the sound later will read this default value.
    // For "TrackLocationInBackgroundPrefsKey", code to track location in background will read this default value.
}

#pragma mark - View Layout

- (void)viewDidAppear:(BOOL)animated
{
    [super viewDidAppear:animated];
    self.navigationItem.rightBarButtonItem.enabled = YES;

}
- (void)viewDidLoad
{
    [super viewDidLoad];

    [self initilizeAudioPlayer];
    [self initilizeLocationTracking];

    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(settingsDidChange:)
                                                 name:NSUserDefaultsDidChangeNotification
                                               object:nil];

    // Allow the user to change the tracking mode on the map view by placing this button in the navigation bar.
    MKUserTrackingBarButtonItem *userTrackingButton =
        [[MKUserTrackingBarButtonItem alloc] initWithMapView:self.map];
    self.navigationItem.leftBarButtonItem = userTrackingButton;
}

- (void)dealloc
{
    // Even though we are using ARC we still need to:

    // 1) Properly balance the unregister from the NSNotificationCenter,
    // which was registered previously in "viewDidLoad".
    //
    [[NSNotificationCenter defaultCenter] removeObserver:self];

    // 2) Manually unregister for delegate callbacks,
    // As of iOS 7, most system objects still use __unsafe_unretained delegates for compatibility.
    //
    self.locationManager.delegate = nil;
    self.audioPlayer.delegate = nil;
}

#pragma mark - Location Tracking

- (void)initilizeLocationTracking
{
    _locationManager = [[CLLocationManager alloc] init];
    assert(self.locationManager);

    self.locationManager.delegate = self; // Tells the location manager to send updates to this object.

    // Note: Doing the following will always provide access to our location.
    [self.locationManager requestAlwaysAuthorization];

    /**
    By default we use the best accuracy setting (kCLLocationAccuracyBest)

    You may instead want to use kCLLocationAccuracyBestForNavigation, which is the highest possible
    accuracy and combine it with additional sensor data.  Note that level of accuracy is intended
    for use in navigation applications that require precise position information at all times and
    are intended to be used only while the device is plugged in.
    */
    self.locationManager.desiredAccuracy =
        [[NSUserDefaults standardUserDefaults] doubleForKey:LocationTrackingAccuracyPrefsKey];

    // Start tracking the user's location.
    [self.locationManager startUpdatingLocation];

    // Observe the application going in and out of the background, so we can toggle location tracking.
    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(handleUIApplicationDidEnterBackgroundNotification:)
                                                 name:UIApplicationDidEnterBackgroundNotification
                                               object:nil];
    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(handleUIApplicationWillEnterForegroundNotification:)
                                                 name:UIApplicationWillEnterForegroundNotification
                                               object:nil];
}

- (void)handleUIApplicationDidEnterBackgroundNotification:(NSNotification *)note
{
    [self switchToBackgroundMode:YES];
}

- (void)handleUIApplicationWillEnterForegroundNotification :(NSNotification *)note
{
    [self switchToBackgroundMode:NO];
}

// Called when the app is moved to the background (user presses the home button) or to the foreground.
//
- (void)switchToBackgroundMode:(BOOL)background
{
    if ([[NSUserDefaults standardUserDefaults] boolForKey:TrackLocationInBackgroundPrefsKey])
    {
        return; // Nothing to do here, just keep tracking location.
    }

    if (background)
    {
        [self.locationManager stopUpdatingLocation];
    }
    else
    {
        [self.locationManager startUpdatingLocation];
    }
}

- (MKCoordinateRegion)coordinateRegionWithCenter:(CLLocationCoordinate2D)centerCoordinate
                       approximateRadiusInMeters:(CLLocationDistance)radiusInMeters
{
    // Multiplying by MKMapPointsPerMeterAtLatitude at the center is only approximate, since latitude isn't fixed.
    //
    double radiusInMapPoints = radiusInMeters*MKMapPointsPerMeterAtLatitude(centerCoordinate.latitude);
    MKMapSize radiusSquared = {radiusInMapPoints,radiusInMapPoints};

    MKMapPoint regionOrigin = MKMapPointForCoordinate(centerCoordinate);
    MKMapRect regionRect = (MKMapRect){regionOrigin, radiusSquared}; // Origin is the top-left corner.

    regionRect = MKMapRectOffset(regionRect, -radiusInMapPoints/2, -radiusInMapPoints/2);

    // clamp the rect to be within the world
    regionRect = MKMapRectIntersection(regionRect, MKMapRectWorld);

    MKCoordinateRegion region = MKCoordinateRegionForMapRect(regionRect);
    return region;
}

- (void)locationManager:(CLLocationManager *)manager didUpdateLocations:(NSArray *)locations
{
    if (locations != nil && locations.count > 0)
    {
        if ([[NSUserDefaults standardUserDefaults] boolForKey:PlaySoundOnLocationUpdatePrefsKey])
        {
            [self setSessionActiveWithMixing:YES]; // YES == duck if other audio is playing.
            [self playSound];
        }

        // We are not using deferred location updates, so always use the latest location.
        CLLocation *newLocation = locations[0];

        if (self.crumbs == nil)
        {
            // This is the first time we're getting a location update, so create
            // the CrumbPath and add it to the map.
            //
            _crumbs = [[CrumbPath alloc] initWithCenterCoordinate:newLocation.coordinate];
            [self.map addOverlay:self.crumbs level:MKOverlayLevelAboveRoads];

            // On the first location update only, zoom map to user location.
            CLLocationCoordinate2D newCoordinate = newLocation.coordinate;

            // Default -boundingMapRect size is 1km^2 centered on coord.
            MKCoordinateRegion region = [self coordinateRegionWithCenter:newCoordinate approximateRadiusInMeters:2500];

            [self.map setRegion:region animated:YES];
        }
        else
        {
            /**
            This is a subsequent location update.

            If the crumbs MKOverlay model object determines that the current location has moved
            far enough from the previous location, use the returned updateRect to redraw just
            the changed area.

            Note: cell-based devices will locate you using the triangulation of the cell towers.
            so you may experience spikes in location data (in small time intervals)
            due to cell tower triangulation.
            */
            BOOL boundingMapRectChanged = NO;
            MKMapRect updateRect = [self.crumbs addCoordinate:newLocation.coordinate boundingMapRectChanged:&boundingMapRectChanged];
            if (boundingMapRectChanged)
            {
                // MKMapView expects an overlay's boundingMapRect to never change (it's a readonly @property).
                // So for the MapView to recognize the overlay's size has changed, we remove it, then add it again.
                [self.map removeOverlays:self.map.overlays];
                _crumbPathRenderer = nil;
                [self.map addOverlay:self.crumbs level:MKOverlayLevelAboveRoads];

                MKMapRect r = self.crumbs.boundingMapRect;
                MKMapPoint pts[] = {
                    MKMapPointMake(MKMapRectGetMinX(r), MKMapRectGetMinY(r)),
                    MKMapPointMake(MKMapRectGetMinX(r), MKMapRectGetMaxY(r)),
                    MKMapPointMake(MKMapRectGetMaxX(r), MKMapRectGetMaxY(r)),
                    MKMapPointMake(MKMapRectGetMaxX(r), MKMapRectGetMinY(r)),
                };
                NSUInteger count = sizeof(pts) / sizeof(pts[0]);
                MKPolygon *boundingMapRectOverlay = [MKPolygon polygonWithPoints:pts count:count];
                [self.map addOverlay:boundingMapRectOverlay level:MKOverlayLevelAboveRoads];
            }
            else if (!MKMapRectIsNull(updateRect))
            {
                // There is a non null update rect.
                // Compute the currently visible map zoom scale
                MKZoomScale currentZoomScale = (CGFloat)(self.map.bounds.size.width / self.map.visibleMapRect.size.width);
                // Find out the line width at this zoom scale and outset the updateRect by that amount.
                CGFloat lineWidth = MKRoadWidthAtZoomScale(currentZoomScale);
                updateRect = MKMapRectInset(updateRect, -lineWidth, -lineWidth);
                // Ask the overlay view to update just the changed area.
                [self.crumbPathRenderer setNeedsDisplayInMapRect:updateRect];
            }
        }
    }
}

- (void)locationManager:(CLLocationManager *)manager didFailWithError:(NSError *)error
{
    NSLog(@"%s:%d %@", __func__, __LINE__, error);
}

static NSString *DescriptionOfCLAuthorizationStatus(CLAuthorizationStatus status)
{
    switch (status)
    {
        case kCLAuthorizationStatusNotDetermined:
            return @"kCLAuthorizationStatusNotDetermined";
        case kCLAuthorizationStatusRestricted:
            return @"kCLAuthorizationStatusRestricted";
        case kCLAuthorizationStatusDenied:
            return @"kCLAuthorizationStatusDenied";
        //case kCLAuthorizationStatusAuthorized: is the same as
        //kCLAuthorizationStatusAuthorizedAlways
        case kCLAuthorizationStatusAuthorizedAlways:
            return @"kCLAuthorizationStatusAuthorizedAlways";
        case kCLAuthorizationStatusAuthorizedWhenInUse:
            return @"kCLAuthorizationStatusAuthorizedWhenInUse";
    }
    return [NSString stringWithFormat:@"Unknown CLAuthorizationStatus value: %d", status];
}

- (void)locationManager:(CLLocationManager *)manager didChangeAuthorizationStatus:(CLAuthorizationStatus)status
{
    NSLog(@"%s:%d %@", __func__, __LINE__, DescriptionOfCLAuthorizationStatus(status));

    if (status == kCLAuthorizationStatusDenied)
    {
        // User denied access to our location, alert the user.
        UIAlertController *alert =
            [UIAlertController alertControllerWithTitle:NSLocalizedString(@"This device as restricted access to your location.", nil)
                                                message:NSLocalizedString(@"Open Settings to change access.", nil)
                                         preferredStyle:UIAlertControllerStyleAlert];

        UIAlertAction *okAction =
            [UIAlertAction actionWithTitle:NSLocalizedString(@"OK", nil)
                                                           style:UIAlertActionStyleCancel
                                                         handler:^(UIAlertAction * action) {
                                                                   [self.locationManager requestAlwaysAuthorization];
                                                               }];
        [alert addAction:okAction];

        UIAlertAction *settingsAction =
            [UIAlertAction actionWithTitle:NSLocalizedString(@"Settings", nil) style:UIAlertActionStyleDefault handler:^(UIAlertAction * action) {
            // Take the user to Settings app to possibly change permission.
            NSURL *settingsURL = [NSURL URLWithString:UIApplicationOpenSettingsURLString];
            if ([[UIApplication sharedApplication] canOpenURL:settingsURL])
            {
                [[UIApplication sharedApplication] openURL:settingsURL options:@{} completionHandler:nil];
            }
        }];
        [alert addAction:settingsAction];

        // Disable our tracking button (button tap will freeze if enabled when during restricted access).
        self.navigationItem.leftBarButtonItem.enabled = NO;

        [self presentViewController:alert animated:YES completion:^{ }];
    }
    else
    {
        if (status == kCLAuthorizationStatusAuthorizedAlways)
        {
            self.navigationItem.leftBarButtonItem.enabled = YES;
        }
    }
}

#pragma mark - MapKit

- (MKOverlayRenderer *)mapView:(MKMapView *)mapView rendererForOverlay:(id <MKOverlay>)overlay
{
    MKOverlayRenderer *renderer = nil;

    if ([overlay isKindOfClass:[CrumbPath class]])
    {
        if (self.crumbPathRenderer == nil)
        {
            _crumbPathRenderer = [[CrumbPathRenderer alloc] initWithOverlay:overlay];
        }
        renderer = self.crumbPathRenderer;
    }
    else if ([overlay isKindOfClass:[MKPolygon class]])
    {
#if kDebugShowArea
        if (![self.drawingAreaRenderer.polygon isEqual:overlay])
        {
            _drawingAreaRenderer = [[MKPolygonRenderer alloc] initWithPolygon:overlay];
            self.drawingAreaRenderer.fillColor = [[UIColor blueColor] colorWithAlphaComponent:0.25];
        }
        renderer = self.drawingAreaRenderer;
#endif
    }

    if (renderer == nil)
    {
        renderer = [[MKOverlayRenderer alloc] init];
    }

    return renderer;
}

#pragma mark - Audio Support

- (void)initilizeAudioPlayer
{
    // Set our default audio session state.
    [self setSessionActiveWithMixing:NO];

    NSURL *heroSoundURL = [NSURL fileURLWithPath:[[NSBundle mainBundle] pathForResource:@"Hero" ofType:@"aiff"]];
    assert(heroSoundURL);
    _audioPlayer = [[AVAudioPlayer alloc] initWithContentsOfURL:heroSoundURL error:nil];
}

- (void)setSessionActiveWithMixing:(BOOL)duckIfOtherAudioIsPlaying
{
    [[AVAudioSession sharedInstance] setCategory:AVAudioSessionCategoryPlayback
                                     withOptions:AVAudioSessionCategoryOptionMixWithOthers
                                           error:nil];

    if ([AVAudioSession sharedInstance].otherAudioPlaying && duckIfOtherAudioIsPlaying)
    {
        [[AVAudioSession sharedInstance] setCategory:AVAudioSessionCategoryPlayback
                                         withOptions:AVAudioSessionCategoryOptionMixWithOthers | AVAudioSessionCategoryOptionDuckOthers
                                               error:nil];
    }

    [[AVAudioSession sharedInstance] setActive:YES error:nil];
}

- (void)playSound
{
    assert(self.audioPlayer);
    if (self.audioPlayer && (self.audioPlayer.isPlaying == NO))
    {
        [self.audioPlayer prepareToPlay];
        [self.audioPlayer play];
    }
}

- (void)audioPlayerDidFinishPlaying:(AVAudioPlayer *)player successfully:(BOOL)flag
{
    [[AVAudioSession sharedInstance] setActive:NO error:nil];
}

@end
```

[Next](Breadcrumb-SettingsViewController.m.md)[Previous](Breadcrumb-BreadcrumbViewController.h.md)
