---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Objective-C/UIKit.html
archived_at: '2026-07-18T02:57:28.267393Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# UIKit Changes for Objective-C

### UIKit

#### NSLayoutConstraint.h

Added [NSLayoutConstraint.firstAnchor](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1644261-firstanchor)Added [NSLayoutConstraint.secondAnchor](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1644260-secondanchor)

#### NSLayoutManager.h

Modified [NSLayoutManager.firstUnlaidCharacterIndex](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403067-firstunlaidcharacterindex)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSUInteger)firstUnlaidCharacterIndex ``` | -- |
| To | ``` @property(nonatomic, readonly) NSUInteger firstUnlaidCharacterIndex ``` | yes |

Modified [NSLayoutManager.firstUnlaidGlyphIndex](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403245-firstunlaidglyphindex)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSUInteger)firstUnlaidGlyphIndex ``` | -- |
| To | ``` @property(nonatomic, readonly) NSUInteger firstUnlaidGlyphIndex ``` | yes |

#### NSParagraphStyle.h

Added [NSParagraphStyle.defaultParagraphStyle](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1532681-default)Modified [NSTextTab](https://developer.apple.com/documentation/uikit/nstexttab)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCoding, NSCopying, NSSecureCoding |

#### UIAccessibility.h

Added [UIAccessibilityAssistiveTouchStatusDidChangeNotification](https://developer.apple.com/documentation/uikit/uiaccessibility/1648473-assistivetouchstatusdidchangenot)Added [UIAccessibilityHearingDeviceEar](https://developer.apple.com/documentation/uikit/uiaccessibility/hearingdeviceear)Added [UIAccessibilityIsAssistiveTouchRunning()](https://developer.apple.com/documentation/uikit/1648479-uiaccessibilityisassistivetouchr)

#### UIAccessibilityConstants.h

Added [UIAccessibilityTraitTabBar](https://developer.apple.com/documentation/uikit/uiaccessibilitytraittabbar)

#### UIAccessibilityCustomRotor.h (Added)

Added [NSObject.accessibilityCustomRotors](https://developer.apple.com/documentation/objectivec/nsobject/1649788-accessibilitycustomrotors)Added [UIAccessibilityCustomRotor](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor)Added [-[UIAccessibilityCustomRotor initWithName:itemSearchBlock:]](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/1649751-initwithname)Added [UIAccessibilityCustomRotor.itemSearchBlock](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/1649800-itemsearchblock)Added [UIAccessibilityCustomRotor.name](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/1649745-name)Added [UIAccessibilityCustomRotorItemResult](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotoritemresult)Added [-[UIAccessibilityCustomRotorItemResult initWithTargetElement:targetRange:]](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotoritemresult/1649911-init)Added [UIAccessibilityCustomRotorItemResult.targetElement](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotoritemresult/1649842-targetelement)Added [UIAccessibilityCustomRotorItemResult.targetRange](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotoritemresult/1649803-targetrange)Added [UIAccessibilityCustomRotorSearchPredicate](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotorsearchpredicate)Added [UIAccessibilityCustomRotorSearchPredicate.currentItem](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotorsearchpredicate/1649821-currentitem)Added [UIAccessibilityCustomRotorSearchPredicate.searchDirection](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotorsearchpredicate/1649916-searchdirection)Added NSObject(UIAccessibilityCustomRotor)Added [UIAccessibilityCustomRotorDirection](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/direction)Added [UIAccessibilityCustomRotorDirectionNext](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/direction/next)Added [UIAccessibilityCustomRotorDirectionPrevious](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/direction/previous)Added [UIAccessibilityCustomRotorSearch](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotorsearch)

#### UIAccessibilityElement.h

Added [UIAccessibilityElement.accessibilityFrameInContainerSpace](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/1649543-accessibilityframeincontainerspa)

#### UIActivity.h

Added [UIActivityType](https://developer.apple.com/documentation/uikit/uiactivity/activitytype)

#### UIActivityIndicatorView.h

Removed -[UIActivityIndicatorView isAnimating]Added [UIActivityIndicatorView.animating](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/2097554-isanimating)

#### UIActivityItemProvider.h

Modified [-[UIActivityItemSource activityViewController:dataTypeIdentifierForActivityType:]](https://developer.apple.com/documentation/uikit/uiactivityitemsource/1620456-activityviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)activityViewController:(UIActivityViewController *)activityViewController dataTypeIdentifierForActivityType:(NSString *)activityType ``` |
| To | ``` - (NSString *)activityViewController:(UIActivityViewController *)activityViewController dataTypeIdentifierForActivityType:(UIActivityType)activityType ``` |

Modified [-[UIActivityItemSource activityViewController:itemForActivityType:]](https://developer.apple.com/documentation/uikit/uiactivityitemsource/1620453-activityviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (id)activityViewController:(UIActivityViewController *)activityViewController itemForActivityType:(NSString *)activityType ``` |
| To | ``` - (id)activityViewController:(UIActivityViewController *)activityViewController itemForActivityType:(UIActivityType)activityType ``` |

Modified [-[UIActivityItemSource activityViewController:subjectForActivityType:]](https://developer.apple.com/documentation/uikit/uiactivityitemsource/1620455-activityviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)activityViewController:(UIActivityViewController *)activityViewController subjectForActivityType:(NSString *)activityType ``` |
| To | ``` - (NSString *)activityViewController:(UIActivityViewController *)activityViewController subjectForActivityType:(UIActivityType)activityType ``` |

Modified [-[UIActivityItemSource activityViewController:thumbnailImageForActivityType:suggestedSize:]](https://developer.apple.com/documentation/uikit/uiactivityitemsource/1620462-activityviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (UIImage *)activityViewController:(UIActivityViewController *)activityViewController thumbnailImageForActivityType:(NSString *)activityType suggestedSize:(CGSize)size ``` |
| To | ``` - (UIImage *)activityViewController:(UIActivityViewController *)activityViewController thumbnailImageForActivityType:(UIActivityType)activityType suggestedSize:(CGSize)size ``` |

#### UIApplication.h

Removed -[UIApplication isIgnoringInteractionEvents]Removed [-[UIApplication isRegisteredForRemoteNotifications]](https://developer.apple.com/documentation/uikit/uiapplication/1623069-isregisteredforremotenotificatio)Added [UIApplication.applicationIconBadgeNumber](https://developer.apple.com/documentation/uikit/uiapplication/1622918-applicationiconbadgenumber)Added [UIApplication.ignoringInteractionEvents](https://developer.apple.com/documentation/uikit/uiapplication/2097536-ignoringinteractionevents)Added [-[UIApplication openURL:options:completionHandler:]](https://developer.apple.com/documentation/uikit/uiapplication/1648685-open)Added [UIApplication.registeredForRemoteNotifications](https://developer.apple.com/documentation/uikit/uiapplication/1623069-isregisteredforremotenotificatio)Added [UIApplication.sharedApplication](https://developer.apple.com/documentation/uikit/uiapplication/1622975-shared)Added [-[UIApplicationDelegate application:didReceiveRemoteNotification:fetchCompletionHandler:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application)Added [-[UIApplicationDelegate application:userDidAcceptCloudKitShareWithMetadata:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/2206721-application)Added [UIApplicationExtensionPointIdentifier](https://developer.apple.com/documentation/uikit/uiapplication/extensionpointidentifier)Added [UIApplicationLaunchOptionsKey](https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey)Added [UIApplicationOpenURLOptionsKey](https://developer.apple.com/documentation/uikit/uiapplicationopenurloptionskey)Added [UIApplicationOpenURLOptionUniversalLinksOnly](https://developer.apple.com/documentation/uikit/uiapplication/openexternalurloptionskey/1648680-universallinksonly)Added [UIBackgroundFetchResultFailed](https://developer.apple.com/documentation/uikit/uibackgroundfetchresult/failed)Added [UIBackgroundFetchResultNewData](https://developer.apple.com/documentation/uikit/uibackgroundfetchresult/uibackgroundfetchresultnewdata)Added [UIBackgroundFetchResultNoData](https://developer.apple.com/documentation/uikit/uibackgroundfetchresult/nodata)Modified [-[UIApplication openURL:]](https://developer.apple.com/documentation/uikit/uiapplication/1622961-openurl)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 10.0 |

Modified [UIApplication.preferredContentSizeCategory](https://developer.apple.com/documentation/uikit/uiapplication/1623048-preferredcontentsizecategory)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *preferredContentSizeCategory ``` |
| To | ``` @property(nonatomic, readonly) UIContentSizeCategory preferredContentSizeCategory ``` |

Modified [-[UIApplicationDelegate application:didReceiveRemoteNotification:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623117-application)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 10.0 |

Modified [-[UIApplicationDelegate application:openURL:options:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623112-application)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<NSString *,id> *)options ``` |
| To | ``` - (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options ``` |

Modified [-[UIApplicationDelegate application:shouldAllowExtensionPointIdentifier:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623122-application)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)application:(UIApplication *)application shouldAllowExtensionPointIdentifier:(NSString *)extensionPointIdentifier ``` |
| To | ``` - (BOOL)application:(UIApplication *)application shouldAllowExtensionPointIdentifier:(UIApplicationExtensionPointIdentifier)extensionPointIdentifier ``` |

Modified [UIContentSizeCategoryAccessibilityExtraExtraExtraLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategoryaccessibilityextraextraextralarge)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryAccessibilityExtraExtraLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategoryaccessibilityextraextralarge)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryAccessibilityExtraLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategoryaccessibilityextralarge)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryAccessibilityLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategoryaccessibilitylarge)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryAccessibilityMedium](https://developer.apple.com/documentation/uikit/uicontentsizecategoryaccessibilitymedium)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryDidChangeNotification](https://developer.apple.com/documentation/uikit/uicontentsizecategorydidchangenotification)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryExtraExtraExtraLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategoryextraextraextralarge)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryExtraExtraLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategory/1623007-extraextralarge)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryExtraLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategory/1622960-extralarge)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryExtraSmall](https://developer.apple.com/documentation/uikit/uicontentsizecategoryextrasmall)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategorylarge)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryMedium](https://developer.apple.com/documentation/uikit/uicontentsizecategory/1622928-medium)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryNewValueKey](https://developer.apple.com/documentation/uikit/uicontentsizecategorynewvaluekey)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategorySmall](https://developer.apple.com/documentation/uikit/uicontentsizecategorysmall)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

#### UICloudSharingController.h (Added)

Added [UICloudSharingController](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller)Added [-[UICloudSharingController activityItemSource]](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/1649594-activityitemsource)Added [UICloudSharingController.availablePermissions](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/1649602-availablepermissions)Added [UICloudSharingController.delegate](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/1649595-delegate)Added [-[UICloudSharingController initWithPreparationHandler:]](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/1649607-initwithpreparationhandler)Added [-[UICloudSharingController initWithShare:container:]](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/1649597-initwithshare)Added [UICloudSharingController.share](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/1649601-share)Added [UICloudSharingControllerDelegate](https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate)Added [-[UICloudSharingControllerDelegate cloudSharingController:failedToSaveShareWithError:]](https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/1649606-cloudsharingcontroller)Added [-[UICloudSharingControllerDelegate cloudSharingControllerDidSaveShare:]](https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/1649605-cloudsharingcontrollerdidsavesha)Added [-[UICloudSharingControllerDelegate cloudSharingControllerDidStopSharing:]](https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/1649604-cloudsharingcontrollerdidstopsha)Added [-[UICloudSharingControllerDelegate itemThumbnailDataForCloudSharingController:]](https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/2274282-itemthumbnaildataforcloudsharing)Added [-[UICloudSharingControllerDelegate itemTitleForCloudSharingController:]](https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/2274280-itemtitleforcloudsharingcontroll)Added [-[UICloudSharingControllerDelegate itemTypeForCloudSharingController:]](https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/2274281-itemtypeforcloudsharingcontrolle)Added [UICloudSharingPermissionAllowPrivate](https://developer.apple.com/documentation/uikit/uicloudsharingpermissionoptions/uicloudsharingpermissionallowprivate)Added [UICloudSharingPermissionAllowPublic](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/permissionoptions/2274275-allowpublic)Added [UICloudSharingPermissionAllowReadOnly](https://developer.apple.com/documentation/uikit/uicloudsharingpermissionoptions/uicloudsharingpermissionallowreadonly)Added [UICloudSharingPermissionAllowReadWrite](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/permissionoptions/2274279-allowreadwrite)Added [UICloudSharingPermissionOptions](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/permissionoptions)Added [UICloudSharingPermissionStandard](https://developer.apple.com/documentation/uikit/uicloudsharingpermissionoptions/uicloudsharingpermissionstandard)

#### UICollectionView.h

Added [UICollectionView.prefetchDataSource](https://developer.apple.com/documentation/uikit/uicollectionview/1771768-prefetchdatasource)Added [UICollectionView.prefetchingEnabled](https://developer.apple.com/documentation/uikit/uicollectionview/1771771-prefetchingenabled)Added [UICollectionViewDataSourcePrefetching](https://developer.apple.com/documentation/uikit/uicollectionviewdatasourceprefetching)Added [-[UICollectionViewDataSourcePrefetching collectionView:cancelPrefetchingForItemsAtIndexPaths:]](https://developer.apple.com/documentation/uikit/uicollectionviewdatasourceprefetching/1771769-collectionview)Added [-[UICollectionViewDataSourcePrefetching collectionView:prefetchItemsAtIndexPaths:]](https://developer.apple.com/documentation/uikit/uicollectionviewdatasourceprefetching/1771767-collectionview)Modified [UICollectionView.indexPathsForSelectedItems](https://developer.apple.com/documentation/uikit/uicollectionview/1618099-indexpathsforselecteditems)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSArray<NSIndexPath *> *)indexPathsForSelectedItems ``` | -- |
| To | ``` @property(nonatomic, readonly) NSArray<NSIndexPath *> *indexPathsForSelectedItems ``` | yes |

Modified [UICollectionView.indexPathsForVisibleItems](https://developer.apple.com/documentation/uikit/uicollectionview/1618020-indexpathsforvisibleitems)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSArray<NSIndexPath *> *)indexPathsForVisibleItems ``` | -- |
| To | ``` @property(nonatomic, readonly) NSArray<NSIndexPath *> *indexPathsForVisibleItems ``` | yes |

Modified [UICollectionView.numberOfSections](https://developer.apple.com/documentation/uikit/uicollectionview/1618028-numberofsections)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSInteger)numberOfSections ``` | -- |
| To | ``` @property(nonatomic, readonly) NSInteger numberOfSections ``` | yes |

Modified [UICollectionView.visibleCells](https://developer.apple.com/documentation/uikit/uicollectionview/1618056-visiblecells)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSArray<__kindof UICollectionViewCell *> *)visibleCells ``` | -- |
| To | ``` @property(nonatomic, readonly) NSArray<__kindof UICollectionViewCell *> *visibleCells ``` | yes |

Modified [-[UICollectionViewDataSource collectionView:cellForItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/1618029-collectionview)

|  | Declaration |
| --- | --- |
| From | ``` - (UICollectionViewCell *)collectionView:(UICollectionView *)collectionView cellForItemAtIndexPath:(NSIndexPath *)indexPath ``` |
| To | ``` - (__kindof UICollectionViewCell *)collectionView:(UICollectionView *)collectionView cellForItemAtIndexPath:(NSIndexPath *)indexPath ``` |

#### UICollectionViewFlowLayout.h

Added [UICollectionViewFlowLayoutAutomaticSize](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/1779556-automaticsize)

#### UICollectionViewLayout.h

Added [UICollectionViewLayout.invalidationContextClass](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617790-invalidationcontextclass)Added [UICollectionViewLayout.layoutAttributesClass](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617774-layoutattributesclass)Modified [UICollectionViewLayout.collectionViewContentSize](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617796-collectionviewcontentsize)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGSize)collectionViewContentSize ``` | -- |
| To | ``` @property(nonatomic, readonly) CGSize collectionViewContentSize ``` | yes |

#### UIColor.h

Added [UIColor.blackColor](https://developer.apple.com/documentation/uikit/uicolor/1621929-black)Added [UIColor.blueColor](https://developer.apple.com/documentation/uikit/uicolor/1621947-bluecolor)Added [UIColor.brownColor](https://developer.apple.com/documentation/uikit/uicolor/1621950-browncolor)Added [UIColor.clearColor](https://developer.apple.com/documentation/uikit/uicolor/1621945-clearcolor)Added [+[UIColor colorWithDisplayP3Red:green:blue:alpha:]](https://developer.apple.com/documentation/uikit/uicolor/1648569-colorwithdisplayp3red)Added [UIColor.cyanColor](https://developer.apple.com/documentation/uikit/uicolor/1621942-cyancolor)Added [UIColor.darkGrayColor](https://developer.apple.com/documentation/uikit/uicolor/1621952-darkgray)Added [UIColor.grayColor](https://developer.apple.com/documentation/uikit/uicolor/1621941-gray)Added [UIColor.greenColor](https://developer.apple.com/documentation/uikit/uicolor/1621946-greencolor)Added [-[UIColor initWithDisplayP3Red:green:blue:alpha:]](https://developer.apple.com/documentation/uikit/uicolor/1648568-init)Added [UIColor.lightGrayColor](https://developer.apple.com/documentation/uikit/uicolor/1621932-lightgraycolor)Added [UIColor.magentaColor](https://developer.apple.com/documentation/uikit/uicolor/1621934-magentacolor)Added [UIColor.orangeColor](https://developer.apple.com/documentation/uikit/uicolor/1621956-orangecolor)Added [UIColor.purpleColor](https://developer.apple.com/documentation/uikit/uicolor/1621923-purplecolor)Added [UIColor.redColor](https://developer.apple.com/documentation/uikit/uicolor/1621924-redcolor)Added [UIColor.whiteColor](https://developer.apple.com/documentation/uikit/uicolor/1621920-whitecolor)Added [UIColor.yellowColor](https://developer.apple.com/documentation/uikit/uicolor/1621953-yellow)

#### UIContentSizeCategory.h (Added)

Added [UIContentSizeCategory](https://developer.apple.com/documentation/uikit/uicontentsizecategory)Added [UIContentSizeCategoryUnspecified](https://developer.apple.com/documentation/uikit/uicontentsizecategory/1771727-unspecified)Modified [UIContentSizeCategoryAccessibilityExtraExtraExtraLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategoryaccessibilityextraextraextralarge)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryAccessibilityExtraExtraLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategoryaccessibilityextraextralarge)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryAccessibilityExtraLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategoryaccessibilityextralarge)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryAccessibilityLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategoryaccessibilitylarge)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryAccessibilityMedium](https://developer.apple.com/documentation/uikit/uicontentsizecategoryaccessibilitymedium)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryDidChangeNotification](https://developer.apple.com/documentation/uikit/uicontentsizecategorydidchangenotification)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryExtraExtraExtraLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategoryextraextraextralarge)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryExtraExtraLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategory/1623007-extraextralarge)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryExtraLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategory/1622960-extralarge)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryExtraSmall](https://developer.apple.com/documentation/uikit/uicontentsizecategoryextrasmall)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryLarge](https://developer.apple.com/documentation/uikit/uicontentsizecategorylarge)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryMedium](https://developer.apple.com/documentation/uikit/uicontentsizecategory/1622928-medium)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategoryNewValueKey](https://developer.apple.com/documentation/uikit/uicontentsizecategorynewvaluekey)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

Modified [UIContentSizeCategorySmall](https://developer.apple.com/documentation/uikit/uicontentsizecategorysmall)

|  | Header |
| --- | --- |
| From | UIKit/UIApplication.h |
| To | UIKit/UIContentSizeCategory.h |

#### UIContentSizeCategoryAdjusting.h (Added)

Added [UIContentSizeCategoryAdjusting](https://developer.apple.com/documentation/uikit/uicontentsizecategoryadjusting)Added [UIContentSizeCategoryAdjusting.adjustsFontForContentSizeCategory](https://developer.apple.com/documentation/uikit/uicontentsizecategoryadjusting/1771731-adjustsfontforcontentsizecategor)

#### UIControl.h

Modified [UIControl.allControlEvents](https://developer.apple.com/documentation/uikit/uicontrol/1618225-allcontrolevents)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIControlEvents)allControlEvents ``` | -- |
| To | ``` @property(nonatomic, readonly) UIControlEvents allControlEvents ``` | yes |

Modified [UIControl.allTargets](https://developer.apple.com/documentation/uikit/uicontrol/1618207-alltargets)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSSet *)allTargets ``` | -- |
| To | ``` @property(nonatomic, readonly) NSSet *allTargets ``` | yes |

#### UIDevice.h

Added [UIDevice.currentDevice](https://developer.apple.com/documentation/uikit/uidevice/1620014-currentdevice)

#### UIDynamicAnimator.h

Modified [UIDynamicAnimator.elapsedTime](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621202-elapsedtime)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSTimeInterval)elapsedTime ``` | -- |
| To | ``` @property(nonatomic, readonly) NSTimeInterval elapsedTime ``` | yes |

#### UIEvent.h

Modified [UIEvent.allTouches](https://developer.apple.com/documentation/uikit/uievent/1613836-alltouches)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSSet<UITouch *> *)allTouches ``` | -- |
| To | ``` @property(nonatomic, readonly) NSSet<UITouch *> *allTouches ``` | yes |

#### UIFocus.h

Added [UIFocusEnvironment.preferredFocusEnvironments](https://developer.apple.com/documentation/uikit/uifocusenvironment/1648972-preferredfocusenvironments)Added [UIFocusItem](https://developer.apple.com/documentation/uikit/uifocusitem)Added [UIFocusItem.canBecomeFocused](https://developer.apple.com/documentation/uikit/uifocusitem/1648965-canbecomefocused)Added [UIFocusUpdateContext.nextFocusedItem](https://developer.apple.com/documentation/uikit/uifocusupdatecontext/1648967-nextfocuseditem)Added [UIFocusUpdateContext.previouslyFocusedItem](https://developer.apple.com/documentation/uikit/uifocusupdatecontext/1648962-previouslyfocuseditem)Added [UIFocusHeadingNone](https://developer.apple.com/documentation/uikit/uifocusheading/uifocusheadingnone)Modified [UIFocusEnvironment.preferredFocusedView](https://developer.apple.com/documentation/uikit/uifocusenvironment/1616830-preferredfocusedview)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | tvOS 10.0 | yes |

Modified [UIFocusGuide](https://developer.apple.com/documentation/uikit/uifocusguide)

|  | Header |
| --- | --- |
| From | UIKit/UIFocus.h |
| To | UIKit/UIFocusGuide.h |

Modified [UIFocusGuide.enabled](https://developer.apple.com/documentation/uikit/uifocusguide/1616838-isenabled)

|  | Header |
| --- | --- |
| From | UIKit/UIFocus.h |
| To | UIKit/UIFocusGuide.h |

Modified [UIFocusGuide.preferredFocusedView](https://developer.apple.com/documentation/uikit/uifocusguide/1616848-preferredfocusedview)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | UIKit/UIFocus.h |
| To | tvOS 10.0 | UIKit/UIFocusGuide.h |

#### UIFocusGuide.h (Added)

Added [UIFocusGuide.preferredFocusEnvironments](https://developer.apple.com/documentation/uikit/uifocusguide/1648230-preferredfocusenvironments)Modified [UIFocusGuide](https://developer.apple.com/documentation/uikit/uifocusguide)

|  | Header |
| --- | --- |
| From | UIKit/UIFocus.h |
| To | UIKit/UIFocusGuide.h |

Modified [UIFocusGuide.enabled](https://developer.apple.com/documentation/uikit/uifocusguide/1616838-isenabled)

|  | Header |
| --- | --- |
| From | UIKit/UIFocus.h |
| To | UIKit/UIFocusGuide.h |

Modified [UIFocusGuide.preferredFocusedView](https://developer.apple.com/documentation/uikit/uifocusguide/1616848-preferredfocusedview)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | UIKit/UIFocus.h |
| To | tvOS 10.0 | UIKit/UIFocusGuide.h |

#### UIFont.h

Added [UIFont.familyNames](https://developer.apple.com/documentation/uikit/uifont/1619040-familynames)Added [+[UIFont preferredFontForTextStyle:compatibleWithTraitCollection:]](https://developer.apple.com/documentation/uikit/uifont/1771762-preferredfontfortextstyle)Modified [UIFont.fontDescriptor](https://developer.apple.com/documentation/uikit/uifont/1619037-fontdescriptor)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIFontDescriptor *)fontDescriptor ``` | -- |
| To | ``` @property(nonatomic, readonly) UIFontDescriptor *fontDescriptor ``` | yes |

Modified [+[UIFont preferredFontForTextStyle:]](https://developer.apple.com/documentation/uikit/uifont/1619030-preferredfont)

|  | Declaration |
| --- | --- |
| From | ``` + (UIFont *)preferredFontForTextStyle:(NSString *)style ``` |
| To | ``` + (UIFont *)preferredFontForTextStyle:(UIFontTextStyle)style ``` |

#### UIFontDescriptor.h

Added [+[UIFontDescriptor preferredFontDescriptorWithTextStyle:compatibleWithTraitCollection:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1771750-preferredfontdescriptor)Added [UIFontTextStyle](https://developer.apple.com/documentation/uikit/uifont/textstyle)Modified [UIFontDescriptor.fontAttributes](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616698-fontattributes)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSDictionary<NSString *,id> *)fontAttributes ``` | -- |
| To | ``` @property(nonatomic, readonly) NSDictionary<NSString *,id> *fontAttributes ``` | yes |

Modified [+[UIFontDescriptor preferredFontDescriptorWithTextStyle:]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616705-preferredfontdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` + (UIFontDescriptor *)preferredFontDescriptorWithTextStyle:(NSString *)style ``` |
| To | ``` + (UIFontDescriptor *)preferredFontDescriptorWithTextStyle:(UIFontTextStyle)style ``` |

#### UIGeometry.h

Modified [NSValue.CGAffineTransformValue](https://developer.apple.com/documentation/foundation/nsvalue/1624512-cgaffinetransformvalue)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGAffineTransform)CGAffineTransformValue ``` | -- |
| To | ``` @property(nonatomic, readonly) CGAffineTransform CGAffineTransformValue ``` | yes |

Modified [NSValue.CGPointValue](https://developer.apple.com/documentation/foundation/nsvalue/1624534-cgpointvalue)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGPoint)CGPointValue ``` | -- |
| To | ``` @property(nonatomic, readonly) CGPoint CGPointValue ``` | yes |

Modified [NSValue.CGRectValue](https://developer.apple.com/documentation/foundation/nsvalue/1624506-cgrectvalue)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGRect)CGRectValue ``` | -- |
| To | ``` @property(nonatomic, readonly) CGRect CGRectValue ``` | yes |

Modified [NSValue.CGSizeValue](https://developer.apple.com/documentation/foundation/nsvalue/1624489-cgsizevalue)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGSize)CGSizeValue ``` | -- |
| To | ``` @property(nonatomic, readonly) CGSize CGSizeValue ``` | yes |

Modified [NSValue.CGVectorValue](https://developer.apple.com/documentation/foundation/nsvalue/1624486-cgvectorvalue)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGVector)CGVectorValue ``` | -- |
| To | ``` @property(nonatomic, readonly) CGVector CGVectorValue ``` | yes |

Modified [NSValue.UIEdgeInsetsValue](https://developer.apple.com/documentation/foundation/nsvalue/1624517-uiedgeinsetsvalue)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIEdgeInsets)UIEdgeInsetsValue ``` | -- |
| To | ``` @property(nonatomic, readonly) UIEdgeInsets UIEdgeInsetsValue ``` | yes |

Modified [NSValue.UIOffsetValue](https://developer.apple.com/documentation/foundation/nsvalue/1624526-uioffsetvalue)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIOffset)UIOffsetValue ``` | -- |
| To | ``` @property(nonatomic, readonly) UIOffset UIOffsetValue ``` | yes |

#### UIGestureRecognizer.h

Added [UIGestureRecognizer.requiresExclusiveTouchType](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1649116-requiresexclusivetouchtype)Modified [UIGestureRecognizer.numberOfTouches](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1624200-numberoftouches)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSUInteger)numberOfTouches ``` | -- |
| To | ``` @property(nonatomic, readonly) NSUInteger numberOfTouches ``` | yes |

#### UIGestureRecognizerSubclass.h

Modified [-[UIGestureRecognizer touchesEstimatedPropertiesUpdated:]](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1619997-touchesestimatedpropertiesupdate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)touchesEstimatedPropertiesUpdated:(NSSet *)touches ``` |
| To | ``` - (void)touchesEstimatedPropertiesUpdated:(NSSet<UITouch *> *)touches ``` |

#### UIGraphicsImageRenderer.h (Added)

Added [UIGraphicsImageRenderer](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer)Added [-[UIGraphicsImageRenderer imageWithActions:]](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/1649230-imagewithactions)Added [-[UIGraphicsImageRenderer initWithBounds:format:]](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/1649229-init)Added [-[UIGraphicsImageRenderer initWithSize:]](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/1649231-initwithsize)Added [-[UIGraphicsImageRenderer initWithSize:format:]](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/1649236-initwithsize)Added [-[UIGraphicsImageRenderer JPEGDataWithCompressionQuality:actions:]](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/1649234-jpegdatawithcompressionquality)Added [-[UIGraphicsImageRenderer PNGDataWithActions:]](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/1649233-pngdata)Added [UIGraphicsImageRendererContext](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderercontext)Added [UIGraphicsImageRendererContext.currentImage](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderercontext/1649237-currentimage)Added [UIGraphicsImageRendererFormat](https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat)Added [UIGraphicsImageRendererFormat.opaque](https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/1649238-opaque)Added [UIGraphicsImageRendererFormat.prefersExtendedRange](https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/1649227-prefersextendedrange)Added [UIGraphicsImageRendererFormat.scale](https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/1649228-scale)Added [UIGraphicsImageDrawingActions](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/drawingactions)

#### UIGraphicsPDFRenderer.h (Added)

Added [UIGraphicsPDFRenderer](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer)Added [-[UIGraphicsPDFRenderer initWithBounds:format:]](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer/1649127-init)Added [-[UIGraphicsPDFRenderer PDFDataWithActions:]](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer/1649120-pdfdatawithactions)Added [-[UIGraphicsPDFRenderer writePDFToURL:withActions:error:]](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer/1649119-writepdf)Added [UIGraphicsPDFRendererContext](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext)Added [-[UIGraphicsPDFRendererContext addDestinationWithName:atPoint:]](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/1649128-adddestinationwithname)Added [-[UIGraphicsPDFRendererContext beginPage]](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/1649124-beginpage)Added [-[UIGraphicsPDFRendererContext beginPageWithBounds:pageInfo:]](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/1649126-beginpage)Added [UIGraphicsPDFRendererContext.pdfContextBounds](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/1649122-pdfcontextbounds)Added [-[UIGraphicsPDFRendererContext setDestinationWithName:forRect:]](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/1649118-setdestinationwithname)Added [-[UIGraphicsPDFRendererContext setURL:forRect:]](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/1649125-seturl)Added [UIGraphicsPDFRendererFormat](https://developer.apple.com/documentation/uikit/uigraphicspdfrendererformat)Added [UIGraphicsPDFRendererFormat.documentInfo](https://developer.apple.com/documentation/uikit/uigraphicspdfrendererformat/1649130-documentinfo)Added [UIGraphicsPDFDrawingActions](https://developer.apple.com/documentation/uikit/uigraphicspdfdrawingactions)

#### UIGraphicsRenderer.h (Added)

Added [UIGraphicsRenderer](https://developer.apple.com/documentation/uikit/uigraphicsrenderer)Added [UIGraphicsRenderer.allowsImageOutput](https://developer.apple.com/documentation/uikit/uigraphicsrenderer/1648553-allowsimageoutput)Added [UIGraphicsRenderer.format](https://developer.apple.com/documentation/uikit/uigraphicsrenderer/1648556-format)Added [-[UIGraphicsRenderer initWithBounds:]](https://developer.apple.com/documentation/uikit/uigraphicsrenderer/1648548-init)Added [-[UIGraphicsRenderer initWithBounds:format:]](https://developer.apple.com/documentation/uikit/uigraphicsrenderer/1648558-init)Added [UIGraphicsRendererContext](https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext)Added [UIGraphicsRendererContext.CGContext](https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/1648560-cgcontext)Added [-[UIGraphicsRendererContext clipToRect:]](https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/1648549-cliptorect)Added [-[UIGraphicsRendererContext fillRect:]](https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/1648554-fill)Added [-[UIGraphicsRendererContext fillRect:blendMode:]](https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/1648552-fill)Added [UIGraphicsRendererContext.format](https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/1648557-format)Added [-[UIGraphicsRendererContext strokeRect:]](https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/1648555-strokerect)Added [-[UIGraphicsRendererContext strokeRect:blendMode:]](https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/1648562-stroke)Added [UIGraphicsRendererFormat](https://developer.apple.com/documentation/uikit/uigraphicsrendererformat)Added [UIGraphicsRendererFormat.bounds](https://developer.apple.com/documentation/uikit/uigraphicsrendererformat/1648563-bounds)Added [+[UIGraphicsRendererFormat defaultFormat]](https://developer.apple.com/documentation/uikit/uigraphicsrendererformat/1648550-default)

#### UIGraphicsRendererSubclass.h (Added)

Added [+[UIGraphicsRenderer contextWithFormat:]](https://developer.apple.com/documentation/uikit/uigraphicsrenderer/1649838-contextwithformat)Added [+[UIGraphicsRenderer prepareCGContext:withRendererContext:]](https://developer.apple.com/documentation/uikit/uigraphicsrenderer/1649837-prepare)Added [+[UIGraphicsRenderer rendererContextClass]](https://developer.apple.com/documentation/uikit/uigraphicsrenderer/1649730-renderercontextclass)Added [-[UIGraphicsRenderer runDrawingActions:completionActions:error:]](https://developer.apple.com/documentation/uikit/uigraphicsrenderer/1649839-rundrawingactions)Added [UIGraphicsDrawingActions](https://developer.apple.com/documentation/uikit/uigraphicsdrawingactions)Added UIGraphicsRenderer(UIGraphicsRendererProtected)

#### UIGuidedAccessRestrictions.h

Modified [UIGuidedAccessRestrictionDelegate.guidedAccessRestrictionIdentifiers](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate/1621160-guidedaccessrestrictionidentifie)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSArray<NSString *> *)guidedAccessRestrictionIdentifiers ``` | -- |
| To | ``` @property(nonatomic, readonly) NSArray<NSString *> *guidedAccessRestrictionIdentifiers ``` | yes |

#### UIImage.h

Added [UIImage.imageRendererFormat](https://developer.apple.com/documentation/uikit/uiimage/1649497-imagerendererformat)Added [-[UIImage imageWithHorizontallyFlippedOrientation]](https://developer.apple.com/documentation/uikit/uiimage/2113668-imagewithhorizontallyflippedorie)

#### UIImageView.h

Removed -[UIImageView isAnimating]Added [UIImageView.animating](https://developer.apple.com/documentation/uikit/uiimageview/2097534-isanimating)

#### UIImpactFeedbackGenerator.h (Added)

Added [UIImpactFeedbackStyle](https://developer.apple.com/documentation/uikit/uiimpactfeedbackgenerator/feedbackstyle)Added [UIImpactFeedbackStyleHeavy](https://developer.apple.com/documentation/uikit/uiimpactfeedbackstyle/uiimpactfeedbackstyleheavy)Added [UIImpactFeedbackStyleLight](https://developer.apple.com/documentation/uikit/uiimpactfeedbackstyle/uiimpactfeedbackstylelight)Added [UIImpactFeedbackStyleMedium](https://developer.apple.com/documentation/uikit/uiimpactfeedbackstyle/uiimpactfeedbackstylemedium)

#### UIInputViewController.h

Added [-[UIInputViewController handleInputModeListFromView:withEvent:]](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/1649584-handleinputmodelistfromview)Added [UITextDocumentProxy.documentInputMode](https://developer.apple.com/documentation/uikit/uitextdocumentproxy/1649583-documentinputmode)

#### UIInterface.h

Added [UIDisplayGamut](https://developer.apple.com/documentation/uikit/uidisplaygamut)Added [UIDisplayGamutP3](https://developer.apple.com/documentation/uikit/uidisplaygamut/uidisplaygamutp3)Added [UIDisplayGamutSRGB](https://developer.apple.com/documentation/uikit/uidisplaygamut/srgb)Added [UIDisplayGamutUnspecified](https://developer.apple.com/documentation/uikit/uidisplaygamut/unspecified)Added [UITraitEnvironmentLayoutDirection](https://developer.apple.com/documentation/uikit/uitraitenvironmentlayoutdirection)Added [UITraitEnvironmentLayoutDirectionLeftToRight](https://developer.apple.com/documentation/uikit/uitraitenvironmentlayoutdirection/uitraitenvironmentlayoutdirectionlefttoright)Added [UITraitEnvironmentLayoutDirectionRightToLeft](https://developer.apple.com/documentation/uikit/uitraitenvironmentlayoutdirection/righttoleft)Added [UITraitEnvironmentLayoutDirectionUnspecified](https://developer.apple.com/documentation/uikit/uitraitenvironmentlayoutdirection/unspecified)Added [UIUserInterfaceStyle](https://developer.apple.com/documentation/uikit/uiuserinterfacestyle)Added [UIUserInterfaceStyleDark](https://developer.apple.com/documentation/uikit/uiuserinterfacestyle/dark)Added [UIUserInterfaceStyleLight](https://developer.apple.com/documentation/uikit/uiuserinterfacestyle/light)Added [UIUserInterfaceStyleUnspecified](https://developer.apple.com/documentation/uikit/uiuserinterfacestyle/unspecified)Modified [UIUserInterfaceLayoutDirection](https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection)

|  | Header |
| --- | --- |
| From | UIKit/UIView.h |
| To | UIKit/UIInterface.h |

Modified [UIUserInterfaceLayoutDirectionLeftToRight](https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection/lefttoright)

|  | Header |
| --- | --- |
| From | UIKit/UIView.h |
| To | UIKit/UIInterface.h |

Modified [UIUserInterfaceLayoutDirectionRightToLeft](https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection/righttoleft)

|  | Header |
| --- | --- |
| From | UIKit/UIView.h |
| To | UIKit/UIInterface.h |

#### UIKitDefines.h

Added #def UIKIT_CLASS_AVAILABLE_IOS_ONLYAdded #def UIKIT_CLASS_AVAILABLE_WATCHOS_ONLYAdded [#def UIKIT_DEFINE_AS_PROPERTIES](https://developer.apple.com/documentation/uikit/uikit_define_as_properties)Added [#def UIKIT_REMOVE_ZERO_FROM_SWIFT](https://developer.apple.com/documentation/uikit/uikit_remove_zero_from_swift)Added [#def UIKIT_STRING_ENUMS](https://developer.apple.com/documentation/uikit/uikit_string_enums)

#### UILabel.h

Modified [UILabel](https://developer.apple.com/documentation/uikit/uilabel)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSCoding, UIContentSizeCategoryAdjusting |

#### UINibLoading.h

Modified [-[NSObject awakeFromNib]](https://developer.apple.com/documentation/objectivec/nsobject/1402907-awakefromnib)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

#### UINotificationFeedbackGenerator.h (Added)

Added [UINotificationFeedbackType](https://developer.apple.com/documentation/uikit/uinotificationfeedbackgenerator/feedbacktype)Added [UINotificationFeedbackTypeError](https://developer.apple.com/documentation/uikit/uinotificationfeedbackgenerator/feedbacktype/error)Added [UINotificationFeedbackTypeSuccess](https://developer.apple.com/documentation/uikit/uinotificationfeedbackgenerator/feedbacktype/success)Added [UINotificationFeedbackTypeWarning](https://developer.apple.com/documentation/uikit/uinotificationfeedbacktype/uinotificationfeedbacktypewarning)

#### UIPasteboard.h

Removed UIPasteboard(UIPasteboardDataExtensions)Added [UIPasteboardName](https://developer.apple.com/documentation/uikit/uipasteboardname)Added [UIPasteboardOption](https://developer.apple.com/documentation/uikit/uipasteboard/optionskey)

#### UIPopoverBackgroundView.h

Added [UIPopoverBackgroundView.wantsDefaultContentAppearance](https://developer.apple.com/documentation/uikit/uipopoverbackgroundview/1619357-wantsdefaultcontentappearance)

#### UIPresentationController.h

Modified [UIPresentationController.adaptivePresentationStyle](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618340-adaptivepresentationstyle)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIModalPresentationStyle)adaptivePresentationStyle ``` | -- |
| To | ``` @property(nonatomic, readonly) UIModalPresentationStyle adaptivePresentationStyle ``` | yes |

Modified [UIPresentationController.frameOfPresentedViewInContainerView](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618337-frameofpresentedviewincontainerv)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGRect)frameOfPresentedViewInContainerView ``` | -- |
| To | ``` @property(nonatomic, readonly) CGRect frameOfPresentedViewInContainerView ``` | yes |

Modified [-[UIPresentationController initWithPresentedViewController:presentingViewController:]](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618328-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIPresentationController.presentedView](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618321-presentedview)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIView *)presentedView ``` | -- |
| To | ``` @property(nonatomic, readonly) UIView *presentedView ``` | yes |

Modified [UIPresentationController.shouldPresentInFullscreen](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618336-shouldpresentinfullscreen)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (BOOL)shouldPresentInFullscreen ``` | -- |
| To | ``` @property(nonatomic, readonly) BOOL shouldPresentInFullscreen ``` | yes |

Modified [UIPresentationController.shouldRemovePresentersView](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618319-shouldremovepresentersview)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (BOOL)shouldRemovePresentersView ``` | -- |
| To | ``` @property(nonatomic, readonly) BOOL shouldRemovePresentersView ``` | yes |

#### UIPressesEvent.h

Modified [UIPressesEvent.allPresses](https://developer.apple.com/documentation/uikit/uipressesevent/1623575-allpresses)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSSet<UIPress *> *)allPresses ``` | -- |
| To | ``` @property(nonatomic, readonly) NSSet<UIPress *> *allPresses ``` | yes |

#### UIPreviewInteraction.h (Added)

Added [UIPreviewInteractionDelegate](https://developer.apple.com/documentation/uikit/uipreviewinteractiondelegate)

#### UIRegion.h

Added [UIRegion.infiniteRegion](https://developer.apple.com/documentation/uikit/uiregion/1621896-infiniteregion)Modified [+[UIRegion infiniteRegion]](https://developer.apple.com/documentation/uikit/uiregion/1621896-infinite)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)infiniteRegion ``` |
| To | ``` + (UIRegion *)infiniteRegion ``` |

#### UIResponder.h

Removed NSObject(UIResponderStandardEditActions)Added [UIResponderStandardEditActions](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions)Modified [UIResponder](https://developer.apple.com/documentation/uikit/uiresponder)

|  | Protocols |
| --- | --- |
| From | -- |
| To | UIResponderStandardEditActions |

Modified [UIResponder.canBecomeFirstResponder](https://developer.apple.com/documentation/uikit/uiresponder/1621130-canbecomefirstresponder)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (BOOL)canBecomeFirstResponder ``` | -- |
| To | ``` @property(nonatomic, readonly) BOOL canBecomeFirstResponder ``` | yes |

Modified [UIResponder.canResignFirstResponder](https://developer.apple.com/documentation/uikit/uiresponder/1621125-canresignfirstresponder)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (BOOL)canResignFirstResponder ``` | -- |
| To | ``` @property(nonatomic, readonly) BOOL canResignFirstResponder ``` | yes |

Modified [UIResponder.isFirstResponder](https://developer.apple.com/documentation/uikit/uiresponder/1621145-isfirstresponder)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (BOOL)isFirstResponder ``` | -- |
| To | ``` @property(nonatomic, readonly) BOOL isFirstResponder ``` | yes |

Modified [UIResponder.nextResponder](https://developer.apple.com/documentation/uikit/uiresponder/1621099-nextresponder)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIResponder *)nextResponder ``` | -- |
| To | ``` @property(nonatomic, readonly) UIResponder *nextResponder ``` | yes |

Modified [-[UIResponder touchesEstimatedPropertiesUpdated:]](https://developer.apple.com/documentation/uikit/uiresponder/1621147-touchesestimatedpropertiesupdate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)touchesEstimatedPropertiesUpdated:(NSSet *)touches ``` |
| To | ``` - (void)touchesEstimatedPropertiesUpdated:(NSSet<UITouch *> *)touches ``` |

Modified [-[UIResponderStandardEditActions copy:]](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/2354191-copy)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIResponderStandardEditActions cut:]](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/2354193-cut)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIResponderStandardEditActions decreaseSize:]](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/2354192-decreasesize)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIResponderStandardEditActions delete:]](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/2354197-delete)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIResponderStandardEditActions increaseSize:]](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/2354199-increasesize)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIResponderStandardEditActions makeTextWritingDirectionLeftToRight:]](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/2354198-maketextwritingdirectionlefttori)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIResponderStandardEditActions makeTextWritingDirectionRightToLeft:]](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/2354195-maketextwritingdirectionrighttol)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIResponderStandardEditActions paste:]](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/2354189-paste)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIResponderStandardEditActions select:]](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/2354190-select)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIResponderStandardEditActions selectAll:]](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/2354200-selectall)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIResponderStandardEditActions toggleBoldface:]](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/2354196-toggleboldface)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIResponderStandardEditActions toggleItalics:]](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/2354187-toggleitalics)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIResponderStandardEditActions toggleUnderline:]](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/2354194-toggleunderline)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

#### UIScreen.h

Added [UIScreen.focusedItem](https://developer.apple.com/documentation/uikit/uiscreen/1649175-focuseditem)Added [UIScreen.mainScreen](https://developer.apple.com/documentation/uikit/uiscreen/1617815-mainscreen)Added [UIScreen.screens](https://developer.apple.com/documentation/uikit/uiscreen/1617812-screens)

#### UISplitViewController.h

Modified [UISplitViewController.displayModeButtonItem](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623196-displaymodebuttonitem)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIBarButtonItem *)displayModeButtonItem ``` | -- |
| To | ``` @property(nonatomic, readonly) UIBarButtonItem *displayModeButtonItem ``` | yes |

#### UIStackView.h

Added [-[UIStackView initWithCoder:]](https://developer.apple.com/documentation/uikit/uistackview/2097541-initwithcoder)Added [-[UIStackView initWithFrame:]](https://developer.apple.com/documentation/uikit/uistackview/2097542-initwithframe)

#### UITabBar.h

Added [UITabBar.unselectedItemTintColor](https://developer.apple.com/documentation/uikit/uitabbar/1648949-unselecteditemtintcolor)Modified [UITabBar.delegate](https://developer.apple.com/documentation/uikit/uitabbar/1623444-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<UITabBarDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak) id<UITabBarDelegate> delegate ``` |

Modified [UITabBar.selectedItem](https://developer.apple.com/documentation/uikit/uitabbar/1623453-selecteditem)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) UITabBarItem *selectedItem ``` |
| To | ``` @property(nonatomic, weak) UITabBarItem *selectedItem ``` |

#### UITabBarItem.h

Added [UITabBarItem.badgeColor](https://developer.apple.com/documentation/uikit/uitabbaritem/1648567-badgecolor)Added [-[UITabBarItem badgeTextAttributesForState:]](https://developer.apple.com/documentation/uikit/uitabbaritem/1648565-badgetextattributes)Added [-[UITabBarItem setBadgeTextAttributes:forState:]](https://developer.apple.com/documentation/uikit/uitabbaritem/1648566-setbadgetextattributes)

#### UITableView.h

Added [UITableView.prefetchDataSource](https://developer.apple.com/documentation/uikit/uitableview/1771763-prefetchdatasource)Added [UITableViewDataSourcePrefetching](https://developer.apple.com/documentation/uikit/uitableviewdatasourceprefetching)Added [-[UITableViewDataSourcePrefetching tableView:cancelPrefetchingForRowsAtIndexPaths:]](https://developer.apple.com/documentation/uikit/uitableviewdatasourceprefetching/1771765-tableview)Added [-[UITableViewDataSourcePrefetching tableView:prefetchRowsAtIndexPaths:]](https://developer.apple.com/documentation/uikit/uitableviewdatasourceprefetching/1771764-tableview)

#### UITextChecker.h

Removed -[UITextChecker setIgnoredWords:]Added [UITextChecker.availableLanguages](https://developer.apple.com/documentation/uikit/uitextchecker/1621033-availablelanguages)Modified [+[UITextChecker availableLanguages]](https://developer.apple.com/documentation/uikit/uitextchecker/1621033-availablelanguages)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)availableLanguages ``` |
| To | ``` + (NSArray<NSString *> *)availableLanguages ``` |

Modified [-[UITextChecker completionsForPartialWordRange:inString:language:]](https://developer.apple.com/documentation/uikit/uitextchecker/1621034-completions)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)completionsForPartialWordRange:(NSRange)range inString:(NSString *)string language:(NSString *)language ``` |
| To | ``` - (NSArray<NSString *> *)completionsForPartialWordRange:(NSRange)range inString:(NSString *)string language:(NSString *)language ``` |

Modified [-[UITextChecker guessesForWordRange:inString:language:]](https://developer.apple.com/documentation/uikit/uitextchecker/1621037-guessesforwordrange)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)guessesForWordRange:(NSRange)range inString:(NSString *)string language:(NSString *)language ``` |
| To | ``` - (NSArray<NSString *> *)guessesForWordRange:(NSRange)range inString:(NSString *)string language:(NSString *)language ``` |

Modified [UITextChecker.ignoredWords](https://developer.apple.com/documentation/uikit/uitextchecker/1621032-ignoredwords)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)ignoredWords ``` |
| To | ``` @property(nonatomic, strong) NSArray<NSString *> *ignoredWords ``` |

#### UITextField.h

Added [-[UITextFieldDelegate textFieldDidEndEditing:reason:]](https://developer.apple.com/documentation/uikit/uitextfielddelegate/2352220-textfielddidendediting)Added [UITextFieldDidEndEditingReason](https://developer.apple.com/documentation/uikit/uitextfielddidendeditingreason)Added [UITextFieldDidEndEditingReasonCancelled](https://developer.apple.com/documentation/uikit/uitextfield/didendeditingreason/cancelled)Added [UITextFieldDidEndEditingReasonCommitted](https://developer.apple.com/documentation/uikit/uitextfielddidendeditingreason/uitextfielddidendeditingreasoncommitted)Added [UITextFieldDidEndEditingReasonKey](https://developer.apple.com/documentation/uikit/uitextfielddidendeditingreasonkey)Modified [UITextField](https://developer.apple.com/documentation/uikit/uitextfield)

|  | Protocols |
| --- | --- |
| From | NSCoding, UITextInput |
| To | NSCoding, UIContentSizeCategoryAdjusting, UITextInput |

#### UITextInput.h

Added [UITextInputMode.activeInputModes](https://developer.apple.com/documentation/uikit/uitextinputmode/1614522-activeinputmodes)Modified [UIKeyInput.hasText](https://developer.apple.com/documentation/uikit/uikeyinput/1614457-hastext)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (BOOL)hasText ``` | -- |
| To | ``` @property(nonatomic, readonly) BOOL hasText ``` | yes |

Modified [UITextInput.insertDictationResultPlaceholder](https://developer.apple.com/documentation/uikit/uitextinput/1614466-insertdictationresultplaceholder)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (id)insertDictationResultPlaceholder ``` | -- |
| To | ``` @property(nonatomic, readonly) id insertDictationResultPlaceholder ``` | yes |

Modified [+[UITextInputMode activeInputModes]](https://developer.apple.com/documentation/uikit/uitextinputmode/1614522-activeinputmodes)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray<NSString *> *)activeInputModes ``` |
| To | ``` + (NSArray<UITextInputMode *> *)activeInputModes ``` |

#### UITextInputTraits.h

Added [UITextInputTraits.textContentType](https://developer.apple.com/documentation/uikit/uitextinputtraits/1649656-textcontenttype)Added [UIKeyboardTypeASCIICapableNumberPad](https://developer.apple.com/documentation/uikit/uikeyboardtype/uikeyboardtypeasciicapablenumberpad)Added [UITextContentType](https://developer.apple.com/documentation/uikit/uitextcontenttype)Added [UITextContentTypeAddressCity](https://developer.apple.com/documentation/uikit/uitextcontenttypeaddresscity)Added [UITextContentTypeAddressCityAndState](https://developer.apple.com/documentation/uikit/uitextcontenttypeaddresscityandstate)Added [UITextContentTypeAddressState](https://developer.apple.com/documentation/uikit/uitextcontenttypeaddressstate)Added [UITextContentTypeCountryName](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649650-countryname)Added [UITextContentTypeCreditCardNumber](https://developer.apple.com/documentation/uikit/uitextcontenttypecreditcardnumber)Added [UITextContentTypeEmailAddress](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649660-emailaddress)Added [UITextContentTypeFamilyName](https://developer.apple.com/documentation/uikit/uitextcontenttypefamilyname)Added [UITextContentTypeFullStreetAddress](https://developer.apple.com/documentation/uikit/uitextcontenttypefullstreetaddress)Added [UITextContentTypeGivenName](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649659-givenname)Added [UITextContentTypeJobTitle](https://developer.apple.com/documentation/uikit/uitextcontenttypejobtitle)Added [UITextContentTypeLocation](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649646-location)Added [UITextContentTypeMiddleName](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649653-middlename)Added [UITextContentTypeName](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649669-name)Added [UITextContentTypeNamePrefix](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649647-nameprefix)Added [UITextContentTypeNameSuffix](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649665-namesuffix)Added [UITextContentTypeNickname](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649652-nickname)Added [UITextContentTypeOrganizationName](https://developer.apple.com/documentation/uikit/uitextcontenttypeorganizationname)Added [UITextContentTypePostalCode](https://developer.apple.com/documentation/uikit/uitextcontenttypepostalcode)Added [UITextContentTypeStreetAddressLine1](https://developer.apple.com/documentation/uikit/uitextcontenttype/1649663-streetaddressline1)Added [UITextContentTypeStreetAddressLine2](https://developer.apple.com/documentation/uikit/uitextcontenttypestreetaddressline2)Added [UITextContentTypeSublocality](https://developer.apple.com/documentation/uikit/uitextcontenttypesublocality)Added [UITextContentTypeTelephoneNumber](https://developer.apple.com/documentation/uikit/uitextcontenttypetelephonenumber)Added [UITextContentTypeURL](https://developer.apple.com/documentation/uikit/uitextcontenttypeurl)

#### UITextInteraction.h (Added)

Added [UITextItemInteraction](https://developer.apple.com/documentation/uikit/uitextiteminteraction)Added [UITextItemInteractionInvokeDefaultAction](https://developer.apple.com/documentation/uikit/uitextiteminteraction/uitextiteminteractioninvokedefaultaction)Added [UITextItemInteractionPresentActions](https://developer.apple.com/documentation/uikit/uitextiteminteraction/uitextiteminteractionpresentactions)Added [UITextItemInteractionPreview](https://developer.apple.com/documentation/uikit/uitextiteminteraction/uitextiteminteractionpreview)

#### UITextView.h

Added [-[UITextViewDelegate textView:shouldInteractWithTextAttachment:inRange:interaction:]](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1649336-textview)Added [-[UITextViewDelegate textView:shouldInteractWithURL:inRange:interaction:]](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1649337-textview)Modified [UITextView](https://developer.apple.com/documentation/uikit/uitextview)

|  | Protocols |
| --- | --- |
| From | UITextInput |
| To | UIContentSizeCategoryAdjusting, UITextInput |

Modified [-[UITextViewDelegate textView:shouldInteractWithTextAttachment:inRange:]](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618621-textview)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 10.0 |

Modified [-[UITextViewDelegate textView:shouldInteractWithURL:inRange:]](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618606-textview)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 10.0 |

#### UITimingCurveProvider.h (Added)

Added [UITimingCurveProvider](https://developer.apple.com/documentation/uikit/uitimingcurveprovider)Added [UITimingCurveProvider.cubicTimingParameters](https://developer.apple.com/documentation/uikit/uitimingcurveprovider/1648036-cubictimingparameters)Added [UITimingCurveProvider.springTimingParameters](https://developer.apple.com/documentation/uikit/uitimingcurveprovider/1648031-springtimingparameters)Added [UITimingCurveProvider.timingCurveType](https://developer.apple.com/documentation/uikit/uitimingcurveprovider/1648030-timingcurvetype)Added [UITimingCurveType](https://developer.apple.com/documentation/uikit/uitimingcurvetype)Added [UITimingCurveTypeBuiltin](https://developer.apple.com/documentation/uikit/uitimingcurvetype/uitimingcurvetypebuiltin)Added [UITimingCurveTypeComposed](https://developer.apple.com/documentation/uikit/uitimingcurvetype/composed)Added [UITimingCurveTypeCubic](https://developer.apple.com/documentation/uikit/uitimingcurvetype/cubic)Added [UITimingCurveTypeSpring](https://developer.apple.com/documentation/uikit/uitimingcurvetype/spring)

#### UITimingParameters.h (Added)

Added [UICubicTimingParameters](https://developer.apple.com/documentation/uikit/uicubictimingparameters)Added [UICubicTimingParameters.animationCurve](https://developer.apple.com/documentation/uikit/uicubictimingparameters/1649841-animationcurve)Added [UICubicTimingParameters.controlPoint1](https://developer.apple.com/documentation/uikit/uicubictimingparameters/1649914-controlpoint1)Added [UICubicTimingParameters.controlPoint2](https://developer.apple.com/documentation/uikit/uicubictimingparameters/1649907-controlpoint2)Added [-[UICubicTimingParameters init]](https://developer.apple.com/documentation/uikit/uicubictimingparameters/1649799-init)Added [-[UICubicTimingParameters initWithAnimationCurve:]](https://developer.apple.com/documentation/uikit/uicubictimingparameters/1649749-init)Added [-[UICubicTimingParameters initWithCoder:]](https://developer.apple.com/documentation/uikit/uicubictimingparameters/1649910-initwithcoder)Added [-[UICubicTimingParameters initWithControlPoint1:controlPoint2:]](https://developer.apple.com/documentation/uikit/uicubictimingparameters/1649854-initwithcontrolpoint1)Added [UISpringTimingParameters](https://developer.apple.com/documentation/uikit/uispringtimingparameters)Added [-[UISpringTimingParameters init]](https://developer.apple.com/documentation/uikit/uispringtimingparameters/1649802-init)Added [UISpringTimingParameters.initialVelocity](https://developer.apple.com/documentation/uikit/uispringtimingparameters/1649909-initialvelocity)Added [-[UISpringTimingParameters initWithCoder:]](https://developer.apple.com/documentation/uikit/uispringtimingparameters/1649919-init)Added [-[UISpringTimingParameters initWithDampingRatio:]](https://developer.apple.com/documentation/uikit/uispringtimingparameters/1649835-init)Added [-[UISpringTimingParameters initWithDampingRatio:initialVelocity:]](https://developer.apple.com/documentation/uikit/uispringtimingparameters/1649832-initwithdampingratio)Added [-[UISpringTimingParameters initWithMass:stiffness:damping:initialVelocity:]](https://developer.apple.com/documentation/uikit/uispringtimingparameters/1649764-init)

#### UITraitCollection.h

Added [UITraitCollection.displayGamut](https://developer.apple.com/documentation/uikit/uitraitcollection/1771749-displaygamut)Added [UITraitCollection.layoutDirection](https://developer.apple.com/documentation/uikit/uitraitcollection/1648355-layoutdirection)Added [UITraitCollection.preferredContentSizeCategory](https://developer.apple.com/documentation/uikit/uitraitcollection/1771746-preferredcontentsizecategory)Added [+[UITraitCollection traitCollectionWithDisplayGamut:]](https://developer.apple.com/documentation/uikit/uitraitcollection/1771747-init)Added [+[UITraitCollection traitCollectionWithLayoutDirection:]](https://developer.apple.com/documentation/uikit/uitraitcollection/1648354-init)Added [+[UITraitCollection traitCollectionWithPreferredContentSizeCategory:]](https://developer.apple.com/documentation/uikit/uitraitcollection/1771748-init)Added [+[UITraitCollection traitCollectionWithUserInterfaceStyle:]](https://developer.apple.com/documentation/uikit/uitraitcollection/1651062-init)Added [UITraitCollection.userInterfaceStyle](https://developer.apple.com/documentation/uikit/uitraitcollection/1651063-userinterfacestyle)

#### UIView.h

Added [-[UILayoutGuide constraintsAffectingLayoutForAxis:]](https://developer.apple.com/documentation/uikit/uilayoutguide/1648534-constraintsaffectinglayoutforaxi)Added [UILayoutGuide.hasAmbiguousLayout](https://developer.apple.com/documentation/uikit/uilayoutguide/1648533-hasambiguouslayout)Added [UIView.areAnimationsEnabled](https://developer.apple.com/documentation/uikit/uiview/1622571-areanimationsenabled)Added [UIView.effectiveUserInterfaceLayoutDirection](https://developer.apple.com/documentation/uikit/uiview/1648536-effectiveuserinterfacelayoutdire)Added [UIView.inheritedAnimationDuration](https://developer.apple.com/documentation/uikit/uiview/1622479-inheritedanimationduration)Added [UIView.layerClass](https://developer.apple.com/documentation/uikit/uiview/1622626-layerclass)Added [UIView.requiresConstraintBasedLayout](https://developer.apple.com/documentation/uikit/uiview/1622549-requiresconstraintbasedlayout)Added [+[UIView userInterfaceLayoutDirectionForSemanticContentAttribute:relativeToLayoutDirection:]](https://developer.apple.com/documentation/uikit/uiview/1648535-userinterfacelayoutdirection)Added UILayoutGuide(UIConstraintBasedLayoutDebugging)Modified [UIView](https://developer.apple.com/documentation/uikit/uiview)

|  | Protocols |
| --- | --- |
| From | NSCoding, UIAppearance, UIAppearanceContainer, UICoordinateSpace, UIDynamicItem, UIFocusEnvironment, UITraitEnvironment |
| To | CALayerDelegate, NSCoding, UIAppearance, UIAppearanceContainer, UICoordinateSpace, UIDynamicItem, UIFocusItem, UITraitEnvironment |

Modified [UIView.alignmentRectInsets](https://developer.apple.com/documentation/uikit/uiview/1622648-alignmentrectinsets)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIEdgeInsets)alignmentRectInsets ``` | -- |
| To | ``` @property(nonatomic, readonly) UIEdgeInsets alignmentRectInsets ``` | yes |

Modified [UIView.canBecomeFocused](https://developer.apple.com/documentation/uikit/uiview/1622584-canbecomefocused)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (BOOL)canBecomeFocused ``` | -- |
| To | ``` @property(nonatomic, readonly) BOOL canBecomeFocused ``` | yes |

Modified [UIView.hasAmbiguousLayout](https://developer.apple.com/documentation/uikit/uiview/1622517-hasambiguouslayout)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (BOOL)hasAmbiguousLayout ``` | -- |
| To | ``` @property(nonatomic, readonly) BOOL hasAmbiguousLayout ``` | yes |

Modified [UIView.intrinsicContentSize](https://developer.apple.com/documentation/uikit/uiview/1622600-intrinsiccontentsize)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGSize)intrinsicContentSize ``` | -- |
| To | ``` @property(nonatomic, readonly) CGSize intrinsicContentSize ``` | yes |

Modified [-[UIView updateConstraints]](https://developer.apple.com/documentation/uikit/uiview/1622512-updateconstraints)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIUserInterfaceLayoutDirection](https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection)

|  | Header |
| --- | --- |
| From | UIKit/UIView.h |
| To | UIKit/UIInterface.h |

Modified [UIUserInterfaceLayoutDirectionLeftToRight](https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection/lefttoright)

|  | Header |
| --- | --- |
| From | UIKit/UIView.h |
| To | UIKit/UIInterface.h |

Modified [UIUserInterfaceLayoutDirectionRightToLeft](https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection/righttoleft)

|  | Header |
| --- | --- |
| From | UIKit/UIView.h |
| To | UIKit/UIInterface.h |

#### UIViewAnimating.h (Added)

Added [UIViewAnimating](https://developer.apple.com/documentation/uikit/uiviewanimating)Added [-[UIViewAnimating finishAnimationAtPosition:]](https://developer.apple.com/documentation/uikit/uiviewanimating/1649796-finishanimation)Added [UIViewAnimating.fractionComplete](https://developer.apple.com/documentation/uikit/uiviewanimating/1649787-fractioncomplete)Added [-[UIViewAnimating pauseAnimation]](https://developer.apple.com/documentation/uikit/uiviewanimating/1649843-pauseanimation)Added [UIViewAnimating.reversed](https://developer.apple.com/documentation/uikit/uiviewanimating/1649804-reversed)Added [UIViewAnimating.running](https://developer.apple.com/documentation/uikit/uiviewanimating/1649785-isrunning)Added [-[UIViewAnimating startAnimation]](https://developer.apple.com/documentation/uikit/uiviewanimating/1649786-startanimation)Added [-[UIViewAnimating startAnimationAfterDelay:]](https://developer.apple.com/documentation/uikit/uiviewanimating/2097540-startanimation)Added [UIViewAnimating.state](https://developer.apple.com/documentation/uikit/uiviewanimating/1649743-state)Added [-[UIViewAnimating stopAnimation:]](https://developer.apple.com/documentation/uikit/uiviewanimating/1649750-stopanimation)Added [UIViewImplicitlyAnimating](https://developer.apple.com/documentation/uikit/uiviewimplicitlyanimating)Added [-[UIViewImplicitlyAnimating addAnimations:]](https://developer.apple.com/documentation/uikit/uiviewimplicitlyanimating/1829436-addanimations)Added [-[UIViewImplicitlyAnimating addAnimations:delayFactor:]](https://developer.apple.com/documentation/uikit/uiviewimplicitlyanimating/1829428-addanimations)Added [-[UIViewImplicitlyAnimating addCompletion:]](https://developer.apple.com/documentation/uikit/uiviewimplicitlyanimating/1829432-addcompletion)Added [-[UIViewImplicitlyAnimating continueAnimationWithTimingParameters:durationFactor:]](https://developer.apple.com/documentation/uikit/uiviewimplicitlyanimating/1829444-continueanimationwithtimingparam)Added [UIViewAnimatingPosition](https://developer.apple.com/documentation/uikit/uiviewanimatingposition)Added [UIViewAnimatingPositionCurrent](https://developer.apple.com/documentation/uikit/uiviewanimatingposition/uiviewanimatingpositioncurrent)Added [UIViewAnimatingPositionEnd](https://developer.apple.com/documentation/uikit/uiviewanimatingposition/uiviewanimatingpositionend)Added [UIViewAnimatingPositionStart](https://developer.apple.com/documentation/uikit/uiviewanimatingposition/uiviewanimatingpositionstart)Added [UIViewAnimatingState](https://developer.apple.com/documentation/uikit/uiviewanimatingstate)Added [UIViewAnimatingStateActive](https://developer.apple.com/documentation/uikit/uiviewanimatingstate/active)Added [UIViewAnimatingStateInactive](https://developer.apple.com/documentation/uikit/uiviewanimatingstate/inactive)Added [UIViewAnimatingStateStopped](https://developer.apple.com/documentation/uikit/uiviewanimatingstate/uiviewanimatingstatestopped)

#### UIViewController.h

Removed -[UIViewController isBeingDismissed]Removed -[UIViewController isBeingPresented]Removed -[UIViewController isMovingFromParentViewController]Removed -[UIViewController isMovingToParentViewController]Removed -[UIViewController isViewLoaded]Added [UIViewController.beingDismissed](https://developer.apple.com/documentation/uikit/uiviewcontroller/2097562-isbeingdismissed)Added [UIViewController.beingPresented](https://developer.apple.com/documentation/uikit/uiviewcontroller/2097564-isbeingpresented)Added [UIViewController.movingFromParentViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller/2097565-movingfromparentviewcontroller)Added [UIViewController.movingToParentViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller/2097561-movingtoparentviewcontroller)Added [UIViewController.restoresFocusAfterTransition](https://developer.apple.com/documentation/uikit/uiviewcontroller/1829440-restoresfocusaftertransition)Added [UIViewController.viewLoaded](https://developer.apple.com/documentation/uikit/uiviewcontroller/2097563-viewloaded)Modified [UIViewController.disablesAutomaticKeyboardDismissal](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621385-disablesautomatickeyboarddismiss)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)disablesAutomaticKeyboardDismissal ``` |
| To | ``` @property(nonatomic, assign) BOOL disablesAutomaticKeyboardDismissal ``` |

Modified [UIViewController.editButtonItem](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621471-editbuttonitem)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIBarButtonItem *)editButtonItem ``` | -- |
| To | ``` @property(nonatomic, readonly) UIBarButtonItem *editButtonItem ``` | yes |

Modified [UIViewController.previewActionItems](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621408-previewactionitems)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSArray<id<UIPreviewActionItem>> *)previewActionItems ``` | -- |
| To | ``` @property(nonatomic, readonly) NSArray<id<UIPreviewActionItem>> *previewActionItems ``` | yes |

Modified [UIViewController.shouldAutomaticallyForwardAppearanceMethods](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621389-shouldautomaticallyforwardappear)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (BOOL)shouldAutomaticallyForwardAppearanceMethods ``` | -- |
| To | ``` @property(nonatomic, readonly) BOOL shouldAutomaticallyForwardAppearanceMethods ``` | yes |

#### UIViewControllerTransitionCoordinator.h

Removed -[UIViewControllerTransitionCoordinatorContext isAnimated]Removed -[UIViewControllerTransitionCoordinatorContext isCancelled]Removed -[UIViewControllerTransitionCoordinatorContext isInteractive]Added [-[UIViewControllerTransitionCoordinator notifyWhenInteractionChangesUsingBlock:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/1829391-notifywheninteractionchangesusin)Added [UIViewControllerTransitionCoordinatorContext.animated](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/2097566-isanimated)Added [UIViewControllerTransitionCoordinatorContext.cancelled](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/2097568-cancelled)Added [UIViewControllerTransitionCoordinatorContext.interactive](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/2097567-interactive)Added [UIViewControllerTransitionCoordinatorContext.isInterruptible](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1829390-isinterruptible)Added [UITransitionContextViewControllerKey](https://developer.apple.com/documentation/uikit/uitransitioncontextviewcontrollerkey)Added [UITransitionContextViewKey](https://developer.apple.com/documentation/uikit/uitransitioncontextviewkey)Modified [UIViewController.transitionCoordinator](https://developer.apple.com/documentation/uikit/uiviewcontroller/1619294-transitioncoordinator)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (id<UIViewControllerTransitionCoordinator>)transitionCoordinator ``` | -- |
| To | ``` @property(nonatomic, readonly) id<UIViewControllerTransitionCoordinator> transitionCoordinator ``` | yes |

Modified [-[UIViewControllerTransitionCoordinator notifyWhenInteractionEndsUsingBlock:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/1619292-notifywheninteractionends)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 10.0 |

Modified [UIViewControllerTransitionCoordinatorContext.completionCurve](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619299-completioncurve)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIViewAnimationCurve)completionCurve ``` | -- |
| To | ``` @property(nonatomic, readonly) UIViewAnimationCurve completionCurve ``` | yes |

Modified [UIViewControllerTransitionCoordinatorContext.completionVelocity](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619282-completionvelocity)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGFloat)completionVelocity ``` | -- |
| To | ``` @property(nonatomic, readonly) CGFloat completionVelocity ``` | yes |

Modified [UIViewControllerTransitionCoordinatorContext.containerView](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619280-containerview)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIView *)containerView ``` | -- |
| To | ``` @property(nonatomic, readonly) UIView *containerView ``` | yes |

Modified [UIViewControllerTransitionCoordinatorContext.initiallyInteractive](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619285-initiallyinteractive)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (BOOL)initiallyInteractive ``` | -- |
| To | ``` @property(nonatomic, readonly) BOOL initiallyInteractive ``` | yes |

Modified [UIViewControllerTransitionCoordinatorContext.percentComplete](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619290-percentcomplete)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGFloat)percentComplete ``` | -- |
| To | ``` @property(nonatomic, readonly) CGFloat percentComplete ``` | yes |

Modified [UIViewControllerTransitionCoordinatorContext.presentationStyle](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619287-presentationstyle)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIModalPresentationStyle)presentationStyle ``` | -- |
| To | ``` @property(nonatomic, readonly) UIModalPresentationStyle presentationStyle ``` | yes |

Modified [UIViewControllerTransitionCoordinatorContext.targetTransform](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619289-targettransform)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGAffineTransform)targetTransform ``` | -- |
| To | ``` @property(nonatomic, readonly) CGAffineTransform targetTransform ``` | yes |

Modified [UIViewControllerTransitionCoordinatorContext.transitionDuration](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619286-transitionduration)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSTimeInterval)transitionDuration ``` | -- |
| To | ``` @property(nonatomic, readonly) NSTimeInterval transitionDuration ``` | yes |

Modified [-[UIViewControllerTransitionCoordinatorContext viewControllerForKey:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619293-viewcontrollerforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (__kindof UIViewController *)viewControllerForKey:(NSString *)key ``` |
| To | ``` - (__kindof UIViewController *)viewControllerForKey:(UITransitionContextViewControllerKey)key ``` |

Modified [-[UIViewControllerTransitionCoordinatorContext viewForKey:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619302-viewforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (__kindof UIView *)viewForKey:(NSString *)key ``` |
| To | ``` - (__kindof UIView *)viewForKey:(UITransitionContextViewKey)key ``` |

#### UIViewControllerTransitioning.h

Removed -[UIViewControllerContextTransitioning isAnimated]Removed -[UIViewControllerContextTransitioning isInteractive]Added [-[UIPercentDrivenInteractiveTransition pauseInteractiveTransition]](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/1829435-pause)Added [UIPercentDrivenInteractiveTransition.timingCurve](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/1829439-timingcurve)Added [UIPercentDrivenInteractiveTransition.wantsInteractiveStart](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/1829427-wantsinteractivestart)Added [-[UIViewControllerAnimatedTransitioning interruptibleAnimatorForTransition:]](https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning/1829434-interruptibleanimator)Added [UIViewControllerContextTransitioning.animated](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/2097569-animated)Added [UIViewControllerContextTransitioning.interactive](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/2097570-isinteractive)Added [-[UIViewControllerContextTransitioning pauseInteractiveTransition]](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1829437-pauseinteractivetransition)Added [UIViewControllerInteractiveTransitioning.wantsInteractiveStart](https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning/1829433-wantsinteractivestart)Modified [UIViewControllerContextTransitioning.containerView](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622045-containerview)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIView *)containerView ``` | -- |
| To | ``` @property(nonatomic, readonly) UIView *containerView ``` | yes |

Modified [UIViewControllerContextTransitioning.presentationStyle](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622049-presentationstyle)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIModalPresentationStyle)presentationStyle ``` | -- |
| To | ``` @property(nonatomic, readonly) UIModalPresentationStyle presentationStyle ``` | yes |

Modified [UIViewControllerContextTransitioning.targetTransform](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622036-targettransform)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGAffineTransform)targetTransform ``` | -- |
| To | ``` @property(nonatomic, readonly) CGAffineTransform targetTransform ``` | yes |

Modified [UIViewControllerContextTransitioning.transitionWasCancelled](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622039-transitionwascancelled)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (BOOL)transitionWasCancelled ``` | -- |
| To | ``` @property(nonatomic, readonly) BOOL transitionWasCancelled ``` | yes |

Modified [-[UIViewControllerContextTransitioning viewControllerForKey:]](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622043-viewcontrollerforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (__kindof UIViewController *)viewControllerForKey:(NSString *)key ``` |
| To | ``` - (__kindof UIViewController *)viewControllerForKey:(UITransitionContextViewControllerKey)key ``` |

Modified [-[UIViewControllerContextTransitioning viewForKey:]](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622055-view)

|  | Declaration |
| --- | --- |
| From | ``` - (__kindof UIView *)viewForKey:(NSString *)key ``` |
| To | ``` - (__kindof UIView *)viewForKey:(UITransitionContextViewKey)key ``` |

Modified [UIViewControllerInteractiveTransitioning.completionCurve](https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning/1622027-completioncurve)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (UIViewAnimationCurve)completionCurve ``` | -- |
| To | ``` @property(nonatomic, readonly) UIViewAnimationCurve completionCurve ``` | yes |

Modified [UIViewControllerInteractiveTransitioning.completionSpeed](https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning/1622031-completionspeed)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGFloat)completionSpeed ``` | -- |
| To | ``` @property(nonatomic, readonly) CGFloat completionSpeed ``` | yes |

#### UIViewPropertyAnimator.h (Added)

Added [UIViewPropertyAnimator](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator)Added [-[UIViewPropertyAnimator addAnimations:]](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/1648374-addanimations)Added [-[UIViewPropertyAnimator addAnimations:delayFactor:]](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/1648370-addanimations)Added [-[UIViewPropertyAnimator addCompletion:]](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/1648373-addcompletion)Added [-[UIViewPropertyAnimator continueAnimationWithTimingParameters:durationFactor:]](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/1648371-continueanimation)Added [UIViewPropertyAnimator.delay](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/2097549-delay)Added [UIViewPropertyAnimator.duration](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/1648375-duration)Added [-[UIViewPropertyAnimator initWithDuration:controlPoint1:controlPoint2:animations:]](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/1648368-init)Added [-[UIViewPropertyAnimator initWithDuration:curve:animations:]](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/1648366-initwithduration)Added [-[UIViewPropertyAnimator initWithDuration:dampingRatio:animations:]](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/1648369-initwithduration)Added [-[UIViewPropertyAnimator initWithDuration:timingParameters:]](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/1648362-init)Added [UIViewPropertyAnimator.interruptible](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/1648372-isinterruptible)Added [UIViewPropertyAnimator.manualHitTestingEnabled](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/2097548-manualhittestingenabled)Added [+[UIViewPropertyAnimator runningPropertyAnimatorWithDuration:delay:options:animations:completion:]](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/1648367-runningpropertyanimator)Added [UIViewPropertyAnimator.timingParameters](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/1648363-timingparameters)Added [UIViewPropertyAnimator.userInteractionEnabled](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/1648365-isuserinteractionenabled)

#### UIVisualEffectView.h

Added [UIBlurEffectStyleExtraDark](https://developer.apple.com/documentation/uikit/uiblureffect/style/extradark)Added [UIBlurEffectStyleProminent](https://developer.apple.com/documentation/uikit/uiblureffect/style/prominent)Added [UIBlurEffectStyleRegular](https://developer.apple.com/documentation/uikit/uiblureffect/style/regular)

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
