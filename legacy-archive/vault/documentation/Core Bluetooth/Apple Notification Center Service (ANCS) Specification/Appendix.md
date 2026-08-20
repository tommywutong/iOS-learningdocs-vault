---
title: Apple Notification Center Service (ANCS) Specification
apple_id: TP40013460
resource_type: Guide
platform: iOS
topic: Data Management
technology: CoreBluetooth
published: '2014-10-20'
source_url: https://developer.apple.com/library/archive/documentation/CoreBluetooth/Reference/AppleNotificationCenterServiceSpecification/Appendix/Appendix.html
archived_at: '2026-07-15T07:22:05.956369Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple Notification Center Service (ANCS) Specification](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](The%20Apple%20Notification%20Center%20Service.md)

# Appendix

The following tables list important values used in the ANCS.

__Table 3-1__  CategoryID values

| `CategoryIDOther` | = 0, |
| `CategoryIDIncomingCall` | = 1, |
| `CategoryIDMissedCall` | = 2, |
| `CategoryIDVoicemail` | = 3, |
| `CategoryIDSocial` | = 4, |
| `CategoryIDSchedule` | = 5, |
| `CategoryIDEmail` | = 6, |
| `CategoryIDNews` | = 7, |
| `CategoryIDHealthAndFitness` | = 8, |
| `CategoryIDBusinessAndFinance` | = 9, |
| `CategoryIDLocation` | = 10, |
| `CategoryIDEntertainment` | = 11, |
| Reserved `CategoryID` values | = 12–255 |

__Table 3-2__  EventID values

| `EventIDNotificationAdded` | = 0, |
| `EventIDNotificationModified` | = 1, |
| `EventIDNotificationRemoved` | = 2, |
| Reserved `EventID` values | = 3–255 |

__Table 3-3__  EventFlags

| `EventFlagSilent` | = (1 << 0), |
| `EventFlagImportant` | = (1 << 1), |
| `EventFlagPreExisting` | = (1 << 2), |
| `EventFlagPositiveAction` | = (1 << 3), |
| `EventFlagNegativeAction` | = (1 << 4), |
| Reserved `EventFlags` | = (1 << 5)–(1 << 7) |

__Table 3-4__  CommandID values

| `CommandIDGetNotificationAttributes` | = 0, |
| `CommandIDGetAppAttributes` | = 1, |
| `CommandIDPerformNotificationAction` | = 2, |
| Reserved `CommandID` values | = 3–255 |

__Table 3-5__  NotificationAttributeID values

| `NotificationAttributeIDAppIdentifier` | = 0, |
| `NotificationAttributeIDTitle` | = 1, (Needs to be followed by a 2-bytes max length parameter) |
| `NotificationAttributeIDSubtitle` | = 2, (Needs to be followed by a 2-bytes max length parameter) |
| `NotificationAttributeIDMessage` | = 3, (Needs to be followed by a 2-bytes max length parameter) |
| `NotificationAttributeIDMessageSize` | = 4, |
| `NotificationAttributeIDDate` | = 5, |
| `NotificationAttributeIDPositiveActionLabel` | = 6, |
| `NotificationAttributeIDNegativeActionLabel` | = 7, |
| Reserved `NotificationAttributeID` values | = 8–255 |

__Table 3-6__  ActionID values

| `ActionIDPositive` | = 0, |
| `ActionIDNegative` | = 1, |
| Reserved `ActionID` values | = 2–255 |

__Table 3-7__  AppAttributeID values

| `AppAttributeIDDisplayName` | = 0, |
| Reserved `AppAttributeID` values | = 1–255 |

[Next](Document%20Revision%20History.md)[Previous](The%20Apple%20Notification%20Center%20Service.md)

