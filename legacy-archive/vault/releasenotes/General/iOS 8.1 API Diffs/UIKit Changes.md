---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/frameworks/UIKit.html
archived_at: '2026-07-18T02:56:03.213709Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# UIKit Changes

## UIKit

UIActionSheet.hModified [-[UIActionSheet initWithTitle:delegate:cancelButtonTitle:destructiveButtonTitle:otherButtonTitles:]](https://developer.apple.com/documentation/uikit/uiactionsheet/1622875-initwithtitle)

|  | App Extension[Introduction] | App Extension[Message] |
| --- | --- | --- |
| From | -- | -- |
| To | not_available | Use UIAlertController instead. |

UIActivityIndicatorView.hModified [UIActivityIndicatorView.color](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/1622836-color)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UIAlertView.hModified [-[UIAlertView initWithTitle:message:delegate:cancelButtonTitle:otherButtonTitles:]](https://developer.apple.com/documentation/uikit/uialertview/1620765-init)

|  | App Extension[Introduction] | App Extension[Message] |
| --- | --- | --- |
| From | -- | -- |
| To | not_available | Use UIAlertController instead. |

UIApplication.hModified [-[UIApplication beginIgnoringInteractionEvents]](https://developer.apple.com/documentation/uikit/uiapplication/1623047-beginignoringinteractionevents)

|  | App Extension[Introduction] |
| --- | --- |
| From | -- |
| To | not_available |

Modified [-[UIApplication endIgnoringInteractionEvents]](https://developer.apple.com/documentation/uikit/uiapplication/1622938-endignoringinteractionevents)

|  | App Extension[Introduction] |
| --- | --- |
| From | -- |
| To | not_available |

Modified [-[UIApplication openURL:]](https://developer.apple.com/documentation/uikit/uiapplication/1622961-openurl)

|  | App Extension[Introduction] |
| --- | --- |
| From | -- |
| To | not_available |

Modified [+[UIApplication sharedApplication]](https://developer.apple.com/documentation/uikit/uiapplication/1622975-shared)

|  | App Extension[Introduction] | App Extension[Message] |
| --- | --- | --- |
| From | -- | -- |
| To | not_available | Use view controller based solutions where appropriate instead. |

UIBarButtonItem.hModified [-[UIBarButtonItem backButtonBackgroundImageForState:barMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617125-backbuttonbackgroundimageforstat)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIBarButtonItem backButtonBackgroundVerticalPositionAdjustmentForBarMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617120-backbuttonbackgroundverticalposi)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIBarButtonItem backButtonTitlePositionAdjustmentForBarMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617145-backbuttontitlepositionadjustmen)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIBarButtonItem backgroundImageForState:barMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617134-backgroundimageforstate)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIBarButtonItem backgroundImageForState:style:barMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617117-backgroundimageforstate)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIBarButtonItem backgroundVerticalPositionAdjustmentForBarMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617143-backgroundverticalpositionadjust)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIBarButtonItem setBackButtonBackgroundImage:forState:barMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617128-setbackbuttonbackgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIBarButtonItem setBackButtonBackgroundVerticalPositionAdjustment:forBarMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617124-setbackbuttonbackgroundverticalp)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIBarButtonItem setBackButtonTitlePositionAdjustment:forBarMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617139-setbackbuttontitlepositionadjust)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIBarButtonItem setBackgroundImage:forState:barMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617138-setbackgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIBarButtonItem setBackgroundImage:forState:style:barMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617161-setbackgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIBarButtonItem setBackgroundVerticalPositionAdjustment:forBarMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617141-setbackgroundverticalpositionadj)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIBarButtonItem setTitlePositionAdjustment:forBarMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617149-settitlepositionadjustment)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIBarButtonItem titlePositionAdjustmentForBarMetrics:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617160-titlepositionadjustmentforbarmet)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UIBarItem.hModified [-[UIBarItem setTitleTextAttributes:forState:]](https://developer.apple.com/documentation/uikit/uibaritem/1616414-settitletextattributes)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIBarItem titleTextAttributesForState:]](https://developer.apple.com/documentation/uikit/uibaritem/1616422-titletextattributesforstate)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UIButton.hModified [UIButton.contentEdgeInsets](https://developer.apple.com/documentation/uikit/uibutton/1624036-contentedgeinsets)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIButton setBackgroundImage:forState:]](https://developer.apple.com/documentation/uikit/uibutton/1624016-setbackgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIButton setTitleColor:forState:]](https://developer.apple.com/documentation/uikit/uibutton/1623993-settitlecolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIButton setTitleShadowColor:forState:]](https://developer.apple.com/documentation/uikit/uibutton/1623994-settitleshadowcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UIDocumentMenuViewController.hModified [-[UIDocumentMenuViewController initWithDocumentTypes:inMode:]](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/1614187-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIDocumentMenuViewController initWithURL:inMode:]](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/1614191-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

UIDocumentPickerViewController.hModified [-[UIDocumentPickerViewController initWithDocumentTypes:inMode:]](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/1618678-initwithdocumenttypes)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIDocumentPickerViewController initWithURL:inMode:]](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/1618684-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

UINavigationBar.hModified [UINavigationBar.backIndicatorImage](https://developer.apple.com/documentation/uikit/uinavigationbar/1624942-backindicatorimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UINavigationBar.backIndicatorTransitionMaskImage](https://developer.apple.com/documentation/uikit/uinavigationbar/1624938-backindicatortransitionmaskimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UINavigationBar backgroundImageForBarMetrics:]](https://developer.apple.com/documentation/uikit/uinavigationbar/1624962-backgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UINavigationBar backgroundImageForBarPosition:barMetrics:]](https://developer.apple.com/documentation/uikit/uinavigationbar/1624940-backgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UINavigationBar.barTintColor](https://developer.apple.com/documentation/uikit/uinavigationbar/1624931-bartintcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UINavigationBar setBackgroundImage:forBarMetrics:]](https://developer.apple.com/documentation/uikit/uinavigationbar/1624926-setbackgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UINavigationBar setBackgroundImage:forBarPosition:barMetrics:]](https://developer.apple.com/documentation/uikit/uinavigationbar/1624968-setbackgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UINavigationBar setTitleVerticalPositionAdjustment:forBarMetrics:]](https://developer.apple.com/documentation/uikit/uinavigationbar/1624959-settitleverticalpositionadjustme)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UINavigationBar.shadowImage](https://developer.apple.com/documentation/uikit/uinavigationbar/1624963-shadowimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UINavigationBar.titleTextAttributes](https://developer.apple.com/documentation/uikit/uinavigationbar/1624953-titletextattributes)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UINavigationBar titleVerticalPositionAdjustmentForBarMetrics:]](https://developer.apple.com/documentation/uikit/uinavigationbar/1624966-titleverticalpositionadjustment)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UINibDeclarations.hRemoved #def IBInspectableRemoved #def IB_DESIGNABLEUIPageControl.hModified [UIPageControl.currentPageIndicatorTintColor](https://developer.apple.com/documentation/uikit/uipagecontrol/1621233-currentpageindicatortintcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIPageControl.pageIndicatorTintColor](https://developer.apple.com/documentation/uikit/uipagecontrol/1621239-pageindicatortintcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UIProgressView.hModified [UIProgressView.progressImage](https://developer.apple.com/documentation/uikit/uiprogressview/1619837-progressimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIProgressView.progressTintColor](https://developer.apple.com/documentation/uikit/uiprogressview/1619836-progresstintcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIProgressView.trackImage](https://developer.apple.com/documentation/uikit/uiprogressview/1619843-trackimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIProgressView.trackTintColor](https://developer.apple.com/documentation/uikit/uiprogressview/1619841-tracktintcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UIRefreshControl.hModified [UIRefreshControl.attributedTitle](https://developer.apple.com/documentation/uikit/uirefreshcontrol/1624845-attributedtitle)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UISearchBar.hModified [UISearchBar.backgroundImage](https://developer.apple.com/documentation/uikit/uisearchbar/1624276-backgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBar backgroundImageForBarPosition:barMetrics:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624274-backgroundimageforbarposition)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UISearchBar.barTintColor](https://developer.apple.com/documentation/uikit/uisearchbar/1624295-bartintcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBar imageForSearchBarIcon:state:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624296-imageforsearchbaricon)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBar positionAdjustmentForSearchBarIcon:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624323-positionadjustmentforsearchbaric)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UISearchBar.scopeBarBackgroundImage](https://developer.apple.com/documentation/uikit/uisearchbar/1624317-scopebarbackgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBar scopeBarButtonBackgroundImageForState:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624311-scopebarbuttonbackgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBar scopeBarButtonDividerImageForLeftSegmentState:rightSegmentState:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624313-scopebarbuttondividerimageforlef)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBar scopeBarButtonTitleTextAttributesForState:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624309-scopebarbuttontitletextattribute)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBar searchFieldBackgroundImageForState:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624288-searchfieldbackgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UISearchBar.searchFieldBackgroundPositionAdjustment](https://developer.apple.com/documentation/uikit/uisearchbar/1624320-searchfieldbackgroundpositionadj)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UISearchBar.searchTextPositionAdjustment](https://developer.apple.com/documentation/uikit/uisearchbar/1624297-searchtextpositionadjustment)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBar setBackgroundImage:forBarPosition:barMetrics:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624325-setbackgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBar setImage:forSearchBarIcon:state:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624330-setimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBar setPositionAdjustment:forSearchBarIcon:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624278-setpositionadjustment)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBar setScopeBarButtonBackgroundImage:forState:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624290-setscopebarbuttonbackgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBar setScopeBarButtonDividerImage:forLeftSegmentState:rightSegmentState:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624308-setscopebarbuttondividerimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBar setScopeBarButtonTitleTextAttributes:forState:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624277-setscopebarbuttontitletextattrib)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBar setSearchFieldBackgroundImage:forState:]](https://developer.apple.com/documentation/uikit/uisearchbar/1624307-setsearchfieldbackgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UISegmentedControl.hModified [-[UISegmentedControl backgroundImageForState:barMetrics:]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618583-backgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISegmentedControl contentPositionAdjustmentForSegmentType:barMetrics:]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618593-contentpositionadjustmentforsegm)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISegmentedControl dividerImageForLeftSegmentState:rightSegmentState:barMetrics:]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618565-dividerimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISegmentedControl setBackgroundImage:forState:barMetrics:]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618571-setbackgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISegmentedControl setContentPositionAdjustment:forSegmentType:barMetrics:]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618555-setcontentpositionadjustment)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISegmentedControl setDividerImage:forLeftSegmentState:rightSegmentState:barMetrics:]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618558-setdividerimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISegmentedControl setTitleTextAttributes:forState:]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618570-settitletextattributes)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISegmentedControl titleTextAttributesForState:]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618566-titletextattributesforstate)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UISlider.hModified [UISlider.maximumTrackTintColor](https://developer.apple.com/documentation/uikit/uislider/1621334-maximumtracktintcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UISlider.minimumTrackTintColor](https://developer.apple.com/documentation/uikit/uislider/1621348-minimumtracktintcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UISlider.thumbTintColor](https://developer.apple.com/documentation/uikit/uislider/1621332-thumbtintcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UIStepper.hModified [-[UIStepper backgroundImageForState:]](https://developer.apple.com/documentation/uikit/uistepper/1624069-backgroundimageforstate)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIStepper decrementImageForState:]](https://developer.apple.com/documentation/uikit/uistepper/1624077-decrementimageforstate)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIStepper dividerImageForLeftSegmentState:rightSegmentState:]](https://developer.apple.com/documentation/uikit/uistepper/1624072-dividerimageforleftsegmentstate)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIStepper incrementImageForState:]](https://developer.apple.com/documentation/uikit/uistepper/1624080-incrementimageforstate)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIStepper setBackgroundImage:forState:]](https://developer.apple.com/documentation/uikit/uistepper/1624081-setbackgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIStepper setDecrementImage:forState:]](https://developer.apple.com/documentation/uikit/uistepper/1624074-setdecrementimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIStepper setDividerImage:forLeftSegmentState:rightSegmentState:]](https://developer.apple.com/documentation/uikit/uistepper/1624071-setdividerimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIStepper setIncrementImage:forState:]](https://developer.apple.com/documentation/uikit/uistepper/1624070-setincrementimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UISwitch.hModified [UISwitch.offImage](https://developer.apple.com/documentation/uikit/uiswitch/1623683-offimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UISwitch.onImage](https://developer.apple.com/documentation/uikit/uiswitch/1623689-onimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UISwitch.onTintColor](https://developer.apple.com/documentation/uikit/uiswitch/1623687-ontintcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UISwitch.thumbTintColor](https://developer.apple.com/documentation/uikit/uiswitch/1623684-thumbtintcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UITabBar.hModified [UITabBar.backgroundImage](https://developer.apple.com/documentation/uikit/uitabbar/1623469-backgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UITabBar.barStyle](https://developer.apple.com/documentation/uikit/uitabbar/1623454-barstyle)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UITabBar.barTintColor](https://developer.apple.com/documentation/uikit/uitabbar/1623445-bartintcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UITabBar.itemPositioning](https://developer.apple.com/documentation/uikit/uitabbar/1623468-itempositioning)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UITabBar.itemSpacing](https://developer.apple.com/documentation/uikit/uitabbar/1623446-itemspacing)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UITabBar.itemWidth](https://developer.apple.com/documentation/uikit/uitabbar/1623465-itemwidth)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UITabBar.selectedImageTintColor](https://developer.apple.com/documentation/uikit/uitabbar/1623470-selectedimagetintcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UITabBar.selectionIndicatorImage](https://developer.apple.com/documentation/uikit/uitabbar/1623456-selectionindicatorimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UITabBar.shadowImage](https://developer.apple.com/documentation/uikit/uitabbar/1623452-shadowimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UITabBarItem.hModified [-[UITabBarItem setTitlePositionAdjustment:]](https://developer.apple.com/documentation/uikit/uitabbaritem/1617070-titlepositionadjustment)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITabBarItem titlePositionAdjustment]](https://developer.apple.com/documentation/uikit/uitabbaritem/1617070-titlepositionadjustment)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UITableView.hModified [UITableView.sectionIndexBackgroundColor](https://developer.apple.com/documentation/uikit/uitableview/1614918-sectionindexbackgroundcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UITableView.sectionIndexColor](https://developer.apple.com/documentation/uikit/uitableview/1614915-sectionindexcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UITableView.sectionIndexTrackingBackgroundColor](https://developer.apple.com/documentation/uikit/uitableview/1614992-sectionindextrackingbackgroundco)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UITableView.separatorColor](https://developer.apple.com/documentation/uikit/uitableview/1614984-separatorcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UITableView.separatorEffect](https://developer.apple.com/documentation/uikit/uitableview/1614865-separatoreffect)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UITableView.separatorInset](https://developer.apple.com/documentation/uikit/uitableview/1614851-separatorinset)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UITableViewCell.hModified [UITableViewCell.separatorInset](https://developer.apple.com/documentation/uikit/uitableviewcell/1623250-separatorinset)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UIToolbar.hModified [-[UIToolbar backgroundImageForToolbarPosition:barMetrics:]](https://developer.apple.com/documentation/uikit/uitoolbar/1617998-backgroundimagefortoolbarpositio)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIToolbar.barTintColor](https://developer.apple.com/documentation/uikit/uitoolbar/1618002-bartintcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIToolbar setBackgroundImage:forToolbarPosition:barMetrics:]](https://developer.apple.com/documentation/uikit/uitoolbar/1618003-setbackgroundimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIToolbar setShadowImage:forToolbarPosition:]](https://developer.apple.com/documentation/uikit/uitoolbar/1617991-setshadowimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIToolbar shadowImageForToolbarPosition:]](https://developer.apple.com/documentation/uikit/uitoolbar/1618000-shadowimage)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UIView.hModified [UIView.backgroundColor](https://developer.apple.com/documentation/uikit/uiview/1622591-backgroundcolor)

|  | Ui Appearance Selector |
| --- | --- |
| From | -- |
| To | yes |

UIVisualEffectView.hModified [-[UIVisualEffectView initWithEffect:]](https://developer.apple.com/documentation/uikit/uivisualeffectview/1615051-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

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
